# FR-01: Account Registration — Reviewed Final AI Test Suite

> **Document Status:** REVIEWED & AUDITED FINAL AI TEST SUITE  
> **Auditor / Approver:** Phạm Ngọc Gia Bảo (`23127027`)  
> **Source Documents:** Derived from [`generated-ai-original.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr01/generated-ai-original.md) by applying the audited decisions from [`human-audit.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr01/human-audit.md).  
> **Traceability & Integrity:** The original generation file `generated-ai-original.md` remains unchanged and committed. All modifications below reflect audited corrections without erasing the original AI design history.

---

## 1. Test Suite Summary

- **Total Reviewed AI Test Cases:** Exactly **38**
- **Audit Decision Composition:**
  - **VALID Unchanged:** 25 test cases (`FR01-AI-001`, `003`, `007`, `009`, `011`, `012`, `013`, `014`, `016`, `017`, `020`–`032`, `035`, `038`)
  - **INCOMPLETE Calibrated:** 12 test cases (`FR01-AI-002`, `004`, `005`, `006`, `008`, `010`, `015`, `018`, `033`, `034`, `036`, `037`)
  - **INVALID Redesigned:** 1 test case (`FR01-AI-019`)
- **Execution Profile:**
  - **API-Executable Cases:** 37
  - **Non-API Security Verification Cases:** 1 (`FR01-AI-037` — direct SQLite DB inspection)

---

## 2. Detailed Test Case Specifications

### FR01-AI-001: Standard Valid ASCII Name Registration
- **Test ID:** FR01-AI-001
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Lines 32–34; `api_specification.md` Line 21)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Field Presence); EXAMPLE-DERIVED (Body properties `message`, `id`)
- **Category:** Functional / Positive Happy Path
- **Test Objective:** Verify standard registration succeeds when valid ASCII name, valid unique email, and strong password are provided.
- **Preconditions:** SUT running on `http://localhost:3000`.
- **Initial State:** Email `fr01_ai_001@example.com` unregistered in database.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Nguyen Van A",
      "email": "fr01_ai_001@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and numeric `id` (EXAMPLE-DERIVED / INFERRED FROM EXAMPLE).
