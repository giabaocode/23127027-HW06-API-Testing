# FR-01: Account Registration — Real Execution & Test Report

> **Execution Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Execution Date & Time:** 2026-09-02T14:21:04+07:00
> - **Execution Tool:** Newman v6.2.2 with `newman-reporter-htmlextra`
> - **Target SUT URL:** `http://localhost:3000/api/register`
> - **Central Injection Verified:** `X-Student-Id: 23127027` on 100% of HTTP requests

---

## 1. Real SUT Startup & Environment

- **Backend Runtime:** Node.js v20.20.2 / Express v5.2.1
- **Database Path:** `/Users/phamngocgiabao/eshop-sut/backend/database.sqlite`
- **Startup Command:** `node server.js` (executed inside `/Users/phamngocgiabao/eshop-sut/backend`)
- **Real Server Output:** `Server is running on http://localhost:3000`
- **Database Baseline Reset:** Restored from `backend/database.sqlite.bak` prior to official test run.

---

## 2. Newman Execution Summary

```text
======================================================================
NEWMAN RUN METRICS — FR-01 REGISTRATION SUITE
======================================================================
Collection:          hw06/postman/collections/fr01-registration.postman_collection.json
Environment:         hw06/postman/environments/eshop-local.postman_environment.json
Total HTTP Requests: 43 (42 collection requests + 1 chained pre-request registration)
Total Assertions:    167
Passed Assertions:   139 (83.2%)
Failed Assertions:   28  (16.8%)
Skipped Tests:       0
----------------------------------------------------------------------
HTML Report Export:  hw06/newman/fr01/fr01-report.html (968 KB)
CLI Output Log:      hw06/newman/fr01/fr01-cli-output.txt (40 KB)
======================================================================
```

---

## 3. Central `X-Student-Id` Verification

- **Central Pre-Request Hook:** Injected `X-Student-Id: 23127027` on every request.
- **Automated Assertion:** `pm.test('Central Injection - Request header X-Student-Id is present and matches 23127027')`
- **Result:** **PASSED 42 / 42 times (100% pass rate)**.
- **Evidence:** Visible in Newman CLI log and interactive HTML report under each request header inspection tab.

---

## 4. Detailed Failure Triage & Defect Analysis

Every failing assertion was correlated against repository source code (`backend/server.js` Lines 20–30) and classified into root causes:

### Category A: Confirmed SUT Functional Defects (14 Requests / 28 Assertion Failures)

In `backend/server.js`, the `/api/register` endpoint contains zero input validation:
```javascript
app.post("/api/register", (req, res) => {
  const { name, email, password } = req.body;
  db.run(
    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
    [name, email, password],
    function (err) {
      if (err) return res.status(500).json({ error: err.message });
      res.json({ message: "User registered successfully", id: this.lastID });
    },
  );
});
```

1. **Mandatory Field Presence & Blank String Violations (6 cases):**
   - `FR01-AI-003` (missing name), `FR01-AI-004` (empty string name), `FR01-AI-011` (missing email), `FR01-AI-012` (empty string email), `FR01-AI-032` (empty string password), `FR01-AI-035` (empty JSON body `{}`).
   - **Observed Behavior:** SUT returns `200 OK` and inserts rows with `NULL` or empty strings into the database.
   - **Classification:** **LIKELY SUT DEFECT (Runtime-Confirmed)**. Violates `README.md` Lines 32–34.

2. **Email Format Validation Omission (2 cases):**
   - `FR01-AI-013` (missing `@`), `FR01-AI-014` (missing domain after `@`).
   - **Observed Behavior:** SUT returns `200 OK` and inserts invalid email strings.
   - **Classification:** **LIKELY SUT DEFECT (Runtime-Confirmed)**. Violates `README.md` Line 33.

3. **Password Policy Enforcement Omission (4 cases):**
   - `FR01-AI-025` (missing special symbol), `FR01-AI-026` (length 7), `FR01-AI-029` (missing uppercase), `FR01-AI-030` (missing lowercase), `FR01-AI-031` (missing digit).
   - **Observed Behavior:** SUT returns `200 OK` for weak passwords violating the 5 required policy criteria.
   - **Classification:** **LIKELY SUT DEFECT (Runtime-Confirmed)**. Violates `README.md` Line 34.

4. **Duplicate Email Uniqueness Omission (2 cases):**
   - `FR01-AI-016` (duplicate of seeded `test@eshop.com`), `FR01-AI-017` (sequential duplicate call).
   - **Observed Behavior:** SUT returns `200 OK` on duplicate registration attempts and creates duplicate user rows in SQLite because table `users` lacks a `UNIQUE(email)` constraint and `server.js` performs no existence lookup.
   - **Classification:** **LIKELY SUT DEFECT (Runtime-Confirmed)**. Violates `README.md` Line 33.

---

## 5. Non-API Database Security Verification (SEC-01)

- **Test ID:** `FR01-AI-037`
- **Execution Script:** `hw06/postman/scripts/verify-sec01-plaintext.js`
- **Execution Command:** `NODE_PATH=backend/node_modules node hw06/postman/scripts/verify-sec01-plaintext.js`
- **Submitted Password:** `"SecretPlaintextPassword123!"`
- **Direct Database Query:** `SELECT password FROM users WHERE email = ?`
- **Actual SQLite Value:** `"SecretPlaintextPassword123!"`
- **Security Verdict:** **FAILED (SEC-01 VIOLATION RUNTIME-CONFIRMED)**.
- **Root Cause:** Passwords are inserted directly into SQLite in plaintext without hashing (e.g. bcrypt). Violates `README.md` Line 278.

---

## 6. Successful Verifications & Characterization Findings

- **SEC-05 Parameterized Query Security (PASSED):**
  - `FR01-AI-007` (apostrophe in name `"O'Connor"`) and `FR01-AI-019` (redesigned SQL injection `"Robert'); DROP TABLE users;--"`) passed safely. Parameterized query placeholders `VALUES (?, ?, ?)` handled the syntax safely as literal data without database corruption or table drop.
- **Security Hardening (PASSED):**
  - `FR01-AI-038` passed; response JSON did not leak password, salt, hash, or token.
- **Robustness & Characterization (PASSED):**
  - Vietnamese Unicode diacritics (`FR01-AI-002`) accepted with 200 OK and preserved in UTF-8.
  - Non-string integer data types (`FR01-AI-005`, `015`, `033`), 1000-char name (`FR01-AI-006`), 128-char password (`FR01-AI-034`), and extra properties (`FR01-AI-036`) were handled without server crash.
- **Student-Selected Extensions (5/5 PASSED):**
  - `FR01-STU-001` (Malformed JSON missing brace): Express `bodyParser.json()` rejected the syntax with `400 Bad Request`, preventing user creation and server crash.
  - `FR01-STU-002` (`Content-Type: text/plain`): Handled safely without crash.
  - `FR01-STU-003` (Duplicate JSON key): Second email key won in V8 JSON parser; handled safely without multi-row corruption.
  - `FR01-STU-004` (Unsupported `PUT` verb): Express routing returned `404 Not Found`, preventing unauthorized registration.
  - `FR01-STU-005` (Email IP literal domain): Handled safely without crash.
