#!/usr/bin/env python3
"""
Scout Analytics Deployment Verification Script
Tests all Scout Analytics endpoints on Render
"""

import requests
import json
import time
from datetime import datetime

# Configuration
API_BASE_URL = "https://gagambi-backend.onrender.com/api/v1"
HEALTH_URL = "https://gagambi-backend.onrender.com/health"

def test_endpoint(name, url, method="GET", data=None):
    """Test a single endpoint"""
    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        else:
            response = requests.post(url, json=data, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ {name}: SUCCESS ({response.status_code})")
            return True
        else:
            print(f"❌ {name}: FAILED ({response.status_code})")
            return False
    except Exception as e:
        print(f"❌ {name}: ERROR - {str(e)}")
        return False

def main():
    print("🚀 Scout Analytics Deployment Verification")
    print("=" * 50)
    print(f"API Base: {API_BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Test endpoints
    tests = [
        ("Health Check", HEALTH_URL),
        ("Analytics Metrics", f"{API_BASE_URL}/analytics/metrics"),
        ("Sales Trend", f"{API_BASE_URL}/analytics/sales-trend"),
        ("Category Sales", f"{API_BASE_URL}/analytics/category-sales"),
        ("Top Products", f"{API_BASE_URL}/analytics/top-products"),
        ("Geography Data", f"{API_BASE_URL}/analytics/geography"),
        ("PRD Summary", f"{API_BASE_URL}/prd/summary"),
        ("PRD Full Document", f"{API_BASE_URL}/prd/"),
        ("Implementation Status", f"{API_BASE_URL}/prd/implementation-status"),
    ]
    
    passed = 0
    total = len(tests)
    
    for name, url in tests:
        if test_endpoint(name, url):
            passed += 1
        time.sleep(0.5)  # Brief pause between tests
    
    print("=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Scout Analytics is fully deployed!")
    elif passed > 0:
        print("⚠️  Some tests failed. Deployment may be in progress.")
    else:
        print("❌ All tests failed. Check deployment status.")
    
    # Test data creation
    print("\n📊 Testing data creation endpoint...")
    test_transaction = {
        "order_id": f"TEST-{int(time.time())}",
        "order_date": "2024-12-27",
        "ship_date": "2024-12-29",
        "ship_mode": "Standard Class",
        "customer_id": "CU-TEST",
        "customer_name": "Deployment Test",
        "segment": "Consumer",
        "product_id": "PROD-TEST",
        "product_name": "Test Product",
        "category": "Test Category",
        "sub_category": "Test Sub",
        "sales": 1000.00,
        "profit": 300.00,
        "quantity": 1,
        "discount": 0.1,
        "country_region": "Philippines",
        "state": "NCR",
        "city": "Manila",
        "postal_code": "1000",
        "region": "NCR"
    }
    
    if test_endpoint("Create Transaction", f"{API_BASE_URL}/analytics/transactions", "POST", test_transaction):
        print("✅ Data creation working!")
    
    print("\n🔗 Quick Links:")
    print(f"  API Docs: {API_BASE_URL.replace('/api/v1', '/docs')}")
    print(f"  Metrics: {API_BASE_URL}/analytics/metrics")
    print(f"  PRD: {API_BASE_URL}/prd/summary")

if __name__ == "__main__":
    main()