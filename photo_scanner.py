#!/usr/bin/env python3
"""
Photo Scanner for SGP Website
Resizes large images and helps identify which photos match website placeholders
"""

import os
from PIL import Image
import sys

# Source directory with original photos
SOURCE_DIR = "/home/sam/Downloads/images/SGP/Photos-1-001/"

# Temporary directory for resized previews
PREVIEW_DIR = "/tmp/sgp_photo_previews/"

# Maximum dimension for preview (to avoid size issues)
MAX_PREVIEW_SIZE = 1200

def setup_preview_directory():
    """Create preview directory if it doesn't exist"""
    if not os.path.exists(PREVIEW_DIR):
        os.makedirs(PREVIEW_DIR)
    print(f"Preview directory: {PREVIEW_DIR}")

def resize_image_for_preview(image_path, output_path, max_size=MAX_PREVIEW_SIZE):
    """
    Resize an image to fit within max_size while maintaining aspect ratio
    Returns True if successful, False otherwise
    """
    try:
        with Image.open(image_path) as img:
            # Get original size
            orig_width, orig_height = img.size

            # Calculate new size maintaining aspect ratio
            if orig_width > max_size or orig_height > max_size:
                if orig_width > orig_height:
                    new_width = max_size
                    new_height = int((max_size / orig_width) * orig_height)
                else:
                    new_height = max_size
                    new_width = int((max_size / orig_height) * orig_width)

                # Resize
                img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Convert RGBA to RGB if necessary
                if img_resized.mode == 'RGBA':
                    img_resized = img_resized.convert('RGB')

                img_resized.save(output_path, 'JPEG', quality=85, optimize=True)
                return True, new_width, new_height
            else:
                # Image is already small enough, just copy
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img.save(output_path, 'JPEG', quality=85, optimize=True)
                return True, orig_width, orig_height

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False, 0, 0

def get_image_files():
    """Get list of all image files in source directory"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    files = []

    for filename in os.listdir(SOURCE_DIR):
        ext = os.path.splitext(filename)[1].lower()
        if ext in image_extensions:
            files.append(filename)

    files.sort()
    return files

def process_batch(start_index=0, batch_size=20):
    """
    Process a batch of images starting from start_index
    """
    image_files = get_image_files()
    total_files = len(image_files)

    print(f"\nTotal images found: {total_files}")
    print(f"Processing batch: {start_index} to {min(start_index + batch_size, total_files)}")
    print("-" * 60)

    batch_files = image_files[start_index:start_index + batch_size]

    for i, filename in enumerate(batch_files, start=start_index):
        source_path = os.path.join(SOURCE_DIR, filename)
        preview_filename = f"preview_{i:04d}_{filename}"
        preview_path = os.path.join(PREVIEW_DIR, preview_filename)

        # Skip if already processed
        if os.path.exists(preview_path):
            print(f"[{i+1}/{total_files}] ✓ Already processed: {filename}")
            continue

        success, width, height = resize_image_for_preview(source_path, preview_path)

        if success:
            print(f"[{i+1}/{total_files}] ✓ Resized {filename} -> {width}x{height}")
        else:
            print(f"[{i+1}/{total_files}] ✗ Failed: {filename}")

    print("-" * 60)
    print(f"Preview files saved to: {PREVIEW_DIR}")
    print(f"Next batch starts at index: {start_index + batch_size}")

    return start_index + batch_size, total_files

if __name__ == "__main__":
    setup_preview_directory()

    # Process images in batches
    if len(sys.argv) > 1:
        start = int(sys.argv[1])
    else:
        start = 0

    batch_size = 30 if len(sys.argv) <= 2 else int(sys.argv[2])

    next_start, total = process_batch(start, batch_size)

    if next_start < total:
        print(f"\nTo process next batch, run:")
        print(f"python3 photo_scanner.py {next_start} {batch_size}")
    else:
        print(f"\n✅ All {total} images processed!")
        print(f"\nPreviews ready at: {PREVIEW_DIR}")
