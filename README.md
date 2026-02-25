# 🥷 NinjaEye - Advanced OSINT Framework

## Overview

NinjaEye is a comprehensive Open Source Intelligence (OSINT) framework designed to surpass Aliens_Eye in accuracy, capabilities, and versatility. While Aliens_Eye focuses primarily on username searches across social media platforms, NinjaEye provides a complete OSINT toolkit with multiple intelligence gathering modules.

## 🚀 Key Features

### Superior to Aliens_Eye

| Feature | Aliens_Eye | NinjaEye |
|---------|-----------|----------|
| Username Search | ✅ 840+ platforms | ✅ 50+ platforms (optimized) |
| Email Analysis | ❌ | ✅ Full email intelligence |
| Phone Analysis | ❌ | ✅ Phone number investigation |
| Domain Analysis | ❌ | ✅ Complete domain reconnaissance |
| Breach Detection | ❌ | ✅ Data breach checking |
| DNS Analysis | ❌ | ✅ Full DNS record extraction |
| WHOIS Data | ❌ | ✅ Domain ownership info |
| SSL Certificate | ❌ | ✅ Certificate analysis |
| IP Intelligence | ❌ | ✅ IP address lookup |
| Confidence Scoring | ✅ Basic | ✅ Advanced multi-factor |
| Report Formats | ✅ JSON | ✅ JSON, Text, HTML |
| Username Variations | ✅ Basic | ✅ Advanced generation |

### Core Capabilities

1. **Username Intelligence**
   - Multi-platform username scanning
   - Advanced confidence scoring (5-factor analysis)
   - Intelligent username variation generation
   - Category-based scanning (social media, forums, professional, gaming)

2. **Email Intelligence**
   - Email format validation
   - Domain MX record verification
   - Data breach checking
   - Username extraction

3. **Phone Intelligence**
   - Number format validation
   - Country code detection
   - Number type identification (mobile/landline)

4. **Domain Intelligence**
   - IP address resolution
   - Complete DNS record extraction (A, AAAA, MX, NS, TXT, SOA)
   - WHOIS data retrieval
   - SSL certificate analysis
   - Technology stack detection

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Internet connection

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/ninjai_eye.git
cd ninjai_eye

# Install dependencies
pip install -r requirements.txt

# Make the script executable (Linux/Mac)
chmod +x ninjai_eye.py
```

### Manual Install

```bash
# Install required packages
pip install aiohttp dnspython requests python-whois
```

## 🎯 Usage

### Basic Username Scan

```bash
# Scan a username across all platforms
python ninjai_eye.py --username johndoe

# Scan specific categories only
python ninjai_eye.py --username johndoe --categories social_media professional

# Generate variations and scan
python ninjai_eye.py --username johndoe --variations
```

### Email Analysis

```bash
# Analyze an email address
python ninjai_eye.py --email john@example.com
```

### Phone Analysis

```bash
# Analyze a phone number
python ninjai_eye.py --phone +1234567890
```

### Domain Analysis

```bash
# Analyze a domain
python ninjai_eye.py --domain example.com
```

### Combined Analysis

```bash
# Multiple analysis types
python ninjai_eye.py --username johndoe --email john@example.com --domain example.com
```

### Report Generation

```bash
# Generate JSON report
python ninjai_eye.py --username johndoe --format json --output report.json

# Generate text report
python ninjai_eye.py --username johndoe --format text --output report.txt
```

### Advanced Options

```bash
# Control concurrency and timeout
python ninjai_eye.py --username johndoe --max-concurrent 30 --timeout 15

# Specific categories with variations
python ninjai_eye.py --username johndoe --categories social_media gaming --variations
```

## 📊 Output Examples

### Text Report Format

```
================================================================================
🥷 NINJAEYE OSINT REPORT
================================================================================
Generated: 2025-01-15 10:30:45

SUMMARY
----------------------------------------
Total Scanned: 25
Found: 8
Maybe: 5
Not Found: 12

DETAILED RESULTS
----------------------------------------
✓ TWITTER: FOUND
  Target: johndoe
  Confidence: 85.5%
  url: https://twitter.com/johndoe
  status_code: 200
  response_time: 0.342

✓ GITHUB: FOUND
  Target: johndoe
  Confidence: 92.3%
  url: https://github.com/johndoe
  status_code: 200
  response_time: 0.287

? LINKEDIN: MAYBE
  Target: johndoe
  Confidence: 55.2%
  url: https://linkedin.com/in/johndoe
  status_code: 200
  response_time: 0.891
