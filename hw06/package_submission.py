#!/usr/bin/env python3
"""
package_submission.py
Builds the official submission archive: 23127027_HW06_AI_API_100.zip
strictly following PDF Section 14 requirements.
"""

import os
import zipfile
import pypdf
import json

ZIP_FILENAME = "23127027_HW06_AI_API_100.zip"

def create_zip():
    print(f"Creating submission zip: {ZIP_FILENAME}...")
    if os.path.exists(ZIP_FILENAME):
        os.remove(ZIP_FILENAME)

    excluded_patterns = [
        ".ds_store",
        "__pycache__",
        ".git",
        "oral-defense-notes.md",
        ".bak",
        ".env",
        "node_modules",
        "2026.hw06.api testing_en.pdf"
    ]

    with zipfile.ZipFile(ZIP_FILENAME, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Walk hw06 directory
        for root, dirs, files in os.walk("hw06"):
            for f in files:
                full_path = os.path.join(root, f)
                lower_path = full_path.lower()
                
                # Check exclusions
                if any(p in lower_path for p in excluded_patterns):
                    print(f"  [Skipping excluded file] {full_path}")
                    continue

                rel_path = os.path.relpath(full_path, ".")
                zf.write(full_path, rel_path)
                print(f"  + Added: {rel_path}")

        # Also add GitHub Actions workflow to zip so lecturer can inspect CI pipeline
        if os.path.exists(".github/workflows/api-tests.yml"):
            zf.write(".github/workflows/api-tests.yml", ".github/workflows/api-tests.yml")
            print("  + Added: .github/workflows/api-tests.yml")

    size_mb = os.path.getsize(ZIP_FILENAME) / (1024 * 1024)
    print(f"Successfully created {ZIP_FILENAME} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    create_zip()
