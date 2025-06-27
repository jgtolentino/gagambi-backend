-- Scout Analytics Database Schema
-- Run this on your Render MySQL database

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id VARCHAR(50) NOT NULL,
    order_date DATE NOT NULL,
    ship_date DATE,
    ship_mode VARCHAR(50),
    
    -- Customer information
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    
    -- Product information
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    
    -- Financial data
    sales DECIMAL(12,2),
    profit DECIMAL(12,2),
    quantity INT,
    discount DECIMAL(5,2),
    
    -- Geographic data
    country_region VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    
    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Indexes for performance
    INDEX idx_order_date (order_date),
    INDEX idx_customer_id (customer_id),
    INDEX idx_product_id (product_id),
    INDEX idx_category (category),
    INDEX idx_region (region),
    INDEX idx_city (city)
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50),
    brand VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_category (category),
    INDEX idx_sub_category (sub_category),
    INDEX idx_brand (brand)
);

-- Create geography table
CREATE TABLE IF NOT EXISTS geography (
    id INT PRIMARY KEY AUTO_INCREMENT,
    region VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    municipality VARCHAR(100),
    barangay VARCHAR(100),
    location VARCHAR(150),
    coordinates VARCHAR(100), -- Store as "lat,lng"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_region (region),
    INDEX idx_city (city),
    INDEX idx_municipality (municipality)
);

-- Create analytics summary table for performance
CREATE TABLE IF NOT EXISTS analytics_summary (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL UNIQUE,
    total_sales DECIMAL(15,2) NOT NULL DEFAULT 0,
    total_profit DECIMAL(15,2) NOT NULL DEFAULT 0,
    total_orders INT NOT NULL DEFAULT 0,
    profit_margin DECIMAL(5,2) NOT NULL DEFAULT 0,
    avg_order_value DECIMAL(10,2) NOT NULL DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_date (date)
);

-- Create view for dashboard metrics (optional)
CREATE OR REPLACE VIEW dashboard_metrics AS
SELECT 
    COUNT(*) as total_orders,
    COALESCE(SUM(sales), 0) as total_sales,
    COALESCE(SUM(profit), 0) as total_profit,
    CASE 
        WHEN SUM(sales) > 0 THEN (SUM(profit) / SUM(sales) * 100)
        ELSE 0 
    END as profit_margin,
    CASE 
        WHEN COUNT(*) > 0 THEN (SUM(sales) / COUNT(*))
        ELSE 0 
    END as avg_order_value
FROM transactions;

-- Insert sample geography data
INSERT IGNORE INTO geography (region, city, municipality) VALUES
('NCR', 'Manila', 'Manila'),
('NCR', 'Quezon City', 'Quezon City'),
('NCR', 'Makati', 'Makati'),
('NCR', 'Taguig', 'Taguig'),
('Central Luzon', 'Angeles', 'Angeles'),
('Central Luzon', 'San Fernando', 'San Fernando'),
('Southern Luzon', 'Batangas', 'Batangas'),
('Southern Luzon', 'Lipa', 'Lipa'),
('Visayas', 'Cebu City', 'Cebu'),
('Visayas', 'Iloilo', 'Iloilo'),
('Mindanao', 'Davao', 'Davao'),
('Mindanao', 'Cagayan de Oro', 'Cagayan de Oro');

-- Insert sample products
INSERT IGNORE INTO products (product_id, product_name, category, sub_category, brand) VALUES
('ELEC-001', 'iPhone 14', 'Electronics', 'Smartphones', 'Apple'),
('ELEC-002', 'Samsung Galaxy S23', 'Electronics', 'Smartphones', 'Samsung'),
('ELEC-003', 'MacBook Air', 'Electronics', 'Laptops', 'Apple'),
('CLTH-001', 'Nike T-Shirt', 'Clothing', 'Mens Wear', 'Nike'),
('CLTH-002', 'Adidas Shoes', 'Clothing', 'Footwear', 'Adidas'),
('HOME-001', 'IKEA Sofa', 'Home & Garden', 'Furniture', 'IKEA'),
('FOOD-001', 'Coca-Cola 1.5L', 'Food & Beverage', 'Beverages', 'Coca-Cola'),
('FOOD-002', 'Lays Chips', 'Food & Beverage', 'Snacks', 'Lays'),
('SPRT-001', 'Basketball', 'Sports', 'Equipment', 'Spalding'),
('SPRT-002', 'Tennis Racket', 'Sports', 'Equipment', 'Wilson');

-- Create stored procedure for daily analytics update
DELIMITER //
CREATE PROCEDURE UpdateDailyAnalytics(IN target_date DATE)
BEGIN
    INSERT INTO analytics_summary (date, total_sales, total_profit, total_orders, profit_margin, avg_order_value)
    SELECT 
        target_date,
        COALESCE(SUM(sales), 0),
        COALESCE(SUM(profit), 0),
        COUNT(*),
        CASE 
            WHEN SUM(sales) > 0 THEN (SUM(profit) / SUM(sales) * 100)
            ELSE 0 
        END,
        CASE 
            WHEN COUNT(*) > 0 THEN (SUM(sales) / COUNT(*))
            ELSE 0 
        END
    FROM transactions 
    WHERE order_date = target_date
    ON DUPLICATE KEY UPDATE
        total_sales = VALUES(total_sales),
        total_profit = VALUES(total_profit),
        total_orders = VALUES(total_orders),
        profit_margin = VALUES(profit_margin),
        avg_order_value = VALUES(avg_order_value),
        updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;

-- Verify tables were created
SHOW TABLES LIKE '%transaction%';
SHOW TABLES LIKE '%product%';
SHOW TABLES LIKE '%geography%';
SHOW TABLES LIKE '%analytics%';

-- Display table structures
DESCRIBE transactions;
DESCRIBE products;
DESCRIBE geography;
DESCRIBE analytics_summary;