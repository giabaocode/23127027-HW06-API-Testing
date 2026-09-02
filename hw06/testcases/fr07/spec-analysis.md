# FR-07: Shopping Cart — Specification Analysis (Audited & Grounded Version)

> **Document Information:**
> - **Feature ID:** Pool B — `FR-07` (Shopping Cart)
> - **Target Endpoints:** `GET /api/cart`, `POST /api/cart`
> - **Associated Prerequisites:** `POST /api/login`, `POST /api/register` (for authentic JWT tokens)
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Primary Specifications:**
>   - [`api_specification.md`](file:///Users/phamngocgiabao/eshop-sut/api_specification.md) (Section 4.1 & 4.2)
>   - [`README.md`](file:///Users/phamngocgiabao/eshop-sut/README.md) (Section 3 Product Detail, Section 4.1 Shopping Cart, Section 9 Security)

---

## 1. Feature Identification & Scope

FR-07 defines the shopping cart service for the EShop application, allowing authenticated customers to view their current cart selection and add prospective purchases.

### Primary Functional Contracts
1. **Cart Retrieval (`GET /api/cart`):**
   - Retrieves the collection of items currently selected by the authenticated user.
2. **Cart Item Insertion (`POST /api/cart`):**
   - Submits a product selection to be appended or merged into the user's cart.
3. **Item Accumulation / Deduplication Rule (`README.md` Line 96):**
   - *"Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới."*
   - Re-adding the same product item must increment the existing item's quantity rather than creating duplicate entries.
4. **Quantity Domain Constraint (`README.md` Line 86):**
   - *"Có ô nhập Số lượng (chỉ nhận số nguyên dương, tối thiểu là 1)."*
   - Quantity must strictly be a positive integer ($\ge 1$).

---

## 2. Authentication Contract & Status Derivation

| Rule / Requirement | Official Source Evidence | Contract Classification | Exact HTTP Status Classification |
| :--- | :--- | :---: | :---: |
| **Authentication Barrier Required** | `api_specification.md` L112: `*Yêu cầu Header: Authorization: Bearer <token>*`<br>`README.md` L279 (`SEC-02`): *"Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ."* | **`SPECIFIED`** | — |
| **Missing Token Rejection** | Undocumented in text (middleware enforces `401 Unauthorized`) | **`INFERRED`** (Rejection required by `SEC-02`) | **`INFERRED FROM MIDDLEWARE`** (`401` observed) |
| **Invalid / Forged Token Rejection** | Undocumented in text (middleware enforces `403 Forbidden`) | **`INFERRED`** (Rejection required by `SEC-02`) | **`INFERRED FROM MIDDLEWARE`** (`403` observed) |
| **Expired Token Rejection** | Undocumented in text (middleware enforces `403 Forbidden`) | **`INFERRED`** (Rejection required by `SEC-02`) | **`INFERRED FROM MIDDLEWARE`** (`403` observed) |

> [!IMPORTANT]
> The requirement to authenticate via `Authorization: Bearer <token>` is **`SPECIFIED`** by `api_specification.md` Line 112 and **`SEC-02`**. However, the exact HTTP status codes (`401` vs `403` vs `400`) are not explicitly defined in the API contract text and are classified as **`INFERRED FROM MIDDLEWARE`**.

---

## 3. Parameter Specification Matrix & Source Grounding

| Location | Parameter / Field | Formal Type | Required? | Domain Constraints | Source Evidence | Status Classification |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **Header** | `Authorization` | `string` | **Yes** | `Bearer <JWT_TOKEN>` | `api_specification.md` L112, `SEC-02` | **`SPECIFIED`** |
| **Header** | `Content-Type` | `string` | **Yes** | `application/json` for `POST /api/cart` | `api_specification.md` L119 | **`INFERRED FROM SPEC`** |
| **Header** | `X-Student-Id` | `string` | **Yes** | `23127027` | Course Policy / HW06 Rules | **`SPECIFIED (COURSE RULE)`** |
| **POST Body** | `id` | `integer` | Inferred | Product identifier | `api_specification.md` L122 (`"id": 1` in example) | **`INFERRED FROM EXAMPLE`** |
| **POST Body** | `name` | `string` | Inferred | Product display name | `api_specification.md` L123 (`"name": "Sản phẩm A"`) | **`INFERRED FROM EXAMPLE`** |
| **POST Body** | `price` | `number` | Inferred | Unit price in VND | `api_specification.md` L124 (`"price": 100000`) | **`INFERRED FROM EXAMPLE`** |
| **POST Body** | `quantity` | `integer` | **Yes** | Positive integer $\ge 1$ | `README.md` L86 (*"chỉ nhận số nguyên dương, tối thiểu là 1"*) | **`SPECIFIED`** |

### Resolution of Price Rule Contradiction
- In `README.md` Line 196, the rule *"Giá: bắt buộc, phải là số dương (> 0)"* belongs strictly to **`FR-15: Quản lý Sản phẩm (Product CRUD - Admin)`**, NOT FR-07.
- In FR-07, `price` is **NOT** a specified business rule with positive boundary checks; it appears solely in the JSON example (`api_specification.md` L124).
- Testing negative price or price tampering in `POST /api/cart` is therefore classified as a **`ROBUSTNESS / SECURITY PROBE`**, NOT a specified FR-07 contract violation.
- Note: `README.md` Line 107 (*"Backend phải tự tính lại tổng tiền..."*) applies to Checkout (`FR-08`), not cart addition.

---

## 4. Quantity Domain & Boundary Analysis

The quantity domain is formally governed by `README.md` Line 86 (*"chỉ nhận số nguyên dương, tối thiểu là 1"*):

| Test Value | Category | Boundary Type | Expected Semantic Oracle | Classification |
| :---: | :--- | :--- | :--- | :---: |
| **$q = 1$** | Valid Positive Integer | **Exact Minimum Boundary** | Accepted into cart with quantity 1 | **`SPECIFIED`** |
| **$q = 2$** | Valid Positive Integer | **Min + 1 (Typical Small)** | Accepted into cart with quantity 2 | **`SPECIFIED`** |
| **$q = 0$** | Invalid Integer | **Min - 1 Boundary** | Rejected per positive integer rule ($\ge 1$) | **`SPECIFIED REJECTION`** |
| **$q = -1$** | Invalid Negative Integer | **Negative Boundary** | Rejected per positive integer rule | **`SPECIFIED REJECTION`** |
| **$q = 1.5$** | Invalid Decimal Float | **Fractional Boundary** | Rejected per integer constraint | **`SPECIFIED REJECTION`** |
| **$q = "2"$** | String Numeric Integer | Type Violation / Coercion | Non-integer JSON type; probe parser coercion vs strict rejection | **`TYPE ROBUSTNESS / CHARACTERIZATION`** |
| **$q = \text{"abc"}$** | Non-Numeric String | Invalid Type | Rejected per integer constraint | **`INFERRED REJECTION`** |
| **$q = 10^9$** | Extreme Large Integer | **Unknown Upper Bound** | Server handles large integer without crash | **`ROBUSTNESS / UNKNOWN UPPER BOUND`** |

---

## 5. Storage Architecture, User Isolation & Empty Cart Contract

### Storage Architecture: In-Memory Storage
In `backend/server.js` (Line 14, 284–295), cart state is held in memory (`const userCarts = {};`).
- **Official Evaluation:** Neither `api_specification.md` nor `README.md` explicitly mandates SQLite database persistence or persistence across server restarts for the shopping cart.
- **Classification:** **`IMPLEMENTATION DETAIL — NOT A REQUIREMENT`**.
- **Operational Risk:** Cart state is volatile and destroyed upon server process termination. While an operational limitation, this does not violate any written specification contract.

### User Cart Isolation
- `README.md` does not contain explicit textual wording stating "Each user has an isolated cart".
- Rather, user isolation is derived from per-user Bearer authentication (`api_specification.md` L112) and `SEC-02`.
- **Classification:** **`INFERRED FROM AUTHENTICATED-USER CART SEMANTICS & SEC-02`**.

### Empty Cart Contract
- `README.md` Line 100 specifies UI behavior (*"Giỏ hàng trống phải có hình minh họa và thông báo rõ ràng"*).
- The exact API response `[]` is **`INFERRED FROM REST CONVENTIONS & IMPLEMENTATION-OBSERVED`** (not `SPECIFIED`).

---

## 6. Response Contract & Schema Analysis

### `GET /api/cart`
- **Success Status:** `200 OK` (**`INFERRED`**)
- **Empty Cart Response:** `[]` (**`INFERRED / IMPLEMENTATION-OBSERVED`**)
- **Populated Cart Response:** Array of objects `[ { id, name, price, quantity }, ... ]` (**`INFERRED FROM POST EXAMPLE`**)
- **Error Status:** `401 Unauthorized` (missing token), `403 Forbidden` (invalid token) (**`INFERRED FROM MIDDLEWARE`**)

### `POST /api/cart`
- **Success Status:** `200 OK` (**`INFERRED`**)
- **Success Response Body:** `{"message": "Added to cart"}` (**`IMPLEMENTATION-OBSERVED`**; exact string is not specified, any controlled success response is valid)
- **Error Status:** `401 / 403` for auth failures (**`INFERRED FROM MIDDLEWARE`**); validation error codes are **`UNKNOWN`**.

---

## 7. Security Requirements Applicability Matrix

Evaluation against the **authentic `SEC-01` through `SEC-07` definitions** (`README.md` Lines 276–285):

| Requirement ID | Exact Official Definition (`README.md` L276–285) | Applicability to FR-07 | Justification & Test Layer Relevance |
| :---: | :--- | :---: | :--- |
| **`SEC-01`** | Mật khẩu **không** được lưu dưới dạng plaintext. | **NOT APPLICABLE** | FR-07 handles cart items; zero password manipulation occurs. |
| **`SEC-02`** | Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ. | **DIRECTLY APPLICABLE** | `GET /api/cart` and `POST /api/cart` require valid JWT Bearer token; rejects missing/invalid tokens. |
| **`SEC-03`** | API Admin phải kiểm tra `role = 'admin'` trong Token, không chỉ kiểm tra sự tồn tại của Token. | **NOT APPLICABLE** | Cart endpoints are customer-facing APIs, not admin management endpoints. |
| **`SEC-04`** | Mọi dữ liệu từ user nhập vào khi hiển thị trên UI phải được escape đúng cách, không dùng `innerHTML` trực tiếp. | **NOT APPLICABLE TO API LAYER** | Applies to frontend UI HTML/DOM rendering; API layer transmits raw JSON payloads. |
| **`SEC-05`** | Truy vấn CSDL phải dùng Parameterized Query, không nối chuỗi trực tiếp. | **NOT APPLICABLE TO CURRENT FR-07 EXECUTION PATH** | In current SUT, cart operations mutate in-memory `userCarts = {}`, zero SQL queries are executed. |
| **`SEC-06`** | API cập nhật hồ sơ không được cho phép thay đổi trường `role` từ client. | **NOT APPLICABLE** | Specific to profile update (`PUT /api/profile`). |
| **`SEC-07`** | OTP đặt lại mật khẩu phải đủ entropy (tối thiểu 6 chữ số), có thời hạn và vô hiệu hóa sau khi dùng. | **NOT APPLICABLE** | Specific to password reset flow (`POST /api/forgot-password`). |

---

## 8. Cart State & Transition Model

```text
[State 0: Unauthenticated]
       │
       ▼ (Authenticate via JWT per SEC-02)
[State 1: Empty Cart] ───────────► GET /api/cart returns [] [INFERRED]
       │
       ▼ (POST /api/cart: Product A, quantity q1)
[State 2: Single-Item Cart] ─────► GET /api/cart returns [{ id: A, quantity: q1 }] [INFERRED]
       │
       ├──────────────────────────────────────────────┐
       ▼ (POST /api/cart: Product A, quantity q2)     ▼ (POST /api/cart: Product B, quantity q3)
[State 3: Accumulated Cart]                    [State 4: Multi-Item Heterogeneous Cart]
GET returns [{ id: A, quantity: q1 + q2 }]     GET returns [{ id: A, q1 }, { id: B, q3 }]
[SPECIFIED BUSINESS RULE: README L96]          [INFERRED]
```

- **User Cart Isolation:** User 1 operating in State 2 remains completely segregated from User 2 operating in State 1 (**`INFERRED FROM AUTHENTICATED-USER CART SEMANTICS & SEC-02`**).

---

## 9. Static Implementation Discrepancies Register

| Discrepancy Description | Implementation in SUT (`backend/server.js`) | Official Specification Rule | Static Triage Status |
| :--- | :--- | :--- | :---: |
| **Duplicate-Item Accumulation** | `userCarts[userId].push(req.body)` unconditionally pushes new array rows | `README.md` Line 96: *"Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới."* | **`STATIC-ANALYSIS DEFECT CANDIDATE`** *(Pending Runtime Confirmation)* |
| **Positive Integer Quantity Check** | No validation on `req.body.quantity`; accepts $\le 0$, floats, strings | `README.md` Line 86: *"chỉ nhận số nguyên dương, tối thiểu là 1."* | **`STATIC-ANALYSIS DEFECT CANDIDATE`** *(Pending Runtime Confirmation)* |
| **In-Memory Storage** | Stored in volatile `userCarts = {}` | No persistence requirement specified | **`IMPLEMENTATION DETAIL — NOT A REQUIREMENT`** *(Operational risk noted)* |
