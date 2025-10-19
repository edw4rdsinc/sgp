#!/usr/bin/env python3
"""
Create shortlists of photos for each category
Outputs a list of preview files to review for each category
"""

import os

PREVIEW_DIR = "/tmp/sgp_photo_previews/"

# Get all preview files sorted
preview_files = sorted([f for f in os.listdir(PREVIEW_DIR) if f.startswith('preview_')])

print(f"Total preview files: {len(preview_files)}")
print(f"\nTo systematically review, we'll sample every ~20th photo to get ~55 samples")
print(f"This gives us a good spread across the entire collection\n")

# Sample every 20th photo
step = 20
samples = []
for i in range(0, len(preview_files), step):
    samples.append((i, preview_files[i]))

print(f"Sample indices to review (total: {len(samples)}):")
print("=" * 70)

for idx, filename in samples:
    print(f"{idx:04d}: {filename}")

print("\n" + "=" * 70)
print(f"\nSuggested review batches of 10:")
for i in range(0, len(samples), 10):
    batch = samples[i:i+10]
    indices = [str(idx) for idx, _ in batch]
    print(f"Batch {i//10 + 1}: indices {', '.join(indices)}")
