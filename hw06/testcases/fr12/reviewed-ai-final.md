# FR-12: Access Control — Reviewed Final AI Test Suite

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

## FR12-AI-001 — Standard user denied access to GET /api/admin/users

### Identity
- **Test ID:** `FR12-AI-001`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-02`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/users`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that an authenticated standard user (role: 'user') is denied access to the administrative user accounts directory.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Backend running on http://localhost:3000; valid standard user account registered and logged in.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Non-admin subject attempting administrative user listing)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response payload must not expose user account directory rows (passwords, emails, roles).
- **Unauthorized Side-Effect Assertion:** Read-only operation; zero mutation expected.
- **Security Invariant Assertion:** SEC-03: System verifies role === 'admin' and strictly rejects role: 'user'.

### Lifecycle & Automation
- **Setup Required:** Authenticate standard user to obtain valid JWT.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-002 — Standard user denied DELETE /api/admin/users/:id + user not deleted

### Identity
- **Test ID:** `FR12-AI-002`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-04`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/admin/users/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that an authenticated standard user cannot delete an arbitrary user account, and that the target account is not deleted.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable target user account created with ID <TARGET_USER_ID>.
- **Disposable Resource State:** Disposable test user (e.g. test_victim_23127027@eshop.com)

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/users/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Standard user cannot execute administrative user deletion)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must indicate authorization rejection and not confirm deletion.
- **Unauthorized Side-Effect Assertion:** Target user account remains active in database; follow-up login probe with target user credentials must succeed.
- **Security Invariant Assertion:** SEC-03: Deletion requires role === 'admin'; unauthorized deletion side-effect is prevented.

### Lifecycle & Automation
- **Setup Required:** Create disposable test user account via /api/register to act as deletion target.
- **Cleanup Required:** Clean up disposable test user via admin credentials after test completion.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-003 — Standard user denied access to GET /api/admin/orders

### Identity
- **Test ID:** `FR12-AI-003`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-07`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/orders`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that an authenticated standard user is denied access to view system-wide orders across all customers.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** System contains orders from multiple users in database.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/orders`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Non-admin cannot view system-wide customer order history)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response payload must not expose order records belonging to other system users.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** SEC-03: System-wide order viewing is restricted strictly to role: 'admin'.

### Lifecycle & Automation
- **Setup Required:** Obtain standard user JWT token.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-004 — Standard user denied PUT /api/admin/orders/:id/status + status unchanged

### Identity
- **Test ID:** `FR12-AI-004`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-09`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/admin/orders/:id/status`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot update order fulfillment status from pending to confirmed, and that the order status remains unchanged.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable order exists with status: 'pending'.
- **Disposable Resource State:** Order ID <TARGET_ORDER_ID> with initial status 'pending'

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/admin/orders/:id/status`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "status": "confirmed"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Non-admin prohibited from modifying administrative order status)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject status mutation request.
- **Unauthorized Side-Effect Assertion:** Order status in database remains 'pending' (verified via admin order query); no state transition occurred.
- **Security Invariant Assertion:** SEC-03: Order status mutation requires role === 'admin'; isolated from multi-step business state machine rules.

### Lifecycle & Automation
- **Setup Required:** Identify or create a test order with status 'pending'.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-005 — Standard user denied POST /api/admin/import-products + catalog unmutated

### Identity
- **Test ID:** `FR12-AI-005`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-12`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/import-products`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot invoke bulk product catalog import, and that no new products are added to catalog.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Standard user token available; unique product payload prepared.
- **Disposable Resource State:** Product import payload with unique marker 'ImportProbe_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/admin/import-products`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "products": [
    {
      "name": "ImportProbe_23127027",
      "price": 99000,
      "description": "Unauthorized import probe",
      "imageUrl": "",
      "category_id": 1
    }
  ]
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Bulk catalog import restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject import execution.
- **Unauthorized Side-Effect Assertion:** Product 'ImportProbe_23127027' is NOT added to database (verified by fetching full product catalog via GET /api/products and asserting that no product with name 'ImportProbe_23127027' exists, without relying on unestablished ?search= semantics).
- **Security Invariant Assertion:** SEC-03: Bulk catalog import strictly enforces role === 'admin'; verified via direct catalog listing inspection.

### Lifecycle & Automation
- **Setup Required:** Prepare unique import JSON payload.
- **Cleanup Required:** If defect occurs and product is created, delete created product via admin credentials.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-006 — Standard user denied POST /api/admin/coupons + coupon not created