- **Security Assertion:** Response body does not leak password or sensitive credentials.
- **State Assertion:** Exactly 1 row inserted into `users` table.
- **Setup / Cleanup:** Cleanup: `DELETE FROM users WHERE email = 'fr01_ai_001@example.com'`.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-002: Vietnamese Unicode Name Characterization Probe
- **Test ID:** FR01-AI-002
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified from strict requirement to robustness/characterization probe. Spec does not formally guarantee Vietnamese diacritic acceptance; if accepted, verify faithful UTF-8 persistence.
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED / ROBUSTNESS (Diacritic Acceptance); SPECIFIED (Status 200 if accepted)
- **Category:** Robustness / Localization Characterization
- **Test Objective:** Characterize backend behavior when registering with Vietnamese multi-byte diacritics; verify UTF-8 persistence integrity if accepted.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_002@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json; charset=utf-8`
  - Body:
    ```json
    {
      "name": "Trần Thị Bích Hạnh",
      "email": "fr01_ai_002@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Input acceptance is INFERRED / ROBUSTNESS. Rejection is not classified as a spec violation. If accepted, status is 200 OK.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). If rejected by input validation, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** Parseable JSON; no character encoding corruption.
- **Security Assertion:** No server crash; safe handling of multi-byte UTF-8 data.
- **State Assertion:** If inserted, SQLite record preserves `"Trần Thị Bích Hạnh"` without mojibake.
- **Setup / Cleanup:** Cleanup created row if accepted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-003: Omitted Mandatory Name Field Rejection
- **Test ID:** FR01-AI-003
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None (Status remains UNKNOWN / INFERRED 400)
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Input Validation
- **Test Objective:** Verify request is rejected when mandatory `name` property is omitted.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "email": "fr01_ai_003@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected because `name` is mandatory (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope (structure UNKNOWN).
- **Security Assertion:** Server must not crash or throw unhandled exception.
- **State Assertion:** Zero rows inserted into SQLite `users` table.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-004: Empty String Name Value Inferred Rejection
- **Test ID:** FR01-AI-004
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified rejection as INFERRED / robustness probe. Spec requires full name but does not explicitly define empty-string or trimming semantics.
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED (Semantic Rejection & HTTP Status 400); ROBUSTNESS
- **Category:** Negative / Boundary Validation
- **Test Objective:** Verify handling of empty string `""` for `name`; determine whether blank values satisfy field presence.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "",
      "email": "fr01_ai_004@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Semantic rejection is INFERRED (blank string fails providing full name).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero records inserted into `users` table.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-005: Non-String Integer Name Data Type Robustness Probe
- **Test ID:** FR01-AI-005
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as type-robustness probe. String type is inferred from example rather than formal schema; rejection is an inferred convention, not an official requirement.
- **Requirement Reference:** FR-01 (`api_specification.md` Line 16)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED FROM EXAMPLE (Type Expectation); INFERRED (Rejection); ROBUSTNESS
- **Category:** Negative / Type Safety Robustness
- **Test Objective:** Probe backend type robustness when an integer value (`12345`) is supplied for `name`.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": 12345,
      "email": "fr01_ai_005@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Semantic rejection is INFERRED from JSON type conventions.
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Controlled response; no internal crash or unhandled 500 stack trace.
- **Security Assertion:** JSON parser processes types safely.
- **State Assertion:** No invalid-type data inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-006: Extreme Upper Length Name Robustness Probe (1000 Characters)
- **Test ID:** FR01-AI-006
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as pure robustness probe. Specification defines no upper bound; clean acceptance or clean rejection are both valid; test fails only on crash or DB corruption.
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Oracle Classification:** ROBUSTNESS; UNKNOWN (Boundary & Functional Oracle)
- **Category:** Robustness / Boundary Characterization
- **Test Objective:** Probe resilience against extremely long input strings (1000 characters) in `name`.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_006@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
      "email": "fr01_ai_006@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Specification oracle is UNKNOWN. Clean acceptance (200) or clean rejection (400) are both legitimate.
- **Expected HTTP Status:** UNKNOWN by official specification.
- **Expected Response Contract:** Parseable response; no unhandled HTML exception dump.
- **Security Assertion:** Server must not crash, exhaust memory, or corrupt SQLite database.
- **State Assertion:** Database integrity preserved.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-007: Literal SQL Syntax Handling in Name (SEC-05)
- **Test ID:** FR01-AI-007
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None (Security property verified: query unaltered; input treated as literal data)
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** SEC-05 (`README.md` Line 282 — Parameterized Query)
- **Oracle Classification:** SPECIFIED (SEC-05 Property); INFERRED / ROBUSTNESS (Name Acceptance)
- **Category:** Security / SEC-05 Parameterized Query Verification
- **Test Objective:** Verify that apostrophes in `name` (`"O'Connor"`) are treated strictly as data without altering SQL structure.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_007@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "O'Connor",
      "email": "fr01_ai_007@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Parameterized query handles apostrophe as literal data (SPECIFIED SEC-05). Literal storage or clean input validation rejection are both secure.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). If rejected by name policy, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** No SQLite syntax error.
- **Security Assertion:** Query structure unaltered; no unhandled `SQLITE_ERROR: unrecognized token`.
- **State Assertion:** If stored, value `"O'Connor"` is preserved literally.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-008: HTML Script Tag Robustness Probe in Name
- **Test ID:** FR01-AI-008
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as data preservation robustness probe. Clarified that SEC-04 applies to UI display, not backend JSON storage; added verification that raw string is stored without crash.
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** Context of SEC-04 (UI Scope Clarification)
- **Oracle Classification:** ROBUSTNESS; INFERRED (Acceptance)
- **Category:** Robustness / Raw Data Preservation
- **Test Objective:** Verify backend handles HTML string tags safely without crash; confirm JSON API does not corrupt raw input.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_008@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "<script>alert(1)</script>",
      "email": "fr01_ai_008@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Safe handling without crash (ROBUSTNESS). API stores raw data faithfully.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED).
- **Expected Response Contract:** Controlled JSON response.
- **Security Assertion:** No server-side code execution or unhandled crash.
- **State Assertion:** Stored literally as raw string.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-009: Standard Valid RFC Email Format Registration
- **Test ID:** FR01-AI-009
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Format Rule); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Positive Happy Path
- **Test Objective:** Verify registration succeeds with a standard RFC email (`user@domain.com`).
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_009@domain.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Standard User",
      "email": "fr01_ai_009@domain.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and numeric `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-010: Advanced RFC Email Plus-Addressing Characterization Probe
