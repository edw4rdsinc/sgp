#!/usr/bin/env python3
"""
More comprehensive photo review
Sample every 10th photo to review ~110 photos instead of ~50
"""

import os

PREVIEW_DIR = "/tmp/sgp_photo_previews/"

preview_files = sorted([f for f in os.listdir(PREVIEW_DIR) if f.startswith('preview_')])
total = len(preview_files)

# Sample every 10th photo for more thorough coverage
step = 10
samples = list(range(0, total, step))

print(f"Total photos: {total}")
print(f"Will review: {len(samples)} photos (every {step}th)")
print(f"\nSample indices to review in batches of 10:\n")

for i in range(0, len(samples), 10):
    batch = samples[i:i+10]
    print(f"Batch {i//10 + 1} (indices {batch[0]}-{batch[-1] if len(batch) > 1 else batch[0]}):")
    for idx in batch:
        if idx < len(preview_files):
            print(f"  {idx:04d}: {preview_files[idx]}")
    print()

print(f"\nTotal batches: {(len(samples) + 9) // 10}")
