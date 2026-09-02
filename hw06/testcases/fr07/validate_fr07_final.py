#!/usr/bin/env python3
"""
Validation script for FR-07 Human Audit and Reviewed Final Test Suite.
"""
import os
import re
import subprocess
import hashlib

BASE_DIR = "/Users/phamngocgiabao/eshop-sut/hw06/testcases/fr07"
ORIG_PATH = os.path.join(BASE_DIR, "generated-ai-original.md")
AUDIT_PATH = os.path.join(BASE_DIR, "human-audit.md")
COMPACT_PATH = os.path.join(BASE_DIR, "human-review-compact.md")
FINAL_PATH = os.path.join(BASE_DIR, "reviewed-ai-final.md")

def main():
    print("=== PROGRAMMATIC VALIDATION: FR-07 HUMAN AUDIT & REVIEWED FINAL ===")

    # 1. Check generated-ai-original.md against git HEAD~1 (commit ea6f968)
    git_diff = subprocess.run(
        ["git", "diff", "ea6f968", "--", ORIG_PATH],
        capture_output=True, text=True
    )
    assert git_diff.stdout.strip() == "", f"FAIL: generated-ai-original.md has been modified compared to ea6f968!\n{git_diff.stdout}"
    print("✓ Check 1 Passed: generated-ai-original.md is 100% byte-for-byte unchanged from commit ea6f968.")

    # 2. Check human-audit.md
    with open(AUDIT_PATH, "r", encoding="utf-8") as f:
        audit_text = f.read()

    audit_rows = [l for l in audit_text.splitlines() if l.strip().startswith("| **`FR07-AI-")]
    assert len(audit_rows) == 38, f"FAIL: Expected 38 rows in human-audit.md, got {len(audit_rows)}"

    verdicts = []
    for idx, r in enumerate(audit_rows):
        cols = [c.strip() for c in r.split("|")[1:-1]]
        # cols: [Test ID, Coverage ID, Short Test Objective, Student Verdict, Student Reasoning, Student Correction, Student Reviewed At]
        assert len(cols) == 7, f"FAIL: Row {idx+1} does not have 7 columns: {r}"
        tid, cov, obj, v, reason, corr, date = cols
        v_clean = v.replace("**", "").replace("`", "")
        verdicts.append(v_clean)
        assert reason != "", f"FAIL: Row {idx+1} has empty reasoning!"
        assert corr != "", f"FAIL: Row {idx+1} has empty correction field!"
        assert date == "2026-09-02", f"FAIL: Row {idx+1} has unexpected reviewed date: {date}"

        if v_clean == "INCOMPLETE":
            assert corr.lower() != "none required" and len(corr) > 5, f"FAIL: INCOMPLETE case {tid} missing concrete correction!"

    assert verdicts.count("VALID") == 23, f"FAIL: Expected 23 VALID, got {verdicts.count('VALID')}"
    assert verdicts.count("INCOMPLETE") == 15, f"FAIL: Expected 15 INCOMPLETE, got {verdicts.count('INCOMPLETE')}"
    assert verdicts.count("INVALID") == 0, f"FAIL: Expected 0 INVALID, got {verdicts.count('INVALID')}"
    print("✓ Check 2 Passed: human-audit.md has 38 rows (23 VALID / 15 INCOMPLETE / 0 INVALID), all student fields populated.")

    # 3. Check human-review-compact.md
    with open(COMPACT_PATH, "r", encoding="utf-8") as f:
        compact_text = f.read()

    compact_rows = [l for l in compact_text.splitlines() if l.strip().startswith("| **`FR07-AI-")]
    assert len(compact_rows) == 38, f"FAIL: Expected 38 rows in compact sheet, got {len(compact_rows)}"
    for idx, r in enumerate(compact_rows):
        cols = [c.strip() for c in r.split("|")[1:-1]]
        assert len(cols) == 6, f"FAIL: Compact row {idx+1} does not have 6 columns"
        assert cols[4] != "" and cols[5] != "", f"FAIL: Compact row {idx+1} has empty student field!"
    print("✓ Check 3 Passed: human-review-compact.md has 38 complete rows.")

    # 4. Check reviewed-ai-final.md
    with open(FINAL_PATH, "r", encoding="utf-8") as f:
        final_text = f.read()

    final_ids = re.findall(r"### `(FR07-AI-\d{3})`", final_text)
    assert len(final_ids) == 38, f"FAIL: Expected 38 tests in reviewed-ai-final.md, got {len(final_ids)}"
    assert final_ids == [f"FR07-AI-{i:03d}" for i in range(1, 39)], "FAIL: ID continuity broken in final suite"

    # Specific corrections check
    # Check FR07-AI-005 and 032 do not have hardcoded { error: 'Forbidden' }
    f005_block = final_text.split("### `FR07-AI-005`")[1].split("### `FR07-AI-006`")[0]
    assert "{ error: 'Forbidden' }" not in f005_block, "FAIL: FR07-AI-005 still has hardcoded { error: 'Forbidden' }"
    assert "UNKNOWN / IMPLEMENTATION-OBSERVED" in f005_block, "FAIL: FR07-AI-005 missing UNKNOWN/IMPLEMENTATION-OBSERVED note"

    f032_block = final_text.split("### `FR07-AI-032`")[1].split("### `FR07-AI-033`")[0]
    assert "{ error: 'Forbidden' }" not in f032_block, "FAIL: FR07-AI-032 still has hardcoded { error: 'Forbidden' }"

    # Check FR07-AI-012 and 013
    f012_block = final_text.split("### `FR07-AI-012`")[1].split("### `FR07-AI-013`")[0]
    assert "- **Expected HTTP Status:** `200 OK (INFERRED)`" in f012_block, "FAIL: FR07-AI-012 HTTP status not corrected to INFERRED"

    f013_block = final_text.split("### `FR07-AI-013`")[1].split("### `FR07-AI-014`")[0]
    assert "- **Expected HTTP Status:** `200 OK (INFERRED)`" in f013_block, "FAIL: FR07-AI-013 HTTP status not corrected to INFERRED"

    # Check invalid quantity status decoupling
    for q_id in ["FR07-AI-014", "FR07-AI-015", "FR07-AI-016", "FR07-AI-017", "FR07-AI-018", "FR07-AI-020", "FR07-AI-021", "FR07-AI-023", "FR07-AI-024"]:
        q_block = final_text.split(f"### `{q_id}`")[1].split("#### Lifecycle")[0]
        assert "Rejection status != 200" not in q_block, f"FAIL: {q_id} still has 'Rejection status != 200'"
        assert "UNKNOWN by official specification" in q_block, f"FAIL: {q_id} status not UNKNOWN"

    # Check FR07-AI-037 & 038
    f037_block = final_text.split("### `FR07-AI-037`")[1].split("### `FR07-AI-038`")[0]
    assert "no server crash and zero unsafe cart mutation" in f037_block, "FAIL: FR07-AI-037 missing safe robustness oracle"

    f038_block = final_text.split("### `FR07-AI-038`")[1].split("#### Lifecycle")[0]
    assert "Base robustness: no unhandled exception" in f038_block, "FAIL: FR07-AI-038 missing base robustness wording"

    print("✓ Check 4 Passed: reviewed-ai-final.md correctly reflects all 15 adopted calibrations.")
    print("\nALL PROGRAMMATIC AUDIT AND CALIBRATION CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
