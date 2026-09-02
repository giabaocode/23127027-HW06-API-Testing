#!/usr/bin/env python3
"""
Generate Reviewed Final Test Suite for FR-12 (reviewed-ai-final.md)
and Student Extensions Template (student-extensions.md).
Author: Pham Ngoc Gia Bao (23127027)
"""

import copy
import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from generate_fr12_tests import TEST_CASES

# Make a deep copy of TEST_CASES to apply the 10 corrections
FINAL_CASES = copy.deepcopy(TEST_CASES)

for tc in FINAL_CASES:
    tc_id = tc["id"]
    
    # Correction 1: FR12-AI-004
    if tc_id == "FR12-AI-004":
        tc["objective"] = "Verify that a standard user cannot update order fulfillment status from pending to confirmed, and that the order status remains unchanged."
        tc["body"] = {"status": "confirmed"}
        tc["side_effect_assertion"] = "Order status in database remains 'pending' (verified via admin order query); no state transition occurred."
        tc["sec_assertion"] = "SEC-03: Order status mutation requires role === 'admin'; isolated from multi-step business state machine rules."
        tc["condition_summary"] = "Standard user calls PUT /api/admin/orders/:id/status with valid single-step transition status: 'confirmed'"
        tc["oracle_summary"] = "Semantic access denied (SEC-03); order status remains 'pending'"

    # Correction 2: FR12-AI-005
    elif tc_id == "FR12-AI-005":
        tc["side_effect_assertion"] = "Product 'ImportProbe_23127027' is NOT added to database (verified by fetching full product catalog via GET /api/products and asserting that no product with name 'ImportProbe_23127027' exists, without relying on unestablished ?search= semantics)."
        tc["sec_assertion"] = "SEC-03: Bulk catalog import strictly enforces role === 'admin'; verified via direct catalog listing inspection."

    # Correction 3: FR12-AI-006
    elif tc_id == "FR12-AI-006":
        tc["side_effect_assertion"] = "Coupon 'HACK23127027' is NOT created in database (verified directly via authenticated admin GET /api/coupons asserting that coupon code 'HACK23127027' does not exist, rather than relying on checkout calculation rules)."
        tc["sec_assertion"] = "SEC-03: Coupon creation strictly requires role === 'admin'; verified via direct admin coupon listing."

    # Correction 4: FR12-AI-007
    elif tc_id == "FR12-AI-007":
        tc["side_effect_assertion"] = "Disposable coupon record remains intact in database (verified directly via authenticated admin GET /api/coupons asserting that disposable coupon ID/code remains present in the list)."
        tc["sec_assertion"] = "SEC-03: Coupon deletion requires role === 'admin'; verified directly via admin coupon listing inspection."

    # Correction 5: FR12-AI-008
    elif tc_id == "FR12-AI-008":
        tc["side_effect_assertion"] = "Product 'UnauthorizedProduct_23127027' is NOT created in catalog (verified by fetching full product catalog via GET /api/products and confirming absence of product, independent of server-side ?search= behavior)."
        tc["sec_assertion"] = "SEC-03: Catalog creation requires role === 'admin'; verified via direct catalog listing inspection."

    # Correction 6: FR12-AI-016
    elif tc_id == "FR12-AI-016":
        tc["side_effect_assertion"] = "Target disposable user is removed from database (verified by confirming deleted disposable user can no longer authenticate / no longer exists; downstream login rejection code classified as INFERRED/UNKNOWN rather than requiring exact 401)."
        tc["sec_assertion"] = "FR-12 / SEC-03: Admin clearance allows execution of user deletion handler; side-effect verifies user record removal."

    # Correction 7: FR12-AI-029
    elif tc_id == "FR12-AI-029":
        tc["side_effect_assertion"] = "Product 'AnonProduct_23127027' is NOT added to database (verified by fetching full product catalog via GET /api/products and confirming absence of marker, without relying on unestablished search-query behavior)."
        tc["sec_assertion"] = "SEC-02: Catalog mutation requires valid JWT authentication; verified via direct catalog listing inspection."

    # Correction 8: FR12-AI-033
    elif tc_id == "FR12-AI-033":
        tc["side_effect_assertion"] = "Category 'AnonCategory_23127027' is NOT added to database (verified via GET /api/categories)."
        tc["cleanup"] = "Defect-path cleanup: If access-control defect CAND-FR12-03 allows category creation, delete created category 'AnonCategory_23127027' using legitimate admin credentials after test execution."

    # Correction 9: FR12-AI-035
    elif tc_id == "FR12-AI-035":
        tc["jwt_state"] = "Expired JWT (exp claim in the past; cryptographic signature may remain valid, but temporal validity has expired)"
        tc["semantic_outcome"] = "ACCESS DENIED (SEC-02 Violation: Expired token fails temporal validity check; signature may be mathematically intact but exp < currentTime causes verification failure)"
        tc["sec_assertion"] = "SEC-02: Expired tokens must be rejected by JWT verification layer due to expired lifecycle claim, even if cryptographic HMAC signature was signed by valid secret key."

    # Correction 10: FR12-AI-037
    elif tc_id == "FR12-AI-037":
        tc["side_effect_assertion"] = "Coupon 'NOROLE_CPN_23127027' is NOT created in database (verified via admin GET /api/coupons)."
        tc["cleanup"] = "Defect-path cleanup: If SEC-03 authorization failure allows coupon creation, delete created coupon 'NOROLE_CPN_23127027' using legitimate admin credentials after test execution."

