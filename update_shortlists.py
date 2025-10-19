#!/usr/bin/env python3
"""
UPDATED comprehensive shortlists after thorough review
"""

import os
import shutil

SOURCE_DIR = "/home/sam/Downloads/images/SGP/Photos-1-001/"
OUTPUT_BASE = "images/shortlists"

# UPDATED candidates based on comprehensive review
candidates = {
    'festival_stage': [
        (755, 'IMG_20240718_184505346.jpg', '★ BEST - outdoor lake stage with line arrays and truss'),
        (785, 'IMG_20240727_143825796_HDR.jpg', '★ BEST - outdoor stage large truss and PA daytime'),
        (30, '20180720_205509.jpg', '★ EXCELLENT - outdoor festival crowd evening'),
        (50, '20180823_192641.jpg', 'EXCELLENT - huge outdoor crowd daytime'),
        (55, '20180823_204318.jpg', 'EXCELLENT - nighttime festival with moon'),
        (175, '20190817_201101.jpg', 'outdoor barn stage evening'),
        (3, '20180713_152346.jpg', 'large outdoor stage daytime'),
        (299, 'IMAG0347.jpg', 'large festival stage with truss'),
    ],

    'cozy_venue': [
        (311, 'IMAG0586.jpg', '★ BEST - intimate blue lighting'),
        (605, 'IMG_20230804_172316401.jpg', '★ EXCELLENT - First Friday outdoor stage'),
        (245, '20210430_225907.jpg', '★ EXCELLENT - intimate barn venue with crowd'),
        (75, '20181004_201001.jpg', 'EXCELLENT - Ponderosa venue'),
        (135, '20190419_000237.jpg', 'band blue lighting'),
        (304, 'IMAG0390.jpg', 'small covered stage'),
        (315, 'IMAG0590.jpg', 'EXCELLENT - church stage purple/blue lighting'),
        (5, '20180714_211835.jpg', 'small club Trent Beaver'),
    ],

    'full_production': [
        (695, 'IMG_20240126_224601410.jpg', '★ BEST - ballroom overhead orchestra incredible'),
        (385, 'IMG_20180126_204439.jpg', '★ EXCELLENT - dramatic ballroom ceiling lighting'),
        (325, 'IMAG0618.jpg', '★ EXCELLENT - ballroom gobo patterns'),
        (455, 'IMG_20180519_195126.jpg', '★ EXCELLENT - EREBUS club LED dance floor'),
        (145, '20190426_232344.jpg', 'EXCELLENT - club red chandeliers crowd'),
        (100, '20181221_235051.jpg', 'EXCELLENT - band with lighting'),
        (485, 'IMG_20210724_215256824.jpg', 'EXCELLENT - band fog and truss'),
        (70, '20180929_211810.jpg', 'EXCELLENT - band with fog'),
        (65, '20180929_205219.jpg', 'EXCELLENT - band blue lighting'),
        (40, '20180721_221826.jpg', 'DJ with lighting truss'),
    ],

    'on_stage_musician': [
        (635, 'IMG_20231021_192037948.jpg', '★ EXCELLENT - band on modern stage'),
        (485, 'IMG_20210724_215256824.jpg', '★ EXCELLENT - performer with fog dramatic'),
        (315, 'IMAG0590.jpg', '★ EXCELLENT - stage view purple blue'),
        (65, '20180929_205219.jpg', 'EXCELLENT - band dramatic blue'),
        (70, '20180929_211810.jpg', 'EXCELLENT - band with fog'),
        (175, '20190817_201101.jpg', 'band on outdoor stage'),
        (125, '20190316_175137.jpg', 'band Westside'),
        (20, '20180714_223219.jpg', 'band on stage'),
        (10, '20180714_211959.jpg', 'Trent Beaver band'),
        (135, '20190419_000237.jpg', 'band blue lighting'),
    ],

    'venue_partnership': [
        (0, '07bde9e3-edde-46a2-b60d-e41924321d0d.jpg', '★ BEST - setup in progress teamwork'),
        (575, 'IMG_20230608_173124096.jpg', 'GOOD - large event space setup'),
        (120, '20190313_164008.jpg', 'large venue setup'),
        (185, '20191102_164133.jpg', 'venue setup daytime'),
    ],

    'reliability_setup': [
        (785, 'IMG_20240727_143825796_HDR.jpg', '★ BEST - outdoor professional truss daytime'),
        (755, 'IMG_20240718_184505346.jpg', '★ EXCELLENT - clean outdoor stage setup'),
        (3, '20180713_152346.jpg', 'EXCELLENT - daytime stage setup'),
        (605, 'IMG_20230804_172316401.jpg', 'professional outdoor setup'),
        (2, '20180713_152325.jpg', 'outdoor stage setup'),
        (299, 'IMAG0347.jpg', 'festival stage setup'),
    ],

    'hero_background': [
        (695, 'IMG_20240126_224601410.jpg', '★ BEST - ballroom overhead wide spectacular'),
        (50, '20180823_192641.jpg', '★ EXCELLENT - huge crowd wide'),
        (55, '20180823_204318.jpg', '★ EXCELLENT - nighttime wide'),
        (145, '20190426_232344.jpg', 'EXCELLENT - club crowd chandeliers'),
        (30, '20180720_205509.jpg', 'outdoor festival wide'),
        (385, 'IMG_20180126_204439.jpg', 'dramatic ballroom lighting'),
    ],
}

def update_shortlists():
    """Update shortlist folders with comprehensive selections"""

    # Remove old shortlists
    if os.path.exists(OUTPUT_BASE):
        shutil.rmtree(OUTPUT_BASE)

    os.makedirs(OUTPUT_BASE)

    print(f"\n{'='*70}")
    print(f"UPDATED COMPREHENSIVE SHORTLISTS - AFTER FULL REVIEW")
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
            marker = "★ " if "★" in description else "  "
            print(f"{marker}[{rank:02d}] {filename}")
            print(f"       {description.replace('★ ', '')}")

        count = len([p for p in photos if os.path.exists(os.path.join(SOURCE_DIR, p[1]))])
        print(f"\n  Total: {count} photos")

    print(f"\n{'='*70}")
    print(f"✅ COMPLETE! Updated shortlists in: {os.path.abspath(OUTPUT_BASE)}/")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    update_shortlists()
