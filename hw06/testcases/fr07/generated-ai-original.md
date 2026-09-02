# FR-07: Shopping Cart — AI-Generated Original Test Cases (38 Cases)

> **Document Status:** Immutable Original AI Generation Record
> **Feature ID:** Pool B — `FR-07` (Shopping Cart)
> **Endpoints:** `GET /api/cart`, `POST /api/cart`
> **Total Generated Tests:** 38 (`FR07-AI-001` through `FR07-AI-038`)
> **Author:** AI (Gemini 3.7 Flash via Antigravity IDE)
> **Student / Reviewer:** Phạm Ngọc Gia Bảo (`23127027`)
> **Created Date:** 2026-09-02

---

## 1. Test Suite Overview & Coverage Allocation

| Coverage ID | Endpoint | Target Condition | Generated Test Cases | Count |
| :--- | :--- | :--- | :--- | :---: |
| **`COV-FR07-01`** | `GET /api/cart` | Verify newly registered user starts with an empty shopping cart | `FR07-AI-001` | 1 |
| **`COV-FR07-02`** | `POST /api/cart, GET /api/cart` | Verify GET /api/cart correctly reflects a single added product item | `FR07-AI-002`, `FR07-AI-003` | 2 |
| **`COV-FR07-03`** | `GET /api/cart` | Verify GET /api/cart rejects request when Authorization header is completely omitted | `FR07-AI-004` | 1 |
| **`COV-FR07-04`** | `GET /api/cart` | Verify GET /api/cart rejects request with forged or tamper-corrupted JWT signature | `FR07-AI-005`, `FR07-AI-006` | 2 |
| **`COV-FR07-05`** | `POST /api/cart` | Verify POST /api/cart succeeds when adding a valid product item matching the specification example | `FR07-AI-007`, `FR07-AI-008` | 2 |
| **`COV-FR07-06`** | `POST /api/cart, GET /api/cart` | Verify adding the same product ID twice increments quantity and does not create duplicate rows | `FR07-AI-009`, `FR07-AI-010`, `FR07-AI-011` | 3 |
| **`COV-FR07-07`** | `POST /api/cart` | Verify POST /api/cart successfully accepts quantity at exact minimum valid boundary (quantity = 1) | `FR07-AI-012` | 1 |
| **`COV-FR07-08`** | `POST /api/cart` | Verify POST /api/cart successfully accepts quantity at min + 1 boundary (quantity = 2) | `FR07-AI-013` | 1 |
| **`COV-FR07-09`** | `POST /api/cart` | Verify POST /api/cart rejects request when quantity is 0 (min - 1 boundary violation) | `FR07-AI-014` | 1 |
| **`COV-FR07-10`** | `POST /api/cart` | Verify POST /api/cart rejects request when quantity is -1 (immediate negative boundary) | `FR07-AI-015`, `FR07-AI-016` | 2 |
| **`COV-FR07-11`** | `POST /api/cart` | Verify POST /api/cart rejects fractional/decimal quantity (quantity = 1.5) | `FR07-AI-017`, `FR07-AI-018` | 2 |
| **`COV-FR07-12`** | `POST /api/cart` | Characterize SUT behavior when quantity is supplied as a string-encoded integer ('2') | `FR07-AI-019` | 1 |
| **`COV-FR07-13`** | `POST /api/cart` | Verify POST /api/cart rejects request when quantity is an alphabetic string ('abc') | `FR07-AI-020`, `FR07-AI-021` | 2 |
| **`COV-FR07-14`** | `POST /api/cart` | Characterize server handling of extreme large quantity (10^9) without crash or corrupted memory | `FR07-AI-022` | 1 |
| **`COV-FR07-15`** | `POST /api/cart` | Verify POST /api/cart rejects request when the mandatory quantity property is completely omitted | `FR07-AI-023`, `FR07-AI-024` | 2 |
| **`COV-FR07-16`** | `POST /api/cart` | Probe SUT behavior when adding a product ID that does not exist in database catalog (id = 999999) | `FR07-AI-025` | 1 |
| **`COV-FR07-17`** | `POST /api/cart` | Probe SUT handling of a negative integer product identifier (id = -1) | `FR07-AI-026` | 1 |
| **`COV-FR07-18`** | `POST /api/cart` | Probe SUT handling when the product ID property is completely omitted from body | `FR07-AI-027`, `FR07-AI-028` | 2 |
| **`COV-FR07-19`** | `POST /api/cart, GET /api/cart` | Probe whether POST /api/cart trusts client-submitted price (e.g. price: 1) or looks up catalog price | `FR07-AI-029` | 1 |
| **`COV-FR07-20`** | `POST /api/cart` | Probe SUT handling when price is supplied as a negative number (-50000) | `FR07-AI-030` | 1 |
| **`COV-FR07-21`** | `POST /api/cart` | Verify POST /api/cart rejects addition when Authorization header is completely omitted | `FR07-AI-031` | 1 |
| **`COV-FR07-22`** | `POST /api/cart` | Verify POST /api/cart rejects request carrying forged JWT signature | `FR07-AI-032`, `FR07-AI-033` | 2 |
| **`COV-FR07-23`** | `POST /api/cart, GET /api/cart` | Verify User A adding items to their cart leaves User B's cart completely empty | `FR07-AI-034`, `FR07-AI-035`, `FR07-AI-036` | 3 |
| **`COV-FR07-24`** | `POST /api/cart` | Verify POST /api/cart handles empty JSON body ({}) safely without server crash | `FR07-AI-037`, `FR07-AI-038` | 2 |
| **TOTAL** | — | — | **38 Unique Tests** | **38** |

