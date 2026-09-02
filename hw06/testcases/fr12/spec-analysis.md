# FR-12: Access Control (Kiểm soát truy cập) — Specification Analysis

> **Specification Analysis Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Primary Specifications:**
>   - `README.md`: Section 6 (Phân hệ Web Admin, FR-12 Lines 174–180), Section 9 (Yêu cầu Bảo mật, SEC-02 Line 279, SEC-03 Line 280)
>   - `api_specification.md`: Section 6 (API Dành cho Admin Lines 171–215), Section 3.3–3.4 (Product & Category Mutation Lines 87–107)
> - **Implementation Awareness:** `backend/server.js` (Inspected solely for endpoint discovery, middleware structure, and static discrepancy context; implementation findings are static candidates, not ground-truth contracts).

---

## 1. Feature Overview & Scope

FR-12 governs role-based authorization and access control across the administrative interface and data-mutating APIs of the EShop system.

According to `README.md` (Lines 176–180):
- The Admin subsystem is strictly reserved for accounts having `role = 'admin'`.
- **All** Admin APIs (`/api/admin/*`) and all data-mutating APIs affecting system catalog and master data (`POST/PUT/DELETE /api/products`, `/api/categories`, `/api/coupons`) must strictly enforce two prerequisites:
  1. A cryptographically valid JWT Bearer token (`SEC-02`).
  2. The claim `role = 'admin'` embedded within the validated token payload (`SEC-03`).

### Scope Boundaries & Clarifications:
- **Core FR-12 Focus:** Authentication verification (`SEC-02`) and Role-based authorization enforcement (`SEC-03`) across administrative and mutation endpoints.
- **SEC-06 Distinction:** Requirement `SEC-06` (*"API cập nhật hồ sơ không được cho phép thay đổi trường role từ client"*) applies specifically to the user profile update endpoint (`PUT /api/users/me`) and is evaluated independently; it is **NOT** falsely counted toward core FR-12 access control coverage.
- **FR-10 Order State Workflow Distinction:** Admin order state updates (`PUT /api/admin/orders/:id/status`) are tested strictly for access control authorization (whether non-admin users or unauthenticated clients can invoke the endpoint), not for full business lifecycle transition permutations.

---

## 2. Target Endpoint Inventory for FR-12

The official specifications define the following protected endpoints subject to FR-12 enforcement:

### Group A: Dedicated Administrative Endpoints (`/api/admin/*`)
| HTTP Method | Endpoint URI | Description / Purpose | Required Role | Spec Source |
| :---: | :--- | :--- | :---: | :--- |
| `GET` | `/api/admin/users` | List all registered user accounts | `admin` | `api_specification.md` L176 |
| `DELETE` | `/api/admin/users/:id` | Delete a specific user account | `admin` | `api_specification.md` L177 |
| `GET` | `/api/admin/orders` | View all system-wide orders across all customers | `admin` | `api_specification.md` L180 |
| `PUT` | `/api/admin/orders/:id/status` | Update fulfillment status of an order | `admin` | `api_specification.md` L181 |
| `POST` | `/api/admin/import-products` | Bulk import catalog products from payload | `admin` | `api_specification.md` L185 |
| `POST` | `/api/admin/coupons` | Create new promotional discount coupon | `admin` | `api_specification.md` L202 |
| `DELETE` | `/api/admin/coupons/:id` | Delete promotional discount coupon | `admin` | `api_specification.md` L214 |

### Group B: Data-Mutating Administrative APIs Specified in FR-12
| HTTP Method | Endpoint URI | Description / Purpose | Required Role | Spec Source |
| :---: | :--- | :--- | :---: | :--- |
| `POST` | `/api/products` | Create a new catalog product | `admin` | `README.md` L177, `api_spec` L88 |
| `PUT` | `/api/products/:id` | Modify an existing catalog product | `admin` | `README.md` L177, `api_spec` L89 |
| `DELETE` | `/api/products/:id` | Remove a product from catalog | `admin` | `README.md` L177, `api_spec` L90 |
| `POST` | `/api/categories` | Create a new product category | `admin` | `README.md` L177, `api_spec` L104 |
| `PUT` | `/api/categories/:id` | Modify an existing category | `admin` | `README.md` L177, `api_spec` L105 |
| `DELETE` | `/api/categories/:id` | Delete a category | `admin` | `README.md` L177, `api_spec` L106 |