### Identity
- **Test ID:** `FR12-AI-006`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-18`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/coupons`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot create a new promotional coupon, and that the coupon code is not stored in database.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Standard user token available; unique coupon code 'HACK23127027' prepared.
- **Disposable Resource State:** Coupon code 'HACK23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/admin/coupons`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "code": "HACK23127027",
  "type": "percent",
  "discount_value": 50,
  "min_order_amount": 100000,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Promotional coupon creation restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must indicate rejection of coupon creation.
- **Unauthorized Side-Effect Assertion:** Coupon 'HACK23127027' is NOT created in database (verified directly via authenticated admin GET /api/coupons asserting that coupon code 'HACK23127027' does not exist, rather than relying on checkout calculation rules).
- **Security Invariant Assertion:** SEC-03: Coupon creation strictly requires role === 'admin'; verified via direct admin coupon listing.

### Lifecycle & Automation
- **Setup Required:** Prepare coupon creation request body.
- **Cleanup Required:** If defect occurs and coupon is created, delete coupon via admin credentials.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-007 — Standard user denied DELETE /api/admin/coupons/:id + coupon not deleted

### Identity
- **Test ID:** `FR12-AI-007`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-20`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/admin/coupons/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot delete a promotional coupon, and that the coupon remains valid in the database.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable test coupon exists with ID <TARGET_COUPON_ID>.
- **Disposable Resource State:** Disposable test coupon (code: 'DISP_COUPON_23127027')

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/coupons/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Coupon deletion restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject coupon deletion.
- **Unauthorized Side-Effect Assertion:** Disposable coupon record remains intact in database (verified directly via authenticated admin GET /api/coupons asserting that disposable coupon ID/code remains present in the list).
- **Security Invariant Assertion:** SEC-03: Coupon deletion requires role === 'admin'; verified directly via admin coupon listing inspection.

### Lifecycle & Automation
- **Setup Required:** Create disposable test coupon using admin credentials prior to probe.
- **Cleanup Required:** Delete disposable test coupon using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-008 — Standard user denied POST /api/products + product not created

### Identity
- **Test ID:** `FR12-AI-008`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-22`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/products`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot insert a new product into the master catalog, and that the product is not created.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Standard user token available; unique product payload prepared.
- **Disposable Resource State:** Product name 'UnauthorizedProduct_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/products`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "UnauthorizedProduct_23127027",
  "price": 500000,
  "description": "Unauthorized creation probe",
  "imageUrl": "https://placehold.co/300x300/png?text=Probe",
  "category_id": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Master catalog product creation restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must indicate access denial and not return created product ID.
- **Unauthorized Side-Effect Assertion:** Product 'UnauthorizedProduct_23127027' is NOT created in catalog (verified by fetching full product catalog via GET /api/products and confirming absence of product, independent of server-side ?search= behavior).
- **Security Invariant Assertion:** SEC-03: Catalog creation requires role === 'admin'; verified via direct catalog listing inspection.

### Lifecycle & Automation
- **Setup Required:** Prepare unique product payload.
- **Cleanup Required:** If defect occurs and product is created, delete created product via admin credentials.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-009 — Standard user denied PUT /api/products/:id + product unchanged

### Identity
- **Test ID:** `FR12-AI-009`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-25`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/products/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot modify an existing product in the catalog, and that the product attributes remain unchanged.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable test product exists with known original attributes.
- **Disposable Resource State:** Disposable product ID <DISP_PRODUCT_ID> (Original Price: 100,000)

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/products/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "Tampered Product Name",
  "price": 1,
  "description": "Tampered description",
  "imageUrl": "",
  "category_id": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Master catalog product modification restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject product modification request.
- **Unauthorized Side-Effect Assertion:** Product attributes in database remain unchanged (GET /api/products/:id verifies original price 100,000).
- **Security Invariant Assertion:** SEC-03: Catalog modification requires role === 'admin'.

### Lifecycle & Automation
- **Setup Required:** Create disposable test product using admin credentials.
- **Cleanup Required:** Delete disposable test product using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-010 — Standard user denied DELETE /api/products/:id + product not deleted

### Identity
- **Test ID:** `FR12-AI-010`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-28`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/products/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot delete a product from the catalog, and that the product continues to exist.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable test product exists in catalog.
- **Disposable Resource State:** Disposable product ID <DISP_PRODUCT_ID>

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/products/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Master catalog product deletion restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject product deletion request.
- **Unauthorized Side-Effect Assertion:** Product continues to exist in catalog (GET /api/products/:id returns 200 with product data).
- **Security Invariant Assertion:** SEC-03: Catalog product deletion strictly requires role === 'admin'.