---

## 2. Detailed Test Specifications

### `FR07-AI-001` — Verify newly registered user starts with an empty shopping cart

#### Identity
- **Test ID:** `FR07-AI-001`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-01`
- **Endpoint(s):** `GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L100`
- **SEC Reference:** `SEC-02 (Authenticated Session)`
- **Source Reference:** README.md L100, api_specification.md L115
- **Oracle Classification:** **`INFERRED / IMPLEMENTATION-OBSERVED`**

#### Test Design
- **Category:** Positive Functional / State Baseline
- **Test Objective:** Verify newly registered user starts with an empty shopping cart
- **Test Condition:** Authenticated user with no prior cart additions sends GET /api/cart
- **Partition / Boundary:** P_E1 (Initial Empty State)
- **Preconditions:** User account registered and authenticated with valid JWT token
- **Initial Cart State:** Cart is empty (0 items)
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Return empty collection representing absence of items in user cart
- **Expected HTTP Status:** `200 OK (INFERRED)`
- **Expected Response Contract:** JSON array with length 0: []
- **State Assertion:** `Cart remains empty (length 0)`
- **Security Assertion:** Access granted only with valid JWT

#### Lifecycle
- **Setup Required:** Register and log in fresh test user
- **Cleanup Required:** None required (fresh user)
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-002` — Verify GET /api/cart correctly reflects a single added product item

#### Identity
- **Test ID:** `FR07-AI-002`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-02`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L115`
- **SEC Reference:** `SEC-02 (Authenticated Session)`
- **Source Reference:** api_specification.md L115-127
- **Oracle Classification:** **`INFERRED`**

#### Test Design
- **Category:** Positive Functional / State Verification
- **Test Objective:** Verify GET /api/cart correctly reflects a single added product item
- **Test Condition:** Add 1 product (id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2) then retrieve cart
- **Partition / Boundary:** P_E2 (Single Item Cart)
- **Preconditions:** Authenticated user with initially empty cart
- **Initial Cart State:** Cart is empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2
}
```

*Step 2:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Cart returns an array containing exactly the single added item with matching properties
- **Expected HTTP Status:** `POST: 200 OK (INFERRED); GET: 200 OK (INFERRED)`
- **Expected Response Contract:** Array of objects: [{ id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2 }]
- **State Assertion:** `Cart array length === 1; item[0].id === 1; item[0].quantity === 2`
- **Security Assertion:** Session isolation maintained

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-003` — Verify GET /api/cart correctly reflects multiple distinct added products

#### Identity
- **Test ID:** `FR07-AI-003`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-02`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L115`
- **SEC Reference:** `SEC-02 (Authenticated Session)`
- **Source Reference:** api_specification.md L115-127, README.md L95
- **Oracle Classification:** **`INFERRED`**

#### Test Design
- **Category:** Positive Functional / Multi-Item State
- **Test Objective:** Verify GET /api/cart correctly reflects multiple distinct added products
- **Test Condition:** Add Product 1 (q=1) and Product 2 (q=3) then retrieve cart
- **Partition / Boundary:** P_E4 (Multi-Item Heterogeneous Cart)
- **Preconditions:** Authenticated user with initially empty cart
- **Initial Cart State:** Cart is empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

*Step 2:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 2,
  "name": "Sản phẩm B",
  "price": 150000,
  "quantity": 3
}
```

*Step 3:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Cart returns an array containing both distinct product items with their respective quantities
- **Expected HTTP Status:** `POST calls: 200 OK (INFERRED); GET: 200 OK (INFERRED)`
- **Expected Response Contract:** Array of 2 objects containing distinct items with id 1 and id 2
- **State Assertion:** `Cart array length === 2; both product entries retained independently`
- **Security Assertion:** Session isolation maintained

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-004` — Verify GET /api/cart rejects request when Authorization header is completely omitted

#### Identity
- **Test ID:** `FR07-AI-004`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-03`
- **Endpoint(s):** `GET /api/cart`

#### Traceability
- **Requirement Reference:** `SEC-02 / api_specification.md L112`
- **SEC Reference:** `SEC-02 (Mandatory JWT for Secured APIs)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)`**

#### Test Design
- **Category:** Security / Authentication Barrier
- **Test Objective:** Verify GET /api/cart rejects request when Authorization header is completely omitted
- **Test Condition:** Send GET /api/cart with no Authorization header
- **Partition / Boundary:** P_A2 (Missing Token)
- **Preconditions:** Server running
- **Initial Cart State:** N/A
- **Authentication State:** Unauthenticated (No token)

#### HTTP Request(s)
- **Method & Endpoint:** `GET /api/cart`
- **Headers:**
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Access denied; cart information not exposed to unauthenticated callers
- **Expected HTTP Status:** `401 Unauthorized (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)`
- **Expected Response Contract:** JSON error payload indicating unauthenticated access
- **State Assertion:** `No user cart state inspected or leaked`
- **Security Assertion:** SEC-02 enforced: protected resource denies unauthenticated request

#### Lifecycle
- **Setup Required:** None
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-005` — Verify GET /api/cart rejects request with forged or tamper-corrupted JWT signature

