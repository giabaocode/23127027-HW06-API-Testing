# [DEF-FR01-02] High: Duplicate Email Registration Succeeds with HTTP 200 (FR-01 Violation)

- **Defect ID:** `DEF-FR01-02`
- **Feature Area:** FR-01 (Account Registration — Email Uniqueness)
- **Endpoint:** `POST /api/register`
- **Severity:** **High** (Data Integrity Violation / Account Collision)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Associated Test Cases:** `FR01-AI-016`, `FR01-AI-017`

---

## 1. Description

The system allows multiple accounts to be registered with the exact same email address. When an existing email is submitted in a registration request, the SUT returns `HTTP 200 OK` (`"message": "User registered successfully"`) and inserts an additional duplicate row into the `users` table with a new `id`.

This directly violates requirement **`FR-01`** stated in `README.md` (Line 33):
> *"Email là duy nhất, không được trùng lặp với người dùng khác."*

---

## 2. Root Cause Analysis

1. **Missing SQL Constraint:**
   In `backend/database.js` (Line 53), the `users` table definition specifies:
   ```sql
   email TEXT,
   ```
   There is no `UNIQUE` constraint on the `email` column.
2. **Missing Pre-Check Query in Controller:**
   In `backend/server.js` (Lines 20–30), `app.post("/api/register")` executes an unconditional `INSERT INTO users` without first querying whether the requested email already exists in the database.

---

## 3. Steps to Reproduce

1. Register an initial account:
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name":"User One","email":"duplicate_test@example.com","password":"Password123!"}'
   ```
   *Result:* Returns `200 OK`, `{"id": 5}`.
2. Send the identical registration request again:
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name":"User Two","email":"duplicate_test@example.com","password":"Password123!"}'
   ```
3. Inspect SQLite rows:
   ```bash
   sqlite3 backend/database.sqlite "SELECT id, name, email FROM users WHERE email = 'duplicate_test@example.com';"
   ```

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  The second request must be rejected with an appropriate error status (e.g. `400 Bad Request` or `409 Conflict`) with an error message indicating that the email is already registered. Only one user record should exist in the database.
- **Actual Behavior:**
  The second request returns `200 OK` (`{"message": "User registered successfully", "id": 6}`) and creates a duplicate account row:
  ```text
  5|User One|duplicate_test@example.com
  6|User Two|duplicate_test@example.com
  ```

---

## 5. Automated Evidence

- **Newman Test Results:**
  - `FR01-AI-016 — Duplicate Registration of Pre-Seeded Email Rejection`:
    `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-017 — Duplicate Registration via Dynamic Sequential Call`:
    `AssertionError: expected 200 to not equal 200`

---

## 6. Suggested Remediation

1. Add `UNIQUE` constraint to the `email` column in SQLite:
   ```sql
   email TEXT UNIQUE NOT NULL,
   ```
2. Query existing email before insertion or catch the `SQLITE_CONSTRAINT` error and return `409 Conflict`:
   ```javascript
   db.get("SELECT id FROM users WHERE email = ?", [email], (err, row) => {
     if (row) return res.status(409).json({ error: "Email already registered" });
     // proceed with insert...
   });
   ```
