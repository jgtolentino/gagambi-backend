-- Sample data for Scout Analytics
-- Generated for testing purposes

-- Insert sample geography data (comprehensive Philippines data)
INSERT IGNORE INTO geography (region, city, municipality, barangay, location, coordinates) VALUES
-- NCR
('NCR', 'Manila', 'Manila', 'Ermita', 'Manila, NCR, Philippines', '14.588287,120.970134'),
('NCR', 'Manila', 'Manila', 'Malate', 'Manila, NCR, Philippines', '14.575042,120.985003'),
('NCR', 'Manila', 'Manila', 'Intramuros', 'Manila, NCR, Philippines', '14.590600,120.975311'),
('NCR', 'Quezon City', 'Quezon City', 'Diliman', 'Quezon City, NCR, Philippines', '14.654853,121.068314'),
('NCR', 'Quezon City', 'Quezon City', 'Project 4', 'Quezon City, NCR, Philippines', '14.631228,121.067982'),
('NCR', 'Quezon City', 'Quezon City', 'Cubao', 'Quezon City, NCR, Philippines', '14.619534,121.051318'),
('NCR', 'Makati', 'Makati', 'Poblacion', 'Makati, NCR, Philippines', '14.553516,121.018075'),
('NCR', 'Makati', 'Makati', 'Salcedo Village', 'Makati, NCR, Philippines', '14.556025,121.025284'),
('NCR', 'Makati', 'Makati', 'Legazpi Village', 'Makati, NCR, Philippines', '14.555684,121.015311'),
('NCR', 'Taguig', 'Taguig', 'Bonifacio Global City', 'Taguig, NCR, Philippines', '14.551213,121.048023'),
('NCR', 'Taguig', 'Taguig', 'Fort Bonifacio', 'Taguig, NCR, Philippines', '14.544800,121.045311'),
('NCR', 'Taguig', 'Taguig', 'McKinley Hill', 'Taguig, NCR, Philippines', '14.550025,121.051284'),

-- Central Luzon
('Central Luzon', 'Angeles', 'Angeles', 'Balibago', 'Angeles, Central Luzon, Philippines', '15.145042,120.589003'),
('Central Luzon', 'Angeles', 'Angeles', 'Malabanas', 'Angeles, Central Luzon, Philippines', '15.155042,120.579003'),
('Central Luzon', 'Angeles', 'Angeles', 'Santo Rosario', 'Angeles, Central Luzon, Philippines', '15.165042,120.569003'),
('Central Luzon', 'San Fernando', 'San Fernando', 'Del Pilar', 'San Fernando, Central Luzon, Philippines', '15.025042,120.689003'),
('Central Luzon', 'San Fernando', 'San Fernando', 'Santo Niño', 'San Fernando, Central Luzon, Philippines', '15.035042,120.679003'),
('Central Luzon', 'San Fernando', 'San Fernando', 'Sindalan', 'San Fernando, Central Luzon, Philippines', '15.045042,120.669003'),

-- Southern Luzon
('Southern Luzon', 'Batangas', 'Batangas', 'Poblacion', 'Batangas, Southern Luzon, Philippines', '13.765042,121.089003'),
('Southern Luzon', 'Batangas', 'Batangas', 'Alangilan', 'Batangas, Southern Luzon, Philippines', '13.775042,121.079003'),
('Southern Luzon', 'Batangas', 'Batangas', 'Kumintang Ilaya', 'Batangas, Southern Luzon, Philippines', '13.785042,121.069003'),
('Southern Luzon', 'Lipa', 'Lipa', 'Poblacion', 'Lipa, Southern Luzon, Philippines', '13.945042,121.169003'),
('Southern Luzon', 'Lipa', 'Lipa', 'Tambo', 'Lipa, Southern Luzon, Philippines', '13.955042,121.159003'),
('Southern Luzon', 'Lipa', 'Lipa', 'Banaybanay', 'Lipa, Southern Luzon, Philippines', '13.965042,121.149003'),

