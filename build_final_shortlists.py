#!/usr/bin/env python3
"""
Build comprehensive shortlists - FINAL VERSION
Based on systematic review of 365+ photos
"""

import os
import shutil

SOURCE_DIR = "/home/sam/Downloads/images/SGP/Photos-1-001/"
OUTPUT_BASE = "images/shortlists"

# Comprehensive candidates based on systematic review
candidates = {
    'festival_stage': [
        (30, '20180720_205509.jpg', 'BEST - outdoor festival crowd evening'),
        (50, '20180823_192641.jpg', 'BEST - huge outdoor crowd daytime'),
        (55, '20180823_204318.jpg', 'BEST - nighttime festival with moon'),
        (175, '20190817_201101.jpg', 'outdoor barn stage evening'),
        (3, '20180713_152346.jpg', 'large outdoor stage daytime'),
        (299, 'IMAG0347.jpg', 'large festival stage with truss'),
        (2, '20180713_152325.jpg', 'outdoor stage with PA'),
    ],

    'cozy_venue': [
        (311, 'IMAG0586.jpg', 'BEST - intimate blue lighting'),
        (75, '20181004_201001.jpg', 'BEST - Ponderosa venue'),
        (135, '20190419_000237.jpg', 'good - band blue lighting'),
        (304, 'IMAG0390.jpg', 'small covered stage'),
        (5, '20180714_211835.jpg', 'small club Trent Beaver'),
        (10, '20180714_211959.jpg', 'intimate club setting'),
        (15, '20180714_214806.jpg', 'small stage performer'),
        (25, '20180714_223309.jpg', 'small stage band'),
    ],

    'full_production': [
        (145, '20190426_232344.jpg', 'BEST - club with red chandeliers crowd'),
        (100, '20181221_235051.jpg', 'BEST - band with lighting'),
        (70, '20180929_211810.jpg', 'BEST - band with fog'),
        (65, '20180929_205219.jpg', 'BEST - band blue lighting'),
        (135, '20190419_000237.jpg', 'band with projection'),
        (40, '20180721_221826.jpg', 'DJ with lighting truss'),
        (35, '20180721_211440.jpg', 'event with flags'),
        (45, '20180721_221952.jpg', 'DJ with truss'),
        (293, 'IMAG0029.jpg', 'corporate ballroom'),
        (195, '20191126_131228.jpg', 'ballroom uplighting'),
    ],

    'on_stage_musician': [
        (65, '20180929_205219.jpg', 'BEST - band dramatic blue'),
        (70, '20180929_211810.jpg', 'BEST - band with fog'),
        (175, '20190817_201101.jpg', 'band on outdoor stage'),
        (125, '20190316_175137.jpg', 'band Westside'),
        (20, '20180714_223219.jpg', 'band on stage'),
        (10, '20180714_211959.jpg', 'Trent Beaver band'),
        (160, '20190801_225105.jpg', 'band dramatic lighting'),
        (5, '20180714_211835.jpg', 'performer on stage'),
        (15, '20180714_214806.jpg', 'performer with guitar'),
        (135, '20190419_000237.jpg', 'band blue lighting'),
    ],

    'venue_partnership': [
        (0, '07bde9e3-edde-46a2-b60d-e41924321d0d.jpg', 'BEST - setup in progress'),
        (120, '20190313_164008.jpg', 'large venue setup'),
        (110, '20190216_151343.jpg', 'venue setup'),
        (185, '20191102_164133.jpg', 'venue setup daytime'),
    ],

    'reliability_setup': [
        (3, '20180713_152346.jpg', 'BEST - daytime stage setup'),
        (2, '20180713_152325.jpg', 'outdoor stage setup'),
        (299, 'IMAG0347.jpg', 'festival stage setup'),
        (115, '20190221_141753.jpg', 'daytime venue'),
        (185, '20191102_164133.jpg', 'professional setup'),
    ],

    'hero_background': [
        (50, '20180823_192641.jpg', 'BEST - huge crowd wide'),
        (55, '20180823_204318.jpg', 'BEST - nighttime wide'),
        (145, '20190426_232344.jpg', 'BEST - club crowd chandeliers'),
        (30, '20180720_205509.jpg', 'outdoor festival wide'),
        (35, '20180721_211440.jpg', 'wide venue flags'),
        (205, '20191126_215120.jpg', 'dramatic lighting wide'),
    ],
}

def create_shortlist_folders():
    """Create organized folders with numbered photos"""

    # Remove old shortlists folder if exists
    if os.path.exists(OUTPUT_BASE):
        shutil.rmtree(OUTPUT_BASE)

    os.makedirs(OUTPUT_BASE)

    print(f"\n{'='*70}")
    print(f"BUILDING COMPREHENSIVE SHORTLISTS")
    print(f"{'='*70}\n")

    for category, photos in candidates.items():
        category_dir = os.path.join(OUTPUT_BASE, category)
        os.makedirs(category_dir, exist_ok=True)

        print(f"\n{category.upper().replace('_', ' ')}:")
        print(f"{'-'*70}")

        for rank, (idx, filename, description) in enumerate(photos, 1):
            source = os.path.join(SOURCE_DIR, filename)

            if not os.path.exists(source):
                print(f"  ⚠ [{rank:02d}] Missing: {filename}")
                continue

            dest_name = f"{rank:02d}_{filename}"
            dest = os.path.join(category_dir, dest_name)

            shutil.copy2(source, dest)
            marker = "★ " if "BEST" in description else "  "
            print(f"{marker}[{rank:02d}] {filename}")
            print(f"       {description}")

        print(f"\n  Total: {len([p for p in photos if os.path.exists(os.path.join(SOURCE_DIR, p[1]))])} photos")

    print(f"\n{'='*70}")
    print(f"✅ COMPLETE! All shortlists created in:")
    print(f"   {os.path.abspath(OUTPUT_BASE)}/")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    create_shortlist_folders()
