# FR-07: Shopping Cart — Real Execution & Test Report

> **Execution Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Execution Date & Time:** 2026-09-02T21:18:45+07:00
> - **Execution Tool:** Newman v6.2.2 with `newman-reporter-htmlextra`
> - **Target SUT Endpoints:** `http://localhost:3000/api/cart` (`GET`, `POST`)
> - **Central Injection Verified:** `X-Student-Id: 23127027` on 100% of HTTP requests

---

## 1. Real SUT Startup & Environment

- **Backend Runtime:** Node.js v20.20.2 / Express v5.2.1
- **Target Host:** `http://localhost:3000`
- **Cart Storage Model:** In-memory dictionary `const userCarts = {};` (`backend/server.js` Line 14)
- **State Isolation Strategy:** Prior to official test run, SUT backend process was cleanly restarted to ensure in-memory cart state was 100% empty. Dedicated fresh test accounts were registered via legitimate SUT APIs (`/api/register` and `/api/login`) to generate independent JWT Bearer tokens for each test case.

---

## 2. Newman Execution Summary

```text
======================================================================
NEWMAN RUN METRICS — FR-07 SHOPPING CART SUITE
======================================================================
Collection:          hw06/postman/collections/fr07-shopping-cart.postman_collection.json
Environment:         hw06/postman/environments/fr07-environment.json
Total Test Cases:    43 (38 reviewed AI tests + 5 student-selected extensions)
Total HTTP Requests: 67 executed (multi-step state sequences)
Total Assertions:    187
Passed Assertions:   170 (90.9%)
Failed Assertions:   17  ( 9.1%)
Skipped Tests:       0
----------------------------------------------------------------------
HTML Report Export:  hw06/newman/fr07/fr07-report.html (1.4 MB)
CLI Output Log:      hw06/newman/fr07/fr07-cli-output.txt (35.4 KB)
Run Duration:        821ms (Average response time: 1ms)
======================================================================
```

---

## 3. Central `X-Student-Id` Verification

- **Central Pre-Request Hook:** Injected `X-Student-Id: 23127027` into every HTTP request before transmission.
- **Automated Assertion:** `pm.test('Central Injection - Request header X-Student-Id matches 23127027')`
- **Result:** **PASSED 67 / 67 times (100% pass rate)**.
- **Evidence:** Recorded in `hw06/newman/fr07/fr07-cli-output.txt` and visibly rendered in `hw06/newman/fr07/fr07-report.html`.

---

## 4. Failure Triage & Defect Classification

Every failing assertion was correlated against repository source code (`backend/server.js` Lines 284–295) and classified into root causes:

### Category A: Confirmed SUT Defect — Duplicate Product Duplication Instead of Accumulation (`DEF-FR07-01`)
- **Impacted Requests (8 Assertion Failures):**
  - `FR07-AI-009 (Step 3)`: 2 assertion failures (expected 1 row got 2; expected quantity 5 got 2)
  - `FR07-AI-010 (Step 4)`: 2 assertion failures (expected 2 rows got 3; expected p1 quantity 5 got 1)
  - `FR07-AI-011 (Step 3)`: 2 assertion failures (expected 1 row got 2; expected quantity 2 got 1)
  - `FR07-STU-004 (Step 3)`: 2 assertion failures (expected 1 row got 2; expected quantity 5 got 2)
- **Specification Violation:** `README.md` Line 96 explicitly mandates:
  > *"Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới."*
- **Root Cause in Source Code:** `backend/server.js` Line 293 blindly pushes the payload into the array without checking for existing product IDs:
  ```javascript
  userCarts[userId].push(req.body);
  ```
- **Runtime Proof:** Confirmed across 4 independent test sequences.

---

### Category B: Confirmed SUT Defect — Missing Quantity Domain Validation (`DEF-FR07-02`)
- **Impacted Requests (9 Assertion Failures):**
  - `FR07-AI-014`: Zero quantity ($q=0$) accepted with HTTP `200 OK`
  - `FR07-AI-015`: Negative quantity ($q=-1$) accepted with HTTP `200 OK`
  - `FR07-AI-016`: Large negative quantity ($q=-100$) accepted with HTTP `200 OK`
  - `FR07-AI-017`: Fractional quantity ($q=1.5$) accepted with HTTP `200 OK`
  - `FR07-AI-018`: Sub-unit decimal quantity ($q=0.5$) accepted with HTTP `200 OK`
  - `FR07-AI-020`: Non-numeric alphabetic string ($q="abc"$) accepted with HTTP `200 OK`
  - `FR07-AI-021`: Special symbol string ($q="@#$"$) accepted with HTTP `200 OK`
  - `FR07-AI-023`: Omitted quantity field accepted with HTTP `200 OK`
  - `FR07-AI-024`: Explicit null quantity accepted with HTTP `200 OK`
- **Specification Violation:** `README.md` Line 86 explicitly mandates:
  > *"Có ô nhập Số lượng (chỉ nhận số nguyên dương, tối thiểu là 1)."*
- **Root Cause in Source Code:** `backend/server.js` Line 290 contains zero input validation, boundary checking, or type enforcement on `req.body.quantity`.
- **Runtime Proof:** Confirmed across 9 distinct boundary and invalid partitions.

---

## 5. Successful Behavioral Characterizations & Passing Suites

1. **Authentication Barrier Enforcement (`SEC-02`):**
   - Unauthenticated GET (`FR07-AI-004`) and POST (`FR07-AI-031`) were denied with HTTP `401 Unauthorized`.
   - Forged signature GET (`FR07-AI-005`) and POST (`FR07-AI-032`) were denied with HTTP `403 Forbidden`.
   - Non-Bearer scheme GET (`FR07-AI-006`) and POST (`FR07-AI-033`) were denied with HTTP `401 Unauthorized`.
   - Expired JWT token (`FR07-STU-003`) was denied with HTTP `403 Forbidden` and caused zero cart mutation.
2. **Multi-Tenant User Cart Isolation:**
   - Empty cart independence (`FR07-AI-034`) verified User B's cart remained empty despite User A additions.
   - Non-interference (`FR07-AI-035`) verified User B's items were unaffected by User A additions.
   - Independent accumulation (`FR07-AI-036`) verified user-level isolation of identical product IDs.
3. **Robustness Probes:**
   - Syntactically malformed raw JSON (`FR07-STU-001`) was caught cleanly by the body parser with HTTP `400 Bad Request` without server crash.
   - Unexpected MIME type `text/plain` (`FR07-STU-002`) was handled safely without process crash.
   - Repeated GET calls (`FR07-STU-005`) confirmed complete read idempotency across 3 successive invocations.
   - Extreme large integer quantity ($q=10^9$, `FR07-AI-022`), empty body (`FR07-AI-037`), and extra payload properties (`FR07-AI-038`) were handled safely without unhandled crashes.
