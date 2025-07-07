"""
PH Awards API endpoints for campaign intelligence and analytics
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Optional, List, Dict, Any, Union
import sqlite3
import logging
from datetime import datetime
from pydantic import BaseModel

from app.core.config import settings
from app.models.user import User
from app.api import deps

logger = logging.getLogger(__name__)

router = APIRouter()

# Pydantic models
class CampaignSearchRequest(BaseModel):
    query: Optional[str] = ""
    filters: Optional[Dict[str, Any]] = {}
    limit: Optional[int] = 10
    offset: Optional[int] = 0

class AwardPredictionRequest(BaseModel):
    campaign_text: str

class PHAwardsResponse(BaseModel):
    success: bool
    data: Any
    timestamp: str
    message: Optional[str] = None

# Database connection helper
def get_ph_awards_db():
    """Get SQLite database connection for PH Awards data"""
    try:
        # Use SQLite database for PH Awards data
        conn = sqlite3.connect('./ces_intelligence.db')
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        logger.error(f"PH Awards database connection error: {e}")
        raise HTTPException(status_code=500, detail="PH Awards database connection failed")

@router.get("/health")
async def ph_awards_health():
    """Health check for PH Awards service"""
    try:
        conn = get_ph_awards_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        
        return {
            "status": "healthy",
            "service": "ph-awards-api",
            "timestamp": datetime.utcnow().isoformat(),
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PH Awards health check failed: {str(e)}")

@router.get("/stats", response_model=PHAwardsResponse)
async def get_ph_awards_stats(
    current_user: User = Depends(deps.get_current_active_user)
):
    """Get PH Awards campaign statistics"""
    try:
        conn = get_ph_awards_db()
        cursor = conn.cursor()
        
        stats = {
            "total_campaigns": 0,
            "processed_campaigns": 0,
            "award_winners": 0,
            "csr_campaigns": 0,
            "cultural_campaigns": 0,
            "youth_targeting": 0,
            "environmental_campaigns": 0
        }
        
        # Check if campaigns table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='campaigns'")
        table_exists = cursor.fetchone()
        
        if table_exists:
            # Get comprehensive stats
            queries = {
                'total_campaigns': 'SELECT COUNT(*) FROM campaigns',
                'processed_campaigns': 'SELECT COUNT(*) FROM campaigns WHERE campaign_name IS NOT NULL',
                'award_winners': 'SELECT COUNT(*) FROM campaigns WHERE won_award = 1',
                'csr_campaigns': 'SELECT COUNT(*) FROM campaigns WHERE is_csr_campaign = 1',
                'cultural_campaigns': 'SELECT COUNT(*) FROM campaigns WHERE uses_local_culture = 1',
                'youth_targeting': 'SELECT COUNT(*) FROM campaigns WHERE targets_youth = 1',
                'environmental_campaigns': 'SELECT COUNT(*) FROM campaigns WHERE has_environmental_angle = 1'
            }
            
            for key, query in queries.items():
                cursor.execute(query)
                stats[key] = cursor.fetchone()[0]
        
        conn.close()
        
        return PHAwardsResponse(
            success=True,
            data=stats,
            timestamp=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        logger.error(f"PH Awards stats error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve statistics: {str(e)}")

@router.post("/campaigns/search", response_model=PHAwardsResponse)
async def search_campaigns(
    request: CampaignSearchRequest,
    current_user: User = Depends(deps.get_current_active_user)
):
    """Search campaigns by criteria with advanced filtering"""
    try:
        conn = get_ph_awards_db()
        cursor = conn.cursor()
        
        # Build dynamic query
        sql = 'SELECT * FROM campaigns WHERE 1=1'
        params = []
        
        # Text search
        if request.query.strip():
            sql += ' AND (campaign_name LIKE ? OR brand LIKE ? OR award_show LIKE ?)'
            search_term = f'%{request.query}%'
            params.extend([search_term, search_term, search_term])
        
        # Boolean filters
        boolean_filters = {
            'won_award': 'won_award',
            'is_csr_campaign': 'is_csr_campaign', 
            'uses_local_culture': 'uses_local_culture',
            'targets_youth': 'targets_youth',
            'has_environmental_angle': 'has_environmental_angle',
            'is_purpose_driven': 'is_purpose_driven'
        }
        
        for filter_key, db_column in boolean_filters.items():
            if request.filters.get(filter_key) is not None:
                sql += f' AND {db_column} = ?'
                params.append(1 if request.filters[filter_key] else 0)
        
        # Numeric filters
        if request.filters.get('min_score'):
            sql += ' AND overall_ces_score >= ?'
            params.append(request.filters['min_score'])
            
        if request.filters.get('year'):
            sql += ' AND year = ?'
            params.append(request.filters['year'])
        
        # Sorting
        sort_by = request.filters.get('sort_by', 'overall_ces_score')
        sort_order = request.filters.get('sort_order', 'DESC')
        sql += f' ORDER BY {sort_by} {sort_order}'
        
        # Pagination
        sql += ' LIMIT ? OFFSET ?'
        params.extend([request.limit, request.offset])
        
        cursor.execute(sql, params)
        campaigns = [dict(row) for row in cursor.fetchall()]
        
        # Get total count
        count_sql = sql.replace('SELECT *', 'SELECT COUNT(*)')
        count_sql = count_sql.replace(f' ORDER BY {sort_by} {sort_order}', '')
        count_sql = count_sql.replace(f' LIMIT {request.limit} OFFSET {request.offset}', '')
        count_params = params[:-2]
        
        cursor.execute(count_sql, count_params)
        total = cursor.fetchone()[0]
        
        conn.close()
        
        return PHAwardsResponse(
            success=True,
            data={
                "campaigns": campaigns,
                "pagination": {
                    "total": total,
                    "limit": request.limit,
                    "offset": request.offset,
                    "has_more": request.offset + request.limit < total
                },
                "filters_applied": request.filters
            },
            timestamp=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Campaign search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")

@router.get("/cultural/trends", response_model=PHAwardsResponse)
async def get_cultural_trends(
    current_user: User = Depends(deps.get_current_active_user)
):
    """Get Filipino cultural intelligence trends and insights"""
    try:
        conn = get_ph_awards_db()
        cursor = conn.cursor()
        
        trends = {
            "cultural_elements": [],
            "top_performing_cultural": [],
            "csr_insights": [],
            "youth_campaigns": [],
            "summary": {}
        }
        
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='campaigns'")
        table_exists = cursor.fetchone()
        
        if table_exists:
            # Top cultural campaigns
            cursor.execute("""
                SELECT campaign_name, brand, overall_ces_score, cultural_relevance_score, year
                FROM campaigns 
                WHERE uses_local_culture = 1 AND campaign_name IS NOT NULL
                ORDER BY cultural_relevance_score DESC, overall_ces_score DESC
                LIMIT 10
            """)
            cultural_campaigns = [dict(row) for row in cursor.fetchall()]
            
            trends["cultural_elements"] = cultural_campaigns
            
            # CSR + Cultural intersection
            cursor.execute("""
                SELECT campaign_name, brand, overall_ces_score, year
                FROM campaigns 
                WHERE is_csr_campaign = 1 AND uses_local_culture = 1
                ORDER BY overall_ces_score DESC
                LIMIT 10
            """)
            csr_cultural = [dict(row) for row in cursor.fetchall()]
            trends["csr_insights"] = csr_cultural
            
            # Youth targeting trends
            cursor.execute("""
                SELECT campaign_name, brand, overall_ces_score, year
                FROM campaigns 
                WHERE targets_youth = 1
                ORDER BY overall_ces_score DESC
                LIMIT 10
            """)
            youth_campaigns = [dict(row) for row in cursor.fetchall()]
            trends["youth_campaigns"] = youth_campaigns
            
            # Summary statistics
            summary_queries = {
                "total_cultural": "SELECT COUNT(*) FROM campaigns WHERE uses_local_culture = 1",
                "total_csr": "SELECT COUNT(*) FROM campaigns WHERE is_csr_campaign = 1",
                "total_youth": "SELECT COUNT(*) FROM campaigns WHERE targets_youth = 1",
                "cultural_award_winners": "SELECT COUNT(*) FROM campaigns WHERE uses_local_culture = 1 AND won_award = 1",
                "avg_cultural_score": "SELECT AVG(cultural_relevance_score) FROM campaigns WHERE uses_local_culture = 1",
                "avg_overall_score": "SELECT AVG(overall_ces_score) FROM campaigns WHERE campaign_name IS NOT NULL"
            }
            
            summary = {}
            for key, query in summary_queries.items():
                cursor.execute(query)
                result = cursor.fetchone()[0]
                summary[key] = round(result, 2) if result and 'avg' in key else (result or 0)
            
            trends["summary"] = summary
        
        conn.close()
        
        return PHAwardsResponse(
            success=True,
            data=trends,
            timestamp=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Cultural trends error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve cultural trends: {str(e)}")

@router.post("/predict/award", response_model=PHAwardsResponse)
async def predict_award(
    request: AwardPredictionRequest,
    current_user: User = Depends(deps.get_current_active_user)
):
    """Predict award potential for campaign using AI analysis"""
    try:
        campaign_text = request.campaign_text.lower()
        
        # Enhanced prediction algorithm
        base_score = 45
        factors = {
            "award_indicators": [],
            "csr_elements": [],
            "cultural_elements": [],
            "innovation_markers": [],
            "emotional_triggers": []
        }
        
        # Award-winning keywords
        award_keywords = {
            'strong': ['grand prix', 'gold', 'winner', 'champion', 'best', 'outstanding'],
            'medium': ['silver', 'bronze', 'nominated', 'finalist', 'recognized'],
            'weak': ['award', 'competition', 'contest']
        }
        
        for strength, keywords in award_keywords.items():
            matches = [kw for kw in keywords if kw in campaign_text]
            factors["award_indicators"].extend(matches)
            if strength == 'strong':
                base_score += len(matches) * 15
            elif strength == 'medium':
                base_score += len(matches) * 10
            else:
                base_score += len(matches) * 5
        
        # CSR and social impact
        csr_keywords = ['csr', 'social responsibility', 'community', 'sustainability', 
                       'environment', 'social impact', 'giving back', 'charity']
        csr_matches = [kw for kw in csr_keywords if kw in campaign_text]
        factors["csr_elements"] = csr_matches
        base_score += len(csr_matches) * 8
        
        # Filipino cultural elements
        cultural_keywords = ['filipino', 'pinoy', 'pilipinas', 'bayanihan', 'kapamilya', 
                           'malasakit', 'pagmamahal', 'family', 'lola', 'lolo', 'nanay', 'tatay']
        cultural_matches = [kw for kw in cultural_keywords if kw in campaign_text]
        factors["cultural_elements"] = cultural_matches
        base_score += len(cultural_matches) * 7
        
        # Innovation markers
        innovation_keywords = ['digital', 'ai', 'technology', 'innovation', 'creative', 
                             'breakthrough', 'first', 'revolutionary']
        innovation_matches = [kw for kw in innovation_keywords if kw in campaign_text]
        factors["innovation_markers"] = innovation_matches
        base_score += len(innovation_matches) * 6
        
        # Emotional triggers
        emotion_keywords = ['inspiring', 'heartwarming', 'touching', 'emotional', 
                          'powerful', 'moving', 'tear-jerking', 'uplifting']
        emotion_matches = [kw for kw in emotion_keywords if kw in campaign_text]
        factors["emotional_triggers"] = emotion_matches
        base_score += len(emotion_matches) * 5
        
        # Cap score and determine confidence
        final_score = min(base_score, 95)
        
        if final_score >= 80:
            confidence = "very high"
            recommendation = "Excellent award potential - strong indicators across multiple categories"
        elif final_score >= 70:
            confidence = "high"
            recommendation = "Strong award potential - consider submitting to major award shows"
        elif final_score >= 60:
            confidence = "medium"
            recommendation = "Good potential - strengthen cultural or innovation elements"
        elif final_score >= 50:
            confidence = "low-medium"
            recommendation = "Moderate potential - consider adding more emotional or cultural depth"
        else:
            confidence = "low"
            recommendation = "Limited potential - campaign needs significant enhancement"
        
        prediction = {
            "award_probability": final_score,
            "confidence": confidence,
            "factors": factors,
            "recommendation": recommendation,
            "suggested_improvements": get_improvement_suggestions(factors, final_score)
        }
        
        return PHAwardsResponse(
            success=True,
            data=prediction,
            timestamp=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Award prediction error: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

def get_improvement_suggestions(factors: dict, score: int) -> List[str]:
    """Generate specific improvement suggestions based on analysis"""
    suggestions = []
    
    if len(factors["cultural_elements"]) == 0:
        suggestions.append("Add Filipino cultural elements like bayanihan spirit or family values")
    
    if len(factors["csr_elements"]) == 0:
        suggestions.append("Consider adding corporate social responsibility or community impact angle")
    
    if len(factors["emotional_triggers"]) == 0:
        suggestions.append("Strengthen emotional storytelling with inspiring or heartwarming elements")
    
    if len(factors["innovation_markers"]) == 0:
        suggestions.append("Highlight innovative or creative execution methods")
    
    if score < 60:
        suggestions.append("Consider partnering with local communities for authentic cultural connection")
        suggestions.append("Develop measurable social impact metrics to strengthen CSR positioning")
    
    return suggestions

@router.get("/campaigns/{campaign_id}")
async def get_campaign_details(
    campaign_id: int,
    current_user: User = Depends(deps.get_current_active_user)
):
    """Get detailed information about a specific campaign"""
    try:
        conn = get_ph_awards_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM campaigns WHERE id = ?', (campaign_id,))
        campaign = cursor.fetchone()
        
        if not campaign:
            raise HTTPException(status_code=404, detail="Campaign not found")
        
        campaign_dict = dict(campaign)
        
        # Get related campaigns (same brand or similar cultural elements)
        cursor.execute("""
            SELECT id, campaign_name, brand, overall_ces_score 
            FROM campaigns 
            WHERE (brand = ? OR uses_local_culture = ?) 
            AND id != ?
            ORDER BY overall_ces_score DESC
            LIMIT 5
        """, (campaign_dict['brand'], campaign_dict['uses_local_culture'], campaign_id))
        
        related_campaigns = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        
        return PHAwardsResponse(
            success=True,
            data={
                "campaign": campaign_dict,
                "related_campaigns": related_campaigns
            },
            timestamp=datetime.utcnow().isoformat()
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Campaign details error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve campaign: {str(e)}")

@router.get("/dashboard/summary")
async def get_dashboard_summary(
    current_user: User = Depends(deps.get_current_active_user)
):
    """Get summary data for PH Awards dashboard"""
    try:
        conn = get_ph_awards_db()
        cursor = conn.cursor()
        
        # Get key metrics
        cursor.execute("""
            SELECT 
                COUNT(*) as total_campaigns,
                COUNT(CASE WHEN won_award = 1 THEN 1 END) as award_winners,
                COUNT(CASE WHEN is_csr_campaign = 1 THEN 1 END) as csr_campaigns,
                COUNT(CASE WHEN uses_local_culture = 1 THEN 1 END) as cultural_campaigns,
                AVG(overall_ces_score) as avg_score,
                MAX(overall_ces_score) as highest_score
            FROM campaigns
            WHERE campaign_name IS NOT NULL
        """)
        
        summary = dict(cursor.fetchone())
        
        # Get recent top performers
        cursor.execute("""
            SELECT campaign_name, brand, overall_ces_score, year
            FROM campaigns 
            WHERE campaign_name IS NOT NULL
            ORDER BY overall_ces_score DESC
            LIMIT 5
        """)
        
        top_campaigns = [dict(row) for row in cursor.fetchall()]
        
        # Get trend data by year
        cursor.execute("""
            SELECT 
                year,
                COUNT(*) as campaigns,
                AVG(overall_ces_score) as avg_score,
                COUNT(CASE WHEN won_award = 1 THEN 1 END) as awards_won
            FROM campaigns 
            WHERE year IS NOT NULL AND campaign_name IS NOT NULL
            GROUP BY year
            ORDER BY year DESC
            LIMIT 5
        """)
        
        yearly_trends = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        
        return {
            "success": True,
            "data": {
                "summary": summary,
                "top_campaigns": top_campaigns,
                "yearly_trends": yearly_trends
            },
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Dashboard summary error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve dashboard data: {str(e)}")