#### Identity
- **Test ID:** `FR07-AI-005`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-04`
- **Endpoint(s):** `GET /api/cart`

#### Traceability
- **Requirement Reference:** `SEC-02 / api_specification.md L112`
- **SEC Reference:** `SEC-02 (Mandatory JWT for Secured APIs)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)`**

#### Test Design
- **Category:** Security / Token Verification
- **Test Objective:** Verify GET /api/cart rejects request with forged or tamper-corrupted JWT signature
- **Test Condition:** Send GET /api/cart with JWT token having an invalid HMAC signature
- **Partition / Boundary:** P_A3 (Invalid Signature Token)
- **Preconditions:** Server running with SECRET_KEY
- **Initial Cart State:** N/A
- **Authentication State:** Invalid JWT token (corrupted signature)

#### HTTP Request(s)
- **Method & Endpoint:** `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTE2MjM5MDIyfQ.InvalidSignatureStringForTesting`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Access denied; forged or invalid token rejected
- **Expected HTTP Status:** `403 Forbidden (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)`
- **Expected Response Contract:** JSON error payload: { error: 'Forbidden' }
- **State Assertion:** `No user cart state accessed`
- **Security Assertion:** SEC-02 cryptographic signature verification enforced

#### Lifecycle
- **Setup Required:** None
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-006` — Verify GET /api/cart rejects Authorization header lacking the 'Bearer ' scheme prefix

#### Identity
- **Test ID:** `FR07-AI-006`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-04`
- **Endpoint(s):** `GET /api/cart`

#### Traceability
- **Requirement Reference:** `SEC-02 / api_specification.md L112`
- **SEC Reference:** `SEC-02 (Mandatory JWT for Secured APIs)`
- **Source Reference:** api_specification.md L112
- **Oracle Classification:** **`ROBUSTNESS / SPECIFIED REJECTION`**

#### Test Design
- **Category:** Security / Header Format Robustness
- **Test Objective:** Verify GET /api/cart rejects Authorization header lacking the 'Bearer ' scheme prefix
- **Test Condition:** Send GET /api/cart with raw token string without 'Bearer ' prefix
- **Partition / Boundary:** P_A5 (Malformed Authorization Scheme)
- **Preconditions:** Server running
- **Initial Cart State:** N/A
- **Authentication State:** Malformed Authorization header scheme

#### HTTP Request(s)
- **Method & Endpoint:** `GET /api/cart`
- **Headers:**
  - `Authorization`: `RawTokenWithoutBearerPrefix12345`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Access denied; non-Bearer scheme rejected cleanly
- **Expected HTTP Status:** `401 / 403 (INFERRED FROM MIDDLEWARE; official status UNKNOWN)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `No user cart state accessed`
- **Security Assertion:** SEC-02 scheme enforcement

#### Lifecycle
- **Setup Required:** None
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-007` — Verify POST /api/cart succeeds when adding a valid product item matching the specification example

#### Identity
- **Test ID:** `FR07-AI-007`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-05`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L118`
- **SEC Reference:** `SEC-02 (Authenticated Session)`
- **Source Reference:** api_specification.md L118-127
- **Oracle Classification:** **`INFERRED`**

#### Test Design
- **Category:** Positive Functional / Cart Mutation
- **Test Objective:** Verify POST /api/cart succeeds when adding a valid product item matching the specification example
- **Test Condition:** Send POST /api/cart with valid body { id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2 }
- **Partition / Boundary:** P_B1, P_C1, P_D1 (Standard Valid Item Addition)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2
}
```

#### Expected Result
- **Expected Semantic Behavior:** Item accepted and added to user's shopping cart session
- **Expected HTTP Status:** `200 OK (INFERRED)`
- **Expected Response Contract:** JSON object with confirmation message: { message: 'Added to cart' } (IMPLEMENTATION-OBSERVED)
- **State Assertion:** `Subsequent GET /api/cart contains the item`
- **Security Assertion:** Mutation scoped strictly to authenticated user

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-008` — Verify POST /api/cart succeeds when adding a second distinct product item

#### Identity
- **Test ID:** `FR07-AI-008`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-05`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L118`
- **SEC Reference:** `SEC-02 (Authenticated Session)`
- **Source Reference:** api_specification.md L118-127
- **Oracle Classification:** **`INFERRED`**

#### Test Design
- **Category:** Positive Functional / Sequential Additions
- **Test Objective:** Verify POST /api/cart succeeds when adding a second distinct product item
- **Test Condition:** Add product 1 then add product 2
- **Partition / Boundary:** P_B1, P_C1, P_D1 (Second Distinct Product Addition)
- **Preconditions:** Authenticated user with 1 item already in cart
- **Initial Cart State:** Cart contains product 1
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 2,
  "name": "Sản phẩm B",
  "price": 250000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Second item accepted without removing or corrupting first item
- **Expected HTTP Status:** `200 OK (INFERRED)`
- **Expected Response Contract:** JSON object confirming addition
- **State Assertion:** `Cart contains 2 distinct product items`
- **Security Assertion:** Scoped to authenticated user

#### Lifecycle
- **Setup Required:** Register user and add product 1
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-009` — Verify adding the same product ID twice increments quantity and does not create duplicate rows

#### Identity
- **Test ID:** `FR07-AI-009`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-06`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L96`
- **SEC Reference:** `None`
- **Source Reference:** README.md L96: 'Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.'
- **Oracle Classification:** **`SPECIFIED BUSINESS RULE`**

#### Test Design
- **Category:** Business Rule / Cart Accumulation
- **Test Objective:** Verify adding the same product ID twice increments quantity and does not create duplicate rows
- **Test Condition:** POST product id: 1 with q=2, then POST product id: 1 with q=3, then GET cart
- **Partition / Boundary:** P_E3 (Duplicate Product Accumulation)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2
}
```

*Step 2:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 3
}
```