### Lifecycle & Automation
- **Setup Required:** Create disposable test product using admin credentials.
- **Cleanup Required:** Delete disposable test product using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-011 — Standard user denied POST /api/categories + category not created

### Identity
- **Test ID:** `FR12-AI-011`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-30`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/categories`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot create a product category, and that the category is not inserted into database.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Standard user token available; unique category name prepared.
- **Disposable Resource State:** Category name 'UnauthorizedCategory_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/categories`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "UnauthorizedCategory_23127027"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Category creation restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject category creation.
- **Unauthorized Side-Effect Assertion:** Category is NOT inserted into database (GET /api/categories does not contain probe category name).
- **Security Invariant Assertion:** SEC-03: Category mutation requires role === 'admin' (README Line 177).

### Lifecycle & Automation
- **Setup Required:** Prepare unique category name.
- **Cleanup Required:** If defect occurs and category is created, delete category via admin credentials.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-012 — Standard user denied PUT /api/categories/:id + category unchanged

### Identity
- **Test ID:** `FR12-AI-012`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-32`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/categories/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot modify an existing category, and that the category name remains unchanged.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable test category exists with known initial name.
- **Disposable Resource State:** Disposable category ID <DISP_CAT_ID> (Original Name: 'OriginalCat_23127027')

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/categories/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "TamperedCategoryName"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Category modification restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject category modification.
- **Unauthorized Side-Effect Assertion:** Category name in database remains 'OriginalCat_23127027' (verified via GET /api/categories).
- **Security Invariant Assertion:** SEC-03: Category modification requires role === 'admin'.

### Lifecycle & Automation
- **Setup Required:** Create disposable category using admin credentials.
- **Cleanup Required:** Delete disposable category using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-013 — Standard user denied DELETE /api/categories/:id + category not deleted

### Identity
- **Test ID:** `FR12-AI-013`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-33`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/categories/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user cannot delete a category, and that the category continues to exist in database.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** Disposable test category exists in database.
- **Disposable Resource State:** Disposable category ID <DISP_CAT_ID>

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/categories/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Category deletion restricted to admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject category deletion.
- **Unauthorized Side-Effect Assertion:** Category continues to exist in database (verified via GET /api/categories).
- **Security Invariant Assertion:** SEC-03: Category deletion requires role === 'admin'.

### Lifecycle & Automation
- **Setup Required:** Create disposable category using admin credentials.
- **Cleanup Required:** Delete disposable category using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-014 — Standard user denied access to GET /api/coupons

### Identity
- **Test ID:** `FR12-AI-014`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-15`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/coupons`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Standard User
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `user`
- **Authentication Condition:** Valid JWT token containing role: 'user'

### Test Design
- **Objective:** Verify that a standard user is denied access to view the administrative coupon master list.
- **Access-Control Condition:** Valid JWT token containing role: 'user'
- **Preconditions:** System contains active and inactive discount coupons in database.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/coupons`
- **Request Headers:**
  - `Authorization: Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Coupon master list reserved for admin)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must not expose master coupon records, discount values, or usage thresholds.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** SEC-03: Administrative coupon listing requires role === 'admin' (api_spec Section 5.2).

### Lifecycle & Automation
- **Setup Required:** Obtain standard user JWT token.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-015 — Admin authorized for GET /api/admin/users

### Identity
- **Test ID:** `FR12-AI-015`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-03`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/users`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator (role: 'admin') is authorized to retrieve the system user accounts directory.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin user authenticated with valid JWT token.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response returns JSON array containing user accounts as authorized.
- **Unauthorized Side-Effect Assertion:** Read operation; state remains consistent.
- **Security Invariant Assertion:** FR-12 / SEC-03: Valid admin token successfully satisfies authorization check.

### Lifecycle & Automation
- **Setup Required:** Login as administrator (admin@eshop.com) to obtain admin JWT token.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-016 — Admin authorized for DELETE /api/admin/users/:id on disposable user

