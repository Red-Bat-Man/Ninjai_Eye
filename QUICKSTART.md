# 🚀 NinjaEye Quick Start Guide

Get started with NinjaEye in 5 minutes!

## Installation

### Step 1: Clone or Download

```bash
# Clone the repository
git clone https://github.com/yourusername/ninjai_eye.git
cd ninjai_eye
```

### Step 2: Install Dependencies

```bash
# Using the installation script (recommended)
chmod +x install.sh
./install.sh

# Or manually install
pip install -r requirements.txt
```

### Step 3: Verify Installation

```bash
# Test the installation
python3 ninjai_eye.py --help
```

You should see the help message with all available options.

## Basic Usage

### 1. Scan a Username

```bash
# Scan across all platforms
python3 ninjai_eye.py --username johndoe

# Scan specific categories
python3 ninjai_eye.py --username johndoe --categories social_media professional

# Generate variations and scan
python3 ninjai_eye.py --username johndoe --variations
```

### 2. Analyze an Email

```bash
# Basic email analysis
python3 ninjai_eye.py --email john@example.com

# Save results to file
python3 ninjai_eye.py --email john@example.com --output email_report.txt
```

### 3. Analyze a Phone Number

```bash
# Phone number analysis
python3 ninjai_eye.py --phone +1234567890
```

### 4. Analyze a Domain

```bash
# Domain reconnaissance
python3 ninjai_eye.py --domain example.com

# Save JSON report
python3 ninjai_eye.py --domain example.com --format json --output domain_report.json
```

### 5. Combined Analysis

```bash
# Multiple analysis types
python3 ninjai_eye.py --username johndoe --email john@example.com --domain example.com
```

## Understanding Results

### Status Indicators

- **✓ FOUND**: High confidence (≥70%) that the profile exists
- **? MAYBE**: Moderate confidence (40-69%) - profile might exist
- **✗ NOT_FOUND**: Low confidence (<40%) - profile likely doesn't exist
- **! ERROR**: An error occurred during scanning

### Confidence Scores

Each result includes a confidence percentage (0-100%):

- **90-100%**: Very high confidence
- **70-89%**: High confidence
- **40-69%**: Moderate confidence
- **0-39%**: Low confidence

### Example Output

```
✓ TWITTER: FOUND
  Target: johndoe
  Confidence: 85.5%
  url: https://twitter.com/johndoe
  status_code: 200
  response_time: 0.342

? LINKEDIN: MAYBE
  Target: johndoe
  Confidence: 55.2%
  url: https://linkedin.com/in/johndoe
  status_code: 200
  response_time: 0.891
```

## Advanced Options

### Control Performance

```bash
# Limit concurrent connections (useful for slow networks)
python3 ninjai_eye.py --username johndoe --max-concurrent 20

# Increase timeout for slow servers
python3 ninjai_eye.py --username johndoe --timeout 20
```

### Report Formats

```bash
# Generate JSON report
python3 ninjai_eye.py --username johndoe --format json --output report.json

# Generate text report
python3 ninjai_eye.py --username johndoe --format text --output report.txt
```

### Category Selection

```bash
# Scan only social media platforms
python3 ninjai_eye.py --username johndoe --categories social_media

# Scan multiple categories
python3 ninjai_eye.py --username johndoe --categories social_media professional gaming
```

## Common Use Cases

### Use Case 1: Social Media Investigation

```bash
# Investigate a person's social media presence
python3 ninjai_eye.py --username targetperson --categories social_media --output social_report.txt
```

### Use Case 2: Professional Background Check

```bash
# Check professional platforms
python3 ninjai_eye.py --username candidate --categories professional --output professional_report.txt
```

### Use Case 3: Email Verification

```bash
# Verify email and check for breaches
python3 ninjai_eye.py --email suspicious@example.com --output email_check.txt
```

### Use Case 4: Domain Reconnaissance

```bash
# Complete domain intelligence
python3 ninjai_eye.py --domain targetcompany.com --output domain_recon.txt
```

### Use Case 5: Comprehensive Investigation

```bash
# Full investigation with multiple data points
python3 ninjai_eye.py \
  --username target \
  --email target@example.com \
  --domain target.com \
  --output full_investigation.txt
```

## Tips and Best Practices

### 1. Start with Specific Categories

```bash
# Instead of scanning everything, be specific
python3 ninjai_eye.py --username johndoe --categories social_media
```

### 2. Use Username Variations

```bash
# People often use different username variations
python3 ninjai_eye.py --username johndoe --variations
```

### 3. Save Your Results

```bash
# Always save results for later analysis
python3 ninjai_eye.py --username johndoe --output investigation.txt
```

### 4. Combine Multiple Analysis Types

```bash
# Get comprehensive intelligence
python3 ninjai_eye.py --username johndoe --email john@example.com --domain example.com
```

### 5. Adjust Performance Settings

```bash
# For slow connections, reduce concurrency
python3 ninjai_eye.py --username johndoe --max-concurrent 10 --timeout 15
```

## Troubleshooting

### Issue: ModuleNotFoundError

```bash
# Solution: Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Issue: Timeout Errors

```bash
# Solution: Increase timeout
python3 ninjai_eye.py --username johndoe --timeout 20
```

### Issue: Too Many Errors

```bash
# Solution: Reduce concurrent connections
python3 ninjai_eye.py --username johndoe --max-concurrent 10
```

### Issue: DNS Resolution Failures

```bash
# Solution: Check your internet connection and DNS settings
ping google.com
nslookup example.com
```

## Next Steps

1. **Read the full documentation:** Check `README.md` for detailed information
2. **Explore configuration:** Modify `config.json` to customize behavior
3. **Run tests:** Execute `python3 test_ninjai_eye.py` to verify all features
4. **Check comparison:** Read `COMPARISON.md` to see advantages over Aliens_Eye

## Legal and Ethical Use

⚠️ **Important:** Always use NinjaEye responsibly:

- Obtain proper authorization before scanning
- Respect privacy laws and regulations
- Follow terms of service of target platforms
- Use results for legitimate purposes only
- Comply with GDPR, CCPA, and other privacy regulations

## Getting Help

- **Documentation:** Read `README.md` for comprehensive information
- **Examples:** Check `test_ninjai_eye.py` for usage examples
- **Issues:** Report bugs or request features on GitHub
- **Community:** Join discussions and share your experiences

## Quick Reference

| Task | Command |
|------|---------|
| Scan username | `python3 ninjai_eye.py --username <username>` |
| Analyze email | `python3 ninjai_eye.py --email <email>` |
| Analyze phone | `python3 ninjai_eye.py --phone <phone>` |
| Analyze domain | `python3 ninjai_eye.py --domain <domain>` |
| Save report | `python3 ninjai_eye.py --username <user> --output <file>` |
| JSON format | `python3 ninjai_eye.py --username <user> --format json` |
| Specific categories | `python3 ninjai_eye.py --username <user> --categories social_media` |
| Username variations | `python3 ninjai_eye.py --username <user> --variations` |

---

**Ready to start?** Run your first scan:

```bash
python3 ninjai_eye.py --username testuser
```

**Happy Hunting! 🥷**