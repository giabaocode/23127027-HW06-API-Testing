# FR-01: Student-Selected Extension Tests Worksheet

> **Auditor Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Feature:** FR-01 — Account Registration (`POST /api/register`)
> - **Requirement:** Minimum $\ge 5$ extension tests exploring gaps beyond the standard AI-generated test suite.
> - **Truthful Authorship & Provenance Statement:** In strict adherence to course academic integrity principles, the 5 test ideas formalized below were originally surfaced during AI brainstorming and subsequently selected and confirmed by the student for formal specification. They are NOT represented as student-original from scratch.

---

## Provenance & Selection Summary

- **Idea Source:** AI brainstorming
- **Student Action:** Student personally selected these 5 distinct protocol and parsing dimensions
- **Student Selection:** **CONFIRMED**
- **AI Action:** Mechanical formalization of preconditions, concrete raw payloads, assertions, and Postman automation metadata

---

## 1. Extension Test Specifications

### FR01-STU-001: Syntactically Malformed JSON Body Robustness Probe
- **Test ID:** FR01-STU-001
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** FR-01 — Account Registration
- **Requirement Reference:** FR-01 (`api_specification.md` Line 14 — JSON Contract)
- **SEC Reference:** Best Practice Parser Robustness (CWE-20)
- **Oracle Classification:** ROBUSTNESS / PROTOCOL CHARACTERIZATION; UNKNOWN (Exact Error HTTP Status)
- **Category:** Negative / Parser Robustness
- **Test Objective:** Verify backend JSON parser robustness when receiving syntactically broken JSON missing a closing brace; verify that server handles the syntax error gracefully without crashing.
- **Preconditions:** SUT running on `http://localhost:3000`.
- **Initial State:** Target email `stu001_malformed@example.com` unregistered.
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Concrete Request Body (Raw Text):**
  ```text
  {"name": "Malformed User", "email": "stu001_malformed@example.com", "password": "Password123!"
  ```
  *(Note: Intentionally truncated to omit the closing `}` brace; sent as raw unparsed payload).*
- **Expected Semantic Behavior:** Request must NOT execute registration or create an account (ROBUSTNESS). Server body parser must catch syntax error cleanly.
- **Expected HTTP Status:** UNKNOWN by official specification (`400 Bad Request` is standard Express body-parser behavior, but treated as observed implementation behavior).
- **Response Assertion:** Controlled error response; no unhandled crash; no process termination.
- **State Assertion:** Zero rows inserted into SQLite `users` table (`COUNT(*) = 0` for `stu001_malformed@example.com`).
- **Setup / Cleanup:** None required.
- **Automation Status:** READY FOR POSTMAN AUTOMATION (Requires raw body sending without auto-formatting).

---

