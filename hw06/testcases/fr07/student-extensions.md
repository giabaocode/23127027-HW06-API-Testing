# FR-07: Shopping Cart — Student Extension Tests Worksheet

> **Auditor Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature:** Pool B — FR-07: Shopping Cart (`GET /api/cart`, `POST /api/cart`)
> - **Requirement:** Minimum $\ge 5$ original extension test cases exploring coverage gaps, multi-step state transitions, race conditions, or protocol nuances beyond the AI test set.
> - **Truthful Authorship & Provenance Statement:** The 5 test ideas formalized below were surfaced during external AI brainstorming and subsequently selected and confirmed by the student (`Student Selection: CONFIRMED`). They are NOT represented as independently invented from scratch. Gemini performed the mechanical formalization and automation script generation.

---

## 1. Extension Summary Table

| Test ID | Origin | Student Selection | Target Dimension / Gap | Short Test Objective |
| :---: | :---: | :---: | :--- | :--- |
| **`FR07-STU-001`** | Student-selected from AI brainstorming | **CONFIRMED** | Protocol / Parser Robustness | Verify POST /api/cart handles syntactically malformed JSON body (missing closing brace) gracefully without crashing |
| **`FR07-STU-002`** | Student-selected from AI brainstorming | **CONFIRMED** | Protocol / MIME Handling | Verify POST /api/cart handles payload sent with wrong Content-Type (`text/plain`) safely without state corruption |
| **`FR07-STU-003`** | Student-selected from AI brainstorming | **CONFIRMED** | Security / Token Lifecycle | Verify POST /api/cart denies mutation when request carries a syntactically valid but expired JWT token (SEC-02) |
| **`FR07-STU-004`** | Student-selected from AI brainstorming | **CONFIRMED** | Business Rule / Metadata Conflict | Characterize cart behavior when same product ID is added twice with conflicting client-submitted name and price |
| **`FR07-STU-005`** | Student-selected from AI brainstorming | **CONFIRMED** | State / Read Idempotency | Verify repeated GET /api/cart requests on a populated cart are strictly idempotent and cause zero side-effects |

---

## 2. Detailed Extension Test Specifications

### `FR07-STU-001`: Syntactically Malformed JSON Request Body Robustness Probe

#### Identity & Traceability
- **Test ID:** `FR07-STU-001`
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** Pool B — FR-07 (Shopping Cart)
- **Requirement Reference:** FR-07 (`api_specification.md` Line 119)
- **SEC Reference:** Best Practice Parser Robustness (CWE-20)
- **Oracle Classification:** **`PARSER ROBUSTNESS / CHARACTERIZATION`**
- **Category:** Protocol Robustness / JSON Parser Syntax Failure

#### Test Design
- **Test Objective:** Verify backend JSON parser robustness when receiving syntactically malformed JSON missing a closing brace; verify that server handles the syntax error gracefully without process crash or cart corruption.
- **Preconditions:** SUT backend running on `http://localhost:3000`. Authenticated test user with known token.
- **Initial Cart State:** Empty cart (`[]`).
- **Authentication State:** Valid customer JWT Bearer token.

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Concrete Request Body (Raw Text):**
  ```text
  {"id":1,"name":"Sản phẩm A","price":100000,"quantity":1
  ```
  *(Note: Intentionally truncated to omit closing `}` brace; sent as raw unparsed text without Postman JSON auto-repair).*

#### Execution Steps
1. Send `POST /api/cart` with the raw malformed body.
2. Verify server remains alive and responds with controlled HTTP response.
3. Send `GET /api/cart` to verify cart state.

#### Expected Result
- **Expected Semantic Behavior:** Server body parser must catch syntax error cleanly; malformed payload must NOT mutate user's cart.
- **Expected HTTP Status:** `UNKNOWN by official specification` (Express `body-parser` typically returns `400 Bad Request`, treated as implementation-observed).
- **Expected Response Contract:** Controlled error response payload; no process crash.
- **State Assertion:** Subsequent `GET /api/cart` returns empty array `[]` (zero items added).
- **Security Assertion:** Robustness: process remains responsive; no unhandled exception crash (DoS prevention).

#### Lifecycle & Automation
- **Setup Required:** Register/login dedicated fresh test user.
- **Cleanup Required:** None (cart remains empty).
- **Automation Status:** READY FOR POSTMAN AUTOMATION (Requires raw body sending).

---

### `FR07-STU-002`: Wrong Content-Type Header (`text/plain`) Robustness Probe

#### Identity & Traceability
- **Test ID:** `FR07-STU-002`
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** Pool B — FR-07 (Shopping Cart)
- **Requirement Reference:** FR-07 (`api_specification.md` Line 119)
- **SEC Reference:** Best Practice MIME Type Enforcement
- **Oracle Classification:** **`BODY-PARSER ROBUSTNESS / CHARACTERIZATION`**
- **Category:** Protocol Robustness / MIME Type Handling

