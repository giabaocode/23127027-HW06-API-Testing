# FR-01: Account Registration — Original AI-Generated Test Cases

> **Notice on Document Status:** This is the immutable original AI-generated testcase set for **FR-01 (Account Registration)**. In accordance with the course academic integrity and anti-cheat policies, this file preserves the unmodified initial AI generation prior to student audit. Human corrections and verdicts must be recorded separately in `human-audit.md` to ensure full traceability for the AI Audit and AI Critique.

- **Feature:** FR-01 — Account Registration (`POST /api/register`)
- **Total Test Cases Generated:** Exactly 38
  - **API-Executable Cases:** 37
  - **Non-API Security Verification Cases:** 1 (`FR01-AI-037` for SEC-01 DB inspection)
- **Origin:** AI (Antigravity / Gemini 3.7 Flash)
- **Traceability Authority:** `hw06/testcases/fr01/spec-analysis.md` and `hw06/testcases/fr01/coverage-matrix.md`

---

## Test Cases Detailed Specification

### FR01-AI-001: Standard Valid ASCII Name Registration
#### Identity
- **Test ID:** FR01-AI-001
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-01

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Lines 32–34)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 14–21; `README.md` Line 32
- **Oracle Classification:** SPECIFIED (Status 200, Field Presence); EXAMPLE-DERIVED (Body properties `message`, `id`); INFERRED FROM EXAMPLE (Types)

#### Test Design
- **Category:** Functional / Positive Happy Path
- **Test Objective:** Verify that a standard registration request with a standard ASCII alphabetic name is successfully processed.
- **Test Condition:** Valid standard name, valid unique email, strong password meeting all 5 criteria.
- **Partition / Boundary:** `name` standard ASCII valid partition.
- **Preconditions:** SUT backend running on `http://localhost:3000`.
- **Initial State:** Target email `fr01_ai_001@example.com` does not exist in SQLite database.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Nguyen Van A",
    "email": "fr01_ai_001@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** User account is created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and integer `id` (EXAMPLE-DERIVED / INFERRED FROM EXAMPLE).
- **Security Assertion:** Response body must not leak plaintext password or credentials.
- **State Assertion:** A new user record is inserted into SQLite `users` table.

#### Lifecycle
- **Setup Required:** Ensure database initialized.
- **Cleanup Required:** Delete created user row (`DELETE FROM users WHERE email = 'fr01_ai_001@example.com'`).
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-002: Vietnamese Unicode Name with Diacritics
#### Identity
- **Test ID:** FR01-AI-002
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-02

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 32
- **Oracle Classification:** INFERRED / ROBUSTNESS (Diacritic Acceptance); SPECIFIED (Status 200 if accepted); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Positive Localization Robustness
- **Test Objective:** Verify system behavior when registering with a Vietnamese Unicode full name containing complex diacritics.
- **Test Condition:** `name` with UTF-8 multi-byte characters (`"Trần Thị Bích Hạnh"`).
- **Partition / Boundary:** `name` Unicode diacritics partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_002@example.com` does not exist in database.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json; charset=utf-8`
- **Request Body:**
  ```json
  {
    "name": "Trần Thị Bích Hạnh",
    "email": "fr01_ai_002@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Input Acceptance is INFERRED / ROBUSTNESS. If the system accepts localized UTF-8 names, account creation succeeds.
- **Expected HTTP Status:** If accepted, documented status is `200 OK` (SPECIFIED).
- **Expected Response Contract:** If status 200, body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No server crash, UTF-8 strings handled safely.
- **State Assertion:** If created, user name is persisted without character corruption.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-003: Omitted Mandatory Name Field
#### Identity
- **Test ID:** FR01-AI-003
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-03

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 32 ("Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu")
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Input Validation
- **Test Objective:** Verify that omitting the required `name` property results in rejection.
- **Test Condition:** JSON payload completely omits the `name` key.
- **Partition / Boundary:** Missing mandatory field partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "email": "fr01_ai_003@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected because `name` is a mandatory field (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED REST convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** Server must not crash with unhandled exception.
- **State Assertion:** Zero rows inserted into SQLite `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Verify no cleanup needed.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-004: Empty String Name Value
#### Identity
- **Test ID:** FR01-AI-004
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-04

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 32
- **Oracle Classification:** INFERRED (Semantic Rejection & HTTP Status 400)

