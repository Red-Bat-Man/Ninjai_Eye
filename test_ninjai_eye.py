#!/usr/bin/env python3
"""
NinjaEye Test Script
Demonstrates the capabilities of NinjaEye OSINT Framework
"""

import asyncio
import sys
from ninjai_eye import NinjaEye

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")

def test_username_scan():
    """Test username scanning functionality"""
    print_section("TEST 1: Username Scanning")
    
    ninja = NinjaEye(max_concurrent=10, timeout=10)
    
    # Test with a common username
    test_username = "testuser"
    print(f"🔍 Scanning username: {test_username}")
    print("📋 Categories: social_media, professional")
    
    results = asyncio.run(ninja.scan_username(
        test_username, 
        categories=['social_media', 'professional']
    ))
    
    print(f"\n📊 Results Summary:")
    print(f"   Total scanned: {len(results)}")
    print(f"   Found: {len([r for r in results if r.status == 'FOUND'])}")
    print(f"   Maybe: {len([r for r in results if r.status == 'MAYBE'])}")
    print(f"   Not Found: {len([r for r in results if r.status == 'NOT_FOUND'])}")
    print(f"   Errors: {len([r for r in results if r.status == 'ERROR'])}")
    
    # Show some results
    print(f"\n🔍 Sample Results:")
    for result in results[:5]:
        status_symbol = {
            'FOUND': '✓',
            'MAYBE': '?',
            'NOT_FOUND': '✗',
            'ERROR': '!'
        }.get(result.status, '?')
        
        print(f"   {status_symbol} {result.source.upper()}: {result.status} (Confidence: {result.confidence}%)")
    
    return ninja

def test_email_analysis():
    """Test email analysis functionality"""
    print_section("TEST 2: Email Analysis")
    
    ninja = NinjaEye()
    
    # Test with a sample email
    test_email = "test@example.com"
    print(f"📧 Analyzing email: {test_email}")
    
    result = ninja.analyze_email(test_email)
    
    print(f"\n📊 Analysis Results:")
    print(f"   Status: {result.status}")
    print(f"   Confidence: {result.confidence}%")
    print(f"   Valid Format: {result.data.get('valid_format', False)}")
    print(f"   Domain: {result.data.get('domain', 'N/A')}")
    print(f"   Username: {result.data.get('username', 'N/A')}")
    print(f"   Domain Valid: {result.data.get('domain_valid', False)}")
    print(f"   MX Records: {len(result.data.get('mx_records', []))} found")
    
    breach_data = result.data.get('breach_check', {})
    print(f"   Breach Check: {'Found in breaches' if breach_data.get('found_in_breaches') else 'No breaches found'}")
    
    return ninja

def test_phone_analysis():
    """Test phone analysis functionality"""
    print_section("TEST 3: Phone Analysis")
    
    ninja = NinjaEye()
    
    # Test with sample phone numbers
    test_phones = [
        "+1234567890",
        "+441234567890",
        "invalid-phone"
    ]
    
    for phone in test_phones:
        print(f"📱 Analyzing phone: {phone}")
        result = ninja.analyze_phone(phone)
        
        print(f"   Status: {result.status}")
        print(f"   Confidence: {result.confidence}%")
        print(f"   Valid Format: {result.data.get('valid_format', False)}")
        print(f"   Country Code: {result.data.get('country_code', 'N/A')}")
        print(f"   Type: {result.data.get('type', 'N/A')}")
        print()
    
    return ninja