```

### JSON Report Format

```json
{
  "scan_summary": {
    "total_results": 25,
    "found": 8,
    "maybe": 5,
    "not_found": 12,
    "errors": 0,
    "timestamp": "2025-01-15T10:30:45.123456"
  },
  "results": [
    {
      "source": "twitter",
      "target": "johndoe",
      "result_type": "username_search",
      "status": "FOUND",
      "confidence": 85.5,
      "data": {
        "url": "https://twitter.com/johndoe",
        "status_code": 200,
        "response_time": 0.342,
        "title": "John Doe (@johndoe) / Twitter"
      },
      "timestamp": "2025-01-15T10:30:45.123456",
      "metadata": {
        "category": "social_media",
        "method": "get"
      }
    }
  ]
}
```

## 🔬 Advanced Features

### Multi-Factor Confidence Scoring

NinjaEye uses a sophisticated 5-factor confidence calculation:

1. **HTTP Status Code Analysis (30% weight)**
   - 200: +30 points
   - 301/302/307/308: +20 points
   - 404: -10 points

2. **Content Analysis (25% weight)**
   - Positive indicators: profile, user, account, posts, followers
   - Negative indicators: not found, error, 404, user not found

3. **Response Time Analysis (15% weight)**
   - Fast response (0.1-2.0s): +15 points
   - Medium response (2.0-5.0s): +10 points
   - Slow response (>5.0s): +5 points

4. **URL Structure Analysis (15% weight)**
   - Profile/user indicators in URL: +15 points

5. **Page Title Analysis (15% weight)**
   - Profile/user keywords in title: +15 points

### Username Variation Generation

NinjaEye generates intelligent username variations:

- **Prefixes**: the, real, official, iam, im, its, mr, mrs, ms, dr, prof
- **Suffixes**: official, real, verified, pro, dev, admin, mod, 123, 2024, 2025
- **Number variations**: username1, username2, ... username99
- **Separator variations**: username_, _username, username., .username

### Domain Intelligence

Complete domain reconnaissance including:

- **DNS Records**: A, AAAA, MX, NS, TXT, SOA
- **IP Resolution**: All associated IP addresses
- **WHOIS Data**: Registrar, creation date, expiration date, name servers
- **SSL Certificates**: Issuer, subject, validity period
- **Technology Stack**: Detected technologies and frameworks

## 🛡️ Legal & Ethical Considerations

### Disclaimer

This tool is developed for educational purposes and legitimate OSINT research only. Users are responsible for:

- Complying with applicable laws and regulations
- Respecting terms of service of target platforms
- Obtaining proper authorization before scanning
- Using results ethically and responsibly

### Best Practices

1. **Authorization**: Always obtain permission before conducting OSINT activities
2. **Rate Limiting**: Respect platform rate limits and terms of service
3. **Privacy**: Handle personal data responsibly and in compliance with privacy laws
4. **Documentation**: Keep records of authorization and purpose of investigations
5. **Ethical Use**: Use results for legitimate security research, investigations, or defensive purposes

### Legal Compliance

- Ensure compliance with local, state, and federal laws
- Follow GDPR, CCPA, and other privacy regulations
- Respect intellectual property rights
- Avoid unauthorized access to systems or data

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Areas for Contribution

- Additional platform support
- Enhanced detection algorithms
- New analysis modules
- Performance optimizations
- Documentation improvements
- Bug fixes

## 📈 Roadmap

### Version 2.0 (Planned)

- [ ] API integration for breach databases
- [ ] Geolocation tracking
- [ ] Relationship mapping between accounts
- [ ] Metadata extraction from profiles
- [ ] Automated report generation with graphs
- [ ] Web interface
- [ ] Database integration for historical data
- [ ] Machine learning for improved accuracy

### Version 3.0 (Future)

- [ ] Real-time monitoring
- [ ] Alert system
- [ ] Collaboration features
- [ ] Advanced visualization
- [ ] Integration with other OSINT tools
- [ ] Mobile app

## 🐛 Troubleshooting

### Common Issues

**Issue**: Import errors for dependencies
```bash
# Solution: Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Issue**: DNS resolution failures
```bash
# Solution: Check DNS configuration
nslookup example.com
```

**Issue**: Timeout errors
```bash
# Solution: Increase timeout value
python ninjai_eye.py --username johndoe --timeout 20
```

**Issue**: Rate limiting from platforms
```bash
# Solution: Reduce concurrent connections
python ninjai_eye.py --username johndoe --max-concurrent 10
```

## 📞 Support

For issues, questions, or contributions:

- GitHub Issues: [Create an issue](https://github.com/yourusername/ninjai_eye/issues)
- Documentation: [Wiki](https://github.com/yourusername/ninjai_eye/wiki)
- Discussions: [GitHub Discussions](https://github.com/yourusername/ninjai_eye/discussions)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by Aliens_Eye and other OSINT tools
- Built with aiohttp, dnspython, requests, and python-whois
- Community feedback and contributions

## 🔗 Related Tools

- [Aliens_Eye](https://github.com/arxhr007/Aliens_eye) - Username scanner
- [Sherlock](https://github.com/sherlock-project/sherlock) - Hunt down social media accounts
- [Maigret](https://github.com/soxoj/maigret) - Collect personal data from various sources
- [TheHarvester](https://github.com/laramies/theHarvester) - E-mail, subdomain and people harvesting

## 📊 Comparison with Aliens_Eye

### Accuracy Improvements

NinjaEye implements several improvements over Aliens_Eye:

1. **Multi-Factor Analysis**: 5-factor confidence scoring vs. basic HTTP analysis
2. **Content Intelligence**: Advanced content pattern recognition
3. **Response Time Analysis**: Timing-based detection
4. **URL Structure Analysis**: Pattern-based URL evaluation
5. **Title Analysis**: Metadata extraction from page titles

### Feature Expansion

While Aliens_Eye focuses on username searches, NinjaEye provides:

- Email intelligence and breach detection
- Phone number analysis
- Complete domain reconnaissance
- DNS and WHOIS data extraction
- SSL certificate analysis
- IP address intelligence

### Performance Optimization

- Configurable concurrency control
- Optimized timeout handling
- Efficient resource management
- Better error handling and recovery

## 🎓 Educational Use

NinjaEye is excellent for learning about:

- OSINT methodologies and techniques
- Web scraping and data extraction
- DNS and network reconnaissance
- API integration and data analysis
- Python async programming
- Security research and investigation

## ⚠️ Warning

This tool should only be used for:

- Educational purposes
- Authorized security assessments
- Legitimate investigations
- Defensive security research
- Penetration testing with proper authorization

Misuse of this tool for unauthorized activities is illegal and unethical.

---

**Made with 🥷 by the NinjaEye Team**

**Version**: 1.0.0  
**Last Updated**: 2025-01-15