def write_reviewed_final():
    filepath = "hw06/testcases/fr12/reviewed-ai-final.md"
    content = """# FR-12: Access Control — Reviewed Final AI Test Suite

> **Document Status & Human Audit Summary:**
> - **Auditor:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
> - **Feature Pool:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Status:** **REVIEWED FINAL AI TEST SUITE**
> - **Audit Outcome:** 38 Total Tests | **28 VALID** | **10 INCOMPLETE (Corrected)** | **0 INVALID**
> - **Adoption Provenance:** The student reviewed the 38 original AI-generated test cases together with external secondary reference review material from ChatGPT (`CHATGPT-004.md` / `ai-reference-audit.md`). The student formally adopted 10 calibrated state-verification, defect-path cleanup, and oracle precision corrections into this final suite.
> - **Governing Contract Authority:**
>   - `README.md`: Section 6 (FR-12 Lines 174–180), Section 9 (SEC-02 Line 279, SEC-03 Line 280)
>   - `api_specification.md`: Section 5.2 (Lines 165–168), Section 6 (Lines 171–215), Section 3.3–3.4 (Lines 87–107)

---

## Suite Summary & Applied Audit Corrections

This suite contains all **38 finalized test cases** (`FR12-AI-001` through `FR12-AI-038`), incorporating the 10 adopted human audit corrections:
1. **`FR12-AI-004`:** Transition calibrated to valid single-step `pending -> confirmed` to prevent downstream order state-machine validation from masking authorization checks.
2. **`FR12-AI-005`:** Side-effect check updated to direct full catalog inspection, removing reliance on uncontracted `?search=` query semantics.
3. **`FR12-AI-006`:** Coupon absence verified directly through authenticated admin `GET /api/coupons` instead of checkout promotional calculation.
4. **`FR12-AI-007`:** Coupon persistence verified directly through authenticated admin `GET /api/coupons` listing inspection.
5. **`FR12-AI-008`:** Product non-creation verified via direct catalog listing inspection, removing reliance on `?search=`.
6. **`FR12-AI-016`:** User deletion verifier asserts user can no longer authenticate / no longer exists, without elevating downstream login 401 into a contract oracle.
7. **`FR12-AI-029`:** Anonymous product non-creation verified via direct catalog listing inspection, removing reliance on `?search=`.
8. **`FR12-AI-033`:** Defect-path cleanup added: deletes `AnonCategory_23127027` via admin credentials if vulnerable SUT permits anonymous creation.
9. **`FR12-AI-035`:** Terminology corrected: clarifies that token signature may remain mathematically valid while token validity fails because `exp` claim is in the past.
10. **`FR12-AI-037`:** Defect-path cleanup added: deletes `NOROLE_CPN_23127027` via admin credentials if vulnerable SUT permits creation without `role` claim.

---

"""
    for tc in FINAL_CASES:
        body_json = json.dumps(tc["body"], indent=2) if tc["body"] is not None else "None (Empty Body)"
        headers_str = "\n".join([f"  - `{k}: {v}`" for k, v in tc["headers"].items()])

        content += f"""## {tc["id"]} — {tc["short_objective"]}

### Identity
- **Test ID:** `{tc["id"]}`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `{tc["coverage_id"]}`
- **HTTP Method:** `{tc["method"]}`
- **Target Endpoint:** `{tc["endpoint"]}`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `{tc["sec_mapping"]}` (`README.md` Section 9 Line {"279 (SEC-02: Valid JWT required)" if "SEC-02" in tc["sec_mapping"] else "280 (SEC-03: Admin role enforced)" if "SEC-03" in tc["sec_mapping"] else "176-180 (FR-12 Admin Subsystem)"})
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** {tc["caller_type"]}
- **JWT Token State:** {tc["jwt_state"]}
- **Embedded Role Claim:** `{tc["role"]}`
- **Authentication Condition:** {tc["access_condition"]}

### Test Design
- **Objective:** {tc["objective"]}
- **Access-Control Condition:** {tc["access_condition"]}
- **Preconditions:** {tc["preconditions"]}
- **Disposable Resource State:** {tc["disposable_resource"]}

### HTTP Request Specification
- **Method:** `{tc["method"]}`
- **Endpoint:** `{tc["endpoint"]}`
- **Request Headers:**
{headers_str}
- **Request Body:**
```json
{body_json}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** {tc["semantic_outcome"]}
- **Expected HTTP Status:** `{tc["http_status"]}`
- **Response Exposure Assertion:** {tc["exposure_assertion"]}
- **Unauthorized Side-Effect Assertion:** {tc["side_effect_assertion"]}
- **Security Invariant Assertion:** {tc["sec_assertion"]}

### Lifecycle & Automation
- **Setup Required:** {tc["setup"]}
- **Cleanup Required:** {tc["cleanup"]}
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filepath} successfully with 38 reviewed test cases.")

def write_student_extension_template():
    filepath = "hw06/testcases/fr12/student-extensions.md"
    content = """# FR-12: Access Control — Student Extension Test Cases