-- Visayas
('Visayas', 'Cebu City', 'Cebu', 'Lahug', 'Cebu City, Visayas, Philippines', '10.335042,123.889003'),
('Visayas', 'Cebu City', 'Cebu', 'Capitol Site', 'Cebu City, Visayas, Philippines', '10.325042,123.899003'),
('Visayas', 'Cebu City', 'Cebu', 'IT Park', 'Cebu City, Visayas, Philippines', '10.315042,123.909003'),
('Visayas', 'Iloilo', 'Iloilo', 'La Paz', 'Iloilo, Visayas, Philippines', '10.725042,122.569003'),
('Visayas', 'Iloilo', 'Iloilo', 'Jaro', 'Iloilo, Visayas, Philippines', '10.735042,122.559003'),
('Visayas', 'Iloilo', 'Iloilo', 'Molo', 'Iloilo, Visayas, Philippines', '10.745042,122.549003'),

-- Mindanao
('Mindanao', 'Davao', 'Davao', 'Poblacion', 'Davao, Mindanao, Philippines', '7.095042,125.609003'),
('Mindanao', 'Davao', 'Davao', 'Agdao', 'Davao, Mindanao, Philippines', '7.085042,125.619003'),
('Mindanao', 'Davao', 'Davao', 'Buhangin', 'Davao, Mindanao, Philippines', '7.075042,125.629003'),
('Mindanao', 'Cagayan de Oro', 'Cagayan de Oro', 'Carmen', 'Cagayan de Oro, Mindanao, Philippines', '8.485042,124.649003'),
('Mindanao', 'Cagayan de Oro', 'Cagayan de Oro', 'Lapasan', 'Cagayan de Oro, Mindanao, Philippines', '8.475042,124.659003'),
('Mindanao', 'Cagayan de Oro', 'Cagayan de Oro', 'Nazareth', 'Cagayan de Oro, Mindanao, Philippines', '8.465042,124.669003');

-- Insert comprehensive product data
INSERT IGNORE INTO products (product_id, product_name, category, sub_category, brand) VALUES
-- Electronics
('ELEC-SMARTPHONE-01', 'iPhone 14 Pro', 'Electronics', 'Smartphones', 'Apple'),
('ELEC-SMARTPHONE-02', 'Samsung Galaxy S23', 'Electronics', 'Smartphones', 'Samsung'),
('ELEC-SMARTPHONE-03', 'Huawei P50', 'Electronics', 'Smartphones', 'Huawei'),
('ELEC-SMARTPHONE-04', 'Xiaomi 13', 'Electronics', 'Smartphones', 'Xiaomi'),
('ELEC-SMARTPHONE-05', 'OPPO Find X5', 'Electronics', 'Smartphones', 'OPPO'),

('ELEC-LAPTOP-01', 'MacBook Air M2', 'Electronics', 'Laptops', 'Apple'),
('ELEC-LAPTOP-02', 'Dell XPS 13', 'Electronics', 'Laptops', 'Dell'),
('ELEC-LAPTOP-03', 'HP Spectre x360', 'Electronics', 'Laptops', 'HP'),
('ELEC-LAPTOP-04', 'ASUS ZenBook', 'Electronics', 'Laptops', 'ASUS'),
('ELEC-LAPTOP-05', 'Lenovo ThinkPad', 'Electronics', 'Laptops', 'Lenovo'),

('ELEC-TABLET-01', 'iPad Air', 'Electronics', 'Tablets', 'Apple'),
('ELEC-TABLET-02', 'Samsung Galaxy Tab S8', 'Electronics', 'Tablets', 'Samsung'),
('ELEC-TABLET-03', 'Microsoft Surface Pro', 'Electronics', 'Tablets', 'Microsoft'),
('ELEC-TABLET-04', 'Huawei MatePad', 'Electronics', 'Tablets', 'Huawei'),
('ELEC-TABLET-05', 'Lenovo Tab P11', 'Electronics', 'Tablets', 'Lenovo'),

