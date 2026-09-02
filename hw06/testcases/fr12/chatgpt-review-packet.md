# FR-12: Access Control — External AI (ChatGPT) Review Packet

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

### FR12-AI-001

- **Coverage ID:** `COV-FR12-02`
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user (role: 'user') calls GET /api/admin/users
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Non-admin subject attempting administrative user listing)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response payload must not expose user account directory rows (passwords, emails, roles).
- **Unauthorized Side-Effect Assertion:** Read-only operation; zero mutation expected.
- **Setup / Disposable Resource:** Authenticate standard user to obtain valid JWT. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-002

- **Coverage ID:** `COV-FR12-04`
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/users/:id`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls DELETE /api/admin/users/:id on disposable user
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Standard user cannot execute administrative user deletion)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must indicate authorization rejection and not confirm deletion.
- **Unauthorized Side-Effect Assertion:** Target user account remains active in database; follow-up login probe with target user credentials must succeed.
- **Setup / Disposable Resource:** Create disposable test user account via /api/register to act as deletion target. | Resource: Disposable test user (e.g. test_victim_23127027@eshop.com)
- **Cleanup:** Clean up disposable test user via admin credentials after test completion.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable test user account via /api/register to act as deletion target. (Disposable Target: Disposable test user (e.g. test_victim_23127027@eshop.com))
  2. Action: Send `DELETE /api/admin/users/:id` with headers [Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Standard user cannot execute administrative user deletion)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Target user account remains active in database; follow-up login probe with target user credentials must succeed.
  5. Cleanup Step: Clean up disposable test user via admin credentials after test completion.

---

### FR12-AI-003

- **Coverage ID:** `COV-FR12-07`
- **Method:** `GET`
- **Endpoint:** `/api/admin/orders`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls GET /api/admin/orders
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Non-admin cannot view system-wide customer order history)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response payload must not expose order records belonging to other system users.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** Obtain standard user JWT token. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-004

- **Coverage ID:** `COV-FR12-09`
- **Method:** `PUT`
- **Endpoint:** `/api/admin/orders/:id/status`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls PUT /api/admin/orders/:id/status with body status: 'delivered'
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Non-admin prohibited from modifying administrative order status)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject status mutation request.
- **Unauthorized Side-Effect Assertion:** Order status in database remains 'pending' (verified via admin order query); no state transition occurred.
- **Setup / Disposable Resource:** Identify or create a test order with status 'pending'. | Resource: Order ID <TARGET_ORDER_ID> with initial status 'pending'
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "status": "delivered" }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Identify or create a test order with status 'pending'. (Disposable Target: Order ID <TARGET_ORDER_ID> with initial status 'pending')
  2. Action: Send `PUT /api/admin/orders/:id/status` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "status": "delivered" }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Non-admin prohibited from modifying administrative order status)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Order status in database remains 'pending' (verified via admin order query); no state transition occurred.
  5. Cleanup Step: None.

---

### FR12-AI-005

- **Coverage ID:** `COV-FR12-12`
- **Method:** `POST`
- **Endpoint:** `/api/admin/import-products`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls POST /api/admin/import-products with product array
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Bulk catalog import restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject import execution.
- **Unauthorized Side-Effect Assertion:** Product 'ImportProbe_23127027' is NOT added to database (follow-up GET /api/products?search=ImportProbe_23127027 returns empty list).
- **Setup / Disposable Resource:** Prepare unique import JSON payload. | Resource: Product import payload with unique marker 'ImportProbe_23127027'
- **Cleanup:** If defect occurs and product is created, delete created product via admin credentials.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "products": [     {       "name": "ImportProbe_23127027",       "price": 99000,       "description": "Unauthorized import probe",       "imageUrl": "",       "category_id": 1     }   ] }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare unique import JSON payload. (Disposable Target: Product import payload with unique marker 'ImportProbe_23127027')
  2. Action: Send `POST /api/admin/import-products` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "products": [     {       "name": "ImportProbe_23127027",       "price": 99000,       "description": "Unauthorized import probe",       "imageUrl": "",       "category_id": 1     }   ] }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Bulk catalog import restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Product 'ImportProbe_23127027' is NOT added to database (follow-up GET /api/products?search=ImportProbe_23127027 returns empty list).
  5. Cleanup Step: If defect occurs and product is created, delete created product via admin credentials.

---

### FR12-AI-006

- **Coverage ID:** `COV-FR12-18`
- **Method:** `POST`
- **Endpoint:** `/api/admin/coupons`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls POST /api/admin/coupons with coupon payload
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Promotional coupon creation restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must indicate rejection of coupon creation.
- **Unauthorized Side-Effect Assertion:** Coupon 'HACK23127027' is NOT created in database; checkout probe with code returns invalid coupon error.
- **Setup / Disposable Resource:** Prepare coupon creation request body. | Resource: Coupon code 'HACK23127027'
- **Cleanup:** If defect occurs and coupon is created, delete coupon via admin credentials.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "code": "HACK23127027",   "type": "percent",   "discount_value": 50,   "min_order_amount": 100000,   "expired_at": "2099-12-31",   "max_uses_per_user": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare coupon creation request body. (Disposable Target: Coupon code 'HACK23127027')
  2. Action: Send `POST /api/admin/coupons` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "code": "HACK23127027",   "type": "percent",   "discount_value": 50,   "min_order_amount": 100000,   "expired_at": "2099-12-31",   "max_uses_per_user": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Promotional coupon creation restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Coupon 'HACK23127027' is NOT created in database; checkout probe with code returns invalid coupon error.
  5. Cleanup Step: If defect occurs and coupon is created, delete coupon via admin credentials.

---

### FR12-AI-007

- **Coverage ID:** `COV-FR12-20`
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/coupons/:id`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls DELETE /api/admin/coupons/:id on disposable coupon
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Coupon deletion restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject coupon deletion.
- **Unauthorized Side-Effect Assertion:** Coupon record remains in database; query or application of coupon still succeeds.
- **Setup / Disposable Resource:** Create disposable test coupon using admin credentials prior to probe. | Resource: Disposable test coupon (code: 'DISP_COUPON_23127027')
- **Cleanup:** Delete disposable test coupon using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable test coupon using admin credentials prior to probe. (Disposable Target: Disposable test coupon (code: 'DISP_COUPON_23127027'))
  2. Action: Send `DELETE /api/admin/coupons/:id` with headers [Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Coupon deletion restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Coupon record remains in database; query or application of coupon still succeeds.
  5. Cleanup Step: Delete disposable test coupon using admin credentials after test.

---

### FR12-AI-008

- **Coverage ID:** `COV-FR12-22`
- **Method:** `POST`
- **Endpoint:** `/api/products`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls POST /api/products with product payload
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Master catalog product creation restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must indicate access denial and not return created product ID.
- **Unauthorized Side-Effect Assertion:** Product is NOT created in catalog (GET /api/products?search=UnauthorizedProduct_23127027 returns empty list).
- **Setup / Disposable Resource:** Prepare unique product payload. | Resource: Product name 'UnauthorizedProduct_23127027'
- **Cleanup:** If defect occurs and product is created, delete created product via admin credentials.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "UnauthorizedProduct_23127027",   "price": 500000,   "description": "Unauthorized creation probe",   "imageUrl": "https://placehold.co/300x300/png?text=Probe",   "category_id": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare unique product payload. (Disposable Target: Product name 'UnauthorizedProduct_23127027')
  2. Action: Send `POST /api/products` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "UnauthorizedProduct_23127027",   "price": 500000,   "description": "Unauthorized creation probe",   "imageUrl": "https://placehold.co/300x300/png?text=Probe",   "category_id": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Master catalog product creation restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Product is NOT created in catalog (GET /api/products?search=UnauthorizedProduct_23127027 returns empty list).
  5. Cleanup Step: If defect occurs and product is created, delete created product via admin credentials.

---

### FR12-AI-009

- **Coverage ID:** `COV-FR12-25`
- **Method:** `PUT`
- **Endpoint:** `/api/products/:id`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls PUT /api/products/:id with altered price
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Master catalog product modification restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject product modification request.
- **Unauthorized Side-Effect Assertion:** Product attributes in database remain unchanged (GET /api/products/:id verifies original price 100,000).
- **Setup / Disposable Resource:** Create disposable test product using admin credentials. | Resource: Disposable product ID <DISP_PRODUCT_ID> (Original Price: 100,000)
- **Cleanup:** Delete disposable test product using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "Tampered Product Name",   "price": 1,   "description": "Tampered description",   "imageUrl": "",   "category_id": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable test product using admin credentials. (Disposable Target: Disposable product ID <DISP_PRODUCT_ID> (Original Price: 100,000))
  2. Action: Send `PUT /api/products/:id` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "Tampered Product Name",   "price": 1,   "description": "Tampered description",   "imageUrl": "",   "category_id": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Master catalog product modification restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Product attributes in database remain unchanged (GET /api/products/:id verifies original price 100,000).
  5. Cleanup Step: Delete disposable test product using admin credentials after test.

---

### FR12-AI-010

- **Coverage ID:** `COV-FR12-28`
- **Method:** `DELETE`
- **Endpoint:** `/api/products/:id`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls DELETE /api/products/:id on disposable product
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Master catalog product deletion restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject product deletion request.
- **Unauthorized Side-Effect Assertion:** Product continues to exist in catalog (GET /api/products/:id returns 200 with product data).
- **Setup / Disposable Resource:** Create disposable test product using admin credentials. | Resource: Disposable product ID <DISP_PRODUCT_ID>
- **Cleanup:** Delete disposable test product using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable test product using admin credentials. (Disposable Target: Disposable product ID <DISP_PRODUCT_ID>)
  2. Action: Send `DELETE /api/products/:id` with headers [Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Master catalog product deletion restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Product continues to exist in catalog (GET /api/products/:id returns 200 with product data).
  5. Cleanup Step: Delete disposable test product using admin credentials after test.

---

### FR12-AI-011

- **Coverage ID:** `COV-FR12-30`
- **Method:** `POST`
- **Endpoint:** `/api/categories`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls POST /api/categories with category name
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Category creation restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject category creation.
- **Unauthorized Side-Effect Assertion:** Category is NOT inserted into database (GET /api/categories does not contain probe category name).
- **Setup / Disposable Resource:** Prepare unique category name. | Resource: Category name 'UnauthorizedCategory_23127027'
- **Cleanup:** If defect occurs and category is created, delete category via admin credentials.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "UnauthorizedCategory_23127027" }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare unique category name. (Disposable Target: Category name 'UnauthorizedCategory_23127027')
  2. Action: Send `POST /api/categories` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "UnauthorizedCategory_23127027" }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Category creation restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Category is NOT inserted into database (GET /api/categories does not contain probe category name).
  5. Cleanup Step: If defect occurs and category is created, delete category via admin credentials.