> **Author & Provenance:**
> - **Student:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Status:** **BLANK TEMPLATE AWAITING STUDENT SELECTION**
> - **Required Extension Count:** Exactly 5 Student Extension Test Cases (`FR12-STU-001` through `FR12-STU-005`)

---

## 1. Extension Strategy & Coverage Rationale

*(To be formulated upon student selection of extension ideas)*

---

## 2. Student Extension Test Cases (Template)

### FR12-STU-001 — [Pending Student Title]
- **Test ID:** `FR12-STU-001`
- **Origin:** Student
- **Feature:** FR-12 Access Control
- **HTTP Method:** `[Pending]`
- **Target Endpoint:** `[Pending]`
- **Objective:** `[Pending]`
- **Caller / Role:** `[Pending]`
- **Expected Semantic Outcome:** `[Pending]`
- **Expected HTTP Status:** `[Pending]`

---

### FR12-STU-002 — [Pending Student Title]
- **Test ID:** `FR12-STU-002`
- **Origin:** Student
- **Feature:** FR-12 Access Control
- **HTTP Method:** `[Pending]`
- **Target Endpoint:** `[Pending]`
- **Objective:** `[Pending]`
- **Caller / Role:** `[Pending]`
- **Expected Semantic Outcome:** `[Pending]`
- **Expected HTTP Status:** `[Pending]`

---

### FR12-STU-003 — [Pending Student Title]
- **Test ID:** `FR12-STU-003`
- **Origin:** Student
- **Feature:** FR-12 Access Control
- **HTTP Method:** `[Pending]`
- **Target Endpoint:** `[Pending]`
- **Objective:** `[Pending]`
- **Caller / Role:** `[Pending]`
- **Expected Semantic Outcome:** `[Pending]`
- **Expected HTTP Status:** `[Pending]`

---

### FR12-STU-004 — [Pending Student Title]
- **Test ID:** `FR12-STU-004`
- **Origin:** Student
- **Feature:** FR-12 Access Control
- **HTTP Method:** `[Pending]`
- **Target Endpoint:** `[Pending]`
- **Objective:** `[Pending]`
- **Caller / Role:** `[Pending]`
- **Expected Semantic Outcome:** `[Pending]`
- **Expected HTTP Status:** `[Pending]`

---

### FR12-STU-005 — [Pending Student Title]
- **Test ID:** `FR12-STU-005`
- **Origin:** Student
- **Feature:** FR-12 Access Control
- **HTTP Method:** `[Pending]`
- **Target Endpoint:** `[Pending]`
- **Objective:** `[Pending]`
- **Caller / Role:** `[Pending]`
- **Expected Semantic Outcome:** `[Pending]`
- **Expected HTTP Status:** `[Pending]`

---
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filepath} successfully with 5 blank extension slots.")

if __name__ == "__main__":
    write_reviewed_final()
    write_student_extension_template()