-- Clothing
('CLTH-MENS-01', 'Nike Dri-FIT T-Shirt', 'Clothing', 'Mens Wear', 'Nike'),
('CLTH-MENS-02', 'Adidas Originals Hoodie', 'Clothing', 'Mens Wear', 'Adidas'),
('CLTH-MENS-03', 'Uniqlo Cotton Polo', 'Clothing', 'Mens Wear', 'Uniqlo'),
('CLTH-MENS-04', 'H&M Slim Fit Jeans', 'Clothing', 'Mens Wear', 'H&M'),
('CLTH-MENS-05', 'Zara Oxford Shirt', 'Clothing', 'Mens Wear', 'Zara'),

('CLTH-WOMENS-01', 'Nike Yoga Pants', 'Clothing', 'Womens Wear', 'Nike'),
('CLTH-WOMENS-02', 'Zara Floral Dress', 'Clothing', 'Womens Wear', 'Zara'),
('CLTH-WOMENS-03', 'H&M Denim Jacket', 'Clothing', 'Womens Wear', 'H&M'),
('CLTH-WOMENS-04', 'Uniqlo Cashmere Sweater', 'Clothing', 'Womens Wear', 'Uniqlo'),
('CLTH-WOMENS-05', 'Adidas Sports Bra', 'Clothing', 'Womens Wear', 'Adidas'),

('CLTH-FOOTWEAR-01', 'Nike Air Max', 'Clothing', 'Footwear', 'Nike'),
('CLTH-FOOTWEAR-02', 'Adidas Ultraboost', 'Clothing', 'Footwear', 'Adidas'),
('CLTH-FOOTWEAR-03', 'Converse Chuck Taylor', 'Clothing', 'Footwear', 'Converse'),
('CLTH-FOOTWEAR-04', 'Vans Old Skool', 'Clothing', 'Footwear', 'Vans'),
('CLTH-FOOTWEAR-05', 'New Balance 990', 'Clothing', 'Footwear', 'New Balance'),

-- Home & Garden
('HOME-FURNITURE-01', 'IKEA MALM Bed Frame', 'Home & Garden', 'Furniture', 'IKEA'),
('HOME-FURNITURE-02', 'Ashley Sectional Sofa', 'Home & Garden', 'Furniture', 'Ashley'),
('HOME-FURNITURE-03', 'West Elm Dining Table', 'Home & Garden', 'Furniture', 'West Elm'),
('HOME-FURNITURE-04', 'CB2 Office Chair', 'Home & Garden', 'Furniture', 'CB2'),
('HOME-FURNITURE-05', 'Pottery Barn Bookshelf', 'Home & Garden', 'Furniture', 'Pottery Barn'),

('HOME-KITCHEN-01', 'KitchenAid Stand Mixer', 'Home & Garden', 'Kitchen', 'KitchenAid'),
('HOME-KITCHEN-02', 'Instant Pot Pressure Cooker', 'Home & Garden', 'Kitchen', 'Instant Pot'),
('HOME-KITCHEN-03', 'Cuisinart Food Processor', 'Home & Garden', 'Kitchen', 'Cuisinart'),
('HOME-KITCHEN-04', 'Ninja Blender', 'Home & Garden', 'Kitchen', 'Ninja'),
('HOME-KITCHEN-05', 'Breville Espresso Machine', 'Home & Garden', 'Kitchen', 'Breville'),