---

### FR12-AI-012

- **Coverage ID:** `COV-FR12-32`
- **Method:** `PUT`
- **Endpoint:** `/api/categories/:id`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls PUT /api/categories/:id with new name
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Category modification restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject category modification.
- **Unauthorized Side-Effect Assertion:** Category name in database remains 'OriginalCat_23127027' (verified via GET /api/categories).
- **Setup / Disposable Resource:** Create disposable category using admin credentials. | Resource: Disposable category ID <DISP_CAT_ID> (Original Name: 'OriginalCat_23127027')
- **Cleanup:** Delete disposable category using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "TamperedCategoryName" }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable category using admin credentials. (Disposable Target: Disposable category ID <DISP_CAT_ID> (Original Name: 'OriginalCat_23127027'))
  2. Action: Send `PUT /api/categories/:id` with headers [Authorization: Bearer <VALID_USER_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "TamperedCategoryName" }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Category modification restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Category name in database remains 'OriginalCat_23127027' (verified via GET /api/categories).
  5. Cleanup Step: Delete disposable category using admin credentials after test.

---

### FR12-AI-013

- **Coverage ID:** `COV-FR12-33`
- **Method:** `DELETE`
- **Endpoint:** `/api/categories/:id`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls DELETE /api/categories/:id on disposable category
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Category deletion restricted to admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject category deletion.
- **Unauthorized Side-Effect Assertion:** Category continues to exist in database (verified via GET /api/categories).
- **Setup / Disposable Resource:** Create disposable category using admin credentials. | Resource: Disposable category ID <DISP_CAT_ID>
- **Cleanup:** Delete disposable category using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable category using admin credentials. (Disposable Target: Disposable category ID <DISP_CAT_ID>)
  2. Action: Send `DELETE /api/categories/:id` with headers [Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Category deletion restricted to admin)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Category continues to exist in database (verified via GET /api/categories).
  5. Cleanup Step: Delete disposable category using admin credentials after test.