def test_domain_analysis():
    """Test domain analysis functionality"""
    print_section("TEST 4: Domain Analysis")
    
    ninja = NinjaEye()
    
    # Test with a well-known domain
    test_domain = "example.com"
    print(f"🌐 Analyzing domain: {test_domain}")
    
    result = ninja.analyze_domain(test_domain)
    
    print(f"\n📊 Analysis Results:")
    print(f"   Status: {result.status}")
    print(f"   Confidence: {result.confidence}%")
    print(f"   IP Addresses: {', '.join(result.data.get('ip_addresses', ['N/A']))}")
    
    dns_records = result.data.get('dns_records', {})
    print(f"\n   DNS Records:")
    for record_type, records in dns_records.items():
        print(f"      {record_type}: {len(records)} records")
    
    whois_data = result.data.get('whois_data', {})
    print(f"\n   WHOIS Data:")
    print(f"      Registrar: {whois_data.get('registrar', 'N/A')}")
    print(f"      Created: {whois_data.get('creation_date', 'N/A')}")
    print(f"      Expires: {whois_data.get('expiration_date', 'N/A')}")
    
    ssl_info = result.data.get('ssl_info', {})
    if ssl_info:
        print(f"\n   SSL Certificate:")
        print(f"      Issuer: {ssl_info.get('issuer', {}).get('organizationName', 'N/A')}")
        print(f"      Valid From: {ssl_info.get('valid_from', 'N/A')}")
        print(f"      Valid Until: {ssl_info.get('valid_until', 'N/A')}")
    
    return ninja

def test_username_variations():
    """Test username variation generation"""
    print_section("TEST 5: Username Variation Generation")
    
    ninja = NinjaEye()
    
    test_username = "john"
    print(f"🔄 Generating variations for: {test_username}")
    
    variations = ninja.generate_username_variations(test_username)
    
    print(f"\n📋 Generated {len(variations)} variations:")
    print("   First 10 variations:")
    for i, variation in enumerate(variations[:10], 1):
        print(f"      {i}. {variation}")
    
    print(f"\n   Last 5 variations:")
    for i, variation in enumerate(variations[-5:], len(variations)-4):
        print(f"      {i}. {variation}")
    
    return ninja

def test_report_generation():
    """Test report generation functionality"""
    print_section("TEST 6: Report Generation")
    
    ninja = NinjaEye()
    
    # Add some sample results
    from ninjai_eye import OSINTResult
    from datetime import datetime
    
    sample_results = [
        OSINTResult(
            source="twitter",
            target="testuser",
            result_type="username_search",
            status="FOUND",
            confidence=85.5,
            data={"url": "https://twitter.com/testuser", "status_code": 200},
            timestamp=datetime.now().isoformat(),
            metadata={"category": "social_media"}
        ),
        OSINTResult(
            source="github",
            target="testuser",
            result_type="username_search",
            status="FOUND",
            confidence=92.3,
            data={"url": "https://github.com/testuser", "status_code": 200},
            timestamp=datetime.now().isoformat(),
            metadata={"category": "professional"}
        ),
        OSINTResult(
            source="linkedin",
            target="testuser",
            result_type="username_search",
            status="MAYBE",
            confidence=55.2,
            data={"url": "https://linkedin.com/in/testuser", "status_code": 200},
            timestamp=datetime.now().isoformat(),
            metadata={"category": "professional"}
        )
    ]
    
    ninja.results = sample_results
    
    print("📊 Generating reports in different formats...\n")
    
    # Generate JSON report
    json_report = ninja.generate_report('json')
    print("✅ JSON Report (first 500 characters):")
    print("   " + json_report[:500] + "...")
    
    # Generate text report
    text_report = ninja.generate_report('text')
    print("\n✅ Text Report:")
    print(text_report)
    
    # Save reports
    json_file = ninja.save_report('test_report.json', 'json')
    text_file = ninja.save_report('test_report.txt', 'text')
    
    print(f"💾 Reports saved:")
    print(f"   JSON: {json_file}")
    print(f"   Text: {text_file}")
    
    return ninja

def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("  🥷 NinjaEye OSINT Framework - Test Suite")
    print("=" * 80)
    print(f"  Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    try:
        # Run tests
        test_username_scan()
        test_email_analysis()
        test_phone_analysis()
        test_domain_analysis()
        test_username_variations()
        test_report_generation()
        
        # Final summary
        print_section("TEST SUMMARY")
        print("✅ All tests completed successfully!")
        print("\n📊 Test Coverage:")
        print("   ✓ Username Scanning")
        print("   ✓ Email Analysis")
        print("   ✓ Phone Analysis")
        print("   ✓ Domain Analysis")
        print("   ✓ Username Variation Generation")
        print("   ✓ Report Generation")
        print("\n🎉 NinjaEye is ready for use!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print(f"\n  Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_all_tests()