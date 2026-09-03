# FR-12: Access Control — Student Extension Test Cases

> **Auditor Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature Pool:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Status:** **STUDENT-AUTHORED EXTENSION TEST CASES**
> - **Requirement:** Minimum $\ge 5$ original extension test cases exploring cryptographic boundary conditions, role serialization edge cases, and privilege escalation vectors that AI missed, with explicit analysis of why AI missed them (Prompt quality, Model limitations, API characteristics per PDF Section 6.3).
> - **Duplication Check:** All 5 extension ideas were verified against all 38 reviewed AI test cases (`FR12-AI-001` to `FR12-AI-038`); zero duplication found.
> - **Governing Contract Authority:**
>   - `README.md`: Section 6 (FR-12 Lines 174–180), Section 9 (SEC-02 Line 279, SEC-03 Line 280)
>   - `api_specification.md`: Section 5.2, Section 6

---

## 1. Extension Strategy & Coverage Rationale

The 38 reviewed AI test cases cover standard anonymous access, standard authenticated user (`role = 'user'`) boundaries, and baseline administrative capabilities across all 14 real exposed operations. However, critical cryptographic and identity edge cases remain untested:
1. **Cryptographic Algorithm Confusion (`alg=none`):** Probing whether the JWT verification middleware rejects tokens claiming administrative privilege without any signature (`FR12-STU-001`).
2. **Temporal Validity Boundaries (`nbf` claim):** Probing whether tokens with valid signatures but future activation times (`nbf` in the future) are rejected before their validity window opens (`FR12-STU-002`).
3. **Role Claim String Normalization / Whitespace:** Testing whether exact string equality (`role === 'admin'`) is enforced against untrimmed whitespace strings like `" admin "` (`FR12-STU-003`).
4. **Role Type Confusion / Array Injection:** Testing whether non-string role types (`role: ["admin"]`) bypass or satisfy authorization checks (`FR12-STU-004`).
5. **Request-Body Privilege Override:** Testing whether client-supplied request body attributes (`"role": "admin"`) can override the authenticated identity verified from the JWT (`FR12-STU-005`).

---

## 2. Formalized Student Extension Test Cases

### FR12-STU-001 — Unsigned JWT using alg=none with role="admin"

#### Identity & Traceability
- **Test ID:** `FR12-STU-001`
- **Author:** Phạm Ngọc Gia Bảo (23127027)
- **Origin:** Student-Authored Extension Test
- **Why AI Missed This:**
  - **Prompt Quality:** Spec prompts asked for standard role testing (`admin` vs `user` vs anonymous), omitting algorithm-confusion cryptographic vectors.
  - **Model Limitations:** AI models assume modern JWT libraries safely reject `alg=none` by default and fail to generate RFC 7515 bypass vectors.
  - **API Characteristics:** Older or poorly configured instances of `jsonwebtoken` have known CVE bypasses with `alg=none`, making it a crucial penetration probe.
- **Feature:** Pool C — FR-12: Access Control
- **Coverage Category:** Security Robustness / Algorithm Confusion
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/users`
- **Contract Reference:** `README.md` Section 9 Line 279 (`SEC-02`)

#### Subject Identity & JWT State
- **Caller Type:** Attacker / Unauthenticated Client
- **JWT Token State:** Unsigned JWT token constructed with header `{"alg": "none", "typ": "JWT"}` and payload `{"id": 1, "username": "admin", "role": "admin"}`, trailing dot with no signature (`<header>.<payload>.`).
- **Embedded Role Claim:** `admin` (Unverified)

#### Test Execution & Request Specification
- **Request Headers:**
  - `Authorization: Bearer <base64Header>.<base64Payload>.`
  - `X-Student-Id: 23127027`
- **Request Body:** None

#### Expected Access-Control Outcome
- **Semantic Outcome:** **ACCESS DENIED** (SEC-02 Violation: Unsigned token cannot satisfy cryptographic authentication).
- **Expected HTTP Status:** `401 Unauthorized` or `403 Forbidden` (`INFERRED / IMPLEMENTATION-OBSERVED`; SUT jsonwebtoken defaults to 403 on verification failure).
- **Response Exposure Assertion:** Response body must not contain user list data or sensitive credentials.
- **Side-Effect Assertion:** Read-only probe; zero database mutation.
- **Setup & Cleanup:** None required.

---

### FR12-STU-002 — Validly signed admin JWT with future nbf claim

#### Identity & Traceability
- **Test ID:** `FR12-STU-002`
- **Author:** Phạm Ngọc Gia Bảo (23127027)
- **Origin:** Student-Authored Extension Test
- **Why AI Missed This:**
  - **Prompt Quality:** Authorization prompts focused on role permissions rather than temporal claim boundaries (`nbf`, `exp`).
  - **Model Limitations:** LLMs do not simulate future wall-clock timestamps unless specifically prompted for time-travel or temporal token validation.
  - **API Characteristics:** The SUT relies on `jsonwebtoken.verify()`, which requires explicit assertion testing for `NotBeforeError`.
- **Feature:** Pool C — FR-12: Access Control
- **Coverage Category:** Security Robustness / Temporal Claim Boundary
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/orders`
- **Contract Reference:** `README.md` Section 9 Line 279 (`SEC-02`)

