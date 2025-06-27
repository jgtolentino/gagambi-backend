# utils/sample_data.py
# Sample data generator for Scout Analytics

import random
import json
from datetime import datetime, date, timedelta
from typing import List, Dict, Any
from decimal import Decimal

class SampleDataGenerator:
    """Generate sample data for Scout Analytics"""
    
    def __init__(self):
        self.categories = [
            "Electronics", "Clothing", "Home & Garden", "Sports", 
            "Food & Beverage", "Books", "Automotive", "Health & Beauty"
        ]
        
        self.sub_categories = {
            "Electronics": ["Smartphones", "Laptops", "Tablets", "Accessories"],
            "Clothing": ["Mens Wear", "Womens Wear", "Kids Wear", "Footwear"],
            "Home & Garden": ["Furniture", "Kitchen", "Garden", "Decor"],
            "Sports": ["Equipment", "Apparel", "Outdoor", "Fitness"],
            "Food & Beverage": ["Beverages", "Snacks", "Groceries", "Frozen"],
            "Books": ["Fiction", "Non-Fiction", "Educational", "Magazines"],
            "Automotive": ["Parts", "Accessories", "Tools", "Care"],
            "Health & Beauty": ["Skincare", "Makeup", "Supplements", "Personal Care"]
        }
        
        self.regions = [
            "NCR", "Central Luzon", "Southern Luzon", "Visayas", "Mindanao"
        ]
        
        self.cities = {
            "NCR": ["Manila", "Quezon City", "Makati", "Taguig", "Pasig"],
            "Central Luzon": ["Angeles", "San Fernando", "Cabanatuan", "Malolos"],
            "Southern Luzon": ["Batangas", "Lipa", "Calamba", "Lucena"],
            "Visayas": ["Cebu City", "Iloilo", "Bacolod", "Tacloban"],
            "Mindanao": ["Davao", "Cagayan de Oro", "Zamboanga", "Butuan"]
        }
        
        self.segments = ["Consumer", "Corporate", "Home Office"]
        self.ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
        
        self.first_names = [
            "Maria", "Jose", "Juan", "Ana", "Antonio", "Carmen", "Manuel", 
            "Josefa", "Francisco", "Dolores", "David", "Teresa", "Jorge",
            "Luz", "Pedro", "Esperanza", "Jesus", "Concepcion", "Rafael"
        ]
        
        self.last_names = [
            "Santos", "Reyes", "Cruz", "Bautista", "Ocampo", "Garcia", "Mendoza",
            "Torres", "Tomas", "Andres", "Marquez", "Romualdez", "Mercado",
            "Aguilar", "Flores", "Ramos", "Valdez", "Castillo", "Aquino"
        ]

    def generate_transaction_data(self, num_records: int = 1000) -> List[Dict[str, Any]]:
        """Generate sample transaction data"""
        transactions = []
        
        for i in range(num_records):
            # Generate basic info
            order_date = self._random_date(days_back=365)
            ship_date = order_date + timedelta(days=random.randint(1, 10))
            
            # Generate customer
            customer_id = f"CU-{random.randint(1000, 9999)}"
            customer_name = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"
            
            # Generate product
            category = random.choice(self.categories)
            sub_category = random.choice(self.sub_categories[category])
            product_id = f"PROD-{category[:4].upper()}-{random.randint(100, 999)}"
            product_name = f"{sub_category} Item {random.randint(1, 100)}"
            
            # Generate location
            region = random.choice(self.regions)
            city = random.choice(self.cities[region])
            
            # Generate financial data
            quantity = random.randint(1, 10)
            base_price = random.uniform(500, 50000)  # PHP
            discount = random.uniform(0, 0.3)  # 0-30% discount
            sales = round(base_price * quantity * (1 - discount), 2)
            profit_margin = random.uniform(0.1, 0.4)  # 10-40% profit margin
            profit = round(sales * profit_margin, 2)
            
            transaction = {
                "order_id": f"ORD-{i+1:06d}",
                "order_date": order_date.strftime("%Y-%m-%d"),
                "ship_date": ship_date.strftime("%Y-%m-%d"),
                "ship_mode": random.choice(self.ship_modes),
                "customer_id": customer_id,
                "customer_name": customer_name,
                "segment": random.choice(self.segments),
                "product_id": product_id,
                "product_name": product_name,
                "category": category,
                "sub_category": sub_category,
                "sales": sales,
                "profit": profit,
                "quantity": quantity,
                "discount": round(discount, 3),
                "country_region": "Philippines",
                "state": region,
                "city": city,
                "postal_code": f"{random.randint(1000, 9999)}",
                "region": region
            }
            
            transactions.append(transaction)
        
        return transactions

    def generate_product_data(self) -> List[Dict[str, Any]]:
        """Generate sample product data"""
        products = []
        
        brands = {
            "Electronics": ["Apple", "Samsung", "Sony", "LG", "Huawei"],
            "Clothing": ["Nike", "Adidas", "Uniqlo", "H&M", "Zara"],
            "Home & Garden": ["IKEA", "Ashley", "Philips", "Black & Decker"],
            "Sports": ["Nike", "Adidas", "Under Armour", "Puma", "Wilson"],
            "Food & Beverage": ["Nestle", "Coca-Cola", "Pepsi", "San Miguel"],
            "Books": ["Penguin", "Random House", "Scholastic", "National Geographic"],
            "Automotive": ["Toyota", "Honda", "Mitsubishi", "Nissan"],
            "Health & Beauty": ["L'Oreal", "Nivea", "Johnson & Johnson", "Unilever"]
        }
        
        for category in self.categories:
            for sub_category in self.sub_categories[category]:
                for i in range(5):  # 5 products per sub-category
                    product_id = f"PROD-{category[:4].upper()}-{sub_category[:3].upper()}-{i+1:02d}"
                    product_name = f"{sub_category} Product {i+1}"
                    brand = random.choice(brands[category])
                    
                    product = {
                        "product_id": product_id,
                        "product_name": product_name,
                        "category": category,
                        "sub_category": sub_category,
                        "brand": brand
                    }
                    
                    products.append(product)
        
        return products

    def generate_geography_data(self) -> List[Dict[str, Any]]:
        """Generate sample geography data"""
        geography = []
        
        municipalities = [
            "Manila", "Quezon City", "Makati", "Taguig", "Pasig", "Mandaluyong",
            "Angeles", "San Fernando", "Cabanatuan", "Malolos", "Olongapo",
            "Batangas", "Lipa", "Calamba", "Lucena", "Naga",
            "Cebu City", "Iloilo", "Bacolod", "Tacloban", "Dumaguete",
            "Davao", "Cagayan de Oro", "Zamboanga", "Butuan", "General Santos"
        ]
        
        for region in self.regions:
            for city in self.cities[region]:
                # Generate some barangays for each city
                for i in range(3):
                    barangay = f"Barangay {i+1}"
                    location = f"{city}, {region}, Philippines"
                    
                    # Generate random coordinates (approximate for Philippines)
                    lat = random.uniform(5.0, 19.0)  # Philippines latitude range
                    lng = random.uniform(116.0, 127.0)  # Philippines longitude range
                    coordinates = f"{lat:.6f},{lng:.6f}"
                    
                    geo = {
                        "region": region,
                        "city": city,
                        "municipality": city,
                        "barangay": barangay,
                        "location": location,
                        "coordinates": coordinates
                    }
                    
                    geography.append(geo)
        
        return geography

    def _random_date(self, days_back: int = 365) -> date:
        """Generate a random date within the specified days back"""
        start_date = date.today() - timedelta(days=days_back)
        random_days = random.randint(0, days_back)
        return start_date + timedelta(days=random_days)

    def generate_sql_inserts(self, num_transactions: int = 1000) -> str:
        """Generate SQL INSERT statements for sample data"""
        sql_statements = []
        
        # Generate geography data
        geography_data = self.generate_geography_data()
        if geography_data:
            sql_statements.append("-- Insert geography data")
            for geo in geography_data:
                sql = f"""INSERT IGNORE INTO geography (region, city, municipality, barangay, location, coordinates) 
VALUES ('{geo['region']}', '{geo['city']}', '{geo['municipality']}', '{geo['barangay']}', '{geo['location']}', '{geo['coordinates']}');"""
                sql_statements.append(sql)
        
        # Generate product data
        product_data = self.generate_product_data()
        if product_data:
            sql_statements.append("\n-- Insert product data")
            for product in product_data:
                sql = f"""INSERT IGNORE INTO products (product_id, product_name, category, sub_category, brand) 
VALUES ('{product['product_id']}', '{product['product_name']}', '{product['category']}', '{product['sub_category']}', '{product['brand']}');"""
                sql_statements.append(sql)
        
        # Generate transaction data
        transaction_data = self.generate_transaction_data(num_transactions)
        if transaction_data:
            sql_statements.append("\n-- Insert transaction data")
            for trans in transaction_data:
                sql = f"""INSERT INTO transactions (order_id, order_date, ship_date, ship_mode, customer_id, customer_name, segment, product_id, product_name, category, sub_category, sales, profit, quantity, discount, country_region, state, city, postal_code, region) 
VALUES ('{trans['order_id']}', '{trans['order_date']}', '{trans['ship_date']}', '{trans['ship_mode']}', '{trans['customer_id']}', '{trans['customer_name']}', '{trans['segment']}', '{trans['product_id']}', '{trans['product_name']}', '{trans['category']}', '{trans['sub_category']}', {trans['sales']}, {trans['profit']}, {trans['quantity']}, {trans['discount']}, '{trans['country_region']}', '{trans['state']}', '{trans['city']}', '{trans['postal_code']}', '{trans['region']}');"""
                sql_statements.append(sql)
        
        return '\n'.join(sql_statements)

    def generate_api_script(self, api_base_url: str = "https://gagambi-backend.onrender.com/api/v1", num_transactions: int = 100) -> str:
        """Generate Python script to load data via API"""
        transaction_data = self.generate_transaction_data(num_transactions)
        
        script = f'''#!/usr/bin/env python3
# Auto-generated script to load sample data via API
import requests
import json
from datetime import datetime

API_BASE_URL = "{api_base_url}"

def load_sample_data():
    """Load sample transaction data via API"""
    
    print("Loading sample data to Render backend...")
    
    # Sample transactions
    transactions = {json.dumps(transaction_data, indent=2, default=str)}
    
    # Load transactions
    success_count = 0
    error_count = 0
    
    for transaction in transactions:
        try:
            response = requests.post(
                f"{{API_BASE_URL}}/analytics/transactions",
                json=transaction,
                headers={{"Content-Type": "application/json"}}
            )
            
            if response.status_code in [200, 201]:
                success_count += 1
                if success_count % 10 == 0:
                    print(f"Loaded {{success_count}} transactions...")
            else:
                error_count += 1
                print(f"Error loading transaction {{transaction['order_id']}}: {{response.status_code}}")
                
        except Exception as e:
            error_count += 1
            print(f"Exception loading transaction {{transaction['order_id']}}: {{e}}")
    
    print(f"\\nComplete! Successfully loaded {{success_count}} transactions.")
    if error_count > 0:
        print(f"Errors: {{error_count}} transactions failed to load.")
    
    # Test analytics endpoint
    try:
        response = requests.get(f"{{API_BASE_URL}}/analytics/metrics")
        if response.status_code == 200:
            metrics = response.json()
            print(f"\\nAnalytics verification:")
            print(f"- Total Sales: ₱{{metrics.get('total_sales', 0):,.2f}}")
            print(f"- Total Orders: {{metrics.get('total_orders', 0):,}}")
            print(f"- Profit Margin: {{metrics.get('profit_margin', 0):.1f}}%")
        else:
            print(f"\\nError fetching analytics: {{response.status_code}}")
    except Exception as e:
        print(f"\\nError testing analytics: {{e}}")

if __name__ == "__main__":
    load_sample_data()
'''
        
        return script

# Command line usage
if __name__ == "__main__":
    import sys
    
    generator = SampleDataGenerator()
    
    if len(sys.argv) > 1 and sys.argv[1] == "sql":
        # Generate SQL
        num_records = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
        print(generator.generate_sql_inserts(num_records))
    elif len(sys.argv) > 1 and sys.argv[1] == "api":
        # Generate API script
        api_url = sys.argv[2] if len(sys.argv) > 2 else "https://gagambi-backend.onrender.com/api/v1"
        num_records = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        print(generator.generate_api_script(api_url, num_records))
    else:
        # Generate JSON
        num_records = int(sys.argv[1]) if len(sys.argv) > 1 else 100
        data = {
            "transactions": generator.generate_transaction_data(num_records),
            "products": generator.generate_product_data(),
            "geography": generator.generate_geography_data()
        }
        print(json.dumps(data, indent=2, default=str))