- **Test ID:** FR01-AI-010
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as characterization probe. Spec requires valid format but does not explicitly mandate full RFC 5322 plus-addressing support; if accepted, verify 200 and faithful storage.
- **Requirement Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED / RFC (Syntax Acceptance); SPECIFIED (Status 200 if accepted)
- **Category:** Functional / RFC Syntax Characterization
- **Test Objective:** Characterize email regex handling when plus-addressing (`user+tag@domain.com`) is provided.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_010+hw06@domain.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Tagged User",
      "email": "fr01_ai_010+hw06@domain.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Acceptance is INFERRED / RFC. If regex accepts, registration succeeds.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). If rejected by strict regex, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** Body contains `message` and `id` if accepted.
- **Security Assertion:** No server crash.
- **State Assertion:** Email stored faithfully with plus sign.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-011: Omitted Mandatory Email Field Rejection
- **Test ID:** FR01-AI-011
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Input Validation
- **Test Objective:** Verify request is rejected when mandatory `email` property is omitted.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No Email User",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected because `email` is mandatory (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-012: Empty String Email Value Rejection
- **Test ID:** FR01-AI-012
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Lines 32–33)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED (Semantic Rejection & HTTP Status 400)
- **Category:** Negative / Boundary Validation
- **Test Objective:** Verify that an empty string `""` for `email` is rejected.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Empty Email User",
      "email": "",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected as empty email violates format and presence rules (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-013: Malformed Email Missing At-Symbol (@) Rejection
- **Test ID:** FR01-AI-013
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Format Syntax Validation
- **Test Objective:** Verify rejection when email string lacks the `@` symbol.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No At User",
      "email": "fr01_ai_013_userdomain.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected due to invalid email format (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-014: Malformed Email Missing Domain Part Rejection
- **Test ID:** FR01-AI-014
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Format Syntax Validation
- **Test Objective:** Verify rejection when email string lacks the domain part after `@`.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No Domain User",
      "email": "fr01_ai_014_user@",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected due to invalid email format (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-015: Non-String Integer Email Data Type Robustness Probe
- **Test ID:** FR01-AI-015
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as type-robustness/characterization probe. String type is inferred from example; rejection is an inferred convention.
- **Requirement Reference:** FR-01 (`api_specification.md` Line 17)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED FROM EXAMPLE (Type Expectation); INFERRED (Rejection); ROBUSTNESS
- **Category:** Negative / Type Safety Robustness
- **Test Objective:** Probe backend type robustness when a numeric integer (`99999`) is supplied for `email`.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Type User",
      "email": 99999,
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Rejection is INFERRED from JSON type conventions.
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Controlled response; no unhandled crash.
- **Security Assertion:** Safe JSON parsing.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-016: Duplicate Registration of Pre-Seeded Email Rejection
- **Test ID:** FR01-AI-016
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None (Failure status confirmed UNKNOWN / INFERRED 400/409)
- **Requirement Reference:** FR-01 (`README.md` Line 33 — Uniqueness Rule)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); UNKNOWN / INFERRED (HTTP Status 400/409)
- **Category:** Negative / Uniqueness Verification
- **Test Objective:** Verify that attempting to register existing pre-seeded email `test@eshop.com` is rejected.
- **Preconditions:** Database seeded with default users.
- **Initial State:** User `test@eshop.com` exists in SQLite `users` table.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Duplicate SeedTest",
      "email": "test@eshop.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** REJECT DUPLICATE (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; conventional values are `400 Bad Request` or `409 Conflict` (INFERRED).
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash; no duplicate row created.
- **State Assertion:** Exactly 1 row remains with `email = 'test@eshop.com'`.
- **Setup / Cleanup:** Seed user preserved.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-017: Duplicate Registration via Dynamic Sequential Call
- **Test ID:** FR01-AI-017
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 33 — Uniqueness Rule)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); UNKNOWN / INFERRED (HTTP Status 400/409)
- **Category:** State-Dependent / Duplicate Lifecycle
- **Test Objective:** Verify account lifecycle: initial registration succeeds, immediate repeated registration with identical email is rejected.
- **Preconditions:** SUT running.
- **Initial State:** Target email `fr01_ai_017@example.com` unregistered prior to Step 1.
- **Request (Step 2 Repeat):**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Second Instance",
      "email": "fr01_ai_017@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** REJECT DUPLICATE (SPECIFIED) on Step 2.