-- Sports
('SPRT-EQUIPMENT-01', 'Spalding Basketball', 'Sports', 'Equipment', 'Spalding'),
('SPRT-EQUIPMENT-02', 'Wilson Tennis Racket', 'Sports', 'Equipment', 'Wilson'),
('SPRT-EQUIPMENT-03', 'Callaway Golf Clubs', 'Sports', 'Equipment', 'Callaway'),
('SPRT-EQUIPMENT-04', 'YETI Cooler', 'Sports', 'Equipment', 'YETI'),
('SPRT-EQUIPMENT-05', 'Coleman Camping Tent', 'Sports', 'Equipment', 'Coleman'),

-- Food & Beverage
('FOOD-BEVERAGES-01', 'Coca-Cola 1.5L', 'Food & Beverage', 'Beverages', 'Coca-Cola'),
('FOOD-BEVERAGES-02', 'Pepsi 2L', 'Food & Beverage', 'Beverages', 'Pepsi'),
('FOOD-BEVERAGES-03', 'San Miguel Beer', 'Food & Beverage', 'Beverages', 'San Miguel'),
('FOOD-BEVERAGES-04', 'Nestea Iced Tea', 'Food & Beverage', 'Beverages', 'Nestle'),
('FOOD-BEVERAGES-05', 'Red Bull Energy Drink', 'Food & Beverage', 'Beverages', 'Red Bull'),

('FOOD-SNACKS-01', 'Lays Potato Chips', 'Food & Beverage', 'Snacks', 'Lays'),
('FOOD-SNACKS-02', 'Pringles Original', 'Food & Beverage', 'Snacks', 'Pringles'),
('FOOD-SNACKS-03', 'Oreo Cookies', 'Food & Beverage', 'Snacks', 'Oreo'),
('FOOD-SNACKS-04', 'KitKat Chocolate', 'Food & Beverage', 'Snacks', 'KitKat'),
('FOOD-SNACKS-05', 'Doritos Nacho Cheese', 'Food & Beverage', 'Snacks', 'Doritos');

-- Sample transaction data with realistic Philippines retail scenarios
INSERT INTO transactions (order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, product_id, product_name, category, sub_category, sales, profit, quantity, discount, country_region, state, city, postal_code, region) VALUES
-- Recent transactions (last 30 days)
('ORD-000001', '2024-12-01', '2024-12-03', 'Standard Class', 'CU-1001', 'Maria Santos', 'Consumer', 'ELEC-SMARTPHONE-01', 'iPhone 14 Pro', 'Electronics', 'Smartphones', 65000.00, 13000.00, 1, 0.100, 'Philippines', 'NCR', 'Manila', '1000', 'NCR'),
('ORD-000002', '2024-12-01', '2024-12-02', 'Same Day', 'CU-1002', 'Jose Cruz', 'Corporate', 'ELEC-LAPTOP-01', 'MacBook Air M2', 'Electronics', 'Laptops', 75000.00, 22500.00, 1, 0.050, 'Philippines', 'NCR', 'Makati', '1200', 'NCR'),
('ORD-000003', '2024-12-02', '2024-12-04', 'Standard Class', 'CU-1003', 'Ana Reyes', 'Consumer', 'CLTH-WOMENS-01', 'Nike Yoga Pants', 'Clothing', 'Womens Wear', 3500.00, 1400.00, 2, 0.000, 'Philippines', 'NCR', 'Quezon City', '1100', 'NCR'),
('ORD-000004', '2024-12-02', '2024-12-05', 'Second Class', 'CU-1004', 'Juan Bautista', 'Home Office', 'HOME-KITCHEN-01', 'KitchenAid Stand Mixer', 'Home & Garden', 'Kitchen', 18000.00, 5400.00, 1, 0.200, 'Philippines', 'Central Luzon', 'Angeles', '2009', 'Central Luzon'),
('ORD-000005', '2024-12-03', '2024-12-06', 'Standard Class', 'CU-1005', 'Carmen Garcia', 'Consumer', 'FOOD-BEVERAGES-01', 'Coca-Cola 1.5L', 'Food & Beverage', 'Beverages', 240.00, 72.00, 12, 0.150, 'Philippines', 'Southern Luzon', 'Batangas', '4200', 'Southern Luzon'),

