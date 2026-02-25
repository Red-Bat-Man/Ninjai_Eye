#!/bin/bash

# NinjaEye Installation Script
# This script automates the installation of NinjaEye OSINT Framework

set -e

echo "🥷 NinjaEye Installation Script"
echo "================================"
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python version: $PYTHON_VERSION"

# Check if pip is installed
echo "📋 Checking pip installation..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi
echo "✅ pip3 is installed"

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Make the script executable
echo "🔧 Making ninjai_eye.py executable..."
chmod +x ninjai_eye.py

# Create results directory
echo "📁 Creating results directory..."
mkdir -p results

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🚀 You can now run NinjaEye with:"
echo "   python3 ninjai_eye.py --help"
echo "   ./ninjai_eye.py --username <username>"
echo ""
echo "📚 For more information, see README.md"
echo ""