#!/bin/bash
# Quick start setup for texture generation
# Run this script to set up the texture generation environment

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "🎮 Minecraft Texture Generator - Quick Setup"
echo "=============================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment if needed
if [ ! -d "$PROJECT_ROOT/.venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$PROJECT_ROOT/.venv"
fi

# Activate virtual environment
source "$PROJECT_ROOT/.venv/bin/activate"

# Install dependencies
echo "Installing dependencies..."
pip install -q google-genai pillow

echo "✓ Dependencies installed"
echo ""

# Check for API key
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  GOOGLE_API_KEY environment variable not set"
    echo ""
    echo "To use the texture generator, you need to:"
    echo "1. Get an API key from https://aistudio.google.com/apikey"
    echo "2. Set it as an environment variable:"
    echo ""
    echo "   export GOOGLE_API_KEY='your-api-key-here'"
    echo ""
    echo "Add to ~/.zshrc or ~/.bash_profile to make it permanent"
else
    echo "✓ API key is set"
fi

echo ""
echo "=============================================="
echo "✓ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set GOOGLE_API_KEY if you haven't already"
echo "2. Edit scripts/texture_config.json with your texture prompts"
echo "3. Run: python scripts/generate_textures.py batch scripts/texture_config.json -o generated_textures/"
echo ""
echo "Or generate a single texture:"
echo "python scripts/generate_textures.py single \"your texture description\" -o output.png"
echo ""
echo "For help:"
echo "python scripts/generate_textures.py single --help"
echo "python scripts/generate_textures.py batch --help"
