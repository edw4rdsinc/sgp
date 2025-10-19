#!/usr/bin/env python3
"""
Smart photo categorization helper
Uses systematic approach to find candidates for each category
"""

import os
import json
from PIL import Image

PREVIEW_DIR = "/tmp/sgp_photo_previews/"
SOURCE_DIR = "/home/sam/Downloads/images/SGP/Photos-1-001/"

def get_image_info(preview_path, source_filename):
    """Get basic image info"""
    try:
        with Image.open(preview_path) as img:
            width, height = img.size
            aspect = width / height if height > 0 else 1
            return {
                'width': width,
                'height': height,
                'aspect_ratio': round(aspect, 2),
                'orientation': 'landscape' if aspect > 1.1 else ('portrait' if aspect < 0.9 else 'square')
            }
    except:
        return None

def categorize_photos():
    """Systematically categorize photos into potential candidates"""

    preview_files = sorted([f for f in os.listdir(PREVIEW_DIR) if f.startswith('preview_')])

    # Categories we're looking for
    categories = {
        'hero_background': [],      # Wide shots, exciting atmosphere
        'console_engineer': [],      # Mixing boards, engineers
        'on_stage_performer': [],    # Musicians performing
        'venue_staff': [],           # Setup, teamwork
        'reliability_setup': [],     # Clean setup, organized
        'engineer_at_work': [],      # Engineer with event in background
        'cozy_venue': [],            # Small intimate setups
        'full_production': [],       # Mid-size with lighting
        'festival_stage': []         # Large outdoor stages
    }

    print(f"Analyzing {len(preview_files)} preview files...")
    print("=" * 70)

    # Sample every 10th photo for faster initial categorization
    sample_step = 10

    for i in range(0, len(preview_files), sample_step):
        preview_file = preview_files[i]
        preview_path = os.path.join(PREVIEW_DIR, preview_file)

        # Extract original filename
        parts = preview_file.replace('preview_', '').split('_', 1)
        if len(parts) > 1:
            source_filename = parts[1]
        else:
            continue

        info = get_image_info(preview_path, source_filename)
        if not info:
            continue

        # Store candidate info
        candidate = {
            'index': i,
            'preview': preview_file,
            'source': source_filename,
            'aspect': info['aspect_ratio'],
            'orientation': info['orientation']
        }

        # Categorize based on aspect ratio and other heuristics
        # Wide landscape photos good for hero backgrounds
        if info['aspect_ratio'] > 1.5:
            categories['hero_background'].append(candidate)

        # Photos from specific date ranges that might have outdoor events (summer)
        if '0720' in source_filename or '0721' in source_filename or '0801' in source_filename:
            categories['festival_stage'].append(candidate)

        # All landscape photos are potential candidates for various categories
        if info['orientation'] == 'landscape':
            categories['full_production'].append(candidate)
            categories['on_stage_performer'].append(candidate)

        # Photos with "IMG_" prefix from phones often have good action shots
        if source_filename.startswith('IMG_2'):
            categories['engineer_at_work'].append(candidate)
            categories['cozy_venue'].append(candidate)

    # Print summary
    print("\nINITIAL SAMPLING RESULTS:")
    print("=" * 70)
    for cat_name, candidates in categories.items():
        print(f"{cat_name}: {len(candidates)} candidates")

    # Save detailed results
    output = {
        'sampling_step': sample_step,
        'total_sampled': len(preview_files) // sample_step,
        'categories': {}
    }

    # For each category, show top 20 candidates to review
    for cat_name, candidates in categories.items():
        output['categories'][cat_name] = candidates[:20]

    with open('photo_candidates.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nDetailed candidates saved to: photo_candidates.json")

    # Print indices to manually review for each category
    print("\n" + "=" * 70)
    print("RECOMMENDED PHOTOS TO REVIEW MANUALLY:")
    print("=" * 70)

    for cat_name, candidates in categories.items():
        if candidates:
            indices = [str(c['index']) for c in candidates[:10]]
            print(f"\n{cat_name.upper()}:")
            print(f"  Indices: {', '.join(indices)}")

if __name__ == "__main__":
    categorize_photos()