---

### FR12-AI-014

- **Coverage ID:** `COV-FR12-15`
- **Method:** `GET`
- **Endpoint:** `/api/coupons`
- **Caller Type:** Authenticated Standard User
- **JWT State:** Valid cryptographically signed token
- **Role:** `user`
- **One-sentence Test Condition:** Standard user calls GET /api/coupons
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Coupon master list reserved for admin)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must not expose master coupon records, discount values, or usage thresholds.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** Obtain standard user JWT token. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_USER_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-015

- **Coverage ID:** `COV-FR12-03`
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin user (role: 'admin') calls GET /api/admin/users
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response returns JSON array containing user accounts as authorized.
- **Unauthorized Side-Effect Assertion:** Read operation; state remains consistent.
- **Setup / Disposable Resource:** Login as administrator (admin@eshop.com) to obtain admin JWT token. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Login as administrator (admin@eshop.com) to obtain admin JWT token. (Disposable Target: N/A (Read operation))
  2. Action: Send `GET /api/admin/users` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Read operation; state remains consistent.
  5. Cleanup Step: None.

---

### FR12-AI-016

- **Coverage ID:** `COV-FR12-05`
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/users/:id`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls DELETE /api/admin/users/:id on disposable user
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms successful execution of user deletion.
- **Unauthorized Side-Effect Assertion:** Target disposable user is removed from database (subsequent login probe fails with 401).
- **Setup / Disposable Resource:** Register a new disposable user account via /api/register to serve as target. | Resource: Disposable user ID <DISP_USER_ID> (Never delete seeded lecturer users ID 1 or 2)
- **Cleanup:** None (disposable user was deleted by the test).
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Register a new disposable user account via /api/register to serve as target. (Disposable Target: Disposable user ID <DISP_USER_ID> (Never delete seeded lecturer users ID 1 or 2))
  2. Action: Send `DELETE /api/admin/users/:id` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Target disposable user is removed from database (subsequent login probe fails with 401).
  5. Cleanup Step: None (disposable user was deleted by the test).

---

### FR12-AI-017

- **Coverage ID:** `COV-FR12-08`
- **Method:** `GET`
- **Endpoint:** `/api/admin/orders`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls GET /api/admin/orders
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response returns JSON array containing system order records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** Obtain admin JWT token. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Obtain admin JWT token. (Disposable Target: N/A (Read operation))
  2. Action: Send `GET /api/admin/orders` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Zero state modification.
  5. Cleanup Step: None.

---

### FR12-AI-018

- **Coverage ID:** `COV-FR12-10`
- **Method:** `PUT`
- **Endpoint:** `/api/admin/orders/:id/status`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls PUT /api/admin/orders/:id/status with valid status
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response indicates order status update was accepted.
- **Unauthorized Side-Effect Assertion:** Order status updated to 'confirmed' in database.
- **Setup / Disposable Resource:** Locate valid order ID. | Resource: Target order ID <TARGET_ORDER_ID>
- **Cleanup:** Reset status if needed.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "status": "confirmed" }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Locate valid order ID. (Disposable Target: Target order ID <TARGET_ORDER_ID>)
  2. Action: Send `PUT /api/admin/orders/:id/status` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "status": "confirmed" }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Order status updated to 'confirmed' in database.
  5. Cleanup Step: Reset status if needed.

---

### FR12-AI-019

- **Coverage ID:** `COV-FR12-13`
- **Method:** `POST`
- **Endpoint:** `/api/admin/import-products`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls POST /api/admin/import-products with valid payload
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms completion of bulk product import.
- **Unauthorized Side-Effect Assertion:** Product 'AdminImport_23127027' is successfully added into catalog.
- **Setup / Disposable Resource:** Prepare valid import payload with unique marker. | Resource: Disposable product name 'AdminImport_23127027'
- **Cleanup:** Delete imported test product using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "products": [     {       "name": "AdminImport_23127027",       "price": 120000,       "description": "Authorized admin import test item",       "imageUrl": "",       "category_id": 1     }   ] }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare valid import payload with unique marker. (Disposable Target: Disposable product name 'AdminImport_23127027')
  2. Action: Send `POST /api/admin/import-products` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "products": [     {       "name": "AdminImport_23127027",       "price": 120000,       "description": "Authorized admin import test item",       "imageUrl": "",       "category_id": 1     }   ] }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Product 'AdminImport_23127027' is successfully added into catalog.
  5. Cleanup Step: Delete imported test product using admin credentials after test.

---

### FR12-AI-020

- **Coverage ID:** `COV-FR12-19`
- **Method:** `POST`
- **Endpoint:** `/api/admin/coupons`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls POST /api/admin/coupons with valid coupon payload
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms coupon creation with new ID.
- **Unauthorized Side-Effect Assertion:** Coupon 'ADMIN_CPN_23127027' is created in database.
- **Setup / Disposable Resource:** Prepare valid coupon creation payload. | Resource: Disposable coupon code 'ADMIN_CPN_23127027'
- **Cleanup:** Delete created test coupon via DELETE /api/admin/coupons/:id after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "code": "ADMIN_CPN_23127027",   "type": "fixed",   "discount_value": 20000,   "min_order_amount": 150000,   "expired_at": "2099-12-31",   "max_uses_per_user": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare valid coupon creation payload. (Disposable Target: Disposable coupon code 'ADMIN_CPN_23127027')
  2. Action: Send `POST /api/admin/coupons` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "code": "ADMIN_CPN_23127027",   "type": "fixed",   "discount_value": 20000,   "min_order_amount": 150000,   "expired_at": "2099-12-31",   "max_uses_per_user": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Coupon 'ADMIN_CPN_23127027' is created in database.
  5. Cleanup Step: Delete created test coupon via DELETE /api/admin/coupons/:id after test.

---

### FR12-AI-021

- **Coverage ID:** `COV-FR12-21`
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/coupons/:id`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls DELETE /api/admin/coupons/:id on disposable coupon
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms successful deletion of coupon.
- **Unauthorized Side-Effect Assertion:** Disposable coupon is removed from database.
- **Setup / Disposable Resource:** Create disposable test coupon via POST /api/admin/coupons. | Resource: Disposable coupon ID <DISP_COUPON_ID> (Never delete seeded coupons SAVE10, BIGBUY)
- **Cleanup:** None (coupon deleted by test).
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable test coupon via POST /api/admin/coupons. (Disposable Target: Disposable coupon ID <DISP_COUPON_ID> (Never delete seeded coupons SAVE10, BIGBUY))
  2. Action: Send `DELETE /api/admin/coupons/:id` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Disposable coupon is removed from database.
  5. Cleanup Step: None (coupon deleted by test).