---

## 3. Authorization Matrix & Expected Access Control Outcomes

To ensure exhaustive test coverage without combinatorial explosion, FR-12 evaluates requests across 4 distinct subject identity states:

| Subject Identity State | Token Condition | Embedded Role | Expected Authorization Outcome | Expected Semantic Behavior |
| :--- | :--- | :---: | :---: | :--- |
| **State 0: Anonymous** | No `Authorization` header present | None | **DENIED (SEC-02)** | Unauthenticated request rejected; zero data exposure / zero mutation |
| **State 1: Malformed / Invalid Token** | Forged signature, malformed structure, expired token, or non-Bearer scheme | N/A | **DENIED (SEC-02)** | Invalid credentials rejected; zero data exposure / zero mutation |
| **State 2: Authenticated Customer** | Cryptographically valid JWT | `customer` | **DENIED (SEC-03)** | Authenticated non-admin user rejected; access restricted strictly to `role = 'admin'` |
| **State 3: Authenticated Admin** | Cryptographically valid JWT | `admin` | **AUTHORIZED** | Administrative access granted; operation executed successfully |

---

## 4. Equivalence Partitioning (EP) & Boundary Value Analysis (BVA)

### Partition Dimension 1: Authentication Credential State (SEC-02)
- **EP-AUTH-01 (Valid Admin Token):** Valid JWT, signed by SUT, not expired, `role: "admin"`. $\implies$ Authorized.
- **EP-AUTH-02 (Missing Token):** Request omits `Authorization` header entirely. $\implies$ Rejected (HTTP 401 inferred).
- **EP-AUTH-03 (Forged Signature):** Valid JWT structure, but cryptographic signature manipulated. $\implies$ Rejected (HTTP 403 inferred).
- **EP-AUTH-04 (Malformed Token / Wrong Scheme):** Header contains `Basic ...`, raw token without `Bearer `, or corrupted base64 chunks. $\implies$ Rejected.
- **EP-AUTH-05 (Expired Token):** Legitimate signature, but `exp` claim is in the past. $\implies$ Rejected.

### Partition Dimension 2: Role Authorization Invariant (SEC-03)
- **EP-ROLE-01 (Admin Role):** `role === "admin"`. $\implies$ Access Granted.
- **EP-ROLE-02 (Customer Role):** Valid token, but `role === "customer"`. $\implies$ Access Denied (HTTP 403 inferred / UNKNOWN by spec).
- **EP-ROLE-03 (Empty / Missing Role Claim):** Valid token payload `{ id: 10 }` without `role` claim. $\implies$ Access Denied.
- **EP-ROLE-04 (Arbitrary / Elevated Spoofed Role):** Valid token with `role === "superadmin"`, `"manager"`, or `"root"`. $\implies$ Access Denied (system only recognizes `'admin'`).
- **EP-ROLE-05 (Case Sensitivity):** Valid token with `role === "ADMIN"`, `"Admin"`. $\implies$ Access Denied (exact case match required).

### Partition Dimension 3: Target Resource & HTTP Verb Mutation
- **EP-RES-01 (Admin User Management):** `GET /api/admin/users`, `DELETE /api/admin/users/:id`.
- **EP-RES-02 (Admin Order Management):** `GET /api/admin/orders`, `PUT /api/admin/orders/:id/status`.
- **EP-RES-03 (Admin Bulk Import):** `POST /api/admin/import-products`.
- **EP-RES-04 (Admin Coupon Management):** `POST /api/admin/coupons`, `DELETE /api/admin/coupons/:id`.
- **EP-RES-05 (Product Catalog Mutation):** `POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id`.
- **EP-RES-06 (Category Mutation):** `POST /api/categories`, `PUT /api/categories/:id`, `DELETE /api/categories/:id`.

---

## 5. Security Applicability Matrix (Strict Alignment with README.md)

