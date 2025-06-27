# schemas/analytics.py
# Pydantic schemas for Scout Analytics API responses

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import date, datetime

class DashboardMetrics(BaseModel):
    total_sales: float
    total_profit: float
    total_orders: int
    profit_margin: float
    avg_order_value: float
    changes: Dict[str, str] = {
        "sales": "+12.5%",
        "profit": "+8.2%", 
        "orders": "+5.4%",
        "margin": "+2.1%"
    }

class SalesTrend(BaseModel):
    period: str  # "Jan", "Feb", etc. or "2024-01", etc.
    sales: float
    profit: float
    orders: int
    avg_order_value: float

class CategorySales(BaseModel):
    category: str
    sales: float
    profit: float
    orders: int
    avg_order_value: float

class TopProduct(BaseModel):
    product_id: str
    product_name: str
    category: str
    total_sales: float
    total_profit: float
    quantity_sold: int
    profit_margin: float

class GeographyAnalytics(BaseModel):
    region: str
    city: str
    total_sales: float
    total_profit: float
    orders: int
    avg_order_value: float

class TransactionResponse(BaseModel):
    id: int
    order_id: str
    order_date: date
    customer_name: Optional[str]
    product_name: Optional[str]
    category: Optional[str]
    sales: Optional[float]
    profit: Optional[float]
    quantity: Optional[int]
    region: Optional[str]
    city: Optional[str]
    
    class Config:
        from_attributes = True

class PRDDocument(BaseModel):
    title: str
    version: str
    date: str
    owner: str
    content: str
    format: str = "markdown"
    sections: List[str]
    metadata: Dict[str, Any]

class PRDSection(BaseModel):
    section: str
    title: str
    content: str
    format: str = "markdown"

class PRDSummary(BaseModel):
    document: Dict[str, str]
    key_features: List[str]
    architecture: Dict[str, Any]
    endpoints: Dict[str, str]
    deployment: Dict[str, Any]

class ImplementationStatus(BaseModel):
    overall_status: str
    services: Dict[str, Any]
    features_implemented: Dict[str, bool]
    next_steps: List[str]

# Request schemas
class TransactionCreate(BaseModel):
    order_id: str
    order_date: date
    customer_name: Optional[str] = None
    product_name: Optional[str] = None
    category: Optional[str] = None
    sales: Optional[float] = None
    profit: Optional[float] = None
    quantity: Optional[int] = None
    region: Optional[str] = None
    city: Optional[str] = None

class AnalyticsQuery(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    region: Optional[str] = None
    category: Optional[str] = None
    limit: Optional[int] = 100