-- Holiday season transactions (December)
('ORD-000006', '2024-12-05', '2024-12-07', 'First Class', 'CU-1006', 'Antonio Mendoza', 'Corporate', 'ELEC-TABLET-01', 'iPad Air', 'Electronics', 'Tablets', 35000.00, 10500.00, 2, 0.100, 'Philippines', 'Visayas', 'Cebu City', '6000', 'Visayas'),
('ORD-000007', '2024-12-08', '2024-12-10', 'Standard Class', 'CU-1007', 'Dolores Torres', 'Consumer', 'CLTH-FOOTWEAR-01', 'Nike Air Max', 'Clothing', 'Footwear', 8500.00, 2550.00, 1, 0.050, 'Philippines', 'NCR', 'Taguig', '1630', 'NCR'),
('ORD-000008', '2024-12-10', '2024-12-12', 'Same Day', 'CU-1008', 'David Ocampo', 'Home Office', 'SPRT-EQUIPMENT-01', 'Spalding Basketball', 'Sports', 'Equipment', 2500.00, 750.00, 3, 0.000, 'Philippines', 'Mindanao', 'Davao', '8000', 'Mindanao'),
('ORD-000009', '2024-12-12', '2024-12-14', 'Standard Class', 'CU-1009', 'Teresa Tomas', 'Consumer', 'HOME-FURNITURE-01', 'IKEA MALM Bed Frame', 'Home & Garden', 'Furniture', 12000.00, 3600.00, 1, 0.250, 'Philippines', 'Central Luzon', 'San Fernando', '2000', 'Central Luzon'),
('ORD-000010', '2024-12-15', '2024-12-17', 'Second Class', 'CU-1010', 'Jorge Andres', 'Corporate', 'ELEC-SMARTPHONE-02', 'Samsung Galaxy S23', 'Electronics', 'Smartphones', 45000.00, 13500.00, 1, 0.100, 'Philippines', 'Visayas', 'Iloilo', '5000', 'Visayas'),

-- Black Friday / Cyber Monday deals (November)
('ORD-000011', '2024-11-29', '2024-12-01', 'First Class', 'CU-1011', 'Luz Marquez', 'Consumer', 'ELEC-LAPTOP-02', 'Dell XPS 13', 'Electronics', 'Laptops', 60000.00, 15000.00, 1, 0.300, 'Philippines', 'NCR', 'Manila', '1000', 'NCR'),
('ORD-000012', '2024-11-29', '2024-12-02', 'Standard Class', 'CU-1012', 'Pedro Romualdez', 'Home Office', 'HOME-KITCHEN-02', 'Instant Pot Pressure Cooker', 'Home & Garden', 'Kitchen', 8000.00, 2400.00, 1, 0.200, 'Philippines', 'Southern Luzon', 'Lipa', '4217', 'Southern Luzon'),
('ORD-000013', '2024-12-01', '2024-12-03', 'Same Day', 'CU-1013', 'Esperanza Mercado', 'Consumer', 'CLTH-MENS-01', 'Nike Dri-FIT T-Shirt', 'Clothing', 'Mens Wear', 2400.00, 720.00, 3, 0.200, 'Philippines', 'Mindanao', 'Cagayan de Oro', '9000', 'Mindanao'),