---

### FR12-AI-022

- **Coverage ID:** `COV-FR12-23`
- **Method:** `POST`
- **Endpoint:** `/api/products`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls POST /api/products with valid product body
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms product creation with new product ID.
- **Unauthorized Side-Effect Assertion:** Product 'AdminProduct_23127027' is stored in catalog database.
- **Setup / Disposable Resource:** Prepare valid product payload. | Resource: Disposable product 'AdminProduct_23127027'
- **Cleanup:** Delete created product using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "AdminProduct_23127027",   "price": 250000,   "description": "Authorized admin product creation",   "imageUrl": "https://placehold.co/300x300/png?text=AdminProd",   "category_id": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare valid product payload. (Disposable Target: Disposable product 'AdminProduct_23127027')
  2. Action: Send `POST /api/products` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "AdminProduct_23127027",   "price": 250000,   "description": "Authorized admin product creation",   "imageUrl": "https://placehold.co/300x300/png?text=AdminProd",   "category_id": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Product 'AdminProduct_23127027' is stored in catalog database.
  5. Cleanup Step: Delete created product using admin credentials after test.

---

### FR12-AI-023

- **Coverage ID:** `COV-FR12-26`
- **Method:** `PUT`
- **Endpoint:** `/api/products/:id`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls PUT /api/products/:id on disposable product
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms product update.
- **Unauthorized Side-Effect Assertion:** Product attributes updated to new values in catalog database.
- **Setup / Disposable Resource:** Create disposable product via POST /api/products. | Resource: Disposable product ID <DISP_PRODUCT_ID> (Never modify seeded products 1–5)
- **Cleanup:** Delete disposable product after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "Updated AdminProduct_23127027",   "price": 300000,   "description": "Updated description",   "imageUrl": "https://placehold.co/300x300/png?text=Updated",   "category_id": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable product via POST /api/products. (Disposable Target: Disposable product ID <DISP_PRODUCT_ID> (Never modify seeded products 1–5))
  2. Action: Send `PUT /api/products/:id` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "Updated AdminProduct_23127027",   "price": 300000,   "description": "Updated description",   "imageUrl": "https://placehold.co/300x300/png?text=Updated",   "category_id": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Product attributes updated to new values in catalog database.
  5. Cleanup Step: Delete disposable product after test.

