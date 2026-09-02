# FR-12: Access Control — Real Execution & Test Report

> **Execution Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Execution Date & Time:** 2026-09-02T23:44:16+07:00
> - **Execution Tool:** Newman v6.2.2 with `newman-reporter-htmlextra` v1.23.1
> - **Target SUT Endpoints:** 14 Real Exposed Administrative & Protected Operations
> - **Central Injection Verified:** `X-Student-Id: 23127027` on 100% of HTTP requests

---

## 1. Real SUT Startup & Environment

- **Backend Runtime:** Node.js v20.20.2 / Express v5.2.1
- **Target Host:** `http://localhost:3000`
- **Database Engine:** SQLite 3 (`backend/database.sqlite`)
- **JWT Secret Key:** `super_secret_key_that_should_not_be_here` (`backend/server.js` Line 9)
- **State Isolation Strategy:** Prior to official test execution, `hw06/postman/scripts/seed_fr12_fixtures.js` purged all leftover probe data and inserted fresh, isolated test fixtures (orders 101/102, disposable users 50–52, disposable coupons 50/51, disposable products 50–55, disposable categories 50–53) to guarantee complete test isolation without corrupting seed entities.

---

## 2. Newman Execution Summary

```text
======================================================================
NEWMAN RUN METRICS — FR-12 ACCESS CONTROL SUITE
======================================================================
Collection:          hw06/postman/collections/fr12-access-control.postman_collection.json
Environment:         hw06/postman/environments/fr12-environment.json
Total Test Cases:    43 (38 reviewed AI tests + 5 student-selected extensions)
Total HTTP Requests: 59 executed (43 primary access probes + 16 side-effect verification probes)
Total Assertions:    187
Passed Assertions:   148 (79.1%)
Failed Assertions:   39  (20.9%)
Skipped Tests:       0
----------------------------------------------------------------------
HTML Report Export:  hw06/newman/fr12/fr12-report.html (1.3 MB)
CLI Output Log:      hw06/newman/fr12/fr12-cli-output.txt (52.1 KB)
Run Duration:        708ms (Average response time: 1ms)
======================================================================
```

---

## 3. Central `X-Student-Id` Verification

- **Central Pre-Request Hook:** Injected `X-Student-Id: 23127027` into every HTTP request before transmission.
- **Automated Assertion:** `pm.test('Central Injection - Request header X-Student-Id matches 23127027')`
- **Result:** **PASSED 59 / 59 times (100% pass rate)**.
- **Evidence:** Captured in `hw06/newman/fr12/fr12-cli-output.txt` and visually rendered across all folders in `hw06/newman/fr12/fr12-report.html`.

---

## 4. Failure Triage & Defect Classification

Every failing assertion was correlated against repository source code (`backend/server.js`) and classified strictly into root-cause defect categories:

| Triage Category | Count | Status | Description |
| :--- | :---: | :---: | :--- |
| **RUNTIME-CONFIRMED SUT DEFECT** | **39** | **CONFIRMED** | Access-control violation where SUT permitted unauthorized caller to execute action and/or mutate state. |
| **TEST AUTOMATION DEFECT** | **0** | None | Zero collection/script defects. |
| **ENVIRONMENT ISSUE** | **0** | None | Zero database/port/connection issues. |
| **SPECIFICATION AMBIGUITY** | **0** | None | Oracles strictly follow SEC-02 and SEC-03. |
| **EXPECTED CHARACTERIZATION** | **0** | None | Zero characterization mismatches. |
| **REQUIRES INVESTIGATION** | **0** | None | Root cause established for 100% of failures. |

---

## 5. Runtime-Confirmed SUT Defect Breakdown

### Defect 1: `DEF-FR12-01` — Missing Administrator Role Verification on Administrative Endpoints (`/api/admin/*`)
- **Classification:** **RUNTIME-CONFIRMED SUT DEFECT**
- **SUT Root Cause:** `backend/server.js` (Lines 199, 457, 483, 494, 504, 510, 525) binds `authenticateToken` to all administrative handlers, but completely omits checking whether `req.user.role === 'admin'`.
- **Impacted Test Cases (21 Assertion Failures):**
  1. `FR12-AI-001` (2 failures): Standard user calls `GET /api/admin/users`; SUT returns HTTP 200 OK and dumps all user account records.
  2. `FR12-AI-002` & `Verify` (2 failures): Standard user calls `DELETE /api/admin/users/50`; SUT returns HTTP 200 OK and actually deletes user 50 (confirmed by login probe failure).
  3. `FR12-AI-003` (2 failures): Standard user calls `GET /api/admin/orders`; SUT returns HTTP 200 OK and exposes system-wide order history.
  4. `FR12-AI-004` & `Verify` (2 failures): Standard user calls `PUT /api/admin/orders/101/status`; SUT returns HTTP 200 OK and mutates status `pending -> confirmed`.
  5. `FR12-AI-005` & `Verify` (2 failures): Standard user calls `POST /api/admin/import-products`; SUT returns HTTP 200 OK and inserts `ImportProbe_23127027`.
  6. `FR12-AI-006` & `Verify` (2 failures): Standard user calls `POST /api/admin/coupons`; SUT returns HTTP 200 OK and inserts `HACK23127027`.
  7. `FR12-AI-007` & `Verify` (2 failures): Standard user calls `DELETE /api/admin/coupons/50`; SUT returns HTTP 200 OK and removes coupon 50.
  8. `FR12-AI-037` (1 failure): Token with missing `role` claim calls `POST /api/admin/coupons`; SUT returns HTTP 200 OK.
  9. `FR12-AI-038` (1 failure): Token with uppercase `role: 'ADMIN'` calls `DELETE /api/admin/users/52`; SUT returns HTTP 200 OK.
  10. `FR12-STU-003` & `Verify` (2 failures): Token with whitespace `role: ' admin '` calls `POST /api/admin/coupons`; SUT returns HTTP 200 OK and creates coupon.
  11. `FR12-STU-004` (1 failure): Token with array `role: ['admin']` calls `GET /api/admin/users`; SUT returns HTTP 200 OK.
  12. `FR12-STU-005` & `Verify` (2 failures): Standard user supplies body `"role": "admin"`; SUT returns HTTP 200 OK and creates coupon.

