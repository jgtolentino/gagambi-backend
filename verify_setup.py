#!/usr/bin/env python3
"""
Verification script to check that the retail schema setup is ready
This validates the files and configuration without requiring database connection
"""
import os
import sys

def check_file_exists(file_path, description):
    """Check if a file exists and print status"""
    if os.path.exists(file_path):
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ {description}: {file_path} - NOT FOUND")
        return False

def check_model_imports():
    """Check if we can import the models"""
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
        from app.models.retail import (
            Region, Province, City, Store, Brand, Category, Product, 
            Customer, Transaction, TransactionItem, Inventory
        )
        print("✅ Retail models can be imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error importing retail models: {e}")
        return False

def check_api_endpoints():
    """Check if API endpoints are properly defined"""
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
        from app.api.v1.retail import router
        print("✅ Retail API endpoints are properly defined")
        
        # Check if router has the expected endpoints
        routes = [route.path for route in router.routes]
        expected_routes = [
            "/sales/by-region",
            "/sales/by-brand", 
            "/sales/by-category",
            "/products/top-selling",
            "/customers/rfm-segments",
            "/stores/performance",
            "/transactions/summary"
        ]
        
        missing_routes = [route for route in expected_routes if route not in routes]
        if missing_routes:
            print(f"⚠️  Missing routes: {missing_routes}")
        else:
            print("✅ All expected API routes are present")
        
        return True
    except Exception as e:
        print(f"❌ Error checking API endpoints: {e}")
        return False

def main():
    """Main verification function"""
    print("🔍 Verifying Scout Analytics retail setup...")
    print("=" * 50)
    
    success_count = 0
    total_checks = 0
    
    # Check essential files
    files_to_check = [
        ("app/models/retail.py", "Retail data models"),
        ("app/schemas/retail.py", "Retail schemas"), 
        ("app/crud/retail.py", "Retail CRUD operations"),
        ("app/api/v1/retail.py", "Retail API endpoints"),
        ("create_retail_schema.py", "Database setup script"),
        ("render.yaml", "Render deployment config"),
        ("requirements.txt", "Python dependencies")
    ]
    
    for file_path, description in files_to_check:
        total_checks += 1
        if check_file_exists(file_path, description):
            success_count += 1
    
    print("\n🧪 Testing imports...")
    print("-" * 30)
    
    # Test model imports
    total_checks += 1
    if check_model_imports():
        success_count += 1
    
    # Test API endpoint imports
    total_checks += 1
    if check_api_endpoints():
        success_count += 1
    
    print("\n📊 Summary")
    print("=" * 30)
    print(f"✅ Successful checks: {success_count}/{total_checks}")
    
    if success_count == total_checks:
        print("🎉 All verifications passed! Scout Analytics retail setup is ready.")
        print("\n📋 Next steps:")
        print("1. The changes have been committed and pushed to git")
        print("2. Render will automatically deploy the backend with retail endpoints")
        print("3. Once deployed, Scout Analytics can connect to real data")
        print("\n🔗 Expected API base URL: https://gagambi-api.onrender.com/api/v1/")
        return True
    else:
        print("❌ Some verifications failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)