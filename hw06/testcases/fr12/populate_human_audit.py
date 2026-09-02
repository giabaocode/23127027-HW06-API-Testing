#!/usr/bin/env python3
"""
Populate FR-12 Human Audit Worksheet and Compact Review Sheet with Student-Adopted Decisions.
Auditor: Pham Ngoc Gia Bao (23127027)
Timestamp: 2026-09-02T23:26:42+07:00
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from generate_fr12_tests import TEST_CASES

# 10 Incomplete cases with adopted student reasoning and corrections
INCOMPLETE_DATA = {
    "FR12-AI-004": {
        "reasoning": "Access-control objective is valid, but attempting transition pending -> delivered risks rejection by downstream order state machine rules even if authorization is broken, masking the SEC-03 defect.",
        "correction": "Use valid single-step transition pending -> confirmed on disposable order to isolate access-control layer from business validation."
    },
    "FR12-AI-005": {
        "reasoning": "Side-effect non-insertion assertion relies on GET /api/products?search=... returning empty, but search query string semantics are not established in official specification.",
        "correction": "Fetch product list directly and explicitly assert that unique marker ImportProbe_23127027 is absent."
    },
    "FR12-AI-006": {
        "reasoning": "Using coupon checkout application as persistence verifier couples test to unrelated checkout/order business rules.",
        "correction": "Verify absence directly through authenticated admin GET /api/coupons and assert HACK23127027 does not exist."
    },
    "FR12-AI-007": {
        "reasoning": "Side-effect verification phrasing 'query or application succeeds' is ambiguous and checkout application can fail for unrelated reasons.",
        "correction": "Verify disposable coupon directly through admin GET /api/coupons and assert its ID/code remains present in database."
    },
    "FR12-AI-008": {
        "reasoning": "Product non-creation verification relies on ungrounded server-side ?search= query semantics.",
        "correction": "Fetch product catalog data directly and assert that unique UnauthorizedProduct_23127027 marker is absent."
    },
    "FR12-AI-016": {
        "reasoning": "Main authorization test is sound, but requiring exact downstream login probe status 401 elevates an uncontracted endpoint response into an FR-12 oracle.",
        "correction": "Assert that deleted disposable user can no longer authenticate / no longer exists; treat exact login rejection status code as endpoint-specific INFERRED/UNKNOWN."
    },
    "FR12-AI-029": {
        "reasoning": "Anonymous product creation denial is valid, but absence verification must not rely on unestablished ?search= query behavior.",
        "correction": "Fetch product list directly and explicitly assert that AnonProduct_23127027 is absent."
    },
    "FR12-AI-033": {
        "reasoning": "If expected access-control defect occurs on anonymous category creation, category will persist in database because cleanup is currently None.",
        "correction": "Add defect-path cleanup: if AnonCategory_23127027 exists after execution, delete it using legitimate admin credentials."
    },
    "FR12-AI-035": {
        "reasoning": "Semantic expired-JWT test is valid, but wording incorrectly describes token expiration as cryptographic signature verification failure.",
        "correction": "State that cryptographic signature may remain valid while JWT validity fails because exp claim is in the past. Preserve SEC-02 semantic denial."
    },
    "FR12-AI-037": {
        "reasoning": "Missing-role authorization probe is valid, but if SEC-03 is broken the coupon can actually be created and cleanup is currently None.",
        "correction": "Verify absence via admin GET /api/coupons. If NOROLE_CPN_23127027 was created due to defect, delete it using legitimate admin credentials."
    }
}

VALID_REASONINGS = {
    "FR12-AI-001": "Standard-user denial for GET /api/admin/users correctly maps to SEC-03. Semantic outcome is specified denial; exact 403 remains inferred.",
    "FR12-AI-002": "Dual-assertion on user deletion verifies both semantic denial and persistence of target user account via login probe without touching baseline users.",
    "FR12-AI-003": "Standard-user denial for system-wide order history correctly enforces SEC-03 data privacy.",
    "FR12-AI-009": "Side-effect check verifies original price remains unchanged after unauthorized standard-user PUT probe on disposable product.",
    "FR12-AI-010": "Side-effect check verifies product still exists via GET probe after unauthorized standard-user DELETE probe.",
    "FR12-AI-011": "Category non-creation is verified by absence in category list after standard-user POST probe.",
    "FR12-AI-012": "Category modification denial is verified by category name remaining unchanged in database.",
    "FR12-AI-013": "Category deletion denial is verified by category continuing to exist in database.",
    "FR12-AI-014": "Standard user denied access to administrative coupon master list via SEC-03.",
    "FR12-AI-015": "Admin access to GET /api/admin/users correctly defines authorization clearance as primary oracle with 200 as inferred SUT behavior.",
    "FR12-AI-017": "Admin access to GET /api/admin/orders verifies administrative clearance unhindered.",
    "FR12-AI-018": "Admin order status update correctly verifies administrative capability on disposable order.",
    "FR12-AI-019": "Admin product import verifies administrative capability with valid disposable payload.",
    "FR12-AI-020": "Admin coupon creation verifies administrative capability with valid disposable coupon code.",
    "FR12-AI-021": "Admin coupon deletion operates on disposable coupon and verifies deletion.",
    "FR12-AI-022": "Admin product creation verifies administrative capability with valid disposable product body.",
    "FR12-AI-023": "Admin product update operates on disposable product and updates price/description.",
    "FR12-AI-024": "Admin product deletion operates on disposable product and removes it from catalog.",
    "FR12-AI-025": "Admin category creation verifies administrative capability with valid category body.",
    "FR12-AI-026": "Admin category update operates on disposable category and updates name.",
    "FR12-AI-027": "Admin category deletion operates on disposable category and removes it from database.",
    "FR12-AI-028": "Admin coupon listing verifies administrative capability on GET /api/coupons.",
    "FR12-AI-030": "Anonymous product update denial correctly asserts SEC-02 and verifies product unchanged.",
    "FR12-AI-031": "Anonymous product deletion denial correctly asserts SEC-02 and verifies product still exists.",
    "FR12-AI-032": "Anonymous user list denial correctly asserts SEC-02 and prevents user data exposure.",
    "FR12-AI-034": "Anonymous coupon overview denial correctly asserts SEC-02 and prevents coupon data exposure.",
    "FR12-AI-036": "Forged cryptographic signature rejection correctly asserts SEC-02 integrity failure.",
    "FR12-AI-038": "Uppercase role 'ADMIN' probe correctly asserts SEC-03 exact-match case sensitivity."
}

def populate_audit():
    filepath = "hw06/testcases/fr12/human-audit.md"
    timestamp = "2026-09-02T23:26:42+07:00"
    
    content = f"""# FR-12: Access Control — Human Audit Worksheet

