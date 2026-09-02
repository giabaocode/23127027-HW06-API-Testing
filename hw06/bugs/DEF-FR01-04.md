# [DEF-FR01-04] High: Missing Mandatory Field Validation for Name, Email, and Password (FR-01 Violation)

- **Defect ID:** `DEF-FR01-04`
- **Feature Area:** FR-01 (Account Registration — Required Fields)
- **Endpoint:** `POST /api/register`
- **Severity:** **High** (Input Validation / API Robustness)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Associated Test Cases:** `FR01-AI-003`, `FR01-AI-004`, `FR01-AI-011`, `FR01-AI-012`, `FR01-AI-032`, `FR01-AI-035`

---

## 1. Description

The registration route accepts request payloads that completely omit one or more mandatory fields (`name`, `email`, or `password`), pass empty strings (`""`), or send an empty JSON object (`{}`). The server responds with `HTTP 200 OK` and creates a user row containing `NULL` or empty string values in the database.

This directly violates requirement **`FR-01`** stated in `README.md` (Line 32):
> *"Người dùng phải cung cấp: Họ Tên, Email, Mật khẩu."*

---

## 2. Root Cause Analysis

In `backend/database.js` (Lines 52–54), the schema does not enforce `NOT NULL` constraints on `name` or `email`:
```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    ...
);
```
Furthermore, `backend/server.js` (Lines 20–30) performs no check that `name`, `email`, or `password` are present and non-empty prior to executing the `INSERT` query.

---

## 3. Steps to Reproduce

1. Send an empty JSON object:
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{}'
   ```
2. Send a request omitting the `name` property:
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"email":"no_name@example.com","password":"Password123!"}'
   ```
3. Inspect the SQLite database row:
   ```bash
   sqlite3 backend/database.sqlite "SELECT id, name, email, password FROM users ORDER BY id DESC LIMIT 2;"
   ```

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  The server must validate presence of all required fields and reject requests with missing or empty values with `HTTP 400 Bad Request` (`{"error": "Missing required fields"}`).
- **Actual Behavior:**
  Returns `HTTP 200 OK` (`"message": "User registered successfully"`), inserting rows with `NULL` fields into the database.

---

## 5. Automated Evidence

- **Newman Test Results:**
  - `FR01-AI-003 — Omitted Mandatory Name Field Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-004 — Empty String Name Value Inferred Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-011 — Omitted Mandatory Email Field Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-012 — Empty String Email Value Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-032 — Empty String Password Value Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-035 — Empty JSON Body Rejection`: `AssertionError: expected 200 to not equal 200`

---

## 6. Suggested Remediation

1. Enforce `NOT NULL` in SQLite schema.
2. Add input validation guards at the start of `/api/register`:
   ```javascript
   if (!name || typeof name !== "string" || name.trim() === "") {
     return res.status(400).json({ error: "Field 'name' is required" });
   }
   if (!email || typeof email !== "string" || email.trim() === "") {
     return res.status(400).json({ error: "Field 'email' is required" });
   }
   if (!password || typeof password !== "string" || password.trim() === "") {
     return res.status(400).json({ error: "Field 'password' is required" });
   }
   ```