#### Test Design
- **Test Objective:** Probe SUT handling when a syntactically valid JSON body is transmitted with `Content-Type: text/plain` instead of `application/json`.
- **Test Condition:** Send valid cart JSON item with header `Content-Type: text/plain`.
- **Preconditions:** SUT backend running. Authenticated test user.
- **Initial Cart State:** Empty cart (`[]`).
- **Authentication State:** Valid customer JWT Bearer token.

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <VALID_USER_TOKEN>`
  - `Content-Type`: `text/plain`
  - `X-Student-Id`: `23127027`
- **Concrete Request Body (Raw Text):**
  ```text
  {"id":1,"name":"Sản phẩm A","price":100000,"quantity":1}
  ```

#### Execution Steps
1. Send `POST /api/cart` with `Content-Type: text/plain` and raw JSON payload.
2. Capture response status and body.
3. Send `GET /api/cart` to inspect visible cart state.

#### Expected Result
- **Expected Semantic Behavior:** Server handles unexpected MIME type deterministically without crashing. If rejected, cart remains empty; if accepted, cart structure remains internally consistent.
- **Expected HTTP Status:** `UNKNOWN by official specification` (Controlled response, e.g. 400, 415, or 200).
- **Expected Response Contract:** Controlled response payload.
- **State Assertion:** Server remains operational; cart does not contain unparsed raw string blobs.
- **Security Assertion:** Robustness: MIME mismatch does not trigger unhandled exception.

#### Lifecycle & Automation
- **Setup Required:** Register/login dedicated fresh test user.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR POSTMAN AUTOMATION (Explicit header override).

---

### `FR07-STU-003`: Expired JWT Token Authentication Denial Probe

#### Identity & Traceability
- **Test ID:** `FR07-STU-003`
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** Pool B — FR-07 (Shopping Cart)
- **Requirement Reference:** SEC-02 (`README.md` Line 279 — Mandatory Valid JWT)
- **SEC Reference:** `SEC-02 (Protected APIs require a VALID JWT Token)`
- **Oracle Classification:** **`SPECIFIED REJECTION (Semantic Denial) / UNKNOWN (HTTP Status)`**
- **Category:** Security / Token Lifecycle & Expiration

#### Test Design
- **Test Objective:** Verify POST /api/cart strictly denies cart mutation when the client presents a cryptographically signed JWT whose expiration timestamp (`exp`) has elapsed.
- **Test Condition:** Send `POST /api/cart` carrying a token signed with the SUT secret key having `exp < currentTime`.
- **Preconditions:** SUT backend running with JWT verification. Legitimate expired JWT generated via test setup.
- **Initial Cart State:** Empty cart (`[]`).
- **Authentication State:** Expired JWT token (`exp = Date.now() - 3600s`).

#### HTTP Request(s)
- **Method & Endpoint:** `POST /api/cart`
- **Headers:**
  - `Authorization`: `Bearer <EXPIRED_JWT_TOKEN>`
  - `Content-Type`: `application/json`
  - `X-Student-Id`: `23127027`
- **Concrete Request Body (JSON):**
  ```json
  {
    "id": 1,
    "name": "Sản phẩm A",
    "price": 100000,
    "quantity": 1
  }
  ```

#### Execution Steps
1. Generate legitimately signed expired token during pre-request setup.
2. Send `POST /api/cart` with the expired token.
3. Verify access denial.
4. Using valid token for the same user, verify `GET /api/cart` confirms zero mutation.

#### Expected Result
- **Expected Semantic Behavior:** Access denied; expired credentials must never permit shopping cart mutations (SEC-02).
- **Expected HTTP Status:** `UNKNOWN by official specification` (Middleware-observed status is `403 Forbidden` / `401 Unauthorized`).
- **Expected Response Contract:** Controlled error payload (schema UNKNOWN / IMPLEMENTATION-OBSERVED).
- **State Assertion:** Zero cart mutation executed; user cart remains empty.
- **Security Assertion:** SEC-02 token expiration verification enforced.

#### Lifecycle & Automation
- **Setup Required:** Generate expired token dynamically in Postman Pre-request script or environment variable.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR POSTMAN AUTOMATION.

---

### `FR07-STU-004`: Duplicate Product Addition with Conflicting Client Metadata Probe

#### Identity & Traceability
- **Test ID:** `FR07-STU-004`
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** Pool B — FR-07 (Shopping Cart)
- **Requirement Reference:** FR-07 (`README.md` Line 96 — Duplicate Product Accumulation)
- **SEC Reference:** None
- **Oracle Classification:** **`SPECIFIED BUSINESS RULE (Quantity) / CHARACTERIZATION (Metadata Resolution)`**
- **Category:** Business Logic / Metadata Conflict Resolution

#### Test Design
- **Test Objective:** Verify that adding the same product ID twice with conflicting client-supplied metadata (`name` and `price`) strictly obeys the duplicate accumulation rule ($q_1 + q_2$, 1 row) while characterizing metadata resolution behavior.
- **Test Condition:**
  - Step 1: POST product ID 1 with name: "Sản phẩm A", price: 100000, quantity: 2.
  - Step 2: POST product ID 1 with name: "Modified Product Name", price: 1, quantity: 3.
  - Step 3: GET /api/cart to inspect accumulated quantity and metadata.
- **Preconditions:** SUT running. Authenticated test user with empty cart.
- **Initial Cart State:** Empty cart (`[]`).
- **Authentication State:** Valid customer JWT Bearer token.

#### HTTP Request(s)
*Step 1:* `POST /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `Content-Type: application/json`, `X-Student-Id: 23127027`
- **Body:** `{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}`

