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

| Caller State | Required Semantic Outcome | HTTP Status Code | Status Classification | Grounded Contract Source |
| :--- | :--- | :---: | :---: | :--- |
| **Anonymous (Missing Header)** | Access rejected; zero data exposed; zero state mutation | `401 Unauthorized` | **IMPLEMENTATION-OBSERVED / INFERRED** | Semantic denial required by `SEC-02` (`README.md` L279); exact 401 code defined in SUT middleware (`server.js` L103). |
| **Malformed / Forged / Expired Token** | Access rejected; cryptographic verification failed | `403 Forbidden` | **IMPLEMENTATION-OBSERVED / INFERRED** | Semantic denial required by `SEC-02`; exact 403 code defined in SUT middleware (`server.js` L106). |
| **Authenticated Standard User (`role: 'user'`)** | Access denied; non-admin prohibited from admin operations | `403 Forbidden` (Convention) / `UNKNOWN` by spec | **UNSPECIFIED BY SPECIFICATION / CONVENTIONAL INFERENCE** | Semantic denial explicitly mandated by `SEC-03` (`README.md` L280) and `FR-12` (L176–180); exact HTTP status code is unspecified in contract. |
| **Authenticated Administrator (`role: 'admin'`)** | Access granted; administrative operation permitted to execute | `200 OK` / `201 Created` | **SPECIFIED / STANDARD SUCCESS** | Standard REST success response for authorized operations. |

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
| **`CAND-FR12-01`** | `GET/DELETE /api/admin/users`<br>`GET/PUT /api/admin/orders`<br>`POST /api/admin/import-products`<br>`POST/DELETE /api/admin/coupons`<br>`GET /api/coupons` | Missing Admin Role Authorization Check | `SEC-03` (`README.md` L280)<br>`FR-12` (`README.md` L179) | Routes utilize `authenticateToken` but perform zero inspection of `req.user.role === 'admin'`, potentially allowing standard users (`role: 'user'`) to perform admin actions. |
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
