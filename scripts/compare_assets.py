#!/usr/bin/env python3
"""Compare root assets against template assets with colorized output."""
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
from typing import Iterable, List, Tuple

COLOR_RESET = "\033[0m"
COLORS = {
    "identical": "\033[33m",  # yellow
    "missing": "\033[31m",    # red
    "different": "\033[32m",  # green
}


def hash_file(path: Path) -> str:
    """Return the SHA256 hash of a file."""
    sha = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            sha.update(chunk)
    return sha.hexdigest()


def gather_files(base: Path) -> List[Path]:
    """Return all files under *base* recursively."""
    return sorted(p for p in base.rglob("*") if p.is_file())


def compare_assets(root_assets: Path, template_assets: Path) -> None:
    root_files = gather_files(root_assets)
    results: List[Tuple[str, Path]] = []
    counts = {"identical": 0, "missing": 0, "different": 0}

    for root_file in root_files:
        rel_path = root_file.relative_to(root_assets)
        template_file = template_assets / rel_path

        if not template_file.exists():
            status = "missing"
        elif hash_file(root_file) == hash_file(template_file):
            status = "identical"
        else:
            status = "different"

        counts[status] += 1
        results.append((status, rel_path))

    total = sum(counts.values())
    identical_ratio = (counts["identical"] / total * 100) if total else 100.0

    print(f"Compared {total} root files; {counts['identical']} identical ({identical_ratio:.2f}%).")
    for status, rel_path in results:
        color = COLORS[status]
        label = status.upper().ljust(9)
        print(f"{color}[{label}] {rel_path}{COLOR_RESET}")

    print("\nSummary:")
    for key in ("identical", "missing", "different"):
        count = counts[key]
        percent = (count / total * 100) if total else 0.0
        color = COLORS[key]
        title = key.title().ljust(9)
        print(f"{color}{title}{COLOR_RESET}: {count} files ({percent:.2f}%)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare the current pack's assets with the template pack.")
    parser.add_argument(
        "root",
        nargs="?",
        default=Path.cwd() / "assets",
        type=Path,
        help="Path to the root pack's assets directory (default: ./assets)",
    )
    parser.add_argument(
        "template",
        nargs="?",
        default=Path(".packs/template-1.21.11/assets"),
        type=Path,
        help="Path to the template pack's assets directory",
    )
    args = parser.parse_args()

    root_assets = args.root.resolve()
    template_assets = args.template.resolve()

    if not root_assets.exists():
        raise SystemExit(f"Root assets folder not found: {root_assets}")
    if not template_assets.exists():
        raise SystemExit(f"Template assets folder not found: {template_assets}")

    compare_assets(root_assets, template_assets)


if __name__ == "__main__":
    main()