- **Expected HTTP Status:** UNKNOWN / INFERRED (400 or 409).
- **Expected Response Contract:** Error envelope on repeat attempt.
- **Security Assertion:** No server crash.
- **State Assertion:** Exactly 1 row exists with `email = 'fr01_ai_017@example.com'`.
- **Setup / Cleanup:** Execute Step 1 registration first; cleanup created row after test.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-018: Case-Insensitive Duplicate Email Characterization Probe
- **Test ID:** FR01-AI-018
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as characterization probe. Spec mandates uniqueness but does not define case-sensitivity; rejection is an inferred canonicalization behavior, not a hard requirement.
- **Requirement Reference:** FR-01 (`README.md` Line 33)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED (Case-Insensitive Uniqueness & HTTP Status); CHARACTERIZATION
- **Category:** Negative / Data Canonicalization Characterization
- **Test Objective:** Characterize whether email uniqueness check normalizes character casing (`TEST@eshop.com` vs `test@eshop.com`).
- **Preconditions:** Seed user `test@eshop.com` exists.
- **Initial State:** User `test@eshop.com` in database.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Case User",
      "email": "TEST@eshop.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Rejection under case-insensitive canonicalization is INFERRED.
- **Expected HTTP Status:** UNKNOWN / INFERRED (400 or 409).
- **Expected Response Contract:** Error envelope if rejected.
- **Security Assertion:** No duplicate account under different casing.
- **State Assertion:** Single record in database.
- **Setup / Cleanup:** Cleanup uppercase user row if SUT erroneously created one.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-019: Parameterized Query Verification via SQL Injection String in Name (SEC-05 Redesign)
- **Test ID:** FR01-AI-019
- **Audit Status:** INVALID (Original test design flawed)
- **Correction Applied:** **FULL REDESIGN APPLIED.** The original AI test used malformed email `' OR '1'='1'@domain.com` which could be rejected by email regex before ever touching the database, failing to demonstrate SEC-05. Redesigned to inject classic SQL-breaking syntax into the `name` field (`"Robert'); DROP TABLE users;--"`), combined with valid standard email and password. This payload reliably reaches SQLite parameter placeholders (`[name, email, password]`).
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** SEC-05 (`README.md` Line 282 — Parameterized Query Requirement)
- **Oracle Classification:** SPECIFIED (SEC-05 Security Property); INFERRED / ROBUSTNESS (Name Acceptance)
- **Category:** Security / SEC-05 Parameterized Query Verification
- **Test Objective:** Verify that SQL-breaking syntax in `name` is handled strictly as literal data via parameterized query; verify that query structure is not altered and no unintended SQL commands execute.
- **Preconditions:** SUT running.
- **Initial State:** Target email `fr01_ai_019_sec05@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Robert'); DROP TABLE users;--",
      "email": "fr01_ai_019_sec05@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Input is treated strictly as literal data (SPECIFIED SEC-05). Literal storage without executing the injection, or clean rejection without SQL crash, are both valid secure behaviors.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). If rejected by input validation, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** Response must not contain SQLite syntax error.
- **Security Assertion:** Query structure must not be altered; table `users` MUST NOT be dropped; database integrity must remain 100% intact.
- **State Assertion:** Table `users` exists and retains all rows; if created, row name equals literal string `"Robert'); DROP TABLE users;--"`.
- **Setup / Cleanup:** Cleanup created test row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-020: Standard Strong Password Meeting All 5 Criteria
- **Test ID:** FR01-AI-020
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Positive Happy Path
- **Test Objective:** Verify password satisfying all 5 criteria ($\ge 8$ chars, upper, lower, digit, special) is accepted.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_020@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Strong Pass User",
      "email": "fr01_ai_020@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** JSON body contains `message: "User registered successfully"` and numeric `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-021: Documented Special Symbol Coverage: At-Sign (@)
- **Test ID:** FR01-AI-021
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Password Policy Domain Coverage
- **Test Objective:** Verify password policy accepts special character `@` from the documented set.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_021@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Symbol At User",
      "email": "fr01_ai_021@example.com",
      "password": "Passw0rd@"
    }
    ```
- **Expected Semantic Behavior:** Policy requirement satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-022: Documented Special Symbol Coverage: Dollar-Sign ($)
- **Test ID:** FR01-AI-022
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Password Policy Domain Coverage
- **Test Objective:** Verify password policy accepts special character `$` from the documented set.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_022@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Symbol Dollar User",
      "email": "fr01_ai_022@example.com",
      "password": "Passw0rd$"
    }
    ```