#### Subject Identity & JWT State
- **Caller Type:** Administrator with premature token
- **JWT Token State:** Valid HMAC-SHA256 signature using test secret, role `admin`, valid `exp` in future, but `nbf` (Not Before) timestamp set to 1 hour in the future (`currentTime + 3600`).
- **Embedded Role Claim:** `admin`

#### Test Execution & Request Specification
- **Request Headers:**
  - `Authorization: Bearer <future_nbf_token>`
  - `X-Student-Id: 23127027`
- **Request Body:** None

#### Expected Access-Control Outcome
- **Semantic Outcome:** **ACCESS DENIED** (SEC-02 Violation: Token is not yet active; premature activation must be rejected).
- **Expected HTTP Status:** `401 Unauthorized` or `403 Forbidden` (`INFERRED / IMPLEMENTATION-OBSERVED`).
- **Response Exposure Assertion:** Response must not disclose system order records.
- **Side-Effect Assertion:** Read-only probe; zero database mutation.
- **Setup & Cleanup:** None required.

---

### FR12-STU-003 — Validly signed JWT with role=" admin " (whitespace padding)

#### Identity & Traceability
- **Test ID:** `FR12-STU-003`
- **Author:** Phạm Ngọc Gia Bảo (23127027)
- **Origin:** Student-Authored Extension Test
- **Why AI Missed This:**
  - **Prompt Quality:** Spec prompts used clean string literals for roles (`"admin"`, `"user"`).
  - **Model Limitations:** LLMs assume strings are pre-trimmed by serialization layers and overlook whitespace injection attacks.
  - **API Characteristics:** In JavaScript, `" admin " === "admin"` evaluates to `false`, but if middleware performs `.trim()` or regex matching, whitespace can cause unexpected bypasses.