### Identity
- **Test ID:** `FR12-AI-016`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-05`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/admin/users/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to delete a disposable user account from the system.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Disposable test user account registered specifically for this deletion test.
- **Disposable Resource State:** Disposable user ID <DISP_USER_ID> (Never delete seeded lecturer users ID 1 or 2)

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/users/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms successful execution of user deletion.
- **Unauthorized Side-Effect Assertion:** Target disposable user is removed from database (verified by confirming deleted disposable user can no longer authenticate / no longer exists; downstream login rejection code classified as INFERRED/UNKNOWN rather than requiring exact 401).
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin clearance allows execution of user deletion handler; side-effect verifies user record removal.

### Lifecycle & Automation
- **Setup Required:** Register a new disposable user account via /api/register to serve as target.
- **Cleanup Required:** None (disposable user was deleted by the test).
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-017 — Admin authorized for GET /api/admin/orders

### Identity
- **Test ID:** `FR12-AI-017`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-08`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/orders`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to view system-wide customer orders.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin authenticated with valid JWT token.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/orders`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response returns JSON array containing system order records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token passes authorization layer unhindered.

### Lifecycle & Automation
- **Setup Required:** Obtain admin JWT token.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-018 — Admin authorized for PUT /api/admin/orders/:id/status

### Identity
- **Test ID:** `FR12-AI-018`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-10`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/admin/orders/:id/status`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to update order fulfillment status on an existing order.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Existing test order available in database with initial status.
- **Disposable Resource State:** Target order ID <TARGET_ORDER_ID>

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/admin/orders/:id/status`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "status": "confirmed"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response indicates order status update was accepted.
- **Unauthorized Side-Effect Assertion:** Order status updated to 'confirmed' in database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token passes authorization to reach order management handler.

### Lifecycle & Automation
- **Setup Required:** Locate valid order ID.
- **Cleanup Required:** Reset status if needed.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-019 — Admin authorized for POST /api/admin/import-products

### Identity
- **Test ID:** `FR12-AI-019`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-13`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/import-products`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to execute bulk product catalog import.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin authenticated; valid product import payload provided.
- **Disposable Resource State:** Disposable product name 'AdminImport_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/admin/import-products`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "products": [
    {
      "name": "AdminImport_23127027",
      "price": 120000,
      "description": "Authorized admin import test item",
      "imageUrl": "",
      "category_id": 1
    }
  ]
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms completion of bulk product import.
- **Unauthorized Side-Effect Assertion:** Product 'AdminImport_23127027' is successfully added into catalog.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears authorization layer.

### Lifecycle & Automation
- **Setup Required:** Prepare valid import payload with unique marker.
- **Cleanup Required:** Delete imported test product using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-020 — Admin authorized for POST /api/admin/coupons

### Identity
- **Test ID:** `FR12-AI-020`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-19`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/coupons`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to create a new promotional coupon.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin authenticated; unique coupon code 'ADMIN_CPN_23127027' prepared.
- **Disposable Resource State:** Disposable coupon code 'ADMIN_CPN_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/admin/coupons`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "code": "ADMIN_CPN_23127027",
  "type": "fixed",
  "discount_value": 20000,
  "min_order_amount": 150000,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms coupon creation with new ID.
- **Unauthorized Side-Effect Assertion:** Coupon 'ADMIN_CPN_23127027' is created in database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token satisfies coupon creation authorization.

### Lifecycle & Automation
- **Setup Required:** Prepare valid coupon creation payload.
- **Cleanup Required:** Delete created test coupon via DELETE /api/admin/coupons/:id after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-021 — Admin authorized for DELETE /api/admin/coupons/:id on disposable coupon

### Identity
- **Test ID:** `FR12-AI-021`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-21`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/admin/coupons/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to delete a disposable promotional coupon.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Disposable test coupon created prior to execution.
- **Disposable Resource State:** Disposable coupon ID <DISP_COUPON_ID> (Never delete seeded coupons SAVE10, BIGBUY)

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/coupons/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms successful deletion of coupon.
- **Unauthorized Side-Effect Assertion:** Disposable coupon is removed from database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears coupon deletion authorization.

### Lifecycle & Automation
- **Setup Required:** Create disposable test coupon via POST /api/admin/coupons.
- **Cleanup Required:** None (coupon deleted by test).
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-022 — Admin authorized for POST /api/products

### Identity
- **Test ID:** `FR12-AI-022`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-23`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/products`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to add a new product to the catalog.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin authenticated; valid product payload prepared.
- **Disposable Resource State:** Disposable product 'AdminProduct_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/products`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "AdminProduct_23127027",
  "price": 250000,
  "description": "Authorized admin product creation",
  "imageUrl": "https://placehold.co/300x300/png?text=AdminProd",
  "category_id": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms product creation with new product ID.
- **Unauthorized Side-Effect Assertion:** Product 'AdminProduct_23127027' is stored in catalog database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears catalog creation authorization.