#### Test Design
- **Category:** Negative / Boundary Validation
- **Test Objective:** Verify that providing an empty string `""` for `name` is rejected.
- **Test Condition:** `name` is empty string `""` (length 0).
- **Partition / Boundary:** Blank/empty string boundary.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "",
    "email": "fr01_ai_004@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected as a blank name does not satisfy providing full name (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero records inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Verify no row created.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-005: Non-String Integer Name Data Type
#### Identity
- **Test ID:** FR01-AI-005
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-05

#### Traceability
- **Requirement / FR Reference:** FR-01 (`api_specification.md` Line 16)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 16
- **Oracle Classification:** INFERRED FROM EXAMPLE (Type Expectation); INFERRED (Rejection)

#### Test Design
- **Category:** Negative / Type Safety
- **Test Objective:** Verify that supplying a numeric integer value for `name` is rejected.
- **Test Condition:** `name` is JSON integer `12345`.
- **Partition / Boundary:** Wrong data type partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": 12345,
    "email": "fr01_ai_005@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected due to invalid data type (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** Backend JSON parser handles type safely without internal crash.
- **State Assertion:** No database insertion.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-006: Extreme Upper Length Name Robustness (1000 Characters)
#### Identity
- **Test ID:** FR01-AI-006
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-06

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 32 (Max length is UNKNOWN)
- **Oracle Classification:** ROBUSTNESS; UNKNOWN (Specification Oracle & Boundary)

#### Test Design
- **Category:** Robustness / Extreme Input
- **Test Objective:** Probe backend resilience and string handling when an unusually long name (1000 characters) is supplied.
- **Test Condition:** `name` is 1000 repeated ASCII characters (`"A" * 1000`).
- **Partition / Boundary:** Upper length boundary = UNKNOWN.
- **Preconditions:** Backend running.
- **Initial State:** Email `fr01_ai_006@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "email": "fr01_ai_006@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Specification Oracle is UNKNOWN (The specification defines no max length; SQLite `TEXT` has no 255-char limit).
- **Expected HTTP Status:** UNKNOWN by official specification. Either clean rejection (400) or acceptance (200) may occur.
- **Expected Response Contract:** Parseable JSON response; no unhandled HTML error stack dump.
- **Security Assertion:** Server must not crash, buffer overflow, or suffer denial of service.
- **State Assertion:** Database integrity preserved.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if accepted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-007: Literal SQL Syntax Handling in Name (SEC-05)
#### Identity
- **Test ID:** FR01-AI-007
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-07

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** SEC-05 (`README.md` Line 282 — Parameterized Query)
- **Source Reference:** `README.md` Line 282
- **Oracle Classification:** SPECIFIED (SEC-05 Property); INFERRED / ROBUSTNESS (Name Acceptance)

#### Test Design
- **Category:** Security / SEC-05 Parameterized Query Verification
- **Test Objective:** Verify that input containing SQL apostrophes and syntax is treated strictly as literal data without altering query structure or executing unintended SQL.
- **Test Condition:** `name` contains apostrophe and SQL syntax (`"O'Connor"`).
- **Partition / Boundary:** Syntax character boundary.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_007@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "O'Connor",
    "email": "fr01_ai_007@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** SEC-05 requirement is that the query structure is not broken and input is treated as literal data (SPECIFIED). Acceptance of apostrophes in names is INFERRED / ROBUSTNESS. Successful literal storage is secure; clean input-validation rejection is also secure.
- **Expected HTTP Status:** If accepted, documented status is `200 OK` (SPECIFIED). If rejected by name policy, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** No SQLite syntax error in response body.
- **Security Assertion:** Query structure must not be altered; no SQL syntax error (e.g. `SQLITE_ERROR: unrecognized token`) must occur.
- **State Assertion:** If stored, value is preserved literally without altering other database records.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-008: HTML Script Tag Robustness Probe in Name
#### Identity
- **Test ID:** FR01-AI-008
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-08

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A (ROBUSTNESS INPUT — NOT SEC-04 API COVERAGE)
- **Source Reference:** `README.md` Line 32; SRS Line 281 context
- **Oracle Classification:** ROBUSTNESS; INFERRED (Acceptance)

#### Test Design
- **Category:** Robustness / Data Preservation
- **Test Objective:** Verify backend stores HTML strings safely without crashing; confirm API JSON layer does not alter raw data.
- **Test Condition:** `name` contains `<script>alert(1)</script>`.
- **Partition / Boundary:** HTML tag syntax boundary.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_008@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "<script>alert(1)</script>",
    "email": "fr01_ai_008@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Backend safely handles string data without crash (ROBUSTNESS). No HTML escaping is expected at backend API JSON layer (SEC-04 is GUI only).
- **Expected HTTP Status:** If accepted, documented status is `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` if accepted.
- **Security Assertion:** Server must not crash or execute code.
- **State Assertion:** Data stored as literal raw characters without alteration.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-009: Standard Valid RFC Email Format
#### Identity
- **Test ID:** FR01-AI-009
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-09

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 17; `README.md` Line 33
- **Oracle Classification:** SPECIFIED (Status 200, Format Rule); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Positive Happy Path
- **Test Objective:** Verify registration succeeds with a standard RFC 5322 email format.
- **Test Condition:** Standard valid email format (`user@domain.com`).
- **Partition / Boundary:** Standard email format valid partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_009@domain.com` does not exist in SQLite database.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Standard User",
    "email": "fr01_ai_009@domain.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and integer `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** New row exists in `users` table with email `fr01_ai_009@domain.com`.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-010: Advanced RFC Email with Plus-Addressing