*Step 3:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Cart must contain exactly ONE entry for product id: 1 with accumulated quantity === 5 (2 + 3)
- **Expected HTTP Status:** `POST calls: 200 OK (INFERRED); GET: 200 OK (INFERRED)`
- **Expected Response Contract:** Array containing exactly 1 item: [{ id: 1, quantity: 5, ... }]
- **State Assertion:** `cart.length === 1 && cart[0].quantity === 5`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-010` — Verify duplicate product accumulation succeeds when interleaved with a different product

#### Identity
- **Test ID:** `FR07-AI-010`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-06`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L96`
- **SEC Reference:** `None`
- **Source Reference:** README.md L96
- **Oracle Classification:** **`SPECIFIED BUSINESS RULE`**

#### Test Design
- **Category:** Business Rule / Interleaved Accumulation
- **Test Objective:** Verify duplicate product accumulation succeeds when interleaved with a different product
- **Test Condition:** POST product 1 (q=1) -> POST product 2 (q=2) -> POST product 1 (q=4) -> GET cart
- **Partition / Boundary:** P_E3 (Interleaved Duplicate Accumulation)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

*Step 2:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 2,
  "name": "Sản phẩm B",
  "price": 200000,
  "quantity": 2
}
```

*Step 3:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 4
}
```

*Step 4:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Cart has exactly 2 lines: product 1 with quantity === 5 (1 + 4), product 2 with quantity === 2
- **Expected HTTP Status:** `All calls 200 OK (INFERRED)`
- **Expected Response Contract:** Array of 2 objects
- **State Assertion:** `cart.length === 2 && cart.find(x => x.id === 1).quantity === 5`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-011` — Verify duplicate accumulation when adding single-unit increments (q=1 then q=1)

#### Identity
- **Test ID:** `FR07-AI-011`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-06`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L96`
- **SEC Reference:** `None`
- **Source Reference:** README.md L96
- **Oracle Classification:** **`SPECIFIED BUSINESS RULE`**

#### Test Design
- **Category:** Business Rule / Minimum Increment Accumulation
- **Test Objective:** Verify duplicate accumulation when adding single-unit increments (q=1 then q=1)
- **Test Condition:** POST product id: 1 with q=1, then POST product id: 1 with q=1, then GET cart
- **Partition / Boundary:** P_E3 (Minimum Increment Accumulation)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

*Step 2:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

*Step 3:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Cart has exactly 1 entry for product 1 with quantity === 2 (1 + 1)
- **Expected HTTP Status:** `All calls 200 OK (INFERRED)`
- **Expected Response Contract:** Array of 1 object with quantity: 2
- **State Assertion:** `cart.length === 1 && cart[0].quantity === 2`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-012` — Verify POST /api/cart successfully accepts quantity at exact minimum valid boundary (quantity = 1)

#### Identity
- **Test ID:** `FR07-AI-012`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-07`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86: 'chỉ nhận số nguyên dương, tối thiểu là 1.'
- **Oracle Classification:** **`SPECIFIED`**

#### Test Design
- **Category:** Boundary Value Analysis / Lower Valid Bound
- **Test Objective:** Verify POST /api/cart successfully accepts quantity at exact minimum valid boundary (quantity = 1)
- **Test Condition:** Send POST /api/cart with quantity: 1
- **Partition / Boundary:** P_B1 (Exact Minimum Boundary: q=1)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Item accepted with quantity 1
- **Expected HTTP Status:** `200 OK (SPECIFIED / INFERRED)`
- **Expected Response Contract:** JSON confirmation
- **State Assertion:** `Cart retains item with quantity 1`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-013` — Verify POST /api/cart successfully accepts quantity at min + 1 boundary (quantity = 2)

#### Identity
- **Test ID:** `FR07-AI-013`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-08`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86, api_specification.md L125
- **Oracle Classification:** **`SPECIFIED`**

#### Test Design
- **Category:** Boundary Value Analysis / Valid Small Integer
- **Test Objective:** Verify POST /api/cart successfully accepts quantity at min + 1 boundary (quantity = 2)
- **Test Condition:** Send POST /api/cart with quantity: 2
- **Partition / Boundary:** P_B1 (Min + 1 Boundary: q=2)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2
}
```

#### Expected Result
- **Expected Semantic Behavior:** Item accepted with quantity 2
- **Expected HTTP Status:** `200 OK (SPECIFIED / INFERRED)`
- **Expected Response Contract:** JSON confirmation
- **State Assertion:** `Cart retains item with quantity 2`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-014` — Verify POST /api/cart rejects request when quantity is 0 (min - 1 boundary violation)

#### Identity
- **Test ID:** `FR07-AI-014`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-09`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86: 'chỉ nhận số nguyên dương, tối thiểu là 1.'
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)`**

#### Test Design
- **Category:** Boundary Value Analysis / Lower Invalid Bound
- **Test Objective:** Verify POST /api/cart rejects request when quantity is 0 (min - 1 boundary violation)
- **Test Condition:** Send POST /api/cart with quantity: 0
- **Partition / Boundary:** P_B2 (Min - 1 Invalid Boundary: q=0)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 0
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; zero quantity violates minimum 1 rule
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty; no zero-quantity item added`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-015` — Verify POST /api/cart rejects request when quantity is -1 (immediate negative boundary)