| ID | Official Requirement Text | Applicability to FR-12 | Grounded Interpretation & Test Policy |
| :--- | :--- | :---: | :--- |
| **`SEC-01`** | Mật khẩu không được lưu dưới dạng plaintext. | **NOT APPLICABLE** | Belongs to FR-01 Registration and database credential storage. |
| **`SEC-02`** | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ. | **APPLICABLE (Direct)** | **Mandatory:** Every admin and mutating endpoint must reject unauthenticated, forged, or malformed requests. |
| **`SEC-03`** | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token. | **APPLICABLE (Core)** | **Central Requirement:** Admin endpoints must reject valid customer tokens (`role = 'customer'`). Mere token existence is strictly insufficient. |
| **`SEC-04`** | Dữ liệu user nhập vào khi hiển thị trên UI phải được escape đúng cách. | **NOT APPLICABLE** | Client UI rendering requirement; out of scope for backend API testing. |
| **`SEC-05`** | Truy vấn CSDL phải dùng Parameterized Query. | **NOT APPLICABLE** | SQL injection robustness / data access layer. |
| **`SEC-06`** | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client. | **EXCLUDED FROM FR-12 CORE** | Belongs strictly to `PUT /api/users/me` profile update. Documented to prevent false coverage inflation of FR-12. |
| **`SEC-07`** | OTP đặt lại mật khẩu phải đủ entropy, có thời hạn và vô hiệu hóa sau khi dùng. | **NOT APPLICABLE** | Password recovery subsystem; out of scope. |

---

## 6. Specification Contradictions, Discrepancies & Ambiguities

1. **Exact HTTP Rejection Status Code:**
   - Standard REST conventions map missing/malformed authentication to `401 Unauthorized` and authenticated but insufficient privileges to `403 Forbidden`.
   - However, neither `README.md` nor `api_specification.md` explicitly specifies the exact HTTP status codes for non-admin rejection.
   - **Grounded Oracle Policy:** The primary specified oracle is **Semantic Access Denial** (no data returned, zero mutation executed, controlled response). Expected HTTP status is documented as `401 / 403 (INFERRED)` or `UNKNOWN by official specification`.

2. **Public vs. Protected Product Mutation (`/api/products`):**
   - `README.md` Line 177 explicitly includes `POST/PUT/DELETE /api/products` as mutating APIs requiring `role = 'admin'`.
   - `api_specification.md` Section 3.3 headings state: *"3.3 Thêm / Sửa / Xóa Sản phẩm (Dành cho Admin)"*.
   - However, static inspection of `backend/server.js` reveals that `POST /api/products`, `PUT /api/products/:id`, and `DELETE /api/products/:id` currently have **zero middleware attached** (completely open).
   - **Testing Stance:** `README.md` and `api_specification.md` are the governing authority. Test cases will probe these endpoints to confirm whether unauthorized customers or anonymous users can modify the product catalog, treating any unauthorized mutation as a potential defect candidate.

3. **Admin Endpoints Role Verification Implementation Gap:**
   - In `backend/server.js`, `/api/admin/*` endpoints use `authenticateToken` but do NOT check `req.user.role === 'admin'`.
   - **Testing Stance:** This represents a primary candidate defect for `SEC-03` violation, pending runtime execution confirmation.

---

## 7. Static Candidate Defects Identified for Runtime Verification

| Candidate ID | Target Endpoint(s) | Description | Governing Requirement |
| :---: | :--- | :--- | :--- |
| **`CAND-FR12-01`** | `GET/DELETE /api/admin/users`, `GET/PUT /api/admin/orders`, `POST /api/admin/import-products`, `POST/DELETE /api/admin/coupons` | Server checks token existence via `authenticateToken` but fails to check `req.user.role === 'admin'`, allowing customer tokens to perform admin actions. | `SEC-03` (`README.md` Line 280), `FR-12` Line 179 |
| **`CAND-FR12-02`** | `POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id` | Catalog mutation endpoints have zero authentication middleware, allowing anonymous users to create, modify, and delete products. | `SEC-02` / `SEC-03` (`README.md` Line 177) |

*(Note: Per anti-cheat rules, these findings remain static candidates and will only be promoted to confirmed defects upon runtime execution proof).*