-- Regular monthly transactions  
('ORD-000014', '2024-11-15', '2024-11-17', 'Standard Class', 'CU-1014', 'Jesus Aguilar', 'Corporate', 'SPRT-EQUIPMENT-02', 'Wilson Tennis Racket', 'Sports', 'Equipment', 7500.00, 2250.00, 1, 0.100, 'Philippines', 'NCR', 'Makati', '1200', 'NCR'),
('ORD-000015', '2024-11-10', '2024-11-12', 'Second Class', 'CU-1015', 'Concepcion Flores', 'Consumer', 'FOOD-SNACKS-01', 'Lays Potato Chips', 'Food & Beverage', 'Snacks', 480.00, 144.00, 24, 0.100, 'Philippines', 'Central Luzon', 'Angeles', '2009', 'Central Luzon'),
('ORD-000016', '2024-10-25', '2024-10-27', 'Standard Class', 'CU-1016', 'Rafael Ramos', 'Home Office', 'HOME-FURNITURE-02', 'Ashley Sectional Sofa', 'Home & Garden', 'Furniture', 45000.00, 13500.00, 1, 0.150, 'Philippines', 'Visayas', 'Cebu City', '6000', 'Visayas'),
('ORD-000017', '2024-10-20', '2024-10-22', 'First Class', 'CU-1017', 'Dolores Valdez', 'Consumer', 'ELEC-TABLET-02', 'Samsung Galaxy Tab S8', 'Electronics', 'Tablets', 25000.00, 7500.00, 1, 0.200, 'Philippines', 'Southern Luzon', 'Batangas', '4200', 'Southern Luzon'),
('ORD-000018', '2024-10-15', '2024-10-17', 'Standard Class', 'CU-1018', 'Francisco Castillo', 'Corporate', 'CLTH-FOOTWEAR-02', 'Adidas Ultraboost', 'Clothing', 'Footwear', 9500.00, 2850.00, 1, 0.050, 'Philippines', 'Mindanao', 'Davao', '8000', 'Mindanao'),
('ORD-000019', '2024-10-10', '2024-10-12', 'Same Day', 'CU-1019', 'Manuel Aquino', 'Consumer', 'FOOD-BEVERAGES-02', 'Pepsi 2L', 'Food & Beverage', 'Beverages', 320.00, 96.00, 16, 0.050, 'Philippines', 'NCR', 'Quezon City', '1100', 'NCR'),
('ORD-000020', '2024-09-30', '2024-10-02', 'Standard Class', 'CU-1020', 'Josefa Santos', 'Home Office', 'ELEC-SMARTPHONE-03', 'Huawei P50', 'Electronics', 'Smartphones', 35000.00, 10500.00, 1, 0.150, 'Philippines', 'Central Luzon', 'San Fernando', '2000', 'Central Luzon');

-- Update analytics summary for recent dates
INSERT INTO analytics_summary (date, total_sales, total_profit, total_orders, profit_margin, avg_order_value) VALUES
('2024-12-01', 140000.00, 35500.00, 2, 25.36, 70000.00),
('2024-12-02', 21500.00, 6800.00, 2, 31.63, 10750.00),
('2024-12-03', 240.00, 72.00, 1, 30.00, 240.00),
('2024-12-05', 35000.00, 10500.00, 1, 30.00, 35000.00),
('2024-12-08', 8500.00, 2550.00, 1, 30.00, 8500.00),
('2024-12-10', 2500.00, 750.00, 1, 30.00, 2500.00),
('2024-12-12', 12000.00, 3600.00, 1, 30.00, 12000.00),
('2024-12-15', 45000.00, 13500.00, 1, 30.00, 45000.00),
('2024-11-29', 68000.00, 17400.00, 2, 25.59, 34000.00),
('2024-12-01', 2400.00, 720.00, 1, 30.00, 2400.00)
ON DUPLICATE KEY UPDATE
total_sales = VALUES(total_sales),
total_profit = VALUES(total_profit),
total_orders = VALUES(total_orders),
profit_margin = VALUES(profit_margin),
avg_order_value = VALUES(avg_order_value);

-- Verify data was inserted
SELECT 'Sample data loaded successfully!' as status;
SELECT COUNT(*) as transaction_count FROM transactions;
SELECT COUNT(*) as product_count FROM products;
SELECT COUNT(*) as geography_count FROM geography;
SELECT SUM(sales) as total_sales, SUM(profit) as total_profit FROM transactions;