#### Identity
- **Test ID:** `FR07-AI-015`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-10`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)`**

#### Test Design
- **Category:** Input Validation / Negative Quantity Boundary
- **Test Objective:** Verify POST /api/cart rejects request when quantity is -1 (immediate negative boundary)
- **Test Condition:** Send POST /api/cart with quantity: -1
- **Partition / Boundary:** P_B3 (Immediate Negative Boundary: q=-1)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": -1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; negative quantity violates positive integer requirement
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty; no negative quantity item added`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-016` — Verify POST /api/cart rejects request when quantity is a large negative integer (-100)

#### Identity
- **Test ID:** `FR07-AI-016`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-10`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)`**

#### Test Design
- **Category:** Input Validation / Large Negative Quantity
- **Test Objective:** Verify POST /api/cart rejects request when quantity is a large negative integer (-100)
- **Test Condition:** Send POST /api/cart with quantity: -100
- **Partition / Boundary:** P_B3 (Large Negative Integer: q=-100)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": -100
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; negative integer is forbidden
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-017` — Verify POST /api/cart rejects fractional/decimal quantity (quantity = 1.5)

#### Identity
- **Test ID:** `FR07-AI-017`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-11`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86: 'chỉ nhận số nguyên dương'
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)`**

#### Test Design
- **Category:** Type Validation / Fractional Quantity
- **Test Objective:** Verify POST /api/cart rejects fractional/decimal quantity (quantity = 1.5)
- **Test Condition:** Send POST /api/cart with quantity: 1.5
- **Partition / Boundary:** P_B4 (Fractional Decimal > 1: q=1.5)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1.5
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; fractional values violate integer requirement
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty; no fractional item added`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-018` — Verify POST /api/cart rejects decimal quantity between 0 and 1 (quantity = 0.5)

#### Identity
- **Test ID:** `FR07-AI-018`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-11`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)`**

#### Test Design
- **Category:** Type Validation / Sub-Unit Decimal Quantity
- **Test Objective:** Verify POST /api/cart rejects decimal quantity between 0 and 1 (quantity = 0.5)
- **Test Condition:** Send POST /api/cart with quantity: 0.5
- **Partition / Boundary:** P_B4 (Sub-Unit Fractional: q=0.5)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 0.5
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; sub-unit decimal violates both integer and minimum 1 constraints
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-019` — Characterize SUT behavior when quantity is supplied as a string-encoded integer ('2')

#### Identity
- **Test ID:** `FR07-AI-019`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-12`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`TYPE ROBUSTNESS / CHARACTERIZATION`**

#### Test Design
- **Category:** Type Robustness / JSON Type Coercion Probe
- **Test Objective:** Characterize SUT behavior when quantity is supplied as a string-encoded integer ('2')
- **Test Condition:** Send POST /api/cart with quantity: '2'
- **Partition / Boundary:** P_B5 (String Integer Value: q='2')
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": "2"
}
```

#### Expected Result
- **Expected Semantic Behavior:** Characterize whether server strictly rejects non-number type or coerces string integer safely without crash
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled HTTP response, no 500 error)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server remains operational; if stored, cart structure is internally consistent`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-020` — Verify POST /api/cart rejects request when quantity is an alphabetic string ('abc')

#### Identity
- **Test ID:** `FR07-AI-020`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-13`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`INFERRED REJECTION`**

#### Test Design
- **Category:** Type Validation / Alphabetic String
- **Test Objective:** Verify POST /api/cart rejects request when quantity is an alphabetic string ('abc')
- **Test Condition:** Send POST /api/cart with quantity: 'abc'
- **Partition / Boundary:** P_B6 (Non-Numeric Alphabetic String)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": "abc"
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; non-numeric string violates integer constraint
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty; NaN/string not added to cart calculations`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-021` — Verify POST /api/cart rejects request when quantity is special symbols ('@#$')

#### Identity
- **Test ID:** `FR07-AI-021`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-13`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`INFERRED REJECTION`**

#### Test Design
- **Category:** Type Validation / Special Character String
- **Test Objective:** Verify POST /api/cart rejects request when quantity is special symbols ('@#$')
- **Test Condition:** Send POST /api/cart with quantity: '@#$'
- **Partition / Boundary:** P_B6 (Special Symbol String)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": "@#$"
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; special character string cannot represent integer quantity
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-022` — Characterize server handling of extreme large quantity (10^9) without crash or corrupted memory

#### Identity
- **Test ID:** `FR07-AI-022`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-14`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`ROBUSTNESS / UNKNOWN UPPER BOUND`**

#### Test Design
- **Category:** Robustness / Extreme Large Integer
- **Test Objective:** Characterize server handling of extreme large quantity (10^9) without crash or corrupted memory
- **Test Condition:** Send POST /api/cart with quantity: 1000000000
- **Partition / Boundary:** P_B7 (Extreme Large Integer: q=10^9)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1000000000
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server handles large integer safely with controlled response and no process crash
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled response, no crash)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server process remains alive and responsive`
- **Security Assertion:** No unhandled numeric exception or memory failure

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-023` — Verify POST /api/cart rejects request when the mandatory quantity property is completely omitted

#### Identity
- **Test ID:** `FR07-AI-023`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-15`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86: 'Có ô nhập Số lượng'
- **Oracle Classification:** **`INFERRED REJECTION`**

#### Test Design
- **Category:** Input Validation / Omitted Mandatory Property
- **Test Objective:** Verify POST /api/cart rejects request when the mandatory quantity property is completely omitted
- **Test Condition:** Send POST /api/cart with body omitting 'quantity': { id: 1, name: 'Sản phẩm A', price: 100000 }
- **Partition / Boundary:** P_B8 (Omitted Quantity Property)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; quantity is a required input for cart additions
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty; undefined quantity item not added`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-024` — Verify POST /api/cart rejects request when quantity is explicitly passed as null

#### Identity
- **Test ID:** `FR07-AI-024`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-15`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / README.md L86`
- **SEC Reference:** `None`
- **Source Reference:** README.md L86
- **Oracle Classification:** **`INFERRED REJECTION`**

#### Test Design
- **Category:** Input Validation / Explicit Null Quantity
- **Test Objective:** Verify POST /api/cart rejects request when quantity is explicitly passed as null
- **Test Condition:** Send POST /api/cart with quantity: null
- **Partition / Boundary:** P_B8 (Null Quantity Property)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": null
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server must reject request; null quantity cannot satisfy positive integer requirement
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-025` — Probe SUT behavior when adding a product ID that does not exist in database catalog (id = 999999)

#### Identity
- **Test ID:** `FR07-AI-025`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-16`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L122`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L122
- **Oracle Classification:** **`ROBUSTNESS / BUSINESS PROBE`**

#### Test Design
- **Category:** Business Rule / Catalog Existence Probe
- **Test Objective:** Probe SUT behavior when adding a product ID that does not exist in database catalog (id = 999999)
- **Test Condition:** Send POST /api/cart with non-existent id: 999999
- **Partition / Boundary:** P_C2 (Non-Existent Product ID)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 999999,
  "name": "Phantom Item",
  "price": 50000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Characterize whether cart checks database catalog or blindly pushes unverified product IDs
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled response, no crash)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server remains responsive`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-026` — Probe SUT handling of a negative integer product identifier (id = -1)

#### Identity
- **Test ID:** `FR07-AI-026`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-17`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L122`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L122
- **Oracle Classification:** **`ROBUSTNESS PROBE`**

#### Test Design
- **Category:** Input Robustness / Negative Product ID
- **Test Objective:** Probe SUT handling of a negative integer product identifier (id = -1)
- **Test Condition:** Send POST /api/cart with id: -1
- **Partition / Boundary:** P_C3 (Negative Product ID: id=-1)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": -1,
  "name": "Negative ID Item",
  "price": 50000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Probe whether server handles negative ID safely without unexpected state corruption
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled response, no crash)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server process remains alive`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-027` — Probe SUT handling when the product ID property is completely omitted from body

#### Identity
- **Test ID:** `FR07-AI-027`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-18`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L122`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L122
- **Oracle Classification:** **`ROBUSTNESS PROBE`**

#### Test Design
- **Category:** Schema Robustness / Omitted Product ID
- **Test Objective:** Probe SUT handling when the product ID property is completely omitted from body
- **Test Condition:** Send POST /api/cart with body lacking 'id': { name: 'No ID Item', price: 50000, quantity: 1 }
- **Partition / Boundary:** P_C5 (Omitted Product ID)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "name": "No ID Item",
  "price": 50000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Probe whether server requires an item ID or blindly stores ID-less cart entries
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled response, no crash)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server process remains operational`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-028` — Probe SUT handling when product ID is passed as a string ('one')

#### Identity
- **Test ID:** `FR07-AI-028`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-18`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L122`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L122
- **Oracle Classification:** **`ROBUSTNESS PROBE`**

#### Test Design
- **Category:** Type Robustness / Non-Integer Product ID
- **Test Objective:** Probe SUT handling when product ID is passed as a string ('one')
- **Test Condition:** Send POST /api/cart with id: 'one'
- **Partition / Boundary:** P_C4 (String Product ID)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": "one",
  "name": "String ID Item",
  "price": 50000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Probe whether server coerces string ID, rejects it, or allows string key
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled response, no crash)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server process remains operational`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-029` — Probe whether POST /api/cart trusts client-submitted price (e.g. price: 1) or looks up catalog price

#### Identity
- **Test ID:** `FR07-AI-029`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-19`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L124`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L124, README.md L107
- **Oracle Classification:** **`SECURITY / INTEGRITY PROBE`**

#### Test Design
- **Category:** Security / Client Price Tampering Probe
- **Test Objective:** Probe whether POST /api/cart trusts client-submitted price (e.g. price: 1) or looks up catalog price
- **Test Condition:** Send POST /api/cart for known 100000 VND product with tampered price: 1, then GET cart
- **Partition / Boundary:** P_D2 (Client Price Tampering)
- **Preconditions:** Authenticated user with empty cart
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 1,
  "quantity": 1
}
```

*Step 2:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** Characterize whether cart stores arbitrary client price or overrides it with official catalog price
- **Expected HTTP Status:** `UNKNOWN by specification (POST returns controlled response; GET reflects state)`
- **Expected Response Contract:** Array of cart items
- **State Assertion:** `Inspect stored price property in retrieved cart item`
- **Security Assertion:** Integrity probe: identifies if client can manipulate unit price in cart layer

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-030` — Probe SUT handling when price is supplied as a negative number (-50000)

#### Identity
- **Test ID:** `FR07-AI-030`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-20`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L124`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L124
- **Oracle Classification:** **`ROBUSTNESS PROBE`**

