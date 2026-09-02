# FR-07: Shopping Cart — Specification Analysis

> **Document Information:**
> - **Feature ID:** Pool B — `FR-07` (Shopping Cart)
> - **Target Endpoints:** `GET /api/cart`, `POST /api/cart`
> - **Associated Prerequisites:** `POST /api/login`, `POST /api/register` (for authentic JWT tokens)
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Primary Specifications:**
>   - [`api_specification.md`](file:///Users/phamngocgiabao/eshop-sut/api_specification.md) (Section 4.1 & 4.2)
>   - [`README.md`](file:///Users/phamngocgiabao/eshop-sut/README.md) (Section 3 Product Detail & Section 4.1 Shopping Cart)

---

## 1. Feature Identification & Business Objectives

FR-07 governs the shopping cart subsystem for the e-commerce platform. It provides persistent (session/account-scoped) state management enabling authenticated customers to inspect their current selection of items and add prospective purchases prior to order placement.

### Key Functional Requirements (Contract Analysis)
1. **Cart Retrieval (`GET /api/cart`):**
   - Must return the list of items currently retained in the authenticated user's cart.
   - For a newly registered or empty cart, must return an empty list (`[]`).
2. **Cart Item Insertion (`POST /api/cart`):**
   - Must append a designated product item with specified unit price and quantity to the user's cart.
3. **Item Accumulation / Deduplication Rule (`README.md` Line 96):**
   - *"Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới."*
   - Adding a product that already exists in the cart must increment the existing item's quantity rather than appending an additional duplicate row or overwriting existing selections.
4. **Quantity Constraint (`README.md` Line 86):**
   - *"Có ô nhập Số lượng (chỉ nhận số nguyên dương, tối thiểu là 1)."*
   - Item quantity must be a strictly positive integer ($\ge 1$). Zero, negative, and fractional values are formally forbidden by domain rules.
5. **Security & User Cart Isolation (`api_specification.md` Line 112):**
   - Every cart operation requires an authenticated session: `Authorization: Bearer <token>`.
   - Carts must be strictly isolated per user account: User A must never observe, mutate, or overwrite User B's cart contents.

---

## 2. Parameter & Header Specification Matrix

This matrix categorizes all inputs and protocol headers according to their formal declaration status in official project specifications.

| Context / Location | Parameter / Header | Formal Type | Required / Optional | Domain Constraints & Default | Specification Evidence | Status Classification |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **HTTP Request Header** | `Authorization` | `string` | **Required** | Must start with `Bearer ` followed by valid signed JWT token | `api_specification.md` L112: `*Yêu cầu Header: Authorization: Bearer <token>*` | **`SPECIFIED`** |
| **HTTP Request Header** | `Content-Type` | `string` | **Required** | `application/json` for `POST /api/cart` requests | `api_specification.md` L119: `Body (JSON)` | **`INFERRED FROM SPEC`** |
| **HTTP Request Header** | `X-Student-Id` | `string` | **Required** | Must match student ID `23127027` | HW06 PDF Specification & Course Policy | **`SPECIFIED (COURSE RULE)`** |
| **POST Body Field** | `id` | `integer` | **Required** | Primary key identifier of product | `api_specification.md` L122: `"id": 1` in JSON example | **`INFERRED FROM EXAMPLE`** |
| **POST Body Field** | `name` | `string` | **Inferred** | Display name of product | `api_specification.md` L123: `"name": "Sản phẩm A"` | **`INFERRED FROM EXAMPLE`** |
| **POST Body Field** | `price` | `number` | **Inferred** | Unit price in VND ($\ge 0$) | `api_specification.md` L124: `"price": 100000` | **`INFERRED FROM EXAMPLE`** |
| **POST Body Field** | `quantity` | `integer` | **Required** | Positive integer $\ge 1$ | `README.md` L86: *"chỉ nhận số nguyên dương, tối thiểu là 1"* | **`SPECIFIED`** |

---

## 3. Response Contracts & Status Code Derivations

| Scenario / Operation | HTTP Status | Status Classification | Expected Response Body Structure | Evidence / Rationale |
| :--- | :---: | :---: | :--- | :--- |
| **`GET /api/cart` (Empty Cart)** | `200 OK` | **`INFERRED`** | Empty JSON array: `[]` | Standard REST collection convention; `README.md` L100 |
| **`GET /api/cart` (Populated Cart)** | `200 OK` | **`INFERRED`** | Array of cart item objects `[{ id, name, price, quantity }, ...]` | Standard REST representation of state |
| **`POST /api/cart` (Valid Item)** | `200 OK` | **`INFERRED`** | JSON object with confirmation message: `{"message": "Added to cart"}` | Common Express REST idiom; observed in SUT |
| **`POST /api/cart` (Same Item Repeat)** | `200 OK` | **`INFERRED`** | JSON object confirming updated/accumulated item | Must update existing item quantity in cart state |
| **Missing `Authorization` Header** | `401 Unauthorized` | **`INFERRED FROM MIDDLEWARE`** | JSON object: `{"error": "Unauthorized"}` | Enforced by standard JWT authentication barrier |
| **Invalid / Tampered JWT Token** | `403 Forbidden` | **`INFERRED FROM MIDDLEWARE`** | JSON object: `{"error": "Forbidden"}` | Enforced by standard JWT verification handler |
| **Invalid Quantity ($\le 0$ or non-integer)** | `400 Bad Request` | **`UNKNOWN / INFERRED REJECTION`** | Error message indicating invalid quantity | Rejection required by `README.md` L86 rule, exact code undocumented |
| **Missing Required Body Fields** | `400 Bad Request` | **`UNKNOWN / INFERRED REJECTION`** | Error message indicating missing payload | Undocumented status; safe rejection required |
| **Non-Existent Product ID** | `400 / 404` | **`UNKNOWN`** | Error message indicating product not found | Undocumented status; robust rejection expected |

---

## 4. Equivalence Partitioning (EP) & Boundary Value Analysis (BVA)

### Dimension A: Authentication & Authorization (`Authorization` Header)
- **$P_{A1}$ [Valid Token]:** Valid JWT token issued for authenticated user (`SPECIFIED VALID`).
- **$P_{A2}$ [Missing Token]:** Header completely omitted (`SPECIFIED INVALID` $\rightarrow$ 401).
- **$P_{A3}$ [Invalid Token]:** Tampered signature or malformed base64 (`SPECIFIED INVALID` $\rightarrow$ 403).
- **$P_{A4}$ [Expired Token]:** Token beyond `exp` timestamp (`SPECIFIED INVALID` $\rightarrow$ 403).
- **$P_{A5}$ [Malformed Header Scheme]:** Non-Bearer token (e.g. `Basic ...`, raw token without `Bearer `) (`INFERRED INVALID`).

### Dimension B: Quantity Parameter Validation (`quantity`)
- **$P_{B1}$ [Valid Positive Integer]:** $q \in [1, \infty)$.
  - **Boundaries:** $q = 1$ (minimum valid), $q = 2$ (standard small), $q = 99$ (typical upper limit).
- **$P_{B2}$ [Zero Boundary Value]:** $q = 0$ (`SPECIFIED INVALID` $\rightarrow$ rejected, violates min 1).
- **$P_{B3}$ [Negative Integer Value]:** $q = -1, -100$ (`SPECIFIED INVALID` $\rightarrow$ rejected).
- **$P_{B4}$ [Fractional / Decimal Float]:** $q = 1.5, 0.5$ (`SPECIFIED INVALID` $\rightarrow$ rejected, violates integer).
- **$P_{B5}$ [String Integer Value]:** $q = "2"$ (`ROBUSTNESS / TYPE CHARACTERIZATION`).
- **$P_{B6}$ [Non-Numeric String]:** $q = "\text{abc}"$ (`INFERRED INVALID`).
- **$P_{B7}$ [Extreme Large Integer]:** $q = 10^9$, $q = 2^{53}-1$ (`ROBUSTNESS / BOUNDARY`).
- **$P_{B8}$ [Null / Omitted Quantity]:** `quantity` omitted or set to `null` (`INFERRED INVALID`).

### Dimension C: Product ID Validation (`id`)
- **$P_{C1}$ [Valid Existing Product ID]:** $id \in \{1, 2, ...\}$ matching database product catalog (`VALID`).
- **$P_{C2}$ [Non-Existent Product ID]:** $id = 999999$ (`ROBUSTNESS / BUSINESS RULE`).
- **$P_{C3}$ [Negative / Zero Product ID]:** $id = 0, -1$ (`INFERRED INVALID`).
- **$P_{C4}$ [Non-Integer Product ID]:** $id = "\text{one}", 1.5$ (`INFERRED INVALID`).
- **$P_{C5}$ [Missing Product ID]:** Omitted or `null` (`INFERRED INVALID`).

### Dimension D: Price Integrity & Tampering (`price`)
- **$P_{D1}$ [Matching Catalog Price]:** `price` matches official database catalog value (`VALID`).
- **$P_{D2}$ [Client Price Tampering]:** Client submits altered price (e.g. `1 ₫` instead of `100,000 ₫`) (`SECURITY / INTEGRITY PROBE`).
- **$P_{D3}$ [Negative / Zero Price]:** `price = 0, -50000` (`SECURITY / INFERRED INVALID`).
- **$P_{D4}$ [Non-Numeric Price]:** `price = "free"` (`INFERRED INVALID`).

### Dimension E: State Lifecycle & Business Logic
- **$P_{E1}$ [Initial Empty State]:** `GET /api/cart` prior to any additions returns `[]`.
- **$P_{E2}$ [Single Item Lifecycle]:** Add Product A $\rightarrow$ `GET /api/cart` returns exactly `[{ id: A, quantity: q }]`.
- **$P_{E3}$ [Duplicate Item Accumulation]:** Add Product A ($q_1$) then add Product A ($q_2$) $\rightarrow$ `GET /api/cart` must have length 1 with $q_{total} = q_1 + q_2$ (`README.md` Line 96).
- **$P_{E4}$ [Multi-Item Heterogeneous Additions]:** Add Product A and Product B $\rightarrow$ `GET /api/cart` has length 2 with independent quantities.
- **$P_{E5}$ [Cross-User Cart Isolation]:** User 1 adds item $\rightarrow$ User 2 calls `GET /api/cart` $\rightarrow$ User 2's cart is unaffected (`SECURITY ISOLATION`).

---

## 5. SUT Implementation & Defect Risk Assessment

Static analysis of `backend/server.js` (Lines 284–295) reveals critical structural gaps:
```javascript
app.get("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  res.json(userCarts[userId]);
});

app.post("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  userCarts[userId].push(req.body); // <-- DEFECT: Unconditional push, no quantity accumulation!
  res.json({ message: "Added to cart" });
});
```

### Major Defect Candidates Identified:
1. **Defect Risk 1: Violation of Accumulation Rule (`README.md` Line 96):**
   The SUT unconditionally executes `userCarts[userId].push(req.body)`. Adding the same product ID multiple times will produce duplicate array elements rather than accumulating `quantity`.
2. **Defect Risk 2: Complete Absence of Payload Validation:**
   The SUT does not validate `id`, `name`, `price`, or `quantity`. Negative quantities (`-5`), non-integers, empty objects, and arbitrary structures are pushed directly into the cart array.
3. **Defect Risk 3: In-Memory Volatility:**
   Carts are stored in a JavaScript variable `userCarts = {}`. Server restart destroys all user cart state.