*Step 2:* `POST /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `Content-Type: application/json`, `X-Student-Id: 23127027`
- **Body:** `{"id": 1, "name": "Modified Product Name", "price": 1, "quantity": 3}`

*Step 3:* `GET /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `X-Student-Id: 23127027`
- **Body:** None

#### Execution Steps
1. Execute Step 1 (first addition: q=2).
2. Execute Step 2 (conflicting addition: q=3, changed name/price).
3. Execute Step 3 (`GET /api/cart`).

#### Expected Result
- **Expected Semantic Behavior:**
  - **Specified Business Rule:** Exactly ONE row for product ID 1; accumulated quantity must equal 5 ($2 + 3$).
  - **Metadata Resolution (Characterization):** Official specification does not define whether first metadata is preserved, overwritten, or re-fetched from catalog. Characterize observed result.
- **Expected HTTP Status:** `All calls 200 OK (INFERRED)`.
- **Expected Response Contract:** Array containing exactly 1 item.
- **State Assertion:** `cart.length === 1 && cart[0].quantity === 5`.
- **Security Assertion:** None.

#### Lifecycle & Automation
- **Setup Required:** Register fresh test user.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR POSTMAN AUTOMATION.

---

### `FR07-STU-005`: Repeated GET /api/cart Idempotency and Non-Mutation Verification

#### Identity & Traceability
- **Test ID:** `FR07-STU-005`
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** Pool B — FR-07 (Shopping Cart)
- **Requirement Reference:** FR-07 (`api_specification.md` Line 115) / RFC 9110 (HTTP GET Idempotency)
- **SEC Reference:** None
- **Oracle Classification:** **`HTTP SEMANTICS / STATE ROBUSTNESS / CHARACTERIZATION`**
- **Category:** State Verification / Read Idempotency

#### Test Design
- **Test Objective:** Verify that calling `GET /api/cart` repeatedly against a populated cart is strictly idempotent, produces stable representations, and causes zero unintended side-effects or state mutations.
- **Test Condition:** Populate cart with product 1 (q=2); execute `GET /api/cart` (Run 1); execute `GET /api/cart` (Run 2); execute `GET /api/cart` (Run 3); compare state across all runs.
- **Preconditions:** SUT running. Authenticated test user.
- **Initial Cart State:** Empty cart.
- **Authentication State:** Valid customer JWT Bearer token.

#### HTTP Request(s)
*Step 1 (Setup):* `POST /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `Content-Type: application/json`, `X-Student-Id: 23127027`
- **Body:** `{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}`

*Step 2 (Read 1):* `GET /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `X-Student-Id: 23127027`

*Step 3 (Read 2):* `GET /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `X-Student-Id: 23127027`

*Step 4 (Read 3):* `GET /api/cart`
- **Headers:** `Authorization: Bearer <TOKEN>`, `X-Student-Id: 23127027`

#### Execution Steps
1. Populate cart with 1 item.
2. Send GET request 1, record array length, item ID, and quantity.
3. Send GET request 2, record array length, item ID, and quantity.
4. Send GET request 3, record array length, item ID, and quantity.
5. Assert state equivalence across all 3 reads.

#### Expected Result
- **Expected Semantic Behavior:** Read operation must never mutate state. Repeated retrieval must yield identical item count and property values.
- **Expected HTTP Status:** `200 OK (INFERRED) on all GET requests`.
- **Expected Response Contract:** Array of objects representing cart.
- **State Assertion:** `read1.length === read2.length === read3.length === 1 && read1[0].quantity === read2[0].quantity === read3[0].quantity === 2`.
- **Security Assertion:** None.

#### Lifecycle & Automation
- **Setup Required:** Register fresh test user and populate cart.
- **Cleanup Required:** None.
- **Automation Status:** READY FOR POSTMAN AUTOMATION.