#### Test Design
- **Category:** Input Robustness / Negative Price
- **Test Objective:** Probe SUT handling when price is supplied as a negative number (-50000)
- **Test Condition:** Send POST /api/cart with price: -50000
- **Partition / Boundary:** P_D3 (Negative Price)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": -50000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Characterize handling of negative price without server crash
- **Expected HTTP Status:** `UNKNOWN by specification (Controlled response, no crash)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server process remains alive`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-031` — Verify POST /api/cart rejects addition when Authorization header is completely omitted

#### Identity
- **Test ID:** `FR07-AI-031`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-21`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `SEC-02 / api_specification.md L112`
- **SEC Reference:** `SEC-02 (Mandatory JWT for Secured APIs)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)`**

#### Test Design
- **Category:** Security / Authentication Barrier
- **Test Objective:** Verify POST /api/cart rejects addition when Authorization header is completely omitted
- **Test Condition:** Send POST /api/cart with valid body but without Authorization header
- **Partition / Boundary:** P_A2 (Missing Token on Mutation)
- **Preconditions:** Server running
- **Initial Cart State:** N/A
- **Authentication State:** Unauthenticated (No token)

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Cart mutation denied; unauthenticated user cannot mutate any cart
- **Expected HTTP Status:** `401 Unauthorized (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `No user cart state mutated`
- **Security Assertion:** SEC-02 enforced on write endpoint

#### Lifecycle
- **Setup Required:** None
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-032` — Verify POST /api/cart rejects request carrying forged JWT signature

#### Identity
- **Test ID:** `FR07-AI-032`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-22`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `SEC-02 / api_specification.md L112`
- **SEC Reference:** `SEC-02 (Mandatory JWT for Secured APIs)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)`**

#### Test Design
- **Category:** Security / Token Verification
- **Test Objective:** Verify POST /api/cart rejects request carrying forged JWT signature
- **Test Condition:** Send POST /api/cart with valid body and forged HMAC signature
- **Partition / Boundary:** P_A3 (Invalid Signature on Mutation)
- **Preconditions:** Server running
- **Initial Cart State:** N/A
- **Authentication State:** Forged JWT signature

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTE2MjM5MDIyfQ.ForgedSignatureBytes12345`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Cart mutation denied; token signature verification fails
- **Expected HTTP Status:** `403 Forbidden (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)`
- **Expected Response Contract:** JSON error payload: { error: 'Forbidden' }
- **State Assertion:** `No cart mutation executed`
- **Security Assertion:** SEC-02 cryptographic barrier prevents unauthorized mutation

#### Lifecycle
- **Setup Required:** None
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-033` — Verify POST /api/cart rejects Authorization header using Basic scheme instead of Bearer

#### Identity
- **Test ID:** `FR07-AI-033`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-22`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `SEC-02 / api_specification.md L112`
- **SEC Reference:** `SEC-02 (Mandatory JWT for Secured APIs)`
- **Source Reference:** api_specification.md L112
- **Oracle Classification:** **`ROBUSTNESS / SPECIFIED REJECTION`**

#### Test Design
- **Category:** Security / Header Format Robustness
- **Test Objective:** Verify POST /api/cart rejects Authorization header using Basic scheme instead of Bearer
- **Test Condition:** Send POST /api/cart with Authorization: Basic dXNlcjpwYXNz
- **Partition / Boundary:** P_A5 (Wrong Authentication Scheme)
- **Preconditions:** Server running
- **Initial Cart State:** N/A
- **Authentication State:** Basic auth scheme instead of Bearer

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Basic dXNlcjpwYXNz`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 1
}
```

#### Expected Result
- **Expected Semantic Behavior:** Access denied; non-Bearer scheme rejected
- **Expected HTTP Status:** `401 / 403 (INFERRED FROM MIDDLEWARE; official status UNKNOWN)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `No cart mutation`
- **Security Assertion:** SEC-02 scheme enforcement

#### Lifecycle
- **Setup Required:** None
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-034` — Verify User A adding items to their cart leaves User B's cart completely empty

#### Identity
- **Test ID:** `FR07-AI-034`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-23`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / SEC-02`
- **SEC Reference:** `SEC-02 (Authenticated Session Isolation)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02`**

#### Test Design
- **Category:** Security / Multi-Tenant Cart Isolation
- **Test Objective:** Verify User A adding items to their cart leaves User B's cart completely empty
- **Test Condition:** User A adds product 1 -> User B (fresh login) retrieves GET /api/cart
- **Partition / Boundary:** P_E5 (Cross-User Isolation: Empty Cart Independence)
- **Preconditions:** Two distinct registered users (User A, User B)
- **Initial Cart State:** Both carts empty
- **Authentication State:** Separate JWT tokens for User A and User B

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_A_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2
}
```

*Step 2:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_B_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** User B's cart remains completely empty ([]); User A's items are strictly isolated
- **Expected HTTP Status:** `POST: 200 OK (INFERRED); GET: 200 OK (INFERRED)`
- **Expected Response Contract:** User B GET returns empty array: []
- **State Assertion:** `user_b_cart.length === 0`
- **Security Assertion:** Multi-tenant data isolation: no cross-user cart leakage (BOLA prevention)

#### Lifecycle
- **Setup Required:** Register User A and User B
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-035` — Verify User A's additions do not mutate or overwrite User B's existing populated cart

#### Identity
- **Test ID:** `FR07-AI-035`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-23`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / SEC-02`
- **SEC Reference:** `SEC-02 (Authenticated Session Isolation)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02`**