---

### FR12-AI-024

- **Coverage ID:** `COV-FR12-27`
- **Method:** `DELETE`
- **Endpoint:** `/api/products/:id`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls DELETE /api/products/:id on disposable product
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms product deletion.
- **Unauthorized Side-Effect Assertion:** Disposable product is removed from catalog database.
- **Setup / Disposable Resource:** Create disposable product via POST /api/products. | Resource: Disposable product ID <DISP_PRODUCT_ID> (Never delete seeded products 1–5)
- **Cleanup:** None (product deleted by test).
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable product via POST /api/products. (Disposable Target: Disposable product ID <DISP_PRODUCT_ID> (Never delete seeded products 1–5))
  2. Action: Send `DELETE /api/products/:id` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Disposable product is removed from catalog database.
  5. Cleanup Step: None (product deleted by test).

---

### FR12-AI-025

- **Coverage ID:** `COV-FR12-31`
- **Method:** `POST`
- **Endpoint:** `/api/categories`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls POST /api/categories with valid category body
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms category creation with new category ID.
- **Unauthorized Side-Effect Assertion:** Category 'AdminCategory_23127027' is stored in database.
- **Setup / Disposable Resource:** Prepare valid category creation payload. | Resource: Disposable category 'AdminCategory_23127027'
- **Cleanup:** Delete created category using admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "AdminCategory_23127027" }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Prepare valid category creation payload. (Disposable Target: Disposable category 'AdminCategory_23127027')
  2. Action: Send `POST /api/categories` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "AdminCategory_23127027" }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Category 'AdminCategory_23127027' is stored in database.
  5. Cleanup Step: Delete created category using admin credentials after test.

