#!/usr/bin/env python3
"""
Minecraft Texture Generator using Google Gemini API (Nano Banana)

This script generates Minecraft textures using Google's Gemini image generation models.
Supports both Gemini 2.5 Flash (fast) and Gemini 3 Pro (professional) models.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Literal
import time

try:
    from google import genai
    from google.genai import types
    from PIL import Image
    from dotenv import load_dotenv
except ImportError:
    print("Error: Required packages not installed. Run:")
    print("  pip install google-genai pillow python-dotenv")
    sys.exit(1)

# Load environment variables from .env file
load_dotenv()


class TextureGenerator:
    """Generate Minecraft textures using Gemini API."""
    
    # Model options
    MODEL_FAST = "gemini-2.5-flash-image"
    MODEL_PRO = "gemini-3-pro-image-preview"
    
    # Default Minecraft texture aspect ratios
    TEXTURE_SIZES = {
        "item": "1:1",      # 16x16 items
        "block": "1:1",     # 16x16 blocks
        "armor": "1:1",     # Armor textures
        "gui": "1:1",       # GUI elements
        "wide": "16:9",     # Panorama/wide formats
    }
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the texture generator.
        
        Args:
            api_key: Google API key. If None, uses GOOGLE_API_KEY environment variable.
        """
        if api_key is None:
            api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError(
                "API key not provided. Set GOOGLE_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        self.client = genai.Client(api_key=api_key)
        self.api_key_valid = False
        self._validate_api_key()
    
    def _validate_api_key(self):
        """Validate that the API key works."""
        try:
            # Quick test with a minimal request
            response = self.client.models.list()
            self.api_key_valid = True
            print("✓ API key validated successfully")
        except Exception as e:
            print(f"✗ API key validation failed: {e}")
            self.api_key_valid = False
    
    def generate_texture(
        self,
        prompt: str,
        output_path: str,
        model: Literal["fast", "pro"] = "fast",
        texture_type: str = "block",
        input_image: Optional[str] = None,
        input_images: Optional[list] = None,
        resolution: Literal["1K", "2K", "4K"] = "1K",
    ) -> bool:
        """
        Generate a texture using Gemini API.
        
        Args:
            prompt: Description of the texture to generate
            output_path: Where to save the generated texture
            model: "fast" (gemini-2.5-flash-image) or "pro" (gemini-3-pro-image-preview)
            texture_type: Type of texture (item, block, armor, gui, wide)
            input_image: Optional path to single reference image (deprecated, use input_images)
            input_images: Optional list of paths to reference images (up to 3 for fast, up to 14 for pro)
            resolution: Output resolution (1K, 2K, 4K) - only for pro model
        
        Returns:
            True if successful, False otherwise
        """
        if not self.api_key_valid:
            print("✗ API key not validated. Cannot proceed.")
            return False
        
        try:
            model_id = self.MODEL_PRO if model == "pro" else self.MODEL_FAST
            aspect_ratio = self.TEXTURE_SIZES.get(texture_type, "1:1")
            
            # Prepare contents
            contents = [prompt]
            
            # Handle reference images (support both old single image and new multiple images)
            images_to_add = []
            if input_images:
                images_to_add = input_images if isinstance(input_images, list) else [input_images]
            elif input_image:
                images_to_add = [input_image]
            
            # Add reference images
            max_images = 14 if model == "pro" else 3
            if len(images_to_add) > max_images:
                print(f"⚠ Warning: {model} model supports up to {max_images} images, using first {max_images}")
                images_to_add = images_to_add[:max_images]
            
            for img_path in images_to_add:
                if not os.path.exists(img_path):
                    print(f"✗ Input image not found: {img_path}")
                    return False
                image = Image.open(img_path)
                contents.append(image)
            
            if images_to_add:
                print(f"  Using {len(images_to_add)} reference image(s)")
            
            # Build config
            config = types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                ),
            )
            
            # Add resolution for pro model
            if model == "pro":
                config.image_config.image_size = resolution
            
            print(f"→ Generating texture using {model_id}...")
            print(f"  Prompt: {prompt[:60]}...")
            print(f"  Aspect ratio: {aspect_ratio}")
            
            # Generate content
            response = self.client.models.generate_content(
                model=model_id,
                contents=contents,
                config=config,
            )
            
            # Extract and save image
            image_saved = False
            for part in response.parts:
                if part.text:
                    print(f"  Model response: {part.text[:100]}...")
                
                if hasattr(part, 'inline_data') and part.inline_data:
                    if hasattr(part.inline_data, 'mime_type') and 'image' in part.inline_data.mime_type:
                        image = part.as_image()
                        if image:
                            # Create output directory if needed
                            os.makedirs(os.path.dirname(output_path), exist_ok=True)
                            image.save(output_path)
                            image_saved = True
                            print(f"✓ Texture saved to: {output_path}")
                            if hasattr(image, 'size'):
                                print(f"  Size: {image.size}")
            
            if not image_saved:
                print("✗ No image generated in response")
                return False
            
            return True
            
            return True
            
        except Exception as e:
            print(f"✗ Error generating texture: {e}")
            return False
    
    def batch_generate(
        self,
        config_file: str,
        base_output_dir: str,
        model: Literal["fast", "pro"] = "fast",
    ) -> dict:
        """
        Generate multiple textures from a config file.
        
        Args:
            config_file: JSON file with texture specifications
            base_output_dir: Base directory for output textures
            model: Model to use for generation
        
        Returns:
            Dictionary with generation results
        """
        if not os.path.exists(config_file):
            print(f"✗ Config file not found: {config_file}")
            return {"total": 0, "successful": 0, "failed": 0}
        
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        results = {"total": 0, "successful": 0, "failed": 0, "textures": []}
        config_dir = os.path.dirname(os.path.abspath(config_file))
        
        for texture_spec in config.get("textures", []):
            results["total"] += 1
            
            prompt = texture_spec.get("prompt")
            name = texture_spec.get("name", f"texture_{results['total']}")
            texture_type = texture_spec.get("type", "block")
            output_path = os.path.join(base_output_dir, f"{name}.png")
            
            # Handle reference images - resolve relative paths
            input_images = None
            
            # Support both old single reference_image and new reference_images array
            ref_images = texture_spec.get("reference_images") or texture_spec.get("reference_image")
            
            if ref_images:
                # Convert single image to list
                if isinstance(ref_images, str):
                    ref_images = [ref_images]
                
                # Resolve relative paths
                resolved_images = []
                for img_path in ref_images:
                    if not os.path.isabs(img_path):
                        img_path = os.path.join(config_dir, img_path)
                    resolved_images.append(img_path)
                input_images = resolved_images
            
            if not prompt:
                print(f"✗ Skipping texture '{name}': no prompt provided")
                results["failed"] += 1
                continue
            
            print(f"\n[{results['total']}/{len(config.get('textures', []))}]")
            success = self.generate_texture(
                prompt=prompt,
                output_path=output_path,
                model=model,
                texture_type=texture_type,
                input_images=input_images,
            )
            
            if success:
                results["successful"] += 1
                results["textures"].append({
                    "name": name,
                    "path": output_path,
                    "status": "success"
                })
            else:
                results["failed"] += 1
                results["textures"].append({
                    "name": name,
                    "status": "failed"
                })
            
            # Rate limiting
            time.sleep(1)
        
        return results