- **Expected Semantic Behavior:** Policy requirement satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-023: Documented Special Symbol Coverage: Ampersand (&)
- **Test ID:** FR01-AI-023
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Policy Adherence); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Password Policy Domain Coverage
- **Test Objective:** Verify password policy accepts special character `&` from the documented set.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_023@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Symbol Amp User",
      "email": "fr01_ai_023@example.com",
      "password": "Passw0rd&"
    }
    ```
- **Expected Semantic Behavior:** Policy requirement satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-024: Required Special Symbol Plus Extra Symbol (Non-Whitelist Interpretation)
- **Test ID:** FR01-AI-024
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED Valid (Policy Interpretation); SPECIFIED (Status 200 if accepted)
- **Category:** Functional / Non-Whitelist Policy Interpretation
- **Test Objective:** Verify password containing required symbol (`!`) plus extra symbol (`#`) is accepted under non-whitelist rule.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_024@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Combo Symbol User",
      "email": "fr01_ai_024@example.com",
      "password": "Password123!#"
    }
    ```
- **Expected Semantic Behavior:** Acceptance is INFERRED Valid (meets $\ge 1$ from set; no ban on extra symbols).
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` if accepted.
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created if accepted.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-025: Missing Required Special Character from Set Rejection
- **Test ID:** FR01-AI-025
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Password Policy Violation
- **Test Objective:** Verify rejection when password lacks any special symbol from documented set (`@$!%*?&`).
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No Symbol User",
      "email": "fr01_ai_025@example.com",
      "password": "Password1234"
    }
    ```
- **Expected Semantic Behavior:** Request rejected for violating special character requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-026: Password Length Boundary: 7 Characters (Minimum - 1) Rejection
- **Test ID:** FR01-AI-026
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Boundary Value Analysis ($8 - 1$)
- **Test Objective:** Verify rejection when password is 7 characters (just below minimum 8) while other criteria are present.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Len 7 User",
      "email": "fr01_ai_026@example.com",
      "password": "Pass1!a"
    }
    ```
- **Expected Semantic Behavior:** Request rejected because length $< 8$ (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-027: Password Length Boundary: 8 Characters (Exact Minimum) Acceptance
- **Test ID:** FR01-AI-027
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Minimum Boundary); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Boundary Value Analysis ($8$)
- **Test Objective:** Verify acceptance when password has exact minimum length of 8 characters and satisfies all criteria.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_027@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Len 8 User",
      "email": "fr01_ai_027@example.com",
      "password": "Pass12!a"
    }
    ```
- **Expected Semantic Behavior:** Minimum length requirement satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-028: Password Length Boundary: 9 Characters (Minimum + 1) Acceptance
- **Test ID:** FR01-AI-028
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Status 200, Boundary Just Above Minimum); EXAMPLE-DERIVED (Body properties)
- **Category:** Functional / Boundary Value Analysis ($8 + 1$)
- **Test Objective:** Verify acceptance when password is 9 characters (just above minimum) and satisfies all criteria.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_028@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Len 9 User",
      "email": "fr01_ai_028@example.com",
      "password": "Passw12!a"
    }
    ```
- **Expected Semantic Behavior:** Minimum length requirement satisfied (SPECIFIED). Account created.
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** No credential leakage.
- **State Assertion:** Row created in `users` table.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-029: Missing Uppercase Letter in Password Rejection
- **Test ID:** FR01-AI-029
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Character Class Policy Violation
- **Test Objective:** Verify rejection when password lacks an uppercase letter.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No Upper User",
      "email": "fr01_ai_029@example.com",
      "password": "password123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected for violating uppercase letter requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-030: Missing Lowercase Letter in Password Rejection
- **Test ID:** FR01-AI-030
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Character Class Policy Violation
- **Test Objective:** Verify rejection when password lacks a lowercase letter.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No Lower User",
      "email": "fr01_ai_030@example.com",
      "password": "PASSWORD123!"
    }
    ```
- **Expected Semantic Behavior:** Request rejected for violating lowercase letter requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-031: Missing Numeric Digit in Password Rejection
- **Test ID:** FR01-AI-031
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Policy Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Character Class Policy Violation
- **Test Objective:** Verify rejection when password lacks a numeric digit.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "No Digit User",
      "email": "fr01_ai_031@example.com",
      "password": "Password!@#$"
    }
    ```