- **Feature:** Pool C — FR-12: Access Control
- **Coverage Category:** Security Robustness / Role String Normalization
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/coupons`
- **Contract Reference:** `README.md` Section 9 Line 280 (`SEC-03`)

#### Subject Identity & JWT State
- **Caller Type:** Authenticated User with padded role claim
- **JWT Token State:** Valid HMAC-SHA256 signature, `exp` in future, but `role` payload property contains exact whitespace string `" admin "` (leading and trailing space).
- **Embedded Role Claim:** `" admin "`

#### Test Execution & Request Specification
- **Request Headers:**
  - `Authorization: Bearer <whitespace_role_token>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "code": "WSROLE_23127027",
  "discountPercent": 15,
  "validUntil": "2026-12-31T23:59:59Z"
}
```

#### Expected Access-Control Outcome
- **Semantic Outcome:** **ACCESS DENIED** (SEC-03 Violation: Exact role comparison requires `role === 'admin'`; untrimmed whitespace must not match).
- **Expected HTTP Status:** `403 Forbidden` (`INFERRED / IMPLEMENTATION-OBSERVED`).
- **Side-Effect Assertion:** Coupon `WSROLE_23127027` is NOT created in database (verified via admin `GET /api/coupons`).
- **Setup & Cleanup:** Defect-path cleanup: If created due to loose equality or trimming, delete `WSROLE_23127027` via admin credentials.

---

### FR12-STU-004 — Validly signed JWT with role as array ["admin"] (type confusion)

#### Identity & Traceability
- **Test ID:** `FR12-STU-004`
- **Author:** Phạm Ngọc Gia Bảo (23127027)
- **Origin:** Student-Authored Extension Test
- **Why AI Missed This:**
  - **Prompt Quality:** Prompts supplied schemas with `role: string`, never requesting polymorphic or type-confusion payloads.
  - **Model Limitations:** Generative models adhere to schema type contracts and rarely invent non-string primitives for scalar fields.
  - **API Characteristics:** In JavaScript, loose checks or array containers can cause authorization bypasses if `req.user.role` is handled unsafely.
- **Feature:** Pool C — FR-12: Access Control
- **Coverage Category:** Security Robustness / Role Type Confusion
- **HTTP Method:** `GET`
- **Target Endpoint:** `/api/admin/users`
- **Contract Reference:** `README.md` Section 9 Line 280 (`SEC-03`)

#### Subject Identity & JWT State
- **Caller Type:** Authenticated User with array role claim
- **JWT Token State:** Valid HMAC-SHA256 signature, valid `exp`, but `role` property is JSON array `["admin"]` rather than string `"admin"`.
- **Embedded Role Claim:** `["admin"]`

#### Test Execution & Request Specification
- **Request Headers:**
  - `Authorization: Bearer <array_role_token>`
  - `X-Student-Id: 23127027`
- **Request Body:** None

#### Expected Access-Control Outcome
- **Semantic Outcome:** **ACCESS DENIED** (SEC-03 Violation: Role must strictly equal string `'admin'`; array container must not satisfy authorization).
- **Expected HTTP Status:** `403 Forbidden` (`INFERRED / IMPLEMENTATION-OBSERVED`).
- **Response Exposure Assertion:** User list must not be exposed to non-string role caller.
- **Side-Effect Assertion:** Read-only probe; zero mutation.
- **Setup & Cleanup:** None required.

---

### FR12-STU-005 — Valid role="user" JWT plus client-supplied body role="admin"

#### Identity & Traceability
- **Test ID:** `FR12-STU-005`
- **Author:** Phạm Ngọc Gia Bảo (23127027)
- **Origin:** Student-Authored Extension Test
- **Why AI Missed This:**
  - **Prompt Quality:** Prompts focused on JWT header authorization and did not test conflicting authorization claims passed in the request body.
  - **Model Limitations:** LLMs assume backend authorization logic derives identity solely from the decoded JWT token, ignoring parameter pollution / body override attacks.
  - **API Characteristics:** If backend handlers merge `req.body` into `req.user` (mass assignment / parameter override), standard users can escalate privileges by supplying `"role": "admin"` in the JSON body.
- **Feature:** Pool C — FR-12: Access Control
- **Coverage Category:** Security Robustness / Request Parameter Privilege Escalation
- **HTTP Method:** `POST`
- **Target Endpoint:** `/api/admin/coupons`
- **Contract Reference:** `README.md` Section 9 Line 280 (`SEC-03`)

#### Subject Identity & JWT State
- **Caller Type:** Standard Authenticated User (`role = 'user'`)
- **JWT Token State:** Valid HMAC-SHA256 signature for standard user `phamngocgiabao` (`role = 'user'`).
- **Embedded Role Claim:** `user`

#### Test Execution & Request Specification
- **Request Headers:**
  - `Authorization: Bearer <standard_user_token>`
  - `Content-Type: application/json`
  - `X-Student-Id: 23127027`
- **Request Body:**
```json
{
  "code": "BODYOVERRIDE_23127027",
  "discountPercent": 25,
  "validUntil": "2026-12-31T23:59:59Z",
  "role": "admin"
}
```

#### Expected Access-Control Outcome
- **Semantic Outcome:** **ACCESS DENIED** (SEC-03 Violation: Standard user identity in verified JWT cannot be overridden by request body attributes).
- **Expected HTTP Status:** `403 Forbidden` (`INFERRED / IMPLEMENTATION-OBSERVED`).
- **Side-Effect Assertion:** Coupon `BODYOVERRIDE_23127027` is NOT created in database (verified via admin `GET /api/coupons`).
- **Setup & Cleanup:** Defect-path cleanup: If created due to request-body privilege override, delete `BODYOVERRIDE_23127027` via admin credentials.