### Lifecycle & Automation
- **Setup Required:** Prepare valid product payload.
- **Cleanup Required:** Delete created product using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-023 — Admin authorized for PUT /api/products/:id on disposable product

### Identity
- **Test ID:** `FR12-AI-023`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-26`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/products/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to modify an existing disposable product in the catalog.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Disposable test product created prior to execution.
- **Disposable Resource State:** Disposable product ID <DISP_PRODUCT_ID> (Never modify seeded products 1–5)

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/products/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "Updated AdminProduct_23127027",
  "price": 300000,
  "description": "Updated description",
  "imageUrl": "https://placehold.co/300x300/png?text=Updated",
  "category_id": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms product update.
- **Unauthorized Side-Effect Assertion:** Product attributes updated to new values in catalog database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears product modification authorization.

### Lifecycle & Automation
- **Setup Required:** Create disposable product via POST /api/products.
- **Cleanup Required:** Delete disposable product after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-024 — Admin authorized for DELETE /api/products/:id on disposable product

### Identity
- **Test ID:** `FR12-AI-024`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-27`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/products/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to delete a disposable product from the catalog.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Disposable test product created prior to execution.
- **Disposable Resource State:** Disposable product ID <DISP_PRODUCT_ID> (Never delete seeded products 1–5)

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/products/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms product deletion.
- **Unauthorized Side-Effect Assertion:** Disposable product is removed from catalog database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears catalog deletion authorization.

### Lifecycle & Automation
- **Setup Required:** Create disposable product via POST /api/products.
- **Cleanup Required:** None (product deleted by test).
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-025 — Admin authorized for POST /api/categories

### Identity
- **Test ID:** `FR12-AI-025`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-31`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/categories`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to add a new category to the system.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin authenticated; unique category name prepared.
- **Disposable Resource State:** Disposable category 'AdminCategory_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/categories`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "AdminCategory_23127027"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms category creation with new category ID.
- **Unauthorized Side-Effect Assertion:** Category 'AdminCategory_23127027' is stored in database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears category creation authorization.

### Lifecycle & Automation
- **Setup Required:** Prepare valid category creation payload.
- **Cleanup Required:** Delete created category using admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-026 — Admin authorized for PUT /api/categories/:id on disposable category

### Identity
- **Test ID:** `FR12-AI-026`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-32`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/categories/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to modify a disposable category.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Disposable test category created prior to execution.
- **Disposable Resource State:** Disposable category ID <DISP_CAT_ID> (Never modify seeded categories 1–3)

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/categories/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "Updated AdminCategory_23127027"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms category update.
- **Unauthorized Side-Effect Assertion:** Category name in database is updated to 'Updated AdminCategory_23127027'.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears category modification authorization.

### Lifecycle & Automation
- **Setup Required:** Create disposable category via POST /api/categories.
- **Cleanup Required:** Delete disposable category after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-027 — Admin authorized for DELETE /api/categories/:id on disposable category

### Identity
- **Test ID:** `FR12-AI-027`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-34`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/categories/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to delete a disposable category.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Disposable test category created prior to execution.
- **Disposable Resource State:** Disposable category ID <DISP_CAT_ID> (Never delete seeded categories 1–3)

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/categories/:id`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response confirms category deletion.
- **Unauthorized Side-Effect Assertion:** Disposable category is removed from database.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token clears category deletion authorization.

### Lifecycle & Automation
- **Setup Required:** Create disposable category via POST /api/categories.
- **Cleanup Required:** None (category deleted by test).
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-028 — Admin authorized for GET /api/coupons

### Identity
- **Test ID:** `FR12-AI-028`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-16`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/coupons`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `FR-12` (`README.md` Section 9 Line 176-180 (FR-12 Admin Subsystem))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Authenticated Administrator
- **JWT Token State:** Valid cryptographically signed token
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Valid JWT token containing role: 'admin'

### Test Design
- **Objective:** Verify that an authenticated administrator is authorized to view the administrative coupon overview list.
- **Access-Control Condition:** Valid JWT token containing role: 'admin'
- **Preconditions:** Admin authenticated with valid JWT token.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/coupons`
- **Request Headers:**
  - `Authorization: Bearer <VALID_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Response Exposure Assertion:** Response returns JSON array containing all coupon records as authorized for admin.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** FR-12 / SEC-03: Admin token satisfies coupon overview authorization (api_spec Section 5.2).

### Lifecycle & Automation
- **Setup Required:** Obtain admin JWT token.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-029 — Anonymous denied POST /api/products + product not created

### Identity
- **Test ID:** `FR12-AI-029`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-21`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/products`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Anonymous Caller
- **JWT Token State:** No Authorization header present
- **Embedded Role Claim:** `None`
- **Authentication Condition:** Authorization header omitted

### Test Design
- **Objective:** Verify that an unauthenticated caller is denied permission to create a product, and that no product is inserted into database.
- **Access-Control Condition:** Authorization header omitted
- **Preconditions:** Backend running; unique product payload prepared.
- **Disposable Resource State:** Product name 'AnonProduct_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/products`
- **Request Headers:**
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "AnonProduct_23127027",
  "price": 150000,
  "description": "Anonymous creation probe",
  "imageUrl": "",
  "category_id": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Catalog mutation requires valid JWT authentication)