- **Expected Semantic Behavior:** Request rejected for violating digit requirement (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-032: Empty String Password Value Rejection
- **Test ID:** FR01-AI-032
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Lines 32–34)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED (Semantic Rejection & HTTP Status 400)
- **Category:** Negative / Boundary Validation
- **Test Objective:** Verify that an empty string `""` for `password` is rejected.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Empty Pass User",
      "email": "fr01_ai_032@example.com",
      "password": ""
    }
    ```
- **Expected Semantic Behavior:** Request rejected as empty password violates length and policy rules (INFERRED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-033: Non-String Integer Password Data Type Robustness Probe
- **Test ID:** FR01-AI-033
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as type-safety robustness probe. Type contract is inferred from example; exact semantic behavior remains UNKNOWN; server must not crash.
- **Requirement Reference:** FR-01 (`api_specification.md` Line 18)
- **SEC Reference:** N/A
- **Oracle Classification:** INFERRED FROM EXAMPLE (Type Expectation); INFERRED (Rejection); ROBUSTNESS
- **Category:** Negative / Type Safety Robustness
- **Test Objective:** Probe backend type robustness when a numeric integer (`12345678`) is supplied for `password`.
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Type Pass User",
      "email": "fr01_ai_033@example.com",
      "password": 12345678
    }
    ```
- **Expected Semantic Behavior:** Exact semantic behavior is UNKNOWN / INFERRED.
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Controlled response; no unhandled 5xx crash.
- **Security Assertion:** Safe JSON parsing.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-034: Extreme Upper Length Password Robustness Probe (128 Characters)
- **Test ID:** FR01-AI-034
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as pure robustness probe. Removed artificial assumptions demanding bcrypt/argon2; primary assertion is safe string handling, no CPU lockup, and database integrity.
- **Requirement Reference:** FR-01 (`README.md` Line 34)
- **SEC Reference:** N/A
- **Oracle Classification:** ROBUSTNESS; UNKNOWN (Upper Boundary & Contract Behavior)
- **Category:** Robustness / Extreme Input
- **Test Objective:** Probe backend string handling and password hashing limits when an unusually long 128-character valid password is submitted.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_034@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Long Pass User",
      "email": "fr01_ai_034@example.com",
      "password": "Password123!AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }
    ```
- **Expected Semantic Behavior:** Specification oracle is UNKNOWN (no max length specified).
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). Clean rejection (400) is also legitimate.
- **Expected Response Contract:** Parseable response; no unhandled crash.
- **Security Assertion:** Hashing algorithm handles input safely without CPU exhaustion or denial of service.
- **State Assertion:** Database integrity preserved.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-035: Empty JSON Body Rejection
- **Test ID:** FR01-AI-035
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None
- **Requirement Reference:** FR-01 (`README.md` Line 32)
- **SEC Reference:** N/A
- **Oracle Classification:** SPECIFIED (Semantic Rejection); INFERRED (HTTP Status 400)
- **Category:** Negative / Bulk Mandatory Field Validation
- **Test Objective:** Verify rejection when entire JSON body is an empty object (`{}`).
- **Preconditions:** SUT running.
- **Initial State:** N/A.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {}
    ```
- **Expected Semantic Behavior:** Request rejected for omitting all required fields (SPECIFIED).
- **Expected HTTP Status:** UNKNOWN by official specification; `400 Bad Request` is an INFERRED convention.
- **Expected Response Contract:** Error envelope.
- **Security Assertion:** No server crash.
- **State Assertion:** Zero rows inserted.
- **Setup / Cleanup:** None.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-036: Unexpected Extra Field (`confirmPassword`) Robustness Probe
- **Test ID:** FR01-AI-036
- **Audit Status:** INCOMPLETE
- **Correction Applied:** Reclassified as characterization/robustness probe. Spec does not define extra-property behavior; graceful ignore (200) or clean rejection (400) are both legitimate; fails only on crash or unintended side effects.
- **Requirement Reference:** FR-01 (`api_specification.md` Line 14; `README.md` Line 35)
- **SEC Reference:** N/A
- **Oracle Classification:** ROBUSTNESS; UNKNOWN / INFERRED (Contract Additional Property Handling)
- **Category:** Robustness / Schema Tolerance
- **Test Objective:** Probe backend behavior when an unexpected extra field (`confirmPassword`) is present in payload.
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_036@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Extra Field User",
      "email": "fr01_ai_036@example.com",
      "password": "Password123!",
      "confirmPassword": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Contract behavior is UNKNOWN / INFERRED. Graceful ignore or clean rejection are both valid.
