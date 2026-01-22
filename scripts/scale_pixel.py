#!/usr/bin/env python3
"""
Scale images down while preserving pixel style (no blending/antialiasing).
Uses nearest-neighbor resampling to keep crisp pixels.

Examples:
  - Downscale to 16x16:
      python scripts/scale_pixel.py input.png -o output.png --size 16
  - Downscale to width/height:
      python scripts/scale_pixel.py input.png -o output.png --width 16 --height 16
  - Scale by factor (e.g., 0.25 = 25%):
      python scripts/scale_pixel.py input.png -o output.png --factor 0.25
  - Batch process a folder:
      python scripts/scale_pixel.py --input-dir generated_textures --output-dir generated_textures/16x16 --size 16
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional, Tuple

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Downscale images with nearest-neighbor resampling to preserve pixel art style."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("input", nargs="?", help="Input image file path")
    group.add_argument("--input-dir", help="Input directory containing images to process")

    parser.add_argument("-o", "--output", help="Output image file path (for single file mode)")
    parser.add_argument("--output-dir", help="Output directory (for batch mode)")

    size_group = parser.add_mutually_exclusive_group(required=True)
    size_group.add_argument("--size", type=int, help="Target square size (e.g., 16 for 16x16)")
    size_group.add_argument("--factor", type=float, help="Scale factor (e.g., 0.5 = 50%%)")
    size_group.add_argument("--width", type=int, help="Target width in pixels")
    parser.add_argument("--height", type=int, help="Target height in pixels (used with --width)")

    parser.add_argument("--crop-to-square", action="store_true", help="Crop input to square before resizing")
    parser.add_argument("--background", default="transparent", help="Background color when padding (transparent or hex like #000000)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument("--extensions", nargs="+", default=[".png", ".jpg", ".jpeg", ".webp"], help="Extensions for batch mode")

    return parser.parse_args()


def _parse_bg(color: str) -> Optional[Tuple[int, int, int, int]]:
    if color.lower() == "transparent":
        return (0, 0, 0, 0)
    if color.startswith("#") and len(color) in (4, 7):
        # #RGB or #RRGGBB
        if len(color) == 4:
            r = int(color[1] * 2, 16)
            g = int(color[2] * 2, 16)
            b = int(color[3] * 2, 16)
        else:
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
        return (r, g, b, 255)
    raise ValueError(f"Unsupported background color: {color}")


def _compute_target_size(img: Image.Image, args: argparse.Namespace) -> Tuple[int, int]:
    w, h = img.size
    if args.size:
        return (args.size, args.size)
    if args.factor:
        tw = max(1, int(round(w * args.factor)))
        th = max(1, int(round(h * args.factor)))
        return (tw, th)
    if args.width and args.height:
        return (args.width, args.height)
    if args.width and not args.height:
        # keep aspect ratio
        th = max(1, int(round(h * (args.width / w))))
        return (args.width, th)
    raise ValueError("No target size specified")


def _ensure_rgba(img: Image.Image) -> Image.Image:
    if img.mode in ("RGBA", "LA"):
        return img.convert("RGBA")
    if img.mode == "P":
        return img.convert("RGBA")
    return img.convert("RGBA")


def _crop_to_square(img: Image.Image) -> Image.Image:
    w, h = img.size
    if w == h:
        return img
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return img.crop((left, top, left + side, top + side))


def _pad_to_target(img: Image.Image, target_size: Tuple[int, int], bg: Tuple[int, int, int, int]) -> Image.Image:
    tw, th = target_size
    # If aspect ratio differs, pad with background to target size
    canvas = Image.new("RGBA", (tw, th), bg)
    # Fit image within target while preserving aspect
    iw, ih = img.size
    # If already same size, just return
    if (iw, ih) == (tw, th):
        return img
    # Resize to fit either width or height exactly without blending
    scale = min(tw / iw, th / ih)
    nw = max(1, int(round(iw * scale)))
    nh = max(1, int(round(ih * scale)))
    resized = img.resize((nw, nh), resample=Image.NEAREST)
    x = (tw - nw) // 2
    y = (th - nh) // 2
    canvas.paste(resized, (x, y))
    return canvas


def downscale_image(input_path: str, output_path: str, args: argparse.Namespace) -> bool:
    try:
        img = Image.open(input_path)
        img = _ensure_rgba(img)
        if args.crop_to_square:
            img = _crop_to_square(img)
        target_size = _compute_target_size(img, args)

        # If exact target aspect, simple nearest-neighbor resize
        if img.size[0] * target_size[1] == img.size[1] * target_size[0]:
            out = img.resize(target_size, resample=Image.NEAREST)
        else:
            bg = _parse_bg(args.background)
            out = _pad_to_target(img, target_size, bg)

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        if os.path.exists(output_path) and not args.overwrite:
            print(f"✗ Exists, use --overwrite: {output_path}")
            return False
        out.save(output_path)
        print(f"✓ Saved: {output_path} ({out.size[0]}x{out.size[1]})")
        return True
    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")
        return False


def run_single(args: argparse.Namespace) -> int:
    if not args.input or not args.output:
        print("✗ Single mode requires --output and input path")
        return 1
    return 0 if downscale_image(args.input, args.output, args) else 1


def run_batch(args: argparse.Namespace) -> int:
    if not args.input_dir or not args.output_dir:
        print("✗ Batch mode requires --input-dir and --output-dir")
        return 1
    in_dir = Path(args.input_dir)
    out_dir = Path(args.output_dir)
    if not in_dir.exists():
        print(f"✗ Input directory not found: {in_dir}")
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    ok = 0
    exts = {e.lower() for e in args.extensions}
    for path in in_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in exts:
            rel = path.relative_to(in_dir)
            out_path = out_dir / rel
            out_path.parent.mkdir(parents=True, exist_ok=True)
            count += 1
            if downscale_image(str(path), str(out_path), args):
                ok += 1
    print(f"Done. Processed {count}, succeeded {ok}, failed {count - ok}.")
    return 0 if ok == count else 1


def main():
    args = parse_args()
    if args.input_dir:
        sys.exit(run_batch(args))
    else:
        sys.exit(run_single(args))


if __name__ == "__main__":
    main()
