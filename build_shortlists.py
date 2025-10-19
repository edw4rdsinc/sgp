#!/usr/bin/env python3
"""
Build comprehensive shortlists by reviewing every 5th photo
"""

import os
import shutil

SOURCE_DIR = "/home/sam/Downloads/images/SGP/Photos-1-001/"
PREVIEW_DIR = "/tmp/sgp_photo_previews/"
OUTPUT_BASE = "images/shortlists"

# Manually curated list based on systematic review
# Format: (preview_index, original_filename, categories)

candidates = {
    'festival_stage': [
        (30, '20180720_205509.jpg', 'EXCELLENT - outdoor festival crowd'),
        (50, '20180823_192641.jpg', 'EXCELLENT - huge outdoor crowd'),
        (3, '20180713_152346.jpg', 'large outdoor stage daytime'),
        (299, 'IMAG0347.jpg', 'large festival stage with truss'),
        (2, '20180713_152325.jpg', 'outdoor stage with PA'),
    ],

    'cozy_venue': [
        (311, 'IMAG0586.jpg', 'EXCELLENT - intimate stage blue lighting'),
        (304, 'IMAG0390.jpg', 'small covered stage'),
        (5, '20180714_211835.jpg', 'small club Trent Beaver'),
        (15, '20180714_214806.jpg', 'small stage performer'),
        (25, '20180714_223309.jpg', 'small stage band'),
    ],

    'full_production': [
        (100, '20181221_235051.jpg', 'EXCELLENT - band with lighting'),
        (70, '20180929_211810.jpg', 'EXCELLENT - band with fog'),
        (40, '20180721_221826.jpg', 'DJ with lighting truss'),
        (35, '20180721_211440.jpg', 'DJ event with flags'),
        (45, '20180721_221952.jpg', 'DJ with truss lighting'),
        (293, 'IMAG0029.jpg', 'corporate ballroom uplighting'),
    ],

    'on_stage_musician': [
        (20, '20180714_223219.jpg', 'band on stage'),
        (10, '20180714_211959.jpg', 'Trent Beaver band'),
        (160, '20190801_225105.jpg', 'band dramatic lighting'),
        (5, '20180714_211835.jpg', 'performer on stage'),
        (15, '20180714_214806.jpg', 'performer with guitar'),
        (25, '20180714_223309.jpg', 'band performing'),
    ],

    'venue_partnership': [
        (0, '07bde9e3-edde-46a2-b60d-e41924321d0d.jpg', 'setup in progress'),
        (120, '20190313_164008.jpg', 'large venue setup'),
        (110, '20190216_151343.jpg', 'venue setup teardown'),
    ],

    'reliability_setup': [
        (3, '20180713_152346.jpg', 'EXCELLENT - daytime stage setup'),
        (2, '20180713_152325.jpg', 'outdoor stage setup'),
        (299, 'IMAG0347.jpg', 'clean festival stage setup'),
    ],

    'hero_background': [
        (50, '20180823_192641.jpg', 'EXCELLENT - huge crowd wide shot'),
        (30, '20180720_205509.jpg', 'outdoor festival wide'),
        (35, '20180721_211440.jpg', 'wide venue shot with flags'),
    ],
}

def create_shortlist_folders():
    """Create organized folders with top choices"""

    for category, photos in candidates.items():
        category_dir = os.path.join(OUTPUT_BASE, category)
        os.makedirs(category_dir, exist_ok=True)

        print(f"\n{'='*60}")
        print(f"Category: {category.upper().replace('_', ' ')}")
        print(f"{'='*60}")

        for rank, (idx, filename, description) in enumerate(photos, 1):
            source = os.path.join(SOURCE_DIR, filename)

            if not os.path.exists(source):
                print(f"  ⚠ Missing: {filename}")
                continue

            # Name with rank for easy sorting
            dest_name = f"{rank:02d}_{filename}"
            dest = os.path.join(category_dir, dest_name)

            shutil.copy2(source, dest)
            print(f"  ✓ [{rank}] {filename}")
            print(f"      → {description}")

    print(f"\n{'='*60}")
    print(f"✅ All shortlists created in: {OUTPUT_BASE}/")
    print(f"{'='*60}")

if __name__ == "__main__":
    create_shortlist_folders()