#### Identity
- **Test ID:** FR01-AI-010
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-10

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 33
- **Oracle Classification:** INFERRED / RFC (Syntax Acceptance); SPECIFIED (Status 200 if accepted)

#### Test Design
- **Category:** Functional / RFC Syntax Compatibility
- **Test Objective:** Verify email handling when plus-addressing (`user+tag@domain.com`) is provided.
- **Test Condition:** Email local part contains `+tag`.
- **Partition / Boundary:** Advanced RFC syntax partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_010+hw06@domain.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Tagged User",
    "email": "fr01_ai_010+hw06@domain.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Acceptance of plus-addressing is INFERRED / RFC. If RFC-compliant regex is used, registration succeeds.
- **Expected HTTP Status:** If accepted, documented status is `200 OK` (SPECIFIED).
- **Expected Response Contract:** If status 200, body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No server crash.
- **State Assertion:** Email stored faithfully with plus sign.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-011: Omitted Mandatory Email Field
#### Identity
- **Test ID:** FR01-AI-011
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-11

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 32
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Input Validation
- **Test Objective:** Verify that omitting the required `email` property results in rejection.
- **Test Condition:** JSON payload omits the `email` key.
- **Partition / Boundary:** Missing mandatory field partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No Email User",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected because `email` is mandatory (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-012: Empty String Email Value
#### Identity
- **Test ID:** FR01-AI-012
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-12

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Lines 32–33)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Lines 32–33
- **Oracle Classification:** INFERRED (Semantic Rejection & HTTP Status 400)

#### Test Design
- **Category:** Negative / Boundary Validation
- **Test Objective:** Verify that providing an empty string `""` for `email` is rejected.
- **Test Condition:** `email` is empty string `""`.
- **Partition / Boundary:** Blank/empty string boundary.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Empty Email User",
    "email": "",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected as empty string violates email presence and format rules (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-013: Malformed Email Missing At-Symbol (@)
#### Identity
- **Test ID:** FR01-AI-013
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-13

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33 — Format Rule)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 33 ("Email phải có định dạng hợp lệ (user@domain.com)")
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Format Syntax Validation
- **Test Objective:** Verify that an email lacking the `@` symbol is rejected.
- **Test Condition:** `email` string is `"fr01_ai_013_userdomain.com"` (no `@`).
- **Partition / Boundary:** Malformed email syntax partition (missing `@`).
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No At User",
    "email": "fr01_ai_013_userdomain.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected due to invalid email format (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-014: Malformed Email Missing Domain Part