- **Expected HTTP Status:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response must reject creation and not return created ID.
- **Unauthorized Side-Effect Assertion:** Product 'AnonProduct_23127027' is NOT added to database (verified by fetching full product catalog via GET /api/products and confirming absence of marker, without relying on unestablished search-query behavior).
- **Security Invariant Assertion:** SEC-02: Catalog mutation requires valid JWT authentication; verified via direct catalog listing inspection.

### Lifecycle & Automation
- **Setup Required:** Prepare creation payload without Authorization header.
- **Cleanup Required:** If defect CAND-FR12-02 allows insertion, delete created product via admin credentials.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-030 — Anonymous denied PUT /api/products/:id + product unchanged

### Identity
- **Test ID:** `FR12-AI-030`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-24`
- **HTTP Method:** `PUT`
- **Target Endpoint:** `/api/products/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Anonymous Caller
- **JWT Token State:** No Authorization header present
- **Embedded Role Claim:** `None`
- **Authentication Condition:** Authorization header omitted

### Test Design
- **Objective:** Verify that an unauthenticated caller is denied permission to update a product, and that product attributes remain unchanged.
- **Access-Control Condition:** Authorization header omitted
- **Preconditions:** Disposable test product exists with original price 200,000.
- **Disposable Resource State:** Disposable product ID <DISP_PRODUCT_ID> (Original Price: 200,000)

### HTTP Request Specification
- **Method:** `PUT`
- **Endpoint:** `/api/products/:id`
- **Request Headers:**
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "AnonTamperedName",
  "price": 10,
  "description": "Anon update probe",
  "imageUrl": "",
  "category_id": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Product update requires valid JWT authentication)
- **Expected HTTP Status:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response must reject update request.
- **Unauthorized Side-Effect Assertion:** Product attributes in database remain unchanged (GET /api/products/:id verifies original price 200,000).
- **Security Invariant Assertion:** SEC-02: Product modification requires valid JWT authentication.

### Lifecycle & Automation
- **Setup Required:** Create disposable product via admin credentials.
- **Cleanup Required:** Delete disposable product after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-031 — Anonymous denied DELETE /api/products/:id + product not deleted

### Identity
- **Test ID:** `FR12-AI-031`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-27`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/products/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Anonymous Caller
- **JWT Token State:** No Authorization header present
- **Embedded Role Claim:** `None`
- **Authentication Condition:** Authorization header omitted

### Test Design
- **Objective:** Verify that an unauthenticated caller is denied permission to delete a product, and that the product is not deleted.
- **Access-Control Condition:** Authorization header omitted
- **Preconditions:** Disposable test product exists in catalog.
- **Disposable Resource State:** Disposable product ID <DISP_PRODUCT_ID>

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/products/:id`
- **Request Headers:**
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Product deletion requires valid JWT authentication)
- **Expected HTTP Status:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response must reject deletion request.
- **Unauthorized Side-Effect Assertion:** Product continues to exist in database (GET /api/products/:id returns product details).
- **Security Invariant Assertion:** SEC-02: Product deletion requires valid JWT authentication.

### Lifecycle & Automation
- **Setup Required:** Create disposable product via admin credentials.
- **Cleanup Required:** Delete disposable product via admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-032 — Anonymous denied access to GET /api/admin/users

### Identity
- **Test ID:** `FR12-AI-032`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-01`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/users`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Anonymous Caller
- **JWT Token State:** No Authorization header present
- **Embedded Role Claim:** `None`
- **Authentication Condition:** Authorization header omitted

