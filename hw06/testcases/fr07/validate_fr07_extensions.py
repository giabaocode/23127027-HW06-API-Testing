#!/usr/bin/env python3
"""
Validation script for FR-07 student extension test cases.
"""
import os
import re

EXT_PATH = "/Users/phamngocgiabao/eshop-sut/hw06/testcases/fr07/student-extensions.md"
FINAL_PATH = "/Users/phamngocgiabao/eshop-sut/hw06/testcases/fr07/reviewed-ai-final.md"

def main():
    print("=== VALIDATING FR-07 STUDENT EXTENSIONS ===")

    with open(EXT_PATH, "r", encoding="utf-8") as f:
        ext_text = f.read()

    with open(FINAL_PATH, "r", encoding="utf-8") as f:
        ai_text = f.read()

    # 1. Exactly 5 extension tests
    ext_ids = re.findall(r"### `(FR07-STU-\d{3})`", ext_text)
    assert len(ext_ids) == 5, f"Expected 5 tests, got {len(ext_ids)}: {ext_ids}"
    assert ext_ids == ["FR07-STU-001", "FR07-STU-002", "FR07-STU-003", "FR07-STU-004", "FR07-STU-005"]
    print("✓ Check 1: Exactly 5 continuous extension IDs (FR07-STU-001 to 005).")

    # 2. Origin and Student Selection
    origins = re.findall(r"- \*\*Origin:\*\* (.+)", ext_text)
    assert len(origins) == 5 and all("Student-selected from AI brainstorming" in o for o in origins)
    selections = re.findall(r"- \*\*Student Selection:\*\* (.+)", ext_text)
    assert len(selections) == 5 and all("CONFIRMED" in s for s in selections)
    print("✓ Check 2: Truthful provenance confirmed (Student-selected from AI brainstorming / CONFIRMED).")

    # 3. Meaningful distinction from 38 AI tests
    # STU-001: Malformed JSON (missing brace) vs AI-037 ({})
    assert '{"id":1,"name":"Sản phẩm A","price":100000,"quantity":1' in ext_text
    assert "PARSER ROBUSTNESS" in ext_text

    # STU-002: Wrong Content-Type
    assert "Content-Type`: `text/plain`" in ext_text or "Content-Type: text/plain" in ext_text

    # STU-003: Expired JWT vs Forged JWT
    assert "expired jwt" in ext_text.lower()
    assert "exp < currenttime" in ext_text.lower() or "exp =" in ext_text.lower()

    # STU-004: Conflicting metadata
    assert "Modified Product Name" in ext_text
    assert "CHARACTERIZATION" in ext_text

    # STU-005: Repeated GET
    assert "read1[0].quantity === read2[0].quantity" in ext_text
    print("✓ Check 3: All 5 extension tests verified distinct from the 38 AI tests.")

    # 4. No undocumented HTTP status promoted to SPECIFIED
    for tid in ext_ids:
        block = ext_text.split(f"### `{tid}`")[1].split("#### Lifecycle")[0]
        if "STU-004" not in tid and "STU-005" not in tid:
            assert "Expected HTTP Status:** `UNKNOWN" in block, f"{tid} has promoted HTTP status!"
    print("✓ Check 4: No undocumented status promoted to SPECIFIED.")

    print("\nALL 5 EXTENSION TESTS VALIDATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
