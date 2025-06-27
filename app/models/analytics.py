# models/analytics.py
# Scout Analytics data models for SQLAlchemy

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, func, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# If you already have a Base, import it instead
# from .base import Base
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String(50), nullable=False, index=True)
    order_date = Column(Date, nullable=False, index=True)
    ship_date = Column(Date, nullable=True)
    ship_mode = Column(String(50), nullable=True)
    
    # Customer information
    customer_id = Column(String(50), nullable=True, index=True)
    customer_name = Column(String(100), nullable=True)
    segment = Column(String(50), nullable=True)
    
    # Product information
    product_id = Column(String(50), nullable=True, index=True)
    product_name = Column(String(255), nullable=True)
    category = Column(String(50), nullable=True, index=True)
    sub_category = Column(String(50), nullable=True)
    
    # Financial data
    sales = Column(Float, nullable=True)
    profit = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    discount = Column(Float, nullable=True)
    
    # Geographic data
    country_region = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True, index=True)
    postal_code = Column(String(20), nullable=True)
    region = Column(String(50), nullable=True, index=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Transaction(order_id='{self.order_id}', sales={self.sales})>"

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String(50), unique=True, nullable=False, index=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(50), nullable=False, index=True)
    sub_category = Column(String(50), nullable=True)
    brand = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product(product_id='{self.product_id}', name='{self.product_name}')>"

class Geography(Base):
    __tablename__ = "geography"
    
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String(100), nullable=False, index=True)
    city = Column(String(100), nullable=False, index=True)
    municipality = Column(String(100), nullable=True)
    barangay = Column(String(100), nullable=True)
    location = Column(String(150), nullable=True)
    coordinates = Column(String(100), nullable=True)  # Store as "lat,lng"
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Geography(region='{self.region}', city='{self.city}')>"

class AnalyticsSummary(Base):
    __tablename__ = "analytics_summary"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, unique=True, index=True)
    total_sales = Column(Float, nullable=False, default=0.0)
    total_profit = Column(Float, nullable=False, default=0.0)
    total_orders = Column(Integer, nullable=False, default=0)
    profit_margin = Column(Float, nullable=False, default=0.0)
    avg_order_value = Column(Float, nullable=False, default=0.0)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<AnalyticsSummary(date={self.date}, sales={self.total_sales})>"

# Optional: Create a view model for dashboard metrics
class DashboardView(Base):
    __tablename__ = "dashboard_metrics"
    __table_args__ = {'info': {'is_view': True}}
    
    total_orders = Column(Integer, primary_key=True)
    total_sales = Column(Float)
    total_profit = Column(Float)
    profit_margin = Column(Float)
    avg_order_value = Column(Float)