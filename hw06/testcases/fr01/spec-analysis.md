# FR-01: Account Registration — Specification Analysis (Final Calibrated)

> **Feature ID:** FR-01  
> **Pool:** Pool A — Authentication, Categories, and Products  
> **Target Endpoint:** `POST /api/register`  
> **Authoritative Sources:**
> - Course Assignment PDF: `2026.HW06.API Testing_En.pdf`
> - SUT API Specification: `api_specification.md` (Section 1.1)
> - System Requirements Specification (SRS): `README.md` (Section 2, FR-01; Section 9, SEC-01 & SEC-05)

---

## 1. Requirement Extraction & Strict Classification

| Property / Requirement | Official Stated Rule | Classification | Source Evidence / Rationale |
| :--- | :--- | :---: | :--- |
| **Endpoint** | `/api/register` | **SPECIFIED** | `api_specification.md` Line 12 |
| **HTTP Method** | `POST` | **SPECIFIED** | `api_specification.md` Line 12 |
| **Authentication** | None (Public endpoint) | **SPECIFIED** | `api_specification.md` Section 1 (No authorization header defined) |
| **Request Header** | `Content-Type: application/json` | **INFERRED** | Standard HTTP convention derived from JSON body representation |
| **Request Body Fields** | `name`, `email`, `password` | **SPECIFIED** | `api_specification.md` Lines 14–20; `README.md` Line 32 |
| **Field Requirement: `name`** | Full name, mandatory field presence | **SPECIFIED** | `README.md` Line 32: *"Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu."* |
| **Field Requirement: `email`** | Mandatory field, valid format (`user@domain.com`), unique | **SPECIFIED** | `README.md` Lines 32–33: *"Email phải có định dạng hợp lệ (user@domain.com) và là duy nhất trong hệ thống."* |
| **Field Requirement: `password`** | Mandatory field, strong complexity policy | **SPECIFIED** | `README.md` Line 34 |
| **Field Type: `name`** | String data type | **INFERRED FROM EXAMPLE** | Inferred from string value `"Nguyen Van A"` in example JSON payload |
| **Field Type: `email`** | String data type | **INFERRED FROM EXAMPLE** | Inferred from string value `"test@domain.com"` in example JSON payload |
| **Field Type: `password`** | String data type | **INFERRED FROM EXAMPLE** | Inferred from string value `"Password123!"` in example JSON payload |
| **Password Policy Rules** | Min 8 chars, $\ge 1$ uppercase, $\ge 1$ lowercase, $\ge 1$ digit, $\ge 1$ special char from set: `@`, `$`, `!`, `%`, `*`, `?`, `&` | **SPECIFIED** | `README.md` Line 34: *"Tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số và 1 ký tự đặc biệt (@, $, !, %, *, ?, &)."* |
| **Special Character Whitelist** | Prohibition of characters outside `@$!%*?&` | **UNKNOWN** | Spec requires *at least one* from set; it does NOT state whether other symbols are prohibited. |
| **Confirm Password** | GUI form validation requirement | **SPECIFIED** (UI) / **NOT SPECIFIED** (API) | `README.md` Line 35 specifies this for the form; omitted from API schema in `api_specification.md`. |
| **Success Status Code** | `200 OK` | **SPECIFIED** | `api_specification.md` Line 21: *"- Phản hồi thành công (200 OK): ..."* (`201 Created` is an INFERRED REST convention). |
| **Response Contains `message`** | Response body includes `message` property | **EXAMPLE-DERIVED** | Derived from documented example: `{"message": "User registered successfully", "id": 1}`. |
| **Response Contains `id`** | Response body includes `id` property | **EXAMPLE-DERIVED** | Derived from documented example: `{"message": "User registered successfully", "id": 1}`. |
| **Property Type: `message`** | `message` is a string | **INFERRED FROM EXAMPLE** | Inferred from `"User registered successfully"` in documented example. |
| **Property Type: `id`** | `id` is an integer | **INFERRED FROM EXAMPLE** | Inferred from numeric `1` in documented example. |
| **Constraint: `id >= 1`** | Primary key is a positive integer | **INFERRED** | Inferred from SQLite auto-increment behavior; not formally declared in text. |
| **Additional Properties Policy** | Whether non-sensitive extra keys are forbidden | **UNKNOWN / NOT SPECIFIED** | Official spec provides an example object, not a formal JSON Schema declaring `additionalProperties: false`. |
| **Exact Property Requirement** | Formal schema mandatory keys | **UNKNOWN** | Spec text does not formally specify schema constraints beyond the example. |
| **Duplicate Email Rejection** | Semantic rejection of duplicate email | **SPECIFIED** | `README.md` Line 33: Email must be unique. |
| **Duplicate Email HTTP Status** | Exact HTTP status code on duplicate (e.g. 400 or 409) | **UNKNOWN / INFERRED** | Unspecified in official documents. Standard REST conventions suggest 400 or 409. |
| **Validation Error HTTP Status** | Exact HTTP status on validation failure (e.g. 400) | **INFERRED** | Unspecified in official documents; 400 Bad Request is standard REST convention. |
| **Error Response Envelope** | JSON structure of error messages (`{"error": ...}`) | **UNKNOWN** | Unspecified in official documents. |
| **String Length Boundaries** | Max length for `name` and `password` | **UNKNOWN** | Unspecified in official documents. |
| **Security: SEC-01 Plaintext** | Password must NOT be stored in plaintext | **SPECIFIED** | `README.md` Line 278 (Requires Database/Backend layer verification). |
| **Security: SEC-05 SQLi** | Queries must use parameterized queries | **SPECIFIED** | `README.md` Line 282 (Input treated as literal data, query structure unaltered). |
| **Security: SEC-04 XSS** | UI rendering escaping | **NOT APPLICABLE TO API** | `README.md` Line 281 explicitly targets UI rendering, not backend JSON response transformation. |

---

## 2. Parameter Domain Analysis

### 2.1 Parameter: `name`
- **Data Type:** `string` (INFERRED FROM EXAMPLE)
- **Mandatory Presence:** Yes (SPECIFIED — field must be provided in request)
- **Domain Partitions & Conditional Expected Behavior:**
  - Standard ASCII name (e.g. `"Nguyen Van A"`) $\to$ **SPECIFIED / Happy Path** (Acceptance: SPECIFIED; Status: 200).
  - Vietnamese Unicode with diacritics (e.g. `"Nguyễn Văn An"`) $\to$ **INFERRED / ROBUSTNESS** (Acceptance: INFERRED; If accepted, status: 200).
  - Single-word name (`"Bao"`), multi-word, hyphenated (`"Jean-Luc"`), apostrophes (`"O'Connor"`) $\to$ **INFERRED / ROBUSTNESS** (Acceptance: INFERRED; If accepted, status: 200).
- **Invalid & Missing Partitions:**
  - Omitted `name` property from JSON body $\to$ **SPECIFIED Requirement Violation** (Rejection: SPECIFIED semantic; HTTP status: INFERRED).
  - `name: null` $\to$ **INFERRED Invalid** (Rejection: INFERRED).
  - Empty string `""` / whitespace-only `"   "` $\to$ **INFERRED Invalid** (Rejection: INFERRED).
  - Non-string types: integer (`123`), boolean (`true`), array (`["A"]`), object (`{}`) $\to$ **INFERRED Invalid** (Rejection: INFERRED).
- **Boundary & Robustness:**
  - Lower boundary: 1 character (`"A"`) $\to$ **ROBUSTNESS** (Acceptance: INFERRED).
  - Upper length (e.g. 1000 chars) $\to$ **ROBUSTNESS** (Acceptance: UNKNOWN; Expected Result: UNKNOWN; SQLite `TEXT` has no 255-char limit).
  - Literal SQL string (`"O'Connor"`) $\to$ **SPECIFIED (`SEC-05`) / ROBUSTNESS (Name Acceptance)**:
    - *Security Expectation (SPECIFIED):* Query structure is not altered, input treated as data, no unintended SQL executes, database integrity preserved.
    - *Name Acceptance (INFERRED / ROBUSTNESS):* The spec does not explicitly guarantee names with punctuation/SQL characters are accepted. Storing literally is one secure outcome; rejecting via clean input validation without SQL error is also secure.
  - Script tag probe (`"<script>alert(1)</script>"`) $\to$ **ROBUSTNESS INPUT — NOT SEC-04 API COVERAGE** (Ensures backend stores string safely without crashing; no HTML escaping expected at API JSON layer).

### 2.2 Parameter: `email`
- **Data Type:** `string` (INFERRED FROM EXAMPLE)
- **Mandatory Presence:** Yes (SPECIFIED)
- **Format Rule:** Must be valid format (`user@domain.com`) (SPECIFIED)
- **Uniqueness Rule:** Must be unique in system (SPECIFIED)
- **Valid Partitions & Conditional Expected Behavior:**
  - Standard format: `local-part@domain.tld` (e.g. `"user@domain.com"`) $\to$ **SPECIFIED** (Acceptance: SPECIFIED; Status: 200).
  - Plus-addressing (`user+tag@domain.com`), subdomains (`user@sub.domain.edu.vn`) $\to$ **INFERRED / RFC** (Acceptance: INFERRED; If accepted, status: 200).
- **Invalid Partitions:**
  - Omitted `email` property $\to$ **SPECIFIED Requirement Violation** (Rejection: SPECIFIED).
  - Missing `@` (`userdomain.com`), missing domain (`user@`), missing local part (`@domain.com`) $\to$ **SPECIFIED Format Violation** (Rejection: SPECIFIED).
  - Empty string `""`, spaces-only `"   "`, `null`, wrong types (number, boolean) $\to$ **INFERRED Invalid** (Rejection: INFERRED).
  - Pre-existing / duplicate email $\to$ **SPECIFIED Uniqueness Violation** (Expected semantic behavior: REJECT DUPLICATE; exact HTTP status: UNKNOWN / INFERRED).
  - SQL-like syntax (`' OR '1'='1'@domain.com`) $\to$ **SPECIFIED (`SEC-05`)** (Treated as data; rejected due to email format, NOT SQL execution; no SQLite crash).

### 2.3 Parameter: `password`
- **Data Type:** `string` (INFERRED FROM EXAMPLE)
- **Mandatory Presence:** Yes (SPECIFIED)
- **Documented 5-Rule Complexity Policy (`README.md` Line 34):**
  1. Minimum 8 characters in length
  2. At least 1 uppercase letter (`A-Z`)
  3. At least 1 lowercase letter (`a-z`)
  4. At least 1 digit (`0-9`)
  5. At least 1 special character from documented set: `@`, `$`, `!`, `%`, `*`, `?`, `&`
- **Valid Partitions & Conditional Expected Behavior:**
  - Meets all 5 criteria (e.g. `"Password123!"`) $\to$ **SPECIFIED Valid** (Acceptance: SPECIFIED; Status: 200).
  - Documented special characters (`@`, `$`, `&`) $\to$ **SPECIFIED Valid** (Acceptance: SPECIFIED; Status: 200).
  - Required symbol present + extra symbol (e.g. `"Password123!#"`) $\to$ **INFERRED Valid** (Acceptance: INFERRED; If accepted, status: 200. Policy requires $\ge 1$ from set; does not forbid extra symbols).
- **Invalid Partitions:**
  - Omitted `password` property $\to$ **SPECIFIED Requirement Violation** (Rejection: SPECIFIED).
  - Missing uppercase, missing lowercase, or missing digit $\to$ **SPECIFIED Policy Violation** (Rejection: SPECIFIED).
  - Missing required special character from set (e.g. `"Password1234"`) $\to$ **SPECIFIED Policy Violation** (Rejection: SPECIFIED).
  - Empty string `""`, spaces-only, `null`, wrong JSON types $\to$ **INFERRED Invalid** (Rejection: INFERRED).
- **Length Boundaries & Robustness:**
  - Length 7 (Just below minimum, $8 - 1$): `"Pass12!"` $\to$ **SPECIFIED Invalid** (Boundary: Rejection SPECIFIED).
  - Length 8 (Exact minimum boundary): `"Pass12!a"` $\to$ **SPECIFIED Valid** (Boundary: Acceptance SPECIFIED; Status: 200).
  - Length 9 (Just above minimum, $8 + 1$): `"Passw12!a"` $\to$ **SPECIFIED Valid** (Boundary: Acceptance SPECIFIED; Status: 200).
  - Extreme Upper Length (128 chars) $\to$ **ROBUSTNESS** (Boundary = UNKNOWN; Acceptance = UNKNOWN / ROBUSTNESS; Expected Contract Result = UNKNOWN. Spec has no upper limit).

---

## 3. Cross-Field & Extra-Field Behavior

1. **Email Uniqueness across System:**
   - First registration with unregistered email succeeds.
   - Immediate subsequent registration with the identical email must be semantically rejected.
2. **All Three Fields Mandatory:**
   - Omitting any of `{name, email, password}` or sending empty body `{}` violates the requirement.
3. **Unexpected Extra Field (`confirmPassword` / Field Pollution):**
   - Payload: `{"name": "...", "email": "...", "password": "...", "confirmPassword": "..."}`
   - *Classification:* **ROBUSTNESS TEST**.
   - *Expected Contract Behavior:* **UNKNOWN / INFERRED** (Acceptance: UNKNOWN; Backend may ignore extra field or reject; must not crash).

---

## 4. State-Dependent Behavior (Account Lifecycle)

FR-01 does not implement an order state machine. Its state-dependent behavior is strictly governed by **account existence in persistence**:

```
[State 0: Email unregistered in DB]
                 │
                 │ POST /api/register (valid payload)
                 ▼
[State 1: Account Created in DB, assigned ID]
                 │
                 │ Repeated POST /api/register (same email)
                 ▼
[State 2: Duplicate Registration Semantically Rejected]
```
- **Expected Semantic Outcome:** REJECT DUPLICATE (**SPECIFIED**).
- **Exact HTTP Status Code:** **UNKNOWN / INFERRED** (e.g. 400 or 409).

---

## 5. Security Applicability (SEC-01 & SEC-05)

### SEC-01: Password Plaintext Storage
- **Classification:** `REQUIRES NON-API VERIFICATION`.
- **Evidence:** `README.md` Line 278. The registration API returns `{message, id}`; it does not reveal password storage. Verifying that the password is NOT plaintext requires inspecting SQLite DB records (`SELECT password FROM users WHERE id = ?`).

### SEC-05: Parameterized Query / SQL Injection
- **Classification:** `DIRECTLY APPLICABLE`.
- **Evidence:** `README.md` Line 282. `POST /api/register` writes user records to the SQLite database.
- **Expected Security Behavior:**
  - Parameterized queries ensure input is treated strictly as **literal data**, NOT executable SQL commands.
  - Query structure is not altered, no unintended SQL command executes, and database integrity is preserved.
  - Storing names with apostrophes literally without query alteration is one secure outcome; input rejection without SQL errors is also secure.
  - For `email`, rejection of SQL-like payload (e.g. `' OR '1'='1'@test.com`) happens due to standard email syntax validation, not SQL execution.
  - Server must NOT fail due to SQL execution or database corruption.

### SEC-04: UI XSS Escaping
- **Classification:** `NOT APPLICABLE TO API LAYER`.
- SRS Line 281 explicitly targets UI display (`"khi hiển thị trên UI phải được escape đúng cách"`). Backend JSON APIs should store and return raw characters faithfully.

---

## 6. Response Contract Analysis: Example vs. Formal Schema

Documented in `api_specification.md` Line 21:
`- **Phản hồi thành công (200 OK):** {"message": "User registered successfully", "id": 1}`

The official specification provides an **example response**, not a formal JSON Schema specification. Therefore, assertions are strictly categorized:

| Response Element | Contract Rule | Classification | Official Source & Rationale |
| :--- | :--- | :---: | :--- |
| **HTTP Status Code** | `200 OK` | **SPECIFIED** | `api_specification.md` Line 21 explicitly states `200 OK`. |
| **Property: `message`** | Present in response body | **EXAMPLE-DERIVED** | Present in documented example JSON. |
| **Property: `id`** | Present in response body | **EXAMPLE-DERIVED** | Present in documented example JSON. |
| **Type of `message`** | String value | **INFERRED FROM EXAMPLE** | Inferred from `"User registered successfully"` in example. |
| **Type of `id`** | Numeric integer | **INFERRED FROM EXAMPLE** | Inferred from numeric `1` in example. |
| **Constraint: `id >= 1`** | Positive integer auto-increment | **INFERRED** | Inferred from SQLite auto-increment behavior; not formally stated in text. |
| **Additional Properties** | `additionalProperties: false` | **UNKNOWN / NOT SPECIFIED** | Official spec gives an example, not a schema forbidding extra metadata. |
| **Exact Property Requirement** | Formal schema mandatory rules | **UNKNOWN** | No formal JSON Schema schema-definition language is used in the specification. |
| **Credential Non-Leakage** | Response never leaks password/hash/token | **SECURITY-HARDENING ASSERTION** | Defense-in-depth security best practice, separate from explicit API contract. |

---

## 7. Specification vs. Implementation Register (Static Code Inspection)

Inspection of `backend/server.js` (Lines 20–30) and `backend/database.js` (Lines 50–61):

| ID | Specification Requirement | Static Implementation Observation | Classification |
| :--- | :--- | :--- | :--- |
| **DISC-01** | Password must NOT be stored in plaintext (`SEC-01`). | `server.js` Line 23: `INSERT INTO users (name, email, password) VALUES (?, ?, ?)`. The raw password string from `req.body` is inserted directly into SQLite without hashing. | **STATIC-ANALYSIS DEFECT CANDIDATE** (Pending runtime confirmation) |
| **DISC-02** | Email must be unique in system (`README.md` Line 33). | `database.js` Line 53: Column is defined as `email TEXT` without a `UNIQUE` constraint. `server.js` Line 20 performs NO duplicate email check before inserting. Duplicate emails will be silently inserted into the database. | **STATIC-ANALYSIS DEFECT CANDIDATE** (Pending runtime confirmation) |
| **DISC-03** | Password complexity policy enforced (`README.md` Line 34). | `server.js` Line 20 performs zero validation on password length, upper, lower, digits, or symbols. | **STATIC-ANALYSIS DEFECT CANDIDATE** (Pending runtime confirmation) |
| **DISC-04** | Email format must be valid (`README.md` Line 33). | `server.js` Line 20 performs zero regex or format check on email. | **STATIC-ANALYSIS DEFECT CANDIDATE** (Pending runtime confirmation) |
| **DISC-05** | All fields (`name`, `email`, `password`) required (`README.md` Line 32). | `server.js` Line 20 does not validate presence of fields; inserts `null`/`undefined`. | **STATIC-ANALYSIS DEFECT CANDIDATE** (Pending runtime confirmation) |
| **DISC-06** | Success status `200 OK` (`api_specification.md` Line 21). | `server.js` Line 27: `res.json(...)` returns status 200. | **MATCHES SPEC** |
| **DISC-07** | Parameterized query (`SEC-05`). | `server.js` Line 23 uses `db.run(query, [name, email, password])` with parameter placeholders. | **MATCHES SPEC** |

---

## 8. Policy for Future Test Generation: One Concrete Condition Per Test

During future test case generation (Phase 2):
- **ONE Concrete Condition per Generated Test:** Each test case must evaluate exactly **ONE clearly identifiable input/condition combination** and **ONE traceable expected outcome**.
- **No Amorphous Multi-Condition Tests:** Tests will not be combined into vague multi-error buckets (e.g., "test missing @, missing domain, and spaces all together"). Each condition will have its own traceable case or data row.
- **Audit & Traceability Readiness:** Every generated test must support:
  1. Independent human audit (`Student Verdict`: VALID / INVALID / INCOMPLETE, reasoning, correction).
  2. Independent execution traceability in Newman and Postman Console.
  3. Independent pass/fail result recording.
