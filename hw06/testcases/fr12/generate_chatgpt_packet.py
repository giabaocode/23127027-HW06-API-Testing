#!/usr/bin/env python3
"""
Generate ChatGPT External Review Packet for FR-12 AI Test Cases.
Author: Antigravity AI Pair Programmer
Student: Pham Ngoc Gia Bao (23127027)
"""

import os
import json
import sys

# Import TEST_CASES from generate_fr12_tests
sys.path.append(os.path.dirname(__file__))
from generate_fr12_tests import TEST_CASES

HIGH_RISK_MUTATION_CASES = {
    "FR12-AI-002", "FR12-AI-004", "FR12-AI-005", "FR12-AI-006", "FR12-AI-007",
    "FR12-AI-008", "FR12-AI-009", "FR12-AI-010", "FR12-AI-011", "FR12-AI-012", "FR12-AI-013"
}
ADMIN_POSITIVE_CASES = {f"FR12-AI-{i:03d}" for i in range(15, 29)}
TOKEN_BOUNDARY_CASES = {"FR12-AI-035", "FR12-AI-036", "FR12-AI-037", "FR12-AI-038"}

def generate_packet():
    filepath = "hw06/testcases/fr12/chatgpt-review-packet.md"
    
    header = """# FR-12: Access Control — External AI (ChatGPT) Review Packet

> **Notice to External AI Reviewer (ChatGPT):**
> This document contains a structured, neutral extraction of all **38 original AI-generated test cases** for **FR-12: Access Control (Kiểm soát truy cập)** in the EShop SUT.
> 
> **Evaluation Goal:**
> For each test case, independently evaluate its technical quality and assign one of the following verdicts:
> - **VALID:** Testcase is sound, correctly targeted at FR-12 access control, has correct semantic and HTTP oracles, and adheres to test isolation.
> - **INCOMPLETE:** Testcase has technical merit but requires calibrated headers, side-effect assertions, or oracle adjustments.
> - **INVALID:** Testcase violates specification boundaries, tests out-of-scope functional logic, or targets nonexistent endpoints.
> 
> **Key Architectural Context:**
> - **SUT Roles:** Seeded roles are `admin` (Administrator) and `user` (Standard User). The string `customer` does **not** exist as a system role.
> - **SEC-02:** Protected and administrative endpoints require a valid JWT token (`Authorization: Bearer <token>`).
> - **SEC-03:** Administrative endpoints require `role === 'admin'`. Token existence alone is insufficient.
> - **FR-12 Target Scope:** Exactly 14 real exposed operations (7 `/api/admin/*`, 6 `/api/products` and `/api/categories` mutations, 1 `GET /api/coupons`). Nonexistent shorthand routes (`POST/PUT/DELETE /api/coupons`) are excluded.
> - **HTTP Status Policy:** Official contract (`api_specification.md`) specifies semantic outcomes (access granted/denied) but does **not** state numerical HTTP status codes. Statuses like 200, 401, 403 are derived from Express SUT implementation defaults and classified as `INFERRED / IMPLEMENTATION-OBSERVED`.

---

"""
    sections = []
    
    for tc in TEST_CASES:
        tc_id = tc["id"]
        is_high_risk = (tc_id in HIGH_RISK_MUTATION_CASES or 
                        tc_id in ADMIN_POSITIVE_CASES or 
                        tc_id in TOKEN_BOUNDARY_CASES)
        
        body_str = json.dumps(tc["body"], indent=2) if tc["body"] is not None else "None"
        headers_str = "; ".join([f"{k}: {v}" for k, v in tc["headers"].items()])
        
        detail_block = ""
        if is_high_risk:
            detail_block = f"""- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: {tc['setup']} (Disposable Target: {tc['disposable_resource']})
  2. Action: Send `{tc['method']} {tc['endpoint']}` with headers [{headers_str}] and body: `{body_str.replace(chr(10), ' ')}`
  3. Verification Step 1 (Response): Assert semantic outcome `{tc['semantic_outcome']}` and HTTP status `{tc['http_status']}`.
  4. Verification Step 2 (Side-Effect Invariance): {tc['side_effect_assertion']}
  5. Cleanup Step: {tc['cleanup']}
"""

        sec_text = f"""### {tc_id}

- **Coverage ID:** `{tc['coverage_id']}`
- **Method:** `{tc['method']}`
- **Endpoint:** `{tc['endpoint']}`
- **Caller Type:** {tc['caller_type']}
- **JWT State:** {tc['jwt_state']}
- **Role:** `{tc['role']}`
- **One-sentence Test Condition:** {tc['condition_summary']}
- **Official Requirement / SEC:** `{tc['sec_mapping']}` (FR-12 Lines 174–180; {"SEC-02 Line 279" if "SEC-02" in tc['sec_mapping'] else "SEC-03 Line 280" if "SEC-03" in tc['sec_mapping'] else "Admin Subsystem"})
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** {tc['semantic_outcome']}
- **Expected HTTP Status + Classification:** `{tc['http_status']}`
- **Expected Response Exposure Assertion:** {tc['exposure_assertion']}
- **Unauthorized Side-Effect Assertion:** {tc['side_effect_assertion']}
- **Setup / Disposable Resource:** {tc['setup']} | Resource: {tc['disposable_resource']}
- **Cleanup:** {tc['cleanup']}
- **Any Exact Response Body Assertion:** Request headers: `{headers_str}`; Request body: `{body_str.replace(chr(10), ' ')}`
- **Original Automation Status:** NOT AUTOMATED YET
{detail_block}
---
"""
        sections.append(sec_text)
    
    full_content = header + "\n".join(sections)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"Generated {filepath} successfully with {len(sections)} testcase review sections.")

if __name__ == "__main__":
    generate_packet()