### Test Design
- **Objective:** Verify that an unauthenticated caller is denied access to the administrative user accounts list.
- **Access-Control Condition:** Authorization header omitted
- **Preconditions:** Backend running.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Request Headers:**
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Admin API requires valid JWT authentication)
- **Expected HTTP Status:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response payload must not expose user account directory records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** SEC-02: /api/admin/* endpoints strictly require valid JWT authentication.

### Lifecycle & Automation
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-033 — Anonymous denied POST /api/categories + category not created

### Identity
- **Test ID:** `FR12-AI-033`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-29`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/categories`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Anonymous Caller
- **JWT Token State:** No Authorization header present
- **Embedded Role Claim:** `None`
- **Authentication Condition:** Authorization header omitted

### Test Design
- **Objective:** Verify that an unauthenticated caller is denied permission to create a product category, and that category is not inserted.
- **Access-Control Condition:** Authorization header omitted
- **Preconditions:** Backend running; unique category name prepared.
- **Disposable Resource State:** Category name 'AnonCategory_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/categories`
- **Request Headers:**
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "name": "AnonCategory_23127027"
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Category creation requires valid JWT authentication)
- **Expected HTTP Status:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response must reject category creation.
- **Unauthorized Side-Effect Assertion:** Category 'AnonCategory_23127027' is NOT added to database (verified via GET /api/categories).
- **Security Invariant Assertion:** SEC-02: Category mutation requires valid JWT authentication.

### Lifecycle & Automation
- **Setup Required:** Prepare creation payload without Authorization header.
- **Cleanup Required:** Defect-path cleanup: If access-control defect CAND-FR12-03 allows category creation, delete created category 'AnonCategory_23127027' using legitimate admin credentials after test execution.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-034 — Anonymous denied access to GET /api/coupons

### Identity
- **Test ID:** `FR12-AI-034`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-14`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/coupons`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Anonymous Caller
- **JWT Token State:** No Authorization header present
- **Embedded Role Claim:** `None`
- **Authentication Condition:** Authorization header omitted

### Test Design
- **Objective:** Verify that an unauthenticated caller is denied access to view the administrative coupon master list.
- **Access-Control Condition:** Authorization header omitted
- **Preconditions:** Coupons present in database.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/coupons`
- **Request Headers:**
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Coupon overview requires valid JWT authentication)
- **Expected HTTP Status:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response must not return list of discount coupons.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** SEC-02: GET /api/coupons requires Authorization: Bearer <token> (api_spec Section 5.2).

### Lifecycle & Automation
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-035 — Expired admin token denied GET /api/admin/users

### Identity
- **Test ID:** `FR12-AI-035`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-35`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/users`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Expired Admin Token Caller
- **JWT Token State:** Expired JWT (exp claim in the past; cryptographic signature may remain valid, but temporal validity has expired)
- **Embedded Role Claim:** `admin`
- **Authentication Condition:** Token signed with correct secret but exp < currentTime

### Test Design
- **Objective:** Verify that an administrator request bearing an expired JWT token is rejected, preventing unauthorized access past session expiration.
- **Access-Control Condition:** Token signed with correct secret but exp < currentTime
- **Preconditions:** Legitimately signed admin JWT generated with exp timestamp set 1 hour in the past.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Request Headers:**
  - `Authorization: Bearer <EXPIRED_ADMIN_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Expired token fails temporal validity check; signature may be mathematically intact but exp < currentTime causes verification failure)
- **Expected HTTP Status:** `403 Forbidden (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response payload must not expose user directory records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** SEC-02: Expired tokens must be rejected by JWT verification layer due to expired lifecycle claim, even if cryptographic HMAC signature was signed by valid secret key.

### Lifecycle & Automation
- **Setup Required:** Generate expired admin token using test signing script.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-036 — Forged signature token denied GET /api/admin/orders

### Identity
- **Test ID:** `FR12-AI-036`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-36`
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/orders`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-02` (`README.md` Section 9 Line 279 (SEC-02: Valid JWT required))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Forged Signature Token Caller
- **JWT Token State:** Signature chunk altered / invalid cryptographic HMAC
- **Embedded Role Claim:** `admin (claimed in payload)`
- **Authentication Condition:** Header and payload claim admin role, but signature chunk is tampered

### Test Design
- **Objective:** Verify that a request bearing a JWT with a forged/manipulated cryptographic signature is rejected by the access-control layer.
- **Access-Control Condition:** Header and payload claim admin role, but signature chunk is tampered
- **Preconditions:** Admin JWT with modified signature bytes.
- **Disposable Resource State:** N/A (Read operation)

### HTTP Request Specification
- **Method:** `GET`
- **Endpoint:** `/api/admin/orders`
- **Request Headers:**
  - `Authorization: Bearer <FORGED_SIGNATURE_TOKEN>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-02 Violation: Forged signature fails cryptographic integrity check)
- **Expected HTTP Status:** `403 Forbidden (Inferred from SUT middleware / Unspecified in spec)`
- **Response Exposure Assertion:** Response payload must not expose order records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Security Invariant Assertion:** SEC-02: Invalid cryptographic signature rejected by jwt.verify.

### Lifecycle & Automation
- **Setup Required:** Construct token with altered signature chunk.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-037 — Missing role claim token denied POST /api/admin/coupons

### Identity
- **Test ID:** `FR12-AI-037`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-37`
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/coupons`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Missing Role Claim Token Caller
- **JWT Token State:** Valid signature, but payload contains no role field ({ id: 10 })
- **Embedded Role Claim:** `None (Omitted claim)`
- **Authentication Condition:** Valid signature from SUT SECRET_KEY, payload has id but no role claim

### Test Design
- **Objective:** Verify that a request bearing a valid JWT token that omits the 'role' claim entirely is denied access to admin coupon creation.
- **Access-Control Condition:** Valid signature from SUT SECRET_KEY, payload has id but no role claim
- **Preconditions:** Custom token signed without role claim.
- **Disposable Resource State:** Coupon code 'NOROLE_CPN_23127027'

### HTTP Request Specification
- **Method:** `POST`
- **Endpoint:** `/api/admin/coupons`
- **Request Headers:**
  - `Authorization: Bearer <TOKEN_WITHOUT_ROLE_CLAIM>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "code": "NOROLE_CPN_23127027",
  "type": "fixed",
  "discount_value": 10000,
  "min_order_amount": 50000,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Missing role claim does not satisfy role === 'admin')
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject coupon creation.
- **Unauthorized Side-Effect Assertion:** Coupon 'NOROLE_CPN_23127027' is NOT created in database (verified via admin GET /api/coupons).
- **Security Invariant Assertion:** SEC-03: System requires explicit role === 'admin'; missing claim must not grant elevated privileges.

### Lifecycle & Automation
- **Setup Required:** Generate custom signed token omitting role claim.
- **Cleanup Required:** Defect-path cleanup: If SEC-03 authorization failure allows coupon creation, delete created coupon 'NOROLE_CPN_23127027' using legitimate admin credentials after test execution.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

## FR12-AI-038 — Uppercase role 'ADMIN' denied DELETE /api/admin/users/:id

### Identity
- **Test ID:** `FR12-AI-038`
- **Origin:** AI (Reviewed & Corrected by Student)
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `COV-FR12-38`
- **HTTP Method:** `DELETE`
- **Target Endpoint:** `/api/admin/users/:id`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `SEC-03` (`README.md` Section 9 Line 280 (SEC-03: Admin role enforced))
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** Tampered / Spoofed Role Caller
- **JWT Token State:** Valid signature, but payload contains spoofed role ('ADMIN' uppercase or 'manager')
- **Embedded Role Claim:** `ADMIN (Uppercase)`
- **Authentication Condition:** Valid signature from SUT SECRET_KEY, payload has role: 'ADMIN'

### Test Design
- **Objective:** Verify that case sensitivity is strictly enforced and that uppercase role 'ADMIN' or spoofed roles are denied administrative deletion.
- **Access-Control Condition:** Valid signature from SUT SECRET_KEY, payload has role: 'ADMIN'
- **Preconditions:** Disposable test user exists; custom token signed with role: 'ADMIN'.
- **Disposable Resource State:** Disposable test user ID <TARGET_USER_ID>

### HTTP Request Specification
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/users/:id`
- **Request Headers:**
  - `Authorization: Bearer <TOKEN_UPPERCASE_ROLE>`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
None (Empty Body)
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** ACCESS DENIED (SEC-03 Violation: Strict exact-match role === 'admin' required; uppercase or spoofed role rejected)
- **Expected HTTP Status:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Response Exposure Assertion:** Response must reject user deletion.
- **Unauthorized Side-Effect Assertion:** Target disposable user is NOT deleted from database (verified via login probe).
- **Security Invariant Assertion:** SEC-03: Role verification must strictly match 'admin' in exact lowercase.

### Lifecycle & Automation
- **Setup Required:** Create disposable test user; sign custom token with role: 'ADMIN'.
- **Cleanup Required:** Clean up disposable test user via official admin credentials after test.
- **Automation Status:** READY FOR AUTOMATION (Phase 4)

---