### FR01-STU-002: Unsupported Content-Type Header (`text/plain`) Robustness Probe
- **Test ID:** FR01-STU-002
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** FR-01 — Account Registration
- **Requirement Reference:** FR-01 (`api_specification.md` Line 14)
- **SEC Reference:** Best Practice Content-Type Enforcement
- **Oracle Classification:** ROBUSTNESS / PROTOCOL CHARACTERIZATION; UNKNOWN (Exact HTTP Status)
- **Category:** Robustness / MIME Type Handling
- **Test Objective:** Verify protocol behavior when a syntactically valid registration JSON payload is sent with an unexpected `Content-Type: text/plain` header.
- **Preconditions:** SUT running.
- **Initial State:** Email `stu002_plaintext@example.com` unregistered.
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: text/plain`
- **Concrete Request Body:**
  ```json
  {
    "name": "PlainText ContentType",
    "email": "stu002_plaintext@example.com",
    "password": "Password123!"
  }
  ```
- **Expected Semantic Behavior:** Protocol handling is UNKNOWN by official specification. If parser ignores non-JSON MIME types, request should not be parsed into body object; if tolerant, it may parse. Safe expectation: no unhandled crash, no unintended side effects.
- **Expected HTTP Status:** UNKNOWN by official specification (`400`, `415 Unsupported Media Type`, or fallback observed).
- **Response Assertion:** Controlled response; server remains operational.
- **State Assertion:** If body is unparsed (`req.body` undefined), zero rows inserted. Database integrity preserved.
- **Setup / Cleanup:** Cleanup row if inserted: `DELETE FROM users WHERE email = 'stu002_plaintext@example.com'`.
- **Automation Status:** READY FOR POSTMAN AUTOMATION

---

### FR01-STU-003: Duplicate JSON Property Key Parser Characterization Probe
- **Test ID:** FR01-STU-003
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** FR-01 — Account Registration
- **Requirement Reference:** FR-01 (`README.md` Line 33 — Uniqueness & Parsing)
- **SEC Reference:** Best Practice RFC 8259 Key Precedence Handling
- **Oracle Classification:** ROBUSTNESS / PARSER CHARACTERIZATION; INFERRED (Single Account Creation)
- **Category:** Robustness / JSON Duplicate Key Precedence
- **Test Objective:** Characterize how the backend JSON parser resolves duplicate property keys (`email`) in a single payload; verify whether first key wins, last key wins, or an error is raised; verify that at most one single account is created.
- **Preconditions:** SUT running.
- **Initial State:** Emails `first_stu003@example.com` and `second_stu003@example.com` unregistered.
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Concrete Request Body (Raw Text):**
  ```json
  {
    "name": "Duplicate Key User",
    "email": "first_stu003@example.com",
    "email": "second_stu003@example.com",
    "password": "Password123!"
  }
  ```
- **Expected Semantic Behavior:** JSON RFC 8259 notes duplicate keys may produce implementation-defined behavior. Official specification does not define precedence. Deterministic safe requirement: exactly ONE account created (or request cleanly rejected); zero database corruption; no creation of two separate user records from a single request.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). If rejected, `400 Bad Request` (INFERRED).
- **Response Assertion:** Controlled JSON response; body contains message and ID if registered.
- **State Assertion:** Exactly 1 total record created between the two candidate emails; verify which key won at runtime.
- **Setup / Cleanup:** Cleanup both potential emails: `DELETE FROM users WHERE email IN ('first_stu003@example.com', 'second_stu003@example.com')`.
- **Automation Status:** READY FOR POSTMAN AUTOMATION (Requires raw JSON text to prevent client-side deduplication).

---

### FR01-STU-004: Unsupported HTTP Method (`PUT`) Routing Verification Probe
- **Test ID:** FR01-STU-004
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** FR-01 — Account Registration
- **Requirement Reference:** FR-01 (`api_specification.md` Line 11 — Only `POST` Documented)
- **SEC Reference:** Best Practice HTTP Verb Tampering Protection
- **Oracle Classification:** SPECIFIED (Route Non-Execution); UNKNOWN (Exact Error HTTP Status)
- **Category:** Negative / HTTP Verb Routing Validation
- **Test Objective:** Verify that calling `/api/register` with an unsupported HTTP verb (`PUT`) does NOT execute account registration.
- **Preconditions:** SUT running.
- **Initial State:** Email `stu004_put@example.com` unregistered.
- **Method:** `PUT`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Concrete Request Body:**
  ```json
  {
    "name": "Put Method User",
    "email": "stu004_put@example.com",
    "password": "Password123!"
  }
  ```
- **Expected Semantic Behavior:** Registration must NOT execute through unsupported HTTP method (SPECIFIED contract rule: only `POST /api/register` exists).
- **Expected HTTP Status:** UNKNOWN by official course specification (`404 Not Found` or `405 Method Not Allowed` are framework defaults, treated as observed implementation behavior).
- **Response Assertion:** Controlled error response; no crash.
- **State Assertion:** Zero rows inserted into `users` table (`COUNT(*) = 0` for `stu004_put@example.com`).
- **Setup / Cleanup:** None required.
- **Automation Status:** READY FOR POSTMAN AUTOMATION

---

### FR01-STU-005: Email Domain as IP Address Literal Characterization Probe
- **Test ID:** FR01-STU-005
- **Origin:** Student-selected from AI brainstorming
- **Student Selection:** CONFIRMED
- **Feature:** FR-01 — Account Registration
- **Requirement Reference:** FR-01 (`README.md` Line 33 — "Email hợp lệ (user@domain.com)")
- **SEC Reference:** N/A
- **Oracle Classification:** EMAIL FORMAT CHARACTERIZATION / ROBUSTNESS; UNKNOWN (Acceptance Oracle)
- **Category:** Robustness / Email Grammar Boundary Characterization
- **Test Objective:** Characterize backend email validation when the domain portion is represented as an IP address literal (`user@[127.0.0.1]`); verify whether RFC 5321 address-literal syntax is supported or whether validation strictly enforces standard alphanumeric DNS hostnames.
- **Preconditions:** SUT running.
- **Initial State:** Target email `stu005_ip@[127.0.0.1]` unregistered.
- **Method:** `POST`
- **Endpoint:** `/api/register`
- **Headers:** `Content-Type: application/json`
- **Concrete Request Body:**
  ```json
  {
    "name": "IP Domain User",
    "email": "stu005_ip@[127.0.0.1]",
    "password": "Password123!"
  }
  ```
- **Expected Semantic Behavior:** Specification states `user@domain.com`. Whether IP address literal domains are accepted is UNKNOWN / CHARACTERIZATION. Deterministic safe requirement: clean acceptance or clean rejection without crash or SQL error. Rejection must not be classified as a defect unless official course specification is violated.
- **Expected HTTP Status:** If accepted, `200 OK` (SPECIFIED). If rejected by hostname regex, `400 Bad Request` (INFERRED).
- **Response Assertion:** Controlled response; no unhandled crash.
- **State Assertion:** If accepted, email stored faithfully without character truncation.
- **Setup / Cleanup:** Cleanup created row if inserted: `DELETE FROM users WHERE email = 'stu005_ip@[127.0.0.1]'`.
- **Automation Status:** READY FOR POSTMAN AUTOMATION
