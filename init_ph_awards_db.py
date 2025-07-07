"""
Initialize PH Awards SQLite database with sample data
Run this on startup if database doesn't exist
"""

import sqlite3
import os
from datetime import datetime

def create_database():
    """Create SQLite database with PH Awards schema and sample data"""
    
    # Create database
    conn = sqlite3.connect('ces_intelligence.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        filepath TEXT NOT NULL,
        file_extension TEXT,
        file_size INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        processed_at DATETIME
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id INTEGER REFERENCES files(id),
        campaign_name TEXT,
        brand TEXT,
        year INTEGER,
        category TEXT,
        
        -- Award information
        won_award BOOLEAN DEFAULT 0,
        award_show TEXT,
        award_level TEXT,
        award_category TEXT,
        
        -- Campaign classification indicators
        is_csr_campaign BOOLEAN DEFAULT 0,
        is_purpose_driven BOOLEAN DEFAULT 0,
        is_social_impact BOOLEAN DEFAULT 0,
        has_environmental_angle BOOLEAN DEFAULT 0,
        targets_youth BOOLEAN DEFAULT 0,
        uses_local_culture BOOLEAN DEFAULT 0,
        
        -- CES Scores (0-10 scale)
        overall_ces_score REAL,
        message_clarity_score REAL,
        emotional_impact_score REAL,
        cultural_relevance_score REAL,
        innovation_score REAL,
        execution_score REAL,
        award_likelihood REAL,
        
        -- Metadata
        confidence_level REAL,
        feature_count INTEGER DEFAULT 0,
        metric_count INTEGER DEFAULT 0,
        cultural_insight_count INTEGER DEFAULT 0,
        
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create indexes
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_campaigns_brand ON campaigns(brand)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_campaigns_year ON campaigns(year)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_campaigns_ces_score ON campaigns(overall_ces_score)")
    
    # Insert sample data
    sample_campaigns = [
        {
            'campaign_name': 'Jollibee Kwentong Jollibee: Pasko',
            'brand': 'Jollibee',
            'year': 2023,
            'category': 'QSR/Food',
            'won_award': 1,
            'award_show': 'Adobo Design Awards',
            'award_level': 'Gold',
            'is_csr_campaign': 0,
            'uses_local_culture': 1,
            'overall_ces_score': 9.2,
            'cultural_relevance_score': 9.8,
            'emotional_impact_score': 9.5
        },
        {
            'campaign_name': 'Globe #CreateCourage Anti-Cyberbullying',
            'brand': 'Globe Telecom',
            'year': 2023,
            'category': 'Telco',
            'won_award': 1,
            'award_show': 'PANAta Awards',
            'award_level': 'Silver',
            'is_csr_campaign': 1,
            'targets_youth': 1,
            'overall_ces_score': 8.8,
            'social_impact_score': 9.2,
            'message_clarity_score': 8.9
        },
        {
            'campaign_name': 'San Miguel Walang Iwanan',
            'brand': 'San Miguel Corporation',
            'year': 2023,
            'category': 'Beverage',
            'won_award': 0,
            'is_csr_campaign': 1,
            'uses_local_culture': 1,
            'overall_ces_score': 8.5,
            'cultural_relevance_score': 9.0,
            'emotional_impact_score': 8.7
        },
        {
            'campaign_name': 'BDO We Find Ways',
            'brand': 'BDO',
            'year': 2023,
            'category': 'Banking',
            'won_award': 0,
            'is_purpose_driven': 1,
            'overall_ces_score': 7.9,
            'message_clarity_score': 8.5,
            'execution_score': 8.2
        },
        {
            'campaign_name': 'Safeguard Laban Moms',
            'brand': 'Safeguard',
            'year': 2023,
            'category': 'FMCG',
            'won_award': 1,
            'award_show': 'Kidlat Awards',
            'award_level': 'Bronze',
            'uses_local_culture': 1,
            'overall_ces_score': 8.3,
            'cultural_relevance_score': 8.8,
            'emotional_impact_score': 8.5
        }
    ]
    
    for campaign in sample_campaigns:
        columns = ', '.join(campaign.keys())
        placeholders = ', '.join(['?' for _ in campaign])
        values = list(campaign.values())
        
        cursor.execute(f"""
            INSERT INTO campaigns ({columns})
            VALUES ({placeholders})
        """, values)
    
    conn.commit()
    print(f"✅ Database created with {len(sample_campaigns)} sample campaigns")
    
    # Verify data
    cursor.execute("SELECT COUNT(*) FROM campaigns")
    count = cursor.fetchone()[0]
    print(f"✅ Verified: {count} campaigns in database")
    
    conn.close()
    return True

def init_database():
    """Initialize database if it doesn't exist"""
    if not os.path.exists('ces_intelligence.db'):
        print("📦 Creating PH Awards database...")
        return create_database()
    else:
        print("✅ Database already exists")
        return True

if __name__ == "__main__":
    init_database()