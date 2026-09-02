# FR-12: Access Control (Kiểm soát truy cập) — Specification Analysis (Calibrated)

> **Specification Analysis Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Primary Contract Specifications:**
>   - `README.md`: Section 6 (Phân hệ Web Admin, FR-12 Lines 174–180), Section 9 (Yêu cầu Bảo mật, SEC-02 Line 279, SEC-03 Line 280)
>   - `api_specification.md`: Section 5.2 (Coupon Admin List Lines 165–168), Section 6 (API Dành cho Admin Lines 171–215), Section 3.3–3.4 (Product & Category Mutation Lines 87–107)
> - **SUT Implementation Awareness:** `backend/server.js` (Inspected strictly for endpoint routing, middleware structure, and static defect candidate context).

---

## 1. Verified Role Model & SUT Identity Definitions

Source code inspection of `backend/database.js` (Lines 50–61, 90–95) and `backend/server.js` (Lines 20–55) confirms the exact role values:

| Subject Identity | Role Value | Database Definition | Login / JWT Sign-in | Notes |
| :--- | :---: | :--- | :--- | :--- |
| **Standard User** | **`"user"`** | `role TEXT DEFAULT 'user'` (`database.js` L55) | `jwt.sign({ id: user.id, role: user.role })` (`server.js` L51) | Default role assigned upon registration; seeded as `test@eshop.com` with `role: 'user'` |
| **System Administrator** | **`"admin"`** | Seeded explicitly (`database.js` L92) | `jwt.sign({ id: user.id, role: 'admin' })` | Administrative role; seeded as `admin@eshop.com` with `role: 'admin'` |

> [!IMPORTANT]
> **AI Correction Note:** The initial draft used the label `role = 'customer'`. Source code verification confirms the system strictly uses `role = 'user'`. All specifications, coverage matrices, and test cases are strictly calibrated to use `role = 'user'` (standard-user token).

---

## 2. Coupon Route Reconciliation & Truth Table

A reconciliation between `README.md`, `api_specification.md`, and `backend/server.js` was conducted to resolve endpoint scope:

| Route URI | HTTP Method | In API Spec? | In SUT? | FR-12 Admin Rule? | Include in FR-12? | Classification / Resolution |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `/api/coupons` | `GET` | **Yes** (L166) | **Yes** (L356) | **Yes** (L165) | **YES** | `api_specification.md` Section 5.2 explicitly labels this *"Lấy danh sách mã giảm giá (Dành cho Admin)"* with `Authorization: Bearer <token>`. Included as Target Operation #14. |
| `/api/admin/coupons` | `POST` | **Yes** (L202) | **Yes** (L457) | **Yes** (L177) | **YES** | Official admin coupon creation endpoint. Target Operation #6. |
| `/api/admin/coupons/:id` | `DELETE` | **Yes** (L214) | **Yes** (L483) | **Yes** (L177) | **YES** | Official admin coupon deletion endpoint. Target Operation #7. |
| `/api/coupons` | `POST` | No | No | Mentioned | **NO** | `README.md` Line 177 mentions `POST/PUT/DELETE /api/coupons` as a shorthand family reference. Route is non-exposed; classified as `SPECIFIED ACCESS-CONTROL RULE FOR A NON-EXPOSED ROUTE FAMILY`. No synthetic tests generated. |
| `/api/coupons/:id` | `PUT` | No | No | Mentioned | **NO** | Non-exposed route. Classified as `SPECIFIED ACCESS-CONTROL RULE FOR A NON-EXPOSED ROUTE FAMILY`. |
| `/api/coupons/:id` | `DELETE` | No | No | Mentioned | **NO** | Non-exposed route. Official deletion exists at `/api/admin/coupons/:id`. |
| `/api/apply-coupon` | `POST` | **Yes** (L154) | **Yes** (L363) | No | **NO** | Public/customer checkout promotional discount application. Belongs to FR-08, not FR-12. |
| `/api/coupon-usage` | `POST` | No | **Yes** (L444) | No | **NO** | Internal user-level usage tracking endpoint. Not an administrative endpoint. |

---

## 3. Verified FR-12 Target Operations (Exact Count: 14 Operations)

Across the entire system, exactly **14 exposed operations** are subject to FR-12 access control requirements:

### Group A: Dedicated Administrative Endpoints (`/api/admin/*`) — 7 Operations
1. `GET /api/admin/users` — View all system user accounts (`api_spec` L176)
2. `DELETE /api/admin/users/:id` — Delete a specific user account (`api_spec` L177)
3. `GET /api/admin/orders` — View system-wide order history (`api_spec` L180)
4. `PUT /api/admin/orders/:id/status` — Update order fulfillment status (`api_spec` L181)
5. `POST /api/admin/import-products` — Bulk import product catalog (`api_spec` L185)
6. `POST /api/admin/coupons` — Create promotional coupon (`api_spec` L202)
7. `DELETE /api/admin/coupons/:id` — Delete promotional coupon (`api_spec` L214)

### Group B: Data-Mutating Catalog Endpoints — 6 Operations
8. `POST /api/products` — Create new product (`README.md` L177, `api_spec` L88)
9. `PUT /api/products/:id` — Update existing product (`README.md` L177, `api_spec` L89)
10. `DELETE /api/products/:id` — Delete product (`README.md` L177, `api_spec` L90)
11. `POST /api/categories` — Create category (`README.md` L177, `api_spec` L104)
12. `PUT /api/categories/:id` — Update category (`README.md` L177, `api_spec` L105)
13. `DELETE /api/categories/:id` — Delete category (`README.md` L177, `api_spec` L106)

### Group C: Admin Coupon Listing Endpoint — 1 Operation
14. `GET /api/coupons` — Admin coupon overview (`api_spec` Section 5.2 L165–168)

---

## 4. Semantic Contract vs. HTTP Status Oracle Policy

### 4.1 Global Caller State Matrix

| Caller State | Required Semantic Outcome | HTTP Status Code | Status Classification | Grounded Contract Source |
| :--- | :--- | :---: | :---: | :--- |
| **Anonymous (Missing Header)** | Access rejected; zero data exposed; zero state mutation | `401 Unauthorized` | **IMPLEMENTATION-OBSERVED / INFERRED** | Semantic denial required by `SEC-02` (`README.md` L279); exact 401 code defined in SUT middleware (`server.js` L103). |
| **Malformed / Forged / Expired Token** | Access rejected; cryptographic verification failed | `403 Forbidden` | **IMPLEMENTATION-OBSERVED / INFERRED** | Semantic denial required by `SEC-02`; exact 403 code defined in SUT middleware (`server.js` L106). |
| **Authenticated Standard User (`role: 'user'`)** | Access denied; non-admin prohibited from admin operations | `403 Forbidden` (Convention) / `UNKNOWN` by spec | **UNSPECIFIED BY SPECIFICATION / CONVENTIONAL INFERENCE** | Semantic denial explicitly mandated by `SEC-03` (`README.md` L280) and `FR-12` (L176–180); exact HTTP status code is unspecified in contract. |
| **Authenticated Administrator (`role: 'admin'`)** | Authorization layer permits request to reach functional handler | Endpoint-specific | **DECOUPLED (SEE TABLE 4.2)** | Access-control success means clearance through `SEC-02`/`SEC-03`; downstream HTTP code depends strictly on individual endpoint contract. |

---

### 4.2 Authorized Admin Success Status Oracles (Across All 14 FR-12 Target Operations)

> [!IMPORTANT]
> **Decoupling Access Control from REST Conventions:**
> Generic "200 OK / 201 Created" REST convention is **NOT** official contract evidence. The primary FR-12 positive admin oracle is:
> - **Primary Admin Access Assertion:** Request passes `SEC-02` (valid JWT) and `SEC-03` (role `admin`) and is **NOT rejected** by the authentication/authorization layer (i.e. does not return 401 or 403).
> - **Functional Status Assertion:** Evaluated strictly against what `api_specification.md` explicitly documents. Where no exact HTTP code is defined in official text, the status is classified as `INFERRED / IMPLEMENTATION-OBSERVED` (from Express `res.json` default 200) rather than a formal contract mandate.

| # | HTTP Method | Target Endpoint URI | Authorized Admin Semantic Outcome | Documented Success Status | Classification | Grounded Contract / Implementation Source |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| 1 | `GET` | `/api/admin/users` | Permitted to view system users | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L176 text; SUT executes `res.json(rows)` (`server.js` L498). |
| 2 | `DELETE` | `/api/admin/users/:id` | Permitted to delete target user | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L177 text; SUT executes `res.json(...)` (`server.js` L506). |
| 3 | `GET` | `/api/admin/orders` | Permitted to view all orders | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L180 text; SUT executes `res.json(orders)` (`server.js` L521). |
| 4 | `PUT` | `/api/admin/orders/:id/status` | Permitted to update order status | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L181 text; SUT executes `res.json(...)` (`server.js` L540). |
| 5 | `POST` | `/api/admin/import-products` | Permitted to import catalog | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L185 text; SUT executes `res.json(...)` (`server.js` L239). |
| 6 | `POST` | `/api/admin/coupons` | Permitted to create coupon | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L202 text; SUT executes `res.json(...)` (`server.js` L473). |
| 7 | `DELETE` | `/api/admin/coupons/:id` | Permitted to delete coupon | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L214 text; SUT executes `res.json(...)` (`server.js` L487). |
| 8 | `POST` | `/api/products` | Permitted to create product | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L88 text; SUT executes `res.json(...)` (`server.js` L174). |
| 9 | `PUT` | `/api/products/:id` | Permitted to update product | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L89 text; SUT executes `res.json(...)` (`server.js` L186). |
| 10 | `DELETE` | `/api/products/:id` | Permitted to delete product | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L90 text; SUT executes `res.json(...)` (`server.js` L194). |
| 11 | `POST` | `/api/categories` | Permitted to create category | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L104 text; SUT executes `res.json(...)` (`server.js` L253). |
| 12 | `PUT` | `/api/categories/:id` | Permitted to update category | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L105 text; SUT executes `res.json(...)` (`server.js` L264). |
| 13 | `DELETE` | `/api/categories/:id` | Permitted to delete category | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | Not explicitly numbered in `api_spec` L106 text; SUT executes `res.json(...)` (`server.js` L275). |
| 14 | `GET` | `/api/coupons` | Permitted to view all coupons | `200 OK` | **INFERRED / IMPLEMENTATION-OBSERVED** | `api_spec` L165–168 labels endpoint *"Dành cho Admin"*; SUT executes `res.json(rows)` (`server.js` L358). |

---

## 5. Scope Boundary: Access Control vs. Business Validation

FR-12 tests strictly evaluate **ACCESS CONTROL (WHO may invoke the endpoint)**:
- **In Scope for FR-12:**
  - Can unauthenticated callers invoke the API?
  - Can standard users (`role: 'user'`) access admin data or perform catalog mutations?
  - Does the admin user (`role: 'admin'`) have unhindered access to administrative capabilities?
  - Does the system reject expired, forged, or tampered role tokens?
- **Strictly Out of Scope for FR-12 (Excluded from Test Count):**
  - Validation of product price/name domain rules (FR-15 Product CRUD).
  - Validation of category name non-empty rules (FR-14 Category CRUD).
  - CSV rollback transactions and RFC 4180 parsing (FR-16 Import).
  - Coupon mathematical discount calculation and expiration dates (FR-17 Coupon CRUD).
  - Order status transition state machines (FR-18 Order Management).
  - Profile update role immutability (`SEC-06` / `PUT /api/users/me`).

---

## 6. Dual-Assertion Policy: Side-Effect Verification on Mutation

For all data-mutating endpoints (`POST`, `PUT`, `DELETE`), access-control denial assertions must enforce a **two-level validation oracle**:
1. **Response-Level Assertion:** HTTP response indicates controlled rejection (e.g. 401/403) and does not return success.
2. **State/Side-Effect Assertion:** The underlying system state is verified via an independent read operation (`GET`) to guarantee that **unauthorized side-effects did NOT occur**:
   - Unauthorized `DELETE /api/products/:id` $\implies$ followed by `GET /api/products/:id` verifying the item still exists.
   - Unauthorized `POST /api/products` $\implies$ followed by `GET /api/products` verifying the product was not inserted.
   - Unauthorized `DELETE /api/categories/:id` $\implies$ followed by `GET /api/categories` verifying the category still exists.
   - Unauthorized `PUT /api/admin/orders/:id/status` $\implies$ followed by `GET /api/admin/orders` verifying the status was not altered.
   - Unauthorized `DELETE /api/admin/users/:id` $\implies$ followed by login probe verifying the user was not deleted.

---

## 7. Valid Admin Test Safety: Disposable Test Data Policy

To avoid corrupting baseline assessment data:
- Admin test cases that perform mutations (`POST`, `PUT`, `DELETE`) must operate strictly on **disposable, newly created test entities**.
- **Forbidden Actions:** Test cases must **NEVER** modify or delete lecturer-seeded baseline data:
  - Users: `Admin User` (`admin@eshop.com`, ID 1), `Test User` (`test@eshop.com`, ID 2).
  - Products: IDs 1 to 5 (`iPhone 15 Pro Max`, `Samsung Galaxy S24 Ultra`, `MacBook Pro M3`, `Tai nghe AirPods Pro 2`, `Bàn phím cơ Keychron Q1`).
  - Coupons: `SAVE10`, `BIGBUY`, `VIP100`, `EXPIRED`.
  - Categories: IDs 1, 2, 3 (`Điện thoại`, `Laptop`, `Phụ kiện`).

---

## 8. Static-Analysis Defect Candidates (Awaiting Runtime Proof)

| Candidate ID | Target Operation(s) | Description | Governing Requirement | Static Observation in `backend/server.js` |
| :---: | :--- | :--- | :--- | :--- |
| **`CAND-FR12-01`** | `GET/DELETE /api/admin/users`<br>`GET/PUT /api/admin/orders`<br>`POST /api/admin/import-products`<br>`POST/DELETE /api/admin/coupons`<br>`GET /api/coupons` | Missing Admin Role Authorization Check | `SEC-03` (`README.md` L280)<br>`FR-12` (`README.md` L179) | Routes utilize `authenticateToken` but perform zero inspection of `req.user.role === 'admin'`: lines 199 (import), 457 (coupon POST), 483 (coupon DELETE), 494 (users GET), 504 (users DELETE), 510 (orders GET), 525 (order status PUT), and line 356 (`app.get("/api/coupons", authenticateToken, (req, res) => { ... })` Lines 356–360). Standard users (`role: 'user'`) can invoke all 8 admin endpoints. |
| **`CAND-FR12-02`** | `POST /api/products`<br>`PUT /api/products/:id`<br>`DELETE /api/products/:id` | Product Catalog Mutation Missing Authentication & Authorization | `SEC-02` (`README.md` L279)<br>`SEC-03` (`README.md` L280)<br>`FR-12` (`README.md` L177) | Endpoints have zero middleware attached (`server.js` Lines 167–195), allowing anonymous users to create, update, and delete catalog products. |
| **`CAND-FR12-03`** | `POST /api/categories`<br>`PUT /api/categories/:id`<br>`DELETE /api/categories/:id` | Category Mutation Missing Admin Role Authorization Check | `SEC-03` (`README.md` L280)<br>`FR-12` (`README.md` L177) | Endpoints attach `authenticateToken` but do NOT check `req.user.role === 'admin'` (`server.js` Lines 249–275), allowing standard users to modify product categories. |

---

## 9. Security Applicability Matrix (Strict README.md Section 9 Trace)

| Security Requirement ID | Official Specification Text | FR-12 Applicability | Justification & Test Policy |
| :--- | :--- | :---: | :--- |
| **`SEC-01`** | Mật khẩu không được lưu dưới dạng plaintext. | **NOT APPLICABLE** | Belongs to FR-01 Registration and database credential storage. |
| **`SEC-02`** | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ. | **DIRECTLY APPLICABLE** | All 14 FR-12 operations must require a cryptographically valid, unexpired JWT Bearer token. |
| **`SEC-03`** | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token. | **DIRECTLY APPLICABLE** | Core requirement of FR-12: all 14 operations must reject valid tokens belonging to standard users (`role: 'user'`). |
| **`SEC-04`** | Dữ liệu user nhập vào khi hiển thị trên UI phải được escape đúng cách. | **NOT APPLICABLE** | Frontend UI rendering requirement; out of scope for API testing. |
| **`SEC-05`** | Truy vấn CSDL phải dùng Parameterized Query. | **NOT APPLICABLE** | Database data-access layer security; out of scope for access control testing. |
| **`SEC-06`** | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client. | **EXCLUDED FROM FR-12** | Belongs specifically to user profile update (`PUT /api/users/me`). Excluded from FR-12 test count. |
| **`SEC-07`** | OTP đặt lại mật khẩu phải đủ entropy, có thời hạn và vô hiệu hóa sau khi dùng. | **NOT APPLICABLE** | Password recovery subsystem; out of scope. |

---

## 10. AI Error Register & Engineering Lessons

1. **Role Model Naming Discrepancy:** The initial draft used `role = "customer"` by habit. Source verification confirmed `backend/database.js` defines `role TEXT DEFAULT 'user'`. Corrected to `role = "user"` across all artifacts.
2. **Coupon Route Scope Inconsistency:** Initial matrix counted 13 operations and omitted `GET /api/coupons`. Reconciliation against `api_specification.md` Section 5.2 revealed `GET /api/coupons` is explicitly an admin overview endpoint, bringing the true operation count to exactly 14. Non-exposed shorthand routes (`POST/PUT/DELETE /api/coupons`) were correctly classified as non-exposed rather than generating synthetic tests.
3. **Category Mutation Defect Grouping:** Initial draft merged category mutation under generic admin candidates. Re-inspection confirmed `POST/PUT/DELETE /api/categories` requires its own isolated candidate (`CAND-FR12-03`).
4. **Decoupling Admin Access Clearance from REST Success Conventions:** Initial draft incorrectly labeled standard generic `200 OK / 201 Created` REST conventions as `SPECIFIED / STANDARD SUCCESS` across all operations. Corrected to decouple the access-control oracle (*"Request passes SEC-02/SEC-03 and is NOT blocked by authorization layer"*) from downstream functional status codes, which are classified as `INFERRED / IMPLEMENTATION-OBSERVED` based on SUT implementation evidence.