---

### FR12-AI-026

- **Coverage ID:** `COV-FR12-32`
- **Method:** `PUT`
- **Endpoint:** `/api/categories/:id`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls PUT /api/categories/:id on disposable category
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms category update.
- **Unauthorized Side-Effect Assertion:** Category name in database is updated to 'Updated AdminCategory_23127027'.
- **Setup / Disposable Resource:** Create disposable category via POST /api/categories. | Resource: Disposable category ID <DISP_CAT_ID> (Never modify seeded categories 1–3)
- **Cleanup:** Delete disposable category after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "Updated AdminCategory_23127027" }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable category via POST /api/categories. (Disposable Target: Disposable category ID <DISP_CAT_ID> (Never modify seeded categories 1–3))
  2. Action: Send `PUT /api/categories/:id` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "name": "Updated AdminCategory_23127027" }`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Category name in database is updated to 'Updated AdminCategory_23127027'.
  5. Cleanup Step: Delete disposable category after test.

---

### FR12-AI-027

- **Coverage ID:** `COV-FR12-34`
- **Method:** `DELETE`
- **Endpoint:** `/api/categories/:id`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls DELETE /api/categories/:id on disposable category
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response confirms category deletion.
- **Unauthorized Side-Effect Assertion:** Disposable category is removed from database.
- **Setup / Disposable Resource:** Create disposable category via POST /api/categories. | Resource: Disposable category ID <DISP_CAT_ID> (Never delete seeded categories 1–3)
- **Cleanup:** None (category deleted by test).
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable category via POST /api/categories. (Disposable Target: Disposable category ID <DISP_CAT_ID> (Never delete seeded categories 1–3))
  2. Action: Send `DELETE /api/categories/:id` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Disposable category is removed from database.
  5. Cleanup Step: None (category deleted by test).

---

### FR12-AI-028

- **Coverage ID:** `COV-FR12-16`
- **Method:** `GET`
- **Endpoint:** `/api/coupons`
- **Caller Type:** Authenticated Administrator
- **JWT State:** Valid cryptographically signed token
- **Role:** `admin`
- **One-sentence Test Condition:** Admin calls GET /api/coupons
- **Official Requirement / SEC:** `FR-12` (FR-12 Lines 174–180; Admin Subsystem)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)
- **Expected HTTP Status + Classification:** `200 OK (Inferred from SUT / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response returns JSON array containing all coupon records as authorized for admin.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** Obtain admin JWT token. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Obtain admin JWT token. (Disposable Target: N/A (Read operation))
  2. Action: Send `GET /api/coupons` with headers [Authorization: Bearer <VALID_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)` and HTTP status `200 OK (Inferred from SUT / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Zero state modification.
  5. Cleanup Step: None.

---

### FR12-AI-029

- **Coverage ID:** `COV-FR12-21`
- **Method:** `POST`
- **Endpoint:** `/api/products`
- **Caller Type:** Anonymous Caller
- **JWT State:** No Authorization header present
- **Role:** `None`
- **One-sentence Test Condition:** Anonymous caller calls POST /api/products with product payload
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Catalog mutation requires valid JWT authentication)
- **Expected HTTP Status + Classification:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response must reject creation and not return created ID.
- **Unauthorized Side-Effect Assertion:** Product 'AnonProduct_23127027' is NOT added to database (probed via GET /api/products).
- **Setup / Disposable Resource:** Prepare creation payload without Authorization header. | Resource: Product name 'AnonProduct_23127027'
- **Cleanup:** If defect CAND-FR12-02 allows insertion, delete created product via admin credentials.
- **Any Exact Response Body Assertion:** Request headers: `Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "AnonProduct_23127027",   "price": 150000,   "description": "Anonymous creation probe",   "imageUrl": "",   "category_id": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-030

- **Coverage ID:** `COV-FR12-24`
- **Method:** `PUT`
- **Endpoint:** `/api/products/:id`
- **Caller Type:** Anonymous Caller
- **JWT State:** No Authorization header present
- **Role:** `None`
- **One-sentence Test Condition:** Anonymous caller calls PUT /api/products/:id on disposable product
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Product update requires valid JWT authentication)
- **Expected HTTP Status + Classification:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response must reject update request.
- **Unauthorized Side-Effect Assertion:** Product attributes in database remain unchanged (GET /api/products/:id verifies original price 200,000).
- **Setup / Disposable Resource:** Create disposable product via admin credentials. | Resource: Disposable product ID <DISP_PRODUCT_ID> (Original Price: 200,000)
- **Cleanup:** Delete disposable product after test.
- **Any Exact Response Body Assertion:** Request headers: `Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "AnonTamperedName",   "price": 10,   "description": "Anon update probe",   "imageUrl": "",   "category_id": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-031

- **Coverage ID:** `COV-FR12-27`
- **Method:** `DELETE`
- **Endpoint:** `/api/products/:id`
- **Caller Type:** Anonymous Caller
- **JWT State:** No Authorization header present
- **Role:** `None`
- **One-sentence Test Condition:** Anonymous caller calls DELETE /api/products/:id on disposable product
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Product deletion requires valid JWT authentication)
- **Expected HTTP Status + Classification:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response must reject deletion request.
- **Unauthorized Side-Effect Assertion:** Product continues to exist in database (GET /api/products/:id returns product details).
- **Setup / Disposable Resource:** Create disposable product via admin credentials. | Resource: Disposable product ID <DISP_PRODUCT_ID>
- **Cleanup:** Delete disposable product via admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-032