#### Test Design
- **Category:** Security / Multi-Tenant Non-Interference
- **Test Objective:** Verify User A's additions do not mutate or overwrite User B's existing populated cart
- **Test Condition:** User B adds product 2 -> User A adds product 1 -> User B retrieves cart
- **Partition / Boundary:** P_E5 (Cross-User Isolation: Populated Non-Interference)
- **Preconditions:** User A and User B registered
- **Initial Cart State:** Both carts empty
- **Authentication State:** Separate JWT tokens for User A and User B

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_B_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 2,
  "name": "Sản phẩm B",
  "price": 200000,
  "quantity": 1
}
```

*Step 2:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_A_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 3
}
```

*Step 3:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_B_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** User B's cart still contains only product 2 with quantity 1; completely unaffected by User A
- **Expected HTTP Status:** `All calls 200 OK (INFERRED)`
- **Expected Response Contract:** User B GET returns [{ id: 2, quantity: 1 }]
- **State Assertion:** `user_b_cart.length === 1 && user_b_cart[0].id === 2`
- **Security Assertion:** State segregation maintained across concurrent customer sessions

#### Lifecycle
- **Setup Required:** Register User A and User B
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-036` — Verify accumulation of the same product ID operates independently across distinct users

#### Identity
- **Test ID:** `FR07-AI-036`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-23`
- **Endpoint(s):** `POST /api/cart, GET /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / SEC-02`
- **SEC Reference:** `SEC-02 (Authenticated Session Isolation)`
- **Source Reference:** api_specification.md L112, README.md L279
- **Oracle Classification:** **`INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02`**

#### Test Design
- **Category:** Security / Independent Accumulation Isolation
- **Test Objective:** Verify accumulation of the same product ID operates independently across distinct users
- **Test Condition:** User A adds product 1 (q=2) -> User B adds product 1 (q=3) -> User A GET cart
- **Partition / Boundary:** P_E5 (Independent Cross-User Accumulation)
- **Preconditions:** User A and User B registered
- **Initial Cart State:** Both carts empty
- **Authentication State:** Separate JWT tokens for User A and User B

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_A_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2
}
```

*Step 2:* `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_B_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 3
}
```

*Step 3:* `GET /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <USER_A_TOKEN>`
  - `X-Student-Id`: `23127027`
- **Request Body:** None

#### Expected Result
- **Expected Semantic Behavior:** User A's cart quantity for product 1 is strictly 2; not contaminated by User B's addition of product 1
- **Expected HTTP Status:** `All calls 200 OK (INFERRED)`
- **Expected Response Contract:** User A cart returns [{ id: 1, quantity: 2 }]
- **State Assertion:** `user_a_cart[0].quantity === 2`
- **Security Assertion:** Item-level aggregation is strictly per-tenant

#### Lifecycle
- **Setup Required:** Register User A and User B
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-037` — Verify POST /api/cart handles empty JSON body ({}) safely without server crash

#### Identity
- **Test ID:** `FR07-AI-037`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-24`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L119`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L119
- **Oracle Classification:** **`ROBUSTNESS PROBE`**

#### Test Design
- **Category:** Payload Robustness / Empty JSON Object
- **Test Objective:** Verify POST /api/cart handles empty JSON body ({}) safely without server crash
- **Test Condition:** Send POST /api/cart with empty body {}
- **Partition / Boundary:** P_Payload (Empty Object)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{}
```

#### Expected Result
- **Expected Semantic Behavior:** Server safely handles empty object with controlled response; does not crash process
- **Expected HTTP Status:** `Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)`
- **Expected Response Contract:** JSON error payload
- **State Assertion:** `Cart remains empty`
- **Security Assertion:** None

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

### `FR07-AI-038` — Verify POST /api/cart safely handles extra unexpected properties in request payload

#### Identity
- **Test ID:** `FR07-AI-038`
- **Origin:** AI
- **Feature:** FR-07 (Shopping Cart)
- **Coverage ID:** `COV-FR07-24`
- **Endpoint(s):** `POST /api/cart`

#### Traceability
- **Requirement Reference:** `FR-07 / api_specification.md L119`
- **SEC Reference:** `None`
- **Source Reference:** api_specification.md L119
- **Oracle Classification:** **`ROBUSTNESS PROBE`**

#### Test Design
- **Category:** Schema Robustness / Extra Unexpected Properties
- **Test Objective:** Verify POST /api/cart safely handles extra unexpected properties in request payload
- **Test Condition:** Send POST /api/cart with valid item plus extra fields: { id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2, adminNote: 'hack', discountBypass: true }
- **Partition / Boundary:** P_Payload (Extra Properties)
- **Preconditions:** Authenticated user
- **Initial Cart State:** Cart empty
- **Authentication State:** Valid customer JWT Bearer token

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Request Body (JSON):**
```json
{
  "id": 1,
  "name": "Sản phẩm A",
  "price": 100000,
  "quantity": 2,
  "adminNote": "hack",
  "discountBypass": true
}
```

#### Expected Result
- **Expected Semantic Behavior:** Server handles extra properties safely without crashing or corrupting cart state
- **Expected HTTP Status:** `200 OK / 400 (UNKNOWN by spec; controlled response)`
- **Expected Response Contract:** Controlled response payload
- **State Assertion:** `Server remains operational`
- **Security Assertion:** No parameter tampering or privilege escalation

#### Lifecycle
- **Setup Required:** Register fresh user
- **Cleanup Required:** None
- **Automation Status:** NOT AUTOMATED YET

---