- **Expected HTTP Status:** If backend is tolerant, `200 OK` (SPECIFIED). If strict schema validation is applied, `400 Bad Request` (INFERRED).
- **Expected Response Contract:** Parseable response.
- **Security Assertion:** No server crash or mass-assignment vulnerability.
- **State Assertion:** Row created if accepted.
- **Setup / Cleanup:** Cleanup created row if inserted.
- **Automation Status:** NOT AUTOMATED YET

---

### FR01-AI-037: Password Plaintext Storage Verification via SQLite DB Inspection (SEC-01)
- **Test ID:** FR01-AI-037
- **Audit Status:** INCOMPLETE
- **Correction Applied:** **ORACLE CORRECTED TO MATCH SRS EXACTLY.** Removed requirement demanding bcrypt/argon2 or a specific hashing algorithm. The official requirement from SRS (`README.md` Line 278) is strictly: `stored password != submitted plaintext password`.
- **Requirement Reference:** FR-01 (`README.md` Line 278)
- **SEC Reference:** SEC-01 (`README.md` Line 278 — "Mật khẩu không được lưu dưới dạng plaintext")
- **Oracle Classification:** SPECIFIED (SEC-01 Requirement); NON-API SECURITY VERIFICATION
- **Category:** Security / Non-API Storage Layer Verification
- **Test Objective:** Verify that registered password is NOT stored in plaintext in the SQLite database record.
- **Preconditions:** SUT running with SQLite database at `backend/database.sqlite`.
- **Initial State:** Email `fr01_sec01_verify@example.com` unregistered.
- **Verification Procedure:**
  1. Submit registration:
     - Method: `POST /api/register`
     - Body:
       ```json
       {
         "name": "SEC01 Tester",
         "email": "fr01_sec01_verify@example.com",
         "password": "SecretPass123!"
       }
       ```
  2. Inspect database directly:
     ```sql
     SELECT password FROM users WHERE email = 'fr01_sec01_verify@example.com';
     ```
- **Expected Semantic Behavior:** Password is NOT stored in raw plaintext (SPECIFIED SEC-01).
- **Expected HTTP Status:** API registration returns `200 OK` (SPECIFIED).
- **Security Assertion:** The `password` column value in SQLite MUST NOT equal the submitted plaintext string `"SecretPass123!"`. If stored value equals `"SecretPass123!"`, this confirms a violation of SEC-01.
- **State Assertion:** User row exists in database with non-plaintext password.
- **Setup / Cleanup:** Cleanup test user: `DELETE FROM users WHERE email = 'fr01_sec01_verify@example.com'`.
- **Automation Status:** NOT AUTOMATED YET (Requires hybrid API + DB script execution)

---

### FR01-AI-038: Security Hardening: Credential Non-Leakage in Response
- **Test ID:** FR01-AI-038
- **Audit Status:** VALID (Original test design confirmed valid)
- **Correction Applied:** None (Retained as defense-in-depth security hardening, separate from explicit API contract)
- **Requirement Reference:** FR-01 (`api_specification.md` Line 21)
- **SEC Reference:** Best Practice Credential Protection
- **Oracle Classification:** SECURITY-HARDENING ASSERTION; EXAMPLE-DERIVED (Body properties)
- **Category:** Security / Response Payload Hardening
- **Test Objective:** Verify that registration response body does NOT leak sensitive credentials (password, hash, salt, reset token).
- **Preconditions:** SUT running.
- **Initial State:** Email `fr01_ai_038@example.com` unregistered.
- **Request:**
  - Method: `POST /api/register`
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "name": "Hardened User",
      "email": "fr01_ai_038@example.com",
      "password": "Password123!"
    }
    ```
- **Expected Semantic Behavior:** Account created successfully (SPECIFIED).
- **Expected HTTP Status:** `200 OK` (SPECIFIED).
- **Expected Response Contract:** Body contains `message` and `id` (EXAMPLE-DERIVED).
- **Security Assertion:** Response body must NOT contain properties: `password`, `hash`, `salt`, `reset_token`, or any credential data (SECURITY-HARDENING ASSERTION).
- **State Assertion:** Row created in database.
- **Setup / Cleanup:** Cleanup created row.
- **Automation Status:** NOT AUTOMATED YET