- **Coverage ID:** `COV-FR12-01`
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Caller Type:** Anonymous Caller
- **JWT State:** No Authorization header present
- **Role:** `None`
- **One-sentence Test Condition:** Anonymous caller calls GET /api/admin/users
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Admin API requires valid JWT authentication)
- **Expected HTTP Status + Classification:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response payload must not expose user account directory records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** None. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-033

- **Coverage ID:** `COV-FR12-29`
- **Method:** `POST`
- **Endpoint:** `/api/categories`
- **Caller Type:** Anonymous Caller
- **JWT State:** No Authorization header present
- **Role:** `None`
- **One-sentence Test Condition:** Anonymous caller calls POST /api/categories without token
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Category creation requires valid JWT authentication)
- **Expected HTTP Status + Classification:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response must reject category creation.
- **Unauthorized Side-Effect Assertion:** Category is NOT added to database (probed via GET /api/categories).
- **Setup / Disposable Resource:** Prepare creation payload without Authorization header. | Resource: Category name 'AnonCategory_23127027'
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "name": "AnonCategory_23127027" }`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-034

- **Coverage ID:** `COV-FR12-14`
- **Method:** `GET`
- **Endpoint:** `/api/coupons`
- **Caller Type:** Anonymous Caller
- **JWT State:** No Authorization header present
- **Role:** `None`
- **One-sentence Test Condition:** Anonymous caller calls GET /api/coupons without token
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Coupon overview requires valid JWT authentication)
- **Expected HTTP Status + Classification:** `401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response must not return list of discount coupons.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** None. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET

---

### FR12-AI-035

- **Coverage ID:** `COV-FR12-35`
- **Method:** `GET`
- **Endpoint:** `/api/admin/users`
- **Caller Type:** Expired Admin Token Caller
- **JWT State:** Expired JWT (exp claim in the past)
- **Role:** `admin`
- **One-sentence Test Condition:** Expired admin token (exp < now) sent to GET /api/admin/users
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Expired token fails cryptographic verification)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response payload must not expose user directory records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** Generate expired admin token using test signing script. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <EXPIRED_ADMIN_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Generate expired admin token using test signing script. (Disposable Target: N/A (Read operation))
  2. Action: Send `GET /api/admin/users` with headers [Authorization: Bearer <EXPIRED_ADMIN_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-02 Violation: Expired token fails cryptographic verification)` and HTTP status `403 Forbidden (Inferred from SUT middleware / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Zero state modification.
  5. Cleanup Step: None.

---

### FR12-AI-036

- **Coverage ID:** `COV-FR12-36`
- **Method:** `GET`
- **Endpoint:** `/api/admin/orders`
- **Caller Type:** Forged Signature Token Caller
- **JWT State:** Signature chunk altered / invalid cryptographic HMAC
- **Role:** `admin (claimed in payload)`
- **One-sentence Test Condition:** Forged signature token sent to GET /api/admin/orders
- **Official Requirement / SEC:** `SEC-02` (FR-12 Lines 174–180; SEC-02 Line 279)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-02 Violation: Forged signature fails cryptographic integrity check)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred from SUT middleware / Unspecified in spec)`
- **Expected Response Exposure Assertion:** Response payload must not expose order records.
- **Unauthorized Side-Effect Assertion:** Zero state modification.
- **Setup / Disposable Resource:** Construct token with altered signature chunk. | Resource: N/A (Read operation)
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <FORGED_SIGNATURE_TOKEN>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Construct token with altered signature chunk. (Disposable Target: N/A (Read operation))
  2. Action: Send `GET /api/admin/orders` with headers [Authorization: Bearer <FORGED_SIGNATURE_TOKEN>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-02 Violation: Forged signature fails cryptographic integrity check)` and HTTP status `403 Forbidden (Inferred from SUT middleware / Unspecified in spec)`.
  4. Verification Step 2 (Side-Effect Invariance): Zero state modification.
  5. Cleanup Step: None.