> **Academic Integrity Notice & Student Ownership:**
> - **Auditor:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Source Test Suite:** `hw06/testcases/fr12/generated-ai-original.md` (38 AI-generated cases)
> - **Audit Adoption Provenance:** The student reviewed the 38 original AI-generated test cases together with external secondary reference review material from ChatGPT (`CHATGPT-004.md` / `ai-reference-audit.md`). The student formally adopts the final distribution: **28 VALID**, **10 INCOMPLETE**, **0 INVALID** (Total: 38). For incomplete cases, the student adopts calibrated state verification, defect-path cleanup, and oracle precision.
> - **Evaluation Criteria:**
>   - **VALID:** The testcase is logically sound, correctly mapped to FR-12/SEC-02/SEC-03, has realistic oracles, and is ready for execution.
>   - **INCOMPLETE:** The testcase has technical merit but requires calibrated headers, side-effect checks, or oracle corrections.
>   - **INVALID:** The testcase violates specification boundaries, tests out-of-scope functional logic, or targets nonexistent routes.

---

| Test ID | Coverage ID | Short Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
"""
    
    valid_count = 0
    incomplete_count = 0
    
    for tc in TEST_CASES:
        tc_id = tc["id"]
        if tc_id in INCOMPLETE_DATA:
            verdict = "**INCOMPLETE**"
            reasoning = INCOMPLETE_DATA[tc_id]["reasoning"]
            correction = INCOMPLETE_DATA[tc_id]["correction"]
            incomplete_count += 1
        else:
            verdict = "**VALID**"
            reasoning = VALID_REASONINGS[tc_id]
            correction = "None required (Design is sound)."
            valid_count += 1
            
        content += f"| `{tc['id']}` | `{tc['coverage_id']}` | {tc['short_objective']} | {verdict} | {reasoning} | {correction} | {timestamp} |\n"
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Populated {filepath}: {valid_count} VALID, {incomplete_count} INCOMPLETE, 0 INVALID.")

def populate_compact_review():
    filepath = "hw06/testcases/fr12/human-review-compact.md"
    
    content = """# FR-12: Access Control — Compact Human Review Sheet

> **Auditor:** Phạm Ngọc Gia Bảo (`23127027`) | **Total Cases:** 38 | **Distribution:** 28 VALID, 10 INCOMPLETE, 0 INVALID

| Test ID | Endpoint | Caller Identity | One-Sentence Condition | Requirement / Oracle | Student Final Verdict | Student Note |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
"""
    for tc in TEST_CASES:
        tc_id = tc["id"]
        if tc_id in INCOMPLETE_DATA:
            verdict = "INCOMPLETE"
            note = INCOMPLETE_DATA[tc_id]["correction"]
        else:
            verdict = "VALID"
            note = "Accepted as-is."
            
        content += f"| `{tc['id']}` | `{tc['method']} {tc['endpoint']}` | {tc['role']} | {tc['condition_summary']} | {tc['oracle_summary']} | **{verdict}** | {note} |\n"
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Populated {filepath} with 38 rows.")

if __name__ == "__main__":
    populate_audit()
    populate_compact_review()