def main():
    """Command-line interface for texture generation."""
    parser = argparse.ArgumentParser(
        description="Generate Minecraft textures using Google Gemini API"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Single texture generation
    single = subparsers.add_parser("single", help="Generate a single texture")
    single.add_argument("prompt", help="Texture description")
    single.add_argument("-o", "--output", required=True, help="Output file path")
    single.add_argument(
        "-m", "--model", choices=["fast", "pro"], default="fast",
        help="Model to use (default: fast)"
    )
    single.add_argument(
        "-t", "--type", choices=["item", "block", "armor", "gui", "wide"],
        default="block", help="Texture type (default: block)"
    )
    single.add_argument(
        "-r", "--resolution", choices=["1K", "2K", "4K"], default="1K",
        help="Resolution for pro model (default: 1K)"
    )
    single.add_argument("-i", "--input", help="Reference image for editing")
    single.add_argument(
        "--inputs", nargs="+", 
        help="Multiple reference images (up to 3 for fast, up to 14 for pro)"
    )
    
    # Batch generation
    batch = subparsers.add_parser("batch", help="Generate multiple textures from config")
    batch.add_argument("config", help="Config JSON file")
    batch.add_argument("-o", "--output", required=True, help="Output directory")
    batch.add_argument(
        "-m", "--model", choices=["fast", "pro"], default="fast",
        help="Model to use (default: fast)"
    )
    
    # List models
    subparsers.add_parser("models", help="List available models")
    
    args = parser.parse_args()
    
    if args.command == "models":
        print("Available Gemini Image Generation Models:")
        print(f"  fast: {TextureGenerator.MODEL_FAST}")
        print(f"       - Optimized for speed and efficiency")
        print(f"       - 1024x1024 resolution")
        print(f"       - Lower cost, faster generation")
        print()
        print(f"  pro: {TextureGenerator.MODEL_PRO}")
        print(f"      - Optimized for professional asset production")
        print(f"      - Supports 1K, 2K, 4K resolutions")
        print(f"      - Advanced reasoning and text rendering")
        print()
        print("Set GOOGLE_API_KEY environment variable to use these models.")
        return
    
    # Initialize generator
    try:
        generator = TextureGenerator()
    except ValueError as e:
        print(f"✗ Initialization failed: {e}")
        sys.exit(1)
    
    if args.command == "single":
        # Handle both single --input and multiple --inputs
        input_images = None
        if args.inputs:
            input_images = args.inputs
        elif args.input:
            input_images = [args.input]
        
        success = generator.generate_texture(
            prompt=args.prompt,
            output_path=args.output,
            model=args.model,
            texture_type=args.type,
            input_images=input_images,
            resolution=args.resolution,
        )
        sys.exit(0 if success else 1)
    
    elif args.command == "batch":
        results = generator.batch_generate(
            config_file=args.config,
            base_output_dir=args.output,
            model=args.model,
        )
        print("\n" + "="*50)
        print("Batch Generation Results:")
        print(f"  Total:      {results['total']}")
        print(f"  Successful: {results['successful']}")
        print(f"  Failed:     {results['failed']}")
        sys.exit(0 if results['failed'] == 0 else 1)


if __name__ == "__main__":
    main()