---

### FR12-AI-037

- **Coverage ID:** `COV-FR12-37`
- **Method:** `POST`
- **Endpoint:** `/api/admin/coupons`
- **Caller Type:** Missing Role Claim Token Caller
- **JWT State:** Valid signature, but payload contains no role field ({ id: 10 })
- **Role:** `None (Omitted claim)`
- **One-sentence Test Condition:** Valid JWT omitting 'role' claim sent to POST /api/admin/coupons
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Missing role claim does not satisfy role === 'admin')
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject coupon creation.
- **Unauthorized Side-Effect Assertion:** Coupon 'NOROLE_CPN_23127027' is NOT created in database.
- **Setup / Disposable Resource:** Generate custom signed token omitting role claim. | Resource: Coupon code 'NOROLE_CPN_23127027'
- **Cleanup:** None.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <TOKEN_WITHOUT_ROLE_CLAIM>; Content-Type: application/json; X-Student-Id: 23127027`; Request body: `{   "code": "NOROLE_CPN_23127027",   "type": "fixed",   "discount_value": 10000,   "min_order_amount": 50000,   "expired_at": "2099-12-31",   "max_uses_per_user": 1 }`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Generate custom signed token omitting role claim. (Disposable Target: Coupon code 'NOROLE_CPN_23127027')
  2. Action: Send `POST /api/admin/coupons` with headers [Authorization: Bearer <TOKEN_WITHOUT_ROLE_CLAIM>; Content-Type: application/json; X-Student-Id: 23127027] and body: `{   "code": "NOROLE_CPN_23127027",   "type": "fixed",   "discount_value": 10000,   "min_order_amount": 50000,   "expired_at": "2099-12-31",   "max_uses_per_user": 1 }`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Missing role claim does not satisfy role === 'admin')` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Coupon 'NOROLE_CPN_23127027' is NOT created in database.
  5. Cleanup Step: None.

---

### FR12-AI-038

- **Coverage ID:** `COV-FR12-38`
- **Method:** `DELETE`
- **Endpoint:** `/api/admin/users/:id`
- **Caller Type:** Tampered / Spoofed Role Caller
- **JWT State:** Valid signature, but payload contains spoofed role ('ADMIN' uppercase or 'manager')
- **Role:** `ADMIN (Uppercase)`
- **One-sentence Test Condition:** Token with uppercase role: 'ADMIN' sent to DELETE /api/admin/users/:id
- **Official Requirement / SEC:** `SEC-03` (FR-12 Lines 174–180; SEC-03 Line 280)
- **Oracle Classification:** Semantic Denial/Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec
- **Expected Access-Control Semantic Outcome:** ACCESS DENIED (SEC-03 Violation: Strict exact-match role === 'admin' required; uppercase or spoofed role rejected)
- **Expected HTTP Status + Classification:** `403 Forbidden (Inferred) / UNKNOWN by official specification`
- **Expected Response Exposure Assertion:** Response must reject user deletion.
- **Unauthorized Side-Effect Assertion:** Target disposable user is NOT deleted from database (verified via login probe).
- **Setup / Disposable Resource:** Create disposable test user; sign custom token with role: 'ADMIN'. | Resource: Disposable test user ID <TARGET_USER_ID>
- **Cleanup:** Clean up disposable test user via official admin credentials after test.
- **Any Exact Response Body Assertion:** Request headers: `Authorization: Bearer <TOKEN_UPPERCASE_ROLE>; X-Student-Id: 23127027`; Request body: `None`
- **Original Automation Status:** NOT AUTOMATED YET
- **Detailed High-Risk Test Steps:**
  1. Setup / Precondition: Create disposable test user; sign custom token with role: 'ADMIN'. (Disposable Target: Disposable test user ID <TARGET_USER_ID>)
  2. Action: Send `DELETE /api/admin/users/:id` with headers [Authorization: Bearer <TOKEN_UPPERCASE_ROLE>; X-Student-Id: 23127027] and body: `None`
  3. Verification Step 1 (Response): Assert semantic outcome `ACCESS DENIED (SEC-03 Violation: Strict exact-match role === 'admin' required; uppercase or spoofed role rejected)` and HTTP status `403 Forbidden (Inferred) / UNKNOWN by official specification`.
  4. Verification Step 2 (Side-Effect Invariance): Target disposable user is NOT deleted from database (verified via login probe).
  5. Cleanup Step: Clean up disposable test user via official admin credentials after test.

---
