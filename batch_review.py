#!/usr/bin/env python3
"""
Generate batches of specific photos to review for each category
Output paths that Claude can easily read
"""

import os

PREVIEW_DIR = "/tmp/sgp_photo_previews/"

def generate_review_batches():
    """Generate specific photo indices to review for each category"""

    preview_files = sorted([f for f in os.listdir(PREVIEW_DIR) if f.startswith('preview_')])
    total = len(preview_files)

    print(f"Total photos: {total}\n")

    # Define search patterns for each category
    review_plan = {
        'MIXING_CONSOLE': {
            'description': 'Looking for: mixing boards, consoles, FOH, engineer at board',
            'indices': list(range(0, total, 50))[:30]  # Every 50th photo, max 30
        },
        'OUTDOOR_STAGES': {
            'description': 'Looking for: outdoor events, festivals, large stages, crowds',
            'indices': list(range(2, total, 30))[:40]  # Different offset
        },
        'INDOOR_PERFORMERS': {
            'description': 'Looking for: bands on stage, performers, intimate venues',
            'indices': list(range(10, total, 25))[:50]
        },
        'SETUP_SHOTS': {
            'description': 'Looking for: equipment setup, daytime, organized gear',
            'indices': list(range(5, total, 35))[:35]
        },
        'FULL_PRODUCTION': {
            'description': 'Looking for: lighting rigs, DJ setups, mid-size venues',
            'indices': list(range(15, total, 40))[:30]
        }
    }

    # Print review plan
    for category, plan in review_plan.items():
        print(f"\n{'='*70}")
        print(f"{category}")
        print(f"{'='*70}")
        print(f"{plan['description']}")
        print(f"\nReview these {len(plan['indices'])} photos:")

        # Group into batches of 5 for easier reading
        for i in range(0, len(plan['indices']), 5):
            batch = plan['indices'][i:i+5]
            batch_files = [preview_files[idx] for idx in batch if idx < len(preview_files)]
            print(f"\nBatch {i//5 + 1}:")
            for idx, fname in zip(batch, batch_files):
                print(f"  [{idx:04d}] {fname}")

if __name__ == "__main__":
    generate_review_batches()
