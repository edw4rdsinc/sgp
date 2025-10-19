#!/usr/bin/env python3
"""
FINAL COMPLETE SHORTLISTS - After reviewing EVERY 3RD PHOTO (365 total)
Including newly discovered console photo!
"""

import os
import shutil

SOURCE_DIR = "/home/sam/Downloads/images/SGP/Photos-1-001/"
OUTPUT_BASE = "images/shortlists"

# COMPLETE candidates based on FULL systematic review
candidates = {
    'festival_stage': [
        (755, 'IMG_20240718_184505346.jpg', '★ BEST - outdoor lake stage with line arrays'),
        (785, 'IMG_20240727_143825796_HDR.jpg', '★ BEST - large outdoor truss PA daytime'),
        (30, '20180720_205509.jpg', '★ EXCELLENT - outdoor festival crowd evening'),
        (50, '20180823_192641.jpg', 'EXCELLENT - huge outdoor crowd daytime'),
        (55, '20180823_204318.jpg', 'EXCELLENT - nighttime festival with moon'),
        (480, 'IMG_20210724_194238479.jpg', 'EXCELLENT - outdoor stage truss daytime'),
        (175, '20190817_201101.jpg', 'outdoor barn stage evening'),
        (600, 'IMG_20230727_192521371.jpg', 'outdoor community event wide'),
        (3, '20180713_152346.jpg', 'large outdoor stage daytime'),
        (299, 'IMAG0347.jpg', 'large festival stage with truss'),
    ],

    'cozy_venue': [
        (311, 'IMAG0586.jpg', '★ BEST - intimate blue lighting'),
        (780, 'IMG_20240724_193749142_HDR~2.jpg', '★ EXCELLENT - Wednesday Music in Parks tent'),
        (605, 'IMG_20230804_172316401.jpg', '★ EXCELLENT - First Friday outdoor stage'),
        (245, '20210430_225907.jpg', '★ EXCELLENT - intimate barn venue crowd'),
        (570, 'IMG_20230527_235640508.jpg', 'EXCELLENT - covered outdoor stage night'),
        (450, 'IMG_20180512_215834.jpg', 'band in small venue'),
        (75, '20181004_201001.jpg', 'Ponderosa venue'),
        (330, 'IMG_20170121_193050.jpg', 'Slicker band on stage'),
        (315, 'IMAG0590.jpg', 'church stage purple/blue'),
        (5, '20180714_211835.jpg', 'small club Trent Beaver'),
    ],

    'full_production': [
        (695, 'IMG_20240126_224601410.jpg', '★ BEST - ballroom overhead orchestra STUNNING'),
        (210, '20200120_125321_HDR.jpg', '★ BEST - EREBUS stage fog video wall AMAZING'),
        (540, 'IMG_20230127_222401689.jpg', '★ BEST - orchestra overhead balcony view'),
        (385, 'IMG_20180126_204439.jpg', '★ EXCELLENT - dramatic ballroom ceiling'),
        (325, 'IMAG0618.jpg', '★ EXCELLENT - ballroom gobo patterns'),
        (455, 'IMG_20180519_195126.jpg', '★ EXCELLENT - EREBUS LED dance floor'),
        (145, '20190426_232344.jpg', 'EXCELLENT - club red chandeliers'),
        (360, 'IMG_20170903_195326.jpg', 'EXCELLENT - stage with video backdrop'),
        (510, 'IMG_20211009_210541735.jpg', 'EXCELLENT - bar band performance'),
        (100, '20181221_235051.jpg', 'EXCELLENT - band with lighting'),
        (485, 'IMG_20210724_215256824.jpg', 'band fog truss'),
        (70, '20180929_211810.jpg', 'band with fog'),
    ],

    'on_stage_musician': [
        (180, '20190921_183007.jpg', '★ EXCELLENT - drummer outdoor stage'),
        (635, 'IMG_20231021_192037948.jpg', '★ EXCELLENT - band modern stage'),
        (315, 'IMAG0590.jpg', '★ EXCELLENT - stage purple blue dramatic'),
        (240, '20210417_190148.jpg', 'EXCELLENT - stage with good lighting'),
        (65, '20180929_205219.jpg', 'EXCELLENT - band dramatic blue'),
        (70, '20180929_211810.jpg', 'band with fog'),
        (175, '20190817_201101.jpg', 'band on outdoor stage'),
        (330, 'IMG_20170121_193050.jpg', 'Slicker band'),
        (450, 'IMG_20180512_215834.jpg', 'band small venue'),
        (125, '20190316_175137.jpg', 'band Westside'),
    ],

    'venue_partnership': [
        (0, '07bde9e3-edde-46a2-b60d-e41924321d0d.jpg', '★ BEST - setup teamwork'),
        (575, 'IMG_20230608_173124096.jpg', 'large event space setup'),
        (390, 'IMG_20180224_170323.jpg', 'corporate event setup'),
        (120, '20190313_164008.jpg', 'large venue setup'),
        (185, '20191102_164133.jpg', 'venue setup daytime'),
    ],

    'reliability_setup': [
        (785, 'IMG_20240727_143825796_HDR.jpg', '★ BEST - outdoor professional truss daytime'),
        (755, 'IMG_20240718_184505346.jpg', '★ EXCELLENT - clean outdoor stage'),
        (480, 'IMG_20210724_194238479.jpg', '★ EXCELLENT - outdoor stage truss daytime'),
        (300, 'IMAG0349.jpg', 'EXCELLENT - PA speaker stack'),
        (3, '20180713_152346.jpg', 'daytime stage setup'),
        (605, 'IMG_20230804_172316401.jpg', 'professional outdoor setup'),
        (2, '20180713_152325.jpg', 'outdoor stage setup'),
    ],

    'hero_background': [
        (695, 'IMG_20240126_224601410.jpg', '★ BEST - ballroom overhead SPECTACULAR'),
        (210, '20200120_125321_HDR.jpg', '★ BEST - EREBUS wide fog lights'),
        (540, 'IMG_20230127_222401689.jpg', '★ BEST - orchestra overhead wide'),
        (50, '20180823_192641.jpg', '★ EXCELLENT - huge crowd wide'),
        (55, '20180823_204318.jpg', '★ EXCELLENT - nighttime wide'),
        (145, '20190426_232344.jpg', 'club crowd chandeliers'),
        (30, '20180720_205509.jpg', 'outdoor festival wide'),
        (385, 'IMG_20180126_204439.jpg', 'dramatic ballroom lighting'),
    ],

    'console_engineer': [
        (420, 'IMG_20180310_170115.jpg', '★ FOUND! - mixing console with outdoor event'),
    ],
}

def create_final_shortlists():
    """Create final comprehensive shortlist folders"""

    if os.path.exists(OUTPUT_BASE):
        shutil.rmtree(OUTPUT_BASE)

    os.makedirs(OUTPUT_BASE)

    print(f"\n{'='*70}")
    print(f"FINAL COMPLETE SHORTLISTS - FULL REVIEW OF EVERY 3RD PHOTO")
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
    print(f"✅ COMPLETE! Final shortlists: {os.path.abspath(OUTPUT_BASE)}/")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    create_final_shortlists()