#### Identity
- **Test ID:** FR01-AI-014
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-13

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33 — Format Rule)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 33
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Format Syntax Validation
- **Test Objective:** Verify that an email lacking the domain portion after `@` is rejected.
- **Test Condition:** `email` string is `"fr01_ai_014_user@"`.
- **Partition / Boundary:** Malformed email syntax partition (missing domain).
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No Domain User",
    "email": "fr01_ai_014_user@",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected due to invalid email format (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-015: Non-String Integer Email Data Type
#### Identity
- **Test ID:** FR01-AI-015
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-14

#### Traceability
- **Requirement / FR Reference:** FR-01 (`api_specification.md` Line 17)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 17
- **Oracle Classification:** INFERRED FROM EXAMPLE (Type Expectation); INFERRED (Rejection)

#### Test Design
- **Category:** Negative / Type Safety
- **Test Objective:** Verify that supplying a numeric integer value for `email` is rejected.
- **Test Condition:** `email` is JSON integer `99999`.
- **Partition / Boundary:** Wrong data type partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Type User",
    "email": 99999,
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected due to wrong data type (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-016: Duplicate Registration of Pre-Seeded Email
#### Identity
- **Test ID:** FR01-AI-016
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-15

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33 — Uniqueness Rule)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 33 ("Email... là duy nhất trong hệ thống")
- **Oracle Classification:** SPECIFIED (Semantic Rejection); UNKNOWN / INFERRED (HTTP Status 400/409)

#### Test Design
- **Category:** Negative / Uniqueness & State Verification
- **Test Objective:** Verify that attempting to register an email that already exists in the system (pre-seeded user `test@eshop.com`) is rejected.
- **Test Condition:** `email` is identical to existing user `test@eshop.com`.
- **Partition / Boundary:** Duplicate email partition.
- **Preconditions:** Database initialized with default seeds (`backend/database.js`).
- **Initial State:** User `test@eshop.com` exists in SQLite `users` table.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Duplicate SeedTest",
    "email": "test@eshop.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** REJECT DUPLICATE — System must reject duplicate email registration (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; potential conventional values are `400 Bad Request` or `409 Conflict` (INFERRED).
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash; database must not silently insert a duplicate row.
- **State Assertion:** Total count of users with `email = 'test@eshop.com'` remains exactly 1.

#### Lifecycle
- **Setup Required:** Verify seed user exists.
- **Cleanup Required:** None (seed user must be preserved).
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-017: Duplicate Registration via Dynamic Sequential Registration
#### Identity
- **Test ID:** FR01-AI-017
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-15

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33 — Uniqueness Rule)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 33
- **Oracle Classification:** SPECIFIED (Semantic Rejection); UNKNOWN / INFERRED (HTTP Status 400/409)

#### Test Design
- **Category:** State-Dependent / Duplicate Lifecycle
- **Test Objective:** Verify account lifecycle state transition: initial registration succeeds, immediate repeated registration with the exact same email is rejected.
- **Test Condition:** Step 1: Register `fr01_ai_017@example.com` (succeeds). Step 2: Register again with identical email (must fail).
- **Partition / Boundary:** State-dependent duplicate email transition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_017@example.com` unregistered prior to Step 1.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body (Step 2 Repeat):**
  ```json
  {
    "name": "Second Instance",
    "email": "fr01_ai_017@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** REJECT DUPLICATE (SPECIFIED) on Step 2.
- **Expected HTTP Status:** UNKNOWN / INFERRED (e.g. 400 or 409).
- **Expected Response Contract:** Error envelope on duplicate attempt.
- **Security Assertion:** No server crash; no duplicate row created.
- **State Assertion:** Exactly one row exists with `email = 'fr01_ai_017@example.com'`.

#### Lifecycle
- **Setup Required:** Execute Step 1 registration first.
- **Cleanup Required:** Delete created user row after test execution.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-018: Case-Insensitive Duplicate Email Rejection
#### Identity
- **Test ID:** FR01-AI-018
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-16

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 33
- **Oracle Classification:** INFERRED (Case-Insensitive Uniqueness Rule & HTTP Status)

#### Test Design
- **Category:** Negative / Data Canonicalization
- **Test Objective:** Verify whether email uniqueness is enforced case-insensitively (`User@Domain.com` vs `user@domain.com`).
- **Test Condition:** Target email differs only by character case from an existing account (`TEST@eshop.com` vs `test@eshop.com`).
- **Partition / Boundary:** Case variation boundary.
- **Preconditions:** Seed user `test@eshop.com` exists.
- **Initial State:** User `test@eshop.com` in database.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Case User",
    "email": "TEST@eshop.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Semantic rejection is INFERRED (Standard industry practice treats email domain and local parts case-insensitively for uniqueness).
- **Expected HTTP Status:** UNKNOWN / INFERRED (400 or 409).
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No duplicate account created with different casing.
- **State Assertion:** Single record in database.

#### Lifecycle
- **Setup Required:** Seed user present.
- **Cleanup Required:** If SUT erroneously inserts, delete the uppercase user record.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-019: SQL-Like Syntax Handling in Email (SEC-05)
#### Identity
- **Test ID:** FR01-AI-019
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-17

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** SEC-05 (`README.md` Line 282 — Parameterized Query)
- **Source Reference:** `README.md` Line 282
- **Oracle Classification:** SPECIFIED (SEC-05 Property); INFERRED (Email Format Rejection)

#### Test Design
- **Category:** Security / SEC-05 SQL Injection Resistance
- **Test Objective:** Verify parameterized query treats SQL syntax in email as data; verify rejection occurs cleanly via email validation without SQL engine crash.
- **Test Condition:** `email` contains SQL injection payload (`"' OR '1'='1'@domain.com"`).
- **Partition / Boundary:** Syntax boundary in email field.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "SQLi Email User",
    "email": "' OR '1'='1'@domain.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Input is treated strictly as data. Rejection occurs because of invalid email format, NOT SQL syntax execution (SPECIFIED SEC-05).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** No SQLite syntax error in response body.
- **Security Assertion:** Query structure not altered; no unauthorized database modification; no SQL error dump.
- **State Assertion:** Zero rows inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Verify no row created.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-020: Standard Strong Password Meeting All 5 Criteria
#### Identity
- **Test ID:** FR01-AI-020
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-18

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 18; `README.md` Line 34
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Positive Happy Path
- **Test Objective:** Verify that a password satisfying all 5 policy criteria ($\ge 8$ chars, uppercase, lowercase, digit, special character) is accepted.
- **Test Condition:** Password `"Password123!"` (12 chars, 'P', 'assword', '123', '!').
- **Partition / Boundary:** Standard strong password valid partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_020@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Strong Pass User",
    "email": "fr01_ai_020@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and integer `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-021: Documented Special Symbol Coverage: At-Sign (@)
#### Identity
- **Test ID:** FR01-AI-021
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-19

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 (Documented symbol set includes `@`)
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Password Policy Domain Coverage
- **Test Objective:** Verify password policy accepts special character `@` from the documented set.
- **Test Condition:** Password contains `@` as its special character (`"Passw0rd@"`).
- **Partition / Boundary:** Documented special character `@` partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_021@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Symbol At User",
    "email": "fr01_ai_021@example.com",
    "password": "Passw0rd@"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Password policy requirement is satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-022: Documented Special Symbol Coverage: Dollar-Sign ($)
#### Identity
- **Test ID:** FR01-AI-022
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-19

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 (Documented symbol set includes `$`)
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Password Policy Domain Coverage
- **Test Objective:** Verify password policy accepts special character `$` from the documented set.
- **Test Condition:** Password contains `$` as its special character (`"Passw0rd$"`).
- **Partition / Boundary:** Documented special character `$` partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_022@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Symbol Dollar User",
    "email": "fr01_ai_022@example.com",
    "password": "Passw0rd$"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Password policy requirement is satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-023: Documented Special Symbol Coverage: Ampersand (&)
#### Identity
- **Test ID:** FR01-AI-023
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-19

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 (Documented symbol set includes `&`)
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Password Policy Domain Coverage
- **Test Objective:** Verify password policy accepts special character `&` from the documented set.
- **Test Condition:** Password contains `&` as its special character (`"Passw0rd&"`).
- **Partition / Boundary:** Documented special character `&` partition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_023@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Symbol Amp User",
    "email": "fr01_ai_023@example.com",
    "password": "Passw0rd&"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Password policy requirement is satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-024: Required Special Symbol Plus Extra Symbol (Non-Whitelist Interpretation)
#### Identity
- **Test ID:** FR01-AI-024
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-20

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34
- **Oracle Classification:** INFERRED Valid (Policy Interpretation); SPECIFIED (Status 200 if accepted)

#### Test Design
- **Category:** Functional / Non-Whitelist Policy Interpretation
- **Test Objective:** Verify behavior when password contains a required symbol (`!`) plus an additional symbol (`#`).
- **Test Condition:** Password is `"Password123!#"`.
- **Partition / Boundary:** Policy requires $\ge 1$ from set; specification contains no whitelist prohibition.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_024@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Combo Symbol User",
    "email": "fr01_ai_024@example.com",
    "password": "Password123!#"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Acceptance is INFERRED Valid because the password satisfies having at least 1 character from `@$!%*?&` and no explicit whitelist bans `#`.
- **Expected HTTP Status:** If accepted, documented status is `200 OK` (SPECIFIED).
- **Expected Response Contract:** If status 200, body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted if accepted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-025: Missing Required Special Character from Set
#### Identity
- **Test ID:** FR01-AI-025
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-21

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("có ít nhất 1 ký tự đặc biệt (@, $, !, %, *, ?, &)")
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Password Policy Violation
- **Test Objective:** Verify that a password lacking any special character from the required set is rejected.
- **Test Condition:** Password is `"Password1234"` (alphanumeric only, zero special symbols).
- **Partition / Boundary:** Missing special character partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No Symbol User",
    "email": "fr01_ai_025@example.com",
    "password": "Password1234"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected for violating the password complexity policy (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-026: Password Length Boundary: 7 Characters (Minimum - 1)
#### Identity
- **Test ID:** FR01-AI-026
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-22

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34 — Length Boundary)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("Tối thiểu 8 ký tự")
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Boundary Value Analysis ($8 - 1$)
- **Test Objective:** Verify that a password of length 7 (just below the 8-character minimum) is rejected even if all character classes are present.
- **Test Condition:** Password `"Pass1!a"` (length 7, has upper, lower, digit, special).
- **Partition / Boundary:** Lower boundary just below minimum ($8 - 1$).
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Len 7 User",
    "email": "fr01_ai_026@example.com",
    "password": "Pass1!a"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected because password length is less than 8 characters (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-027: Password Length Boundary: 8 Characters (Exact Minimum)
#### Identity
- **Test ID:** FR01-AI-027
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-22

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34 — Length Boundary)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("Tối thiểu 8 ký tự")
- **Oracle Classification:** SPECIFIED (Status 200, Minimum Boundary); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Boundary Value Analysis ($8$)
- **Test Objective:** Verify that a password of exactly 8 characters meeting all character classes is accepted.
- **Test Condition:** Password `"Pass12!a"` (exact length 8, upper, lower, digit, special).
- **Partition / Boundary:** Exact minimum length boundary ($8$).
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_027@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Len 8 User",
    "email": "fr01_ai_027@example.com",
    "password": "Pass12!a"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Password minimum length requirement is satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-028: Password Length Boundary: 9 Characters (Minimum + 1)
#### Identity
- **Test ID:** FR01-AI-028
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-22

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34 — Length Boundary)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("Tối thiểu 8 ký tự")
- **Oracle Classification:** SPECIFIED (Status 200, Boundary Just Above Minimum); EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Functional / Boundary Value Analysis ($8 + 1$)
- **Test Objective:** Verify that a password of 9 characters (just above the 8-character minimum) is accepted.
- **Test Condition:** Password `"Passw12!a"` (exact length 9, upper, lower, digit, special).
- **Partition / Boundary:** Boundary just above minimum ($8 + 1$).
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_028@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Len 9 User",
    "email": "fr01_ai_028@example.com",
    "password": "Passw12!a"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Password satisfies minimum length requirement (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** User record inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-029: Missing Uppercase Letter in Password
#### Identity
- **Test ID:** FR01-AI-029
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-23

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("có ít nhất 1 chữ hoa")
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Character Class Policy Violation
- **Test Objective:** Verify that a password missing an uppercase letter is rejected.
- **Test Condition:** Password `"password123!"` (has lower, digit, special, len 12; zero uppercase).
- **Partition / Boundary:** Missing uppercase character class partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No Upper User",
    "email": "fr01_ai_029@example.com",
    "password": "password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected for violating uppercase letter requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-030: Missing Lowercase Letter in Password
#### Identity
- **Test ID:** FR01-AI-030
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-23

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("có ít nhất 1 chữ thường")
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Character Class Policy Violation
- **Test Objective:** Verify that a password missing a lowercase letter is rejected.
- **Test Condition:** Password `"PASSWORD123!"` (has upper, digit, special, len 12; zero lowercase).
- **Partition / Boundary:** Missing lowercase character class partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No Lower User",
    "email": "fr01_ai_030@example.com",
    "password": "PASSWORD123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected for violating lowercase letter requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-031: Missing Numeric Digit in Password
#### Identity
- **Test ID:** FR01-AI-031
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-23

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 ("có ít nhất 1 chữ số")
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Character Class Policy Violation
- **Test Objective:** Verify that a password missing a numeric digit is rejected.
- **Test Condition:** Password `"Password!@#$"` (has upper, lower, special, len 12; zero digits).
- **Partition / Boundary:** Missing digit character class partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "No Digit User",
    "email": "fr01_ai_031@example.com",
    "password": "Password!@#$"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected for violating digit requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-032: Empty String Password Value
#### Identity
- **Test ID:** FR01-AI-032
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-24

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Lines 32–34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Lines 32–34
- **Oracle Classification:** INFERRED (Semantic Rejection & HTTP Status 400)

#### Test Design
- **Category:** Negative / Boundary Validation
- **Test Objective:** Verify that providing an empty string `""` for `password` is rejected.
- **Test Condition:** `password` is empty string `""`.
- **Partition / Boundary:** Blank/empty string boundary.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Empty Pass User",
    "email": "fr01_ai_032@example.com",
    "password": ""
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected as empty password violates presence, length, and character class requirements (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-033: Non-String Integer Password Data Type
#### Identity
- **Test ID:** FR01-AI-033
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-25

#### Traceability
- **Requirement / FR Reference:** FR-01 (`api_specification.md` Line 18)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 18
- **Oracle Classification:** INFERRED FROM EXAMPLE (Type Expectation); INFERRED (Rejection)

#### Test Design
- **Category:** Negative / Type Safety
- **Test Objective:** Verify that supplying a numeric integer value for `password` is rejected.
- **Test Condition:** `password` is JSON integer `12345678`.
- **Partition / Boundary:** Wrong data type partition.
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Type Pass User",
    "email": "fr01_ai_033@example.com",
    "password": 12345678
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected due to wrong data type (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-034: Extreme Upper Length Password Robustness (128 Characters)
#### Identity
- **Test ID:** FR01-AI-034
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-26

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 34 (Upper length limit is UNKNOWN)
- **Oracle Classification:** ROBUSTNESS; UNKNOWN (Specification Oracle & Boundary)

#### Test Design
- **Category:** Robustness / Large String Handling
- **Test Objective:** Probe backend resilience and password hashing limits when an unusually long 128-character valid password is submitted.
- **Test Condition:** Password is a 128-character valid string meeting all 5 criteria (`"Password123!"` followed by 116 `'A'` characters).
- **Partition / Boundary:** Upper length boundary = UNKNOWN.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_034@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Long Pass User",
    "email": "fr01_ai_034@example.com",
    "password": "Password123!AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Specification Oracle is UNKNOWN (Specification defines no maximum password length).
- **Expected HTTP Status:** Acceptance is UNKNOWN / ROBUSTNESS. If accepted, documented status is `200 OK` (SPECIFIED). Rejection with 400 is also a possible valid contract behavior.
- **Expected Response Contract:** Parseable response; no unhandled server crash.
- **Security Assertion:** Password hashing algorithm (e.g. bcrypt/argon2) must handle string safely without CPU exhaustion denial of service.
- **State Assertion:** Database integrity preserved.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-035: Empty JSON Body Rejection
#### Identity
- **Test ID:** FR01-AI-035
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-27

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 32 — Required Fields)
- **SEC Reference:** N/A
- **Source Reference:** `README.md` Line 32
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)

#### Test Design
- **Category:** Negative / Bulk Mandatory Field Validation
- **Test Objective:** Verify that sending an empty JSON object `{}` with no fields is rejected.
- **Test Condition:** Request body is `{}`.
- **Partition / Boundary:** Structural boundary (all mandatory fields omitted).
- **Preconditions:** Backend running.
- **Initial State:** N/A.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {}
  ```

#### Expected Result
- **Expected Semantic Behavior:** Request should be rejected for omitting all required fields (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (UNKNOWN structure).
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted into `users` table.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-036: Unexpected Extra Field (`confirmPassword`) Robustness
#### Identity
- **Test ID:** FR01-AI-036
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-28

#### Traceability
- **Requirement / FR Reference:** FR-01 (`api_specification.md` Line 14; `README.md` Line 35)
- **SEC Reference:** N/A
- **Source Reference:** `api_specification.md` Line 14; `README.md` Line 35
- **Oracle Classification:** ROBUSTNESS; UNKNOWN / INFERRED (Contract Additional Property Handling)

#### Test Design
- **Category:** Robustness / Extra Field Handling
- **Test Objective:** Verify backend behavior when a valid registration payload includes an extra unexpected field (`confirmPassword`).
- **Test Condition:** Payload includes `{name, email, password, confirmPassword}`.
- **Partition / Boundary:** Additional properties boundary.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_036@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Extra Field User",
    "email": "fr01_ai_036@example.com",
    "password": "Password123!",
    "confirmPassword": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Acceptance is UNKNOWN / INFERRED. The API contract does not define whether extra fields are ignored or rejected; backend must handle gracefully without crashing.
- **Expected HTTP Status:** If backend is tolerant, `200 OK` (SPECIFIED). If strict schema validation is applied, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** Parseable response.
- **Security Assertion:** No mass-assignment vulnerability or server crash.
- **State Assertion:** Database record created if accepted.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-037: Password Plaintext Storage Verification via Database Inspection (SEC-01)
#### Identity
- **Test ID:** FR01-AI-037
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-29

#### Traceability
- **Requirement / FR Reference:** FR-01 (`README.md` Line 278)
- **SEC Reference:** SEC-01 (`README.md` Line 278 — "Mật khẩu không được lưu dưới dạng plaintext")
- **Source Reference:** `README.md` Line 278
- **Oracle Classification:** SPECIFIED (SEC-01 Requirement); NON-API SECURITY VERIFICATION

#### Test Design
- **Category:** Security / Non-API Storage Layer Verification
- **Test Objective:** Verify that the registered password is NOT stored as raw plaintext in the SQLite database record.
- **Test Condition:** Register a controlled test account with known password `"SecretPass123!"`, then inspect the SQLite `users` table record directly.
- **Partition / Boundary:** Storage layer verification boundary.
- **Preconditions:** Backend running with SQLite database at `backend/database.sqlite`.
- **Initial State:** Email `fr01_sec01_verify@example.com` unregistered.

#### Verification Method & Procedure
1. **API Trigger Step:**
   - **Method:** `POST`
   - **Endpoint:** `/api/register`
   - **Body:**
     ```json
     {
       "name": "SEC01 Tester",
       "email": "fr01_sec01_verify@example.com",
       "password": "SecretPass123!"
     }
     ```
2. **Non-API Database Inspection Step:**
   - **Command / Query:**
     ```sql
     SELECT password FROM users WHERE email = 'fr01_sec01_verify@example.com';
     ```

#### Expected Result
- **Expected Semantic Behavior:** The password must be stored in a secured, hashed format (e.g. bcrypt, argon2) (SPECIFIED SEC-01).
- **Expected HTTP Status:** API registration returns `200 OK` (SPECIFIED).
- **Security Assertion:** The `password` column value in SQLite MUST NOT equal the submitted plaintext string `"SecretPass123!"`. If the stored value equals `"SecretPass123!"`, this is a confirmed violation of SEC-01.
- **State Assertion:** User record exists in `users` table with hashed credentials.

#### Lifecycle
- **Setup Required:** Ensure database accessible.
- **Cleanup Required:** Delete created test user (`DELETE FROM users WHERE email = 'fr01_sec01_verify@example.com'`).
- **Automation Status:** NOT AUTOMATED YET (Requires hybrid API + DB script execution)

---

### FR01-AI-038: Security Hardening: Credential Non-Leakage in Response
#### Identity
- **Test ID:** FR01-AI-038
- **Origin:** AI
- **Feature:** FR-01
- **Coverage ID:** COV-FR01-30

#### Traceability
- **Requirement / FR Reference:** FR-01 (`api_specification.md` Line 21)
- **SEC Reference:** Best Practice Credential Protection
- **Source Reference:** `api_specification.md` Line 21
- **Oracle Classification:** SECURITY-HARDENING ASSERTION; EXAMPLE-DERIVED (Body properties)

#### Test Design
- **Category:** Security / Response Payload Hardening
- **Test Objective:** Verify that the successful registration response body does NOT leak sensitive credentials (password, hash, salt, reset token).
- **Test Condition:** Standard valid registration request.
- **Partition / Boundary:** Data exposure boundary.
- **Preconditions:** Backend running.
- **Initial State:** Target email `fr01_ai_038@example.com` unregistered.

#### HTTP Request
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Hardened User",
    "email": "fr01_ai_038@example.com",
    "password": "Password123!"
  }
  ```

#### Expected Result
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** Response JSON body must NOT contain properties: `password`, `hash`, `salt`, `reset_token`, or any credential data (SECURITY-HARDENING ASSERTION).
- **State Assertion:** User record created in database.

#### Lifecycle
- **Setup Required:** None.
- **Cleanup Required:** Delete created user row.
- **Automation Status:** NOT AUTOMATED YET
