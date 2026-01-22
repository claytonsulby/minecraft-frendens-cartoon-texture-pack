# Minecraft Texture Generator

Generate Minecraft textures using Google's Gemini AI image generation models (Nano Banana).

## Setup

### 1. Install Dependencies

```bash
pip install google-genai pillow
```

### 2. Get a Google API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy your API key

### 3. Set Environment Variable

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Or add to your shell profile (`~/.zshrc`, `~/.bash_profile`, etc.):
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Usage

### Generate a Single Texture

```bash
python scripts/generate_textures.py single "A cute cartoon dirt block texture" -o generated_textures/dirt.png
```

**Options:**
- `-m fast` or `-m pro` — Model to use (fast = default, pro = higher quality)
- `-t block|item|armor|gui|wide` — Texture type (default: block)
- `-r 1K|2K|4K` — Resolution for pro model (default: 1K)
- `-i reference.png` — Reference image to edit/enhance

### Generate Multiple Textures from Config

```bash
python scripts/generate_textures.py batch scripts/texture_config.json -o generated_textures/
```

### List Available Models

```bash
python scripts/generate_textures.py models
```

## Model Comparison

| Feature | Fast (Gemini 2.5) | Pro (Gemini 3) |
|---------|-------------------|----------------|
| Speed | Very fast | Moderate |
| Resolution | 1024x1024 | 1K, 2K, 4K |
| Text in images | Limited | Excellent |
| Reference images | Up to 3 | Up to 14 |
| Best for | Quick generation | Professional assets |
| Cost | Lower | Higher |

## Examples

### Cartoon Block Texture
```bash
python scripts/generate_textures.py single \
  "A cheerful cartoon Minecraft grass block top texture with bright green grass, simple grass blade details, and small cartoon flowers in a sunny, happy appearance" \
  -o generated_textures/grass.png \
  -m fast \
  -t block
```

### High-Quality Item Texture (Pro Model)
```bash
python scripts/generate_textures.py single \
  "A brilliant diamond sword texture with a blue diamond blade that glimmers with magical sparkles, dark handle with grip details, and metallic highlights" \
  -o generated_textures/diamond_sword.png \
  -m pro \
  -t item \
  -r 2K
```

### Edit Existing Texture
```bash
python scripts/generate_textures.py single \
  "Make this texture more vibrant and add cartoon-style highlights" \
  -o generated_textures/improved_stone.png \
  -i existing_stone.png \
  -m pro
```

### Style Transfer Using Reference Image
```bash
python scripts/generate_textures.py single \
  "Transform this texture to match cartoon aesthetic with cute features" \
  -o generated_textures/stone_cartoon.png \
  -i assets/minecraft/textures/block/stone.png \
  -m pro
```

### Batch Generation with Reference Images

Use the `reference_image` field in your config to apply changes to existing textures:

```json
{
  "textures": [
    {
      "name": "dirt_enhanced",
      "type": "block",
      "prompt": "Make this dirt block more vibrant with cartoon-style shading",
      "reference_image": "existing_textures/dirt.png"
    },
    {
      "name": "stone_cartoon",
      "type": "block", 
      "prompt": "Transform to cartoon style while preserving the core structure",
      "reference_image": "existing_textures/stone.png"
    }
  ]
}
```

Paths can be:
- **Relative**: Resolved relative to the config file directory
- **Absolute**: Full filesystem path

## Configuration File Format

Create a JSON file with multiple texture specifications:

```json
{
  "project": "My Texture Pack",
  "description": "Batch texture generation config",
  "textures": [
    {
      "name": "dirt",
      "type": "block",
      "prompt": "A cute cartoon dirt block texture..."
    },
    {
      "name": "stone",
      "type": "block",
      "prompt": "A cheerful cartoon stone texture..."
    },
    {
      "name": "enhanced_dirt",
      "type": "block",
      "prompt": "Make this texture more vibrant and add cartoon highlights...",
      "reference_image": "path/to/original_dirt.png"
    }
  ]
}
```

### Fields:
- **name** (required): Output filename (without .png)
- **prompt** (required): Description of the texture to generate
- **type** (optional): Texture type - `block`, `item`, `armor`, `gui`, `wide` (default: block)
- **reference_image** (optional): Path to reference image for editing/enhancement
  - Can be absolute path or relative to config file location
  - Used for style transfer, enhancement, or element modification

## Tips for Better Results

### Be Descriptive
Instead of: "dirt block"
Try: "A cute cartoon-style Minecraft dirt block with friendly brown color, exaggerated texture details, and soft shading in a children's illustration aesthetic"

### Specify Style
- "cartoon style" — Playful, illustrated look
- "pixel art inspired" — Blocky, retro look
- "realistic" — Photographic appearance
- "watercolor" — Artistic, painted look

### Use Photography Terms
- "soft lighting" — Gentle, diffused light
- "high contrast" — Bold, dramatic lighting
- "warm tones" — Yellow/orange color palette
- "cool tones" — Blue/purple color palette

### Reference Existing Style
```bash
python scripts/generate_textures.py single \
  "Match the cartoon style of this reference image but generate a stone texture" \
  -o generated_textures/stone.png \
  -i existing_cartoon_texture.png \
  -m pro
```

## Output

Generated textures are saved as PNG files. They include a SynthID watermark from Google.

## Troubleshooting

### "API key not provided" error
Make sure `GOOGLE_API_KEY` environment variable is set:
```bash
echo $GOOGLE_API_KEY  # Should print your key
```

### "API key validation failed" error
Check that:
1. Your API key is correct
2. You have API quota remaining
3. Your Google account has billing enabled

### Low quality results
- Try the "pro" model (`-m pro`) for better quality
- Use more detailed, descriptive prompts
- Specify the artistic style explicitly
- Try higher resolution with pro model (`-r 2K` or `-r 4K`)

### Generation is slow
- The pro model takes longer but produces better results
- Use the fast model (`-m fast`) for quicker iterations
- Pro model with 4K resolution takes the longest

## API Costs

Pricing varies by model and resolution. Check [Google's pricing page](https://ai.google.dev/pricing) for current rates.

## Integration with Pack

Generated textures can be integrated into the pack by:
1. Generating to the appropriate texture directory
2. Updating atlases if needed
3. Testing in-game

Example placement:
```
assets/minecraft/textures/block/dirt.png
assets/minecraft/textures/block/stone.png
assets/minecraft/textures/item/diamond_sword.png
```

## Next Steps

1. Edit `scripts/texture_config.json` with your texture specifications
2. Run batch generation: `python scripts/generate_textures.py batch scripts/texture_config.json -o generated_textures/`
3. Review generated textures
4. Move approved textures to the pack directories
5. Test in-game

## References

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Nano Banana (Image Generation) Guide](https://ai.google.dev/docs/gemini-docs/image-generation)
- [Gemini Cookbook](https://github.com/google-gemini/cookbook)