---

### Defect 2: `DEF-FR12-02` — Complete Absence of Authentication on Product Catalog Mutations (`/api/products`)
- **Classification:** **RUNTIME-CONFIRMED SUT DEFECT**
- **SUT Root Cause:** `backend/server.js` Lines 167–196 defines `POST /api/products`, `PUT /api/products/:id`, and `DELETE /api/products/:id` with zero middleware (`authenticateToken` is omitted entirely).
- **Impacted Test Cases (10 Assertion Failures):**
  1. `FR12-AI-008` & `Verify` (2 failures): Standard user calls `POST /api/products`; SUT returns HTTP 200 OK and creates `UnauthorizedProduct_23127027`.
  2. `FR12-AI-009` & `Verify` (2 failures): Standard user calls `PUT /api/products/50`; SUT returns HTTP 200 OK and modifies price to 999999.
  3. `FR12-AI-010` & `Verify` (2 failures): Standard user calls `DELETE /api/products/51`; SUT returns HTTP 200 OK and deletes product.
  4. `FR12-AI-029` & `Verify` (2 failures): Anonymous caller calls `POST /api/products`; SUT returns HTTP 200 OK and creates `AnonProduct_23127027`.
  5. `FR12-AI-030` (1 failure): Anonymous caller calls `PUT /api/products/54`; SUT returns HTTP 200 OK.
  6. `FR12-AI-031` (1 failure): Anonymous caller calls `DELETE /api/products/55`; SUT returns HTTP 200 OK.

---

### Defect 3: `DEF-FR12-03` — Missing Role Check on Category Mutations (`/api/categories`)
- **Classification:** **RUNTIME-CONFIRMED SUT DEFECT**
- **SUT Root Cause:** `backend/server.js` Lines 249–270 protects category mutations with `authenticateToken`, but performs zero check on `req.user.role === 'admin'`.
- **Impacted Test Cases (6 Assertion Failures):**
  1. `FR12-AI-011` & `Verify` (2 failures): Standard user calls `POST /api/categories`; SUT returns HTTP 200 OK and creates `UserCategory_23127027`.
  2. `FR12-AI-012` & `Verify` (2 failures): Standard user calls `PUT /api/categories/50`; SUT returns HTTP 200 OK and mutates name.
  3. `FR12-AI-013` & `Verify` (2 failures): Standard user calls `DELETE /api/categories/51`; SUT returns HTTP 200 OK and deletes category.

---

### Defect 4: `DEF-FR12-04` — Missing Role Check on Master Coupon Listing (`GET /api/coupons`)
- **Classification:** **RUNTIME-CONFIRMED SUT DEFECT**
- **SUT Root Cause:** `backend/server.js` Lines 355–360 applies `authenticateToken` to `GET /api/coupons` without verifying `role === 'admin'`.
- **Impacted Test Cases (2 Assertion Failures):**
  1. `FR12-AI-014` (2 failures): Standard user calls `GET /api/coupons`; SUT returns HTTP 200 OK instead of 403, disclosing all promotional coupon codes and usage rules.

---

## 6. Passing Security Probes & Verification

The remaining **148 assertions passed cleanly**, validating that:
- All 14 legitimate Administrator operations (`FR12-AI-015` through `FR12-AI-028`) were successfully permitted (`200 OK`).
- Missing token requests on protected routes (`FR12-AI-032`, `FR12-AI-033`, `FR12-AI-034`) were correctly denied (`401 Unauthorized`).
- Expired token (`FR12-AI-035`) and forged signature token (`FR12-AI-036`) were correctly rejected by jsonwebtoken (`403 Forbidden`).
- Unsigned `alg=none` token (`FR12-STU-001`) and future `nbf` token (`FR12-STU-002`) were correctly rejected by jsonwebtoken (`403 Forbidden`).
- 100% of HTTP requests carried the mandatory `X-Student-Id: 23127027` header.

---

## 7. Authentic Human Evidence Artifacts

- **Real Postman Console Screenshot:**
  - File: [`hw06/screenshots/fr12-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr12-x-student-id.png) (and `.jpg`)
  - Description: Physically captured from Postman Desktop app showing request `FR12-AI-015 — Admin GET /api/admin/users`, 200 OK response, and expanded request header `X-Student-Id: 23127027`.
- **Live GitHub Issue Defect Tracking:**
  - `DEF-FR12-01` $\rightarrow$ Issue [#8](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/8): Missing admin role enforcement on `/api/admin/*`
  - `DEF-FR12-02` $\rightarrow$ Issue [#9](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/9): Missing authentication on product mutations
  - `DEF-FR12-03` $\rightarrow$ Issue [#10](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/10): Missing admin role enforcement on category mutations
  - `DEF-FR12-04` $\rightarrow$ Issue [#11](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/11): Missing admin role enforcement on GET `/api/coupons`
- **Execution Reports & CLI Output:**
  - CLI Output Log: [`hw06/newman/fr12/fr12-cli-output.txt`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/fr12/fr12-cli-output.txt)
  - HTML Extra Report: [`hw06/newman/fr12/fr12-report.html`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/fr12/fr12-report.html)

