# [DEF-FR01-01] Critical: User Passwords Stored in Plaintext in SQLite Database (SEC-01 Violation)

- **Defect ID:** `DEF-FR01-01`
- **Feature Area:** FR-01 (Account Registration) / SEC-01 (Password Storage Security)
- **Endpoint:** `POST /api/register`
- **Severity:** **Critical** (CWE-256: Unprotected Storage of Credentials, CWE-312: Cleartext Storage of Sensitive Information)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Associated Test Case:** `FR01-AI-037` (Database Inspection Probe)

---

## 1. Description

When a new user registers via `POST /api/register`, the submitted password string is inserted directly into the SQLite database (`backend/database.sqlite`) in raw plaintext without applying any cryptographic hashing algorithm (such as bcrypt, Argon2, or PBKDF2) or salt.

This directly violates requirement **`SEC-01`** stated in `README.md` (Line 278):
> *"Mật khẩu người dùng phải được mã hoá (hash) trước khi lưu vào cơ sở dữ liệu."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 20–30):
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
The parameter `password` extracted from `req.body` is directly passed to `db.run()` without any hashing step. In `backend/database.js` (Line 54), the schema defines `password TEXT`, allowing raw strings to persist permanently.

---

## 3. Steps to Reproduce

1. Start the backend server (`node server.js` on port 3000).
2. Send a registration request with a known password:
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name":"SEC01 Test","email":"sec01_repro@example.com","password":"SuperSecretPassword123!"}'
   ```
3. Inspect the SQLite database row:
   ```bash
   sqlite3 backend/database.sqlite "SELECT id, email, password FROM users WHERE email = 'sec01_repro@example.com';"
   ```

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  The `password` column in table `users` must contain a salted cryptographic hash (e.g. `$2b$10$...`).
  Verification oracle: `stored_password != submitted_plaintext_password`.
- **Actual Behavior:**
  The `password` column contains the exact plaintext string:
  ```text
  3|sec01_repro@example.com|SuperSecretPassword123!
  ```

---

## 5. Automated Evidence

- Script: `hw06/postman/scripts/verify-sec01-plaintext.js`
- Real CLI Output:
  ```text
  DATABASE RECORD FOUND:
  Stored Email:    fr01_sec01_1788333652931@example.com
  Stored Password: SecretPlaintextPassword123!
  COMPARISON: stored_password === submitted_plaintext: true
  SECURITY VERDICT: FAILED (SEC-01 VIOLATION CONFIRMED)
  ```

---

## 6. Suggested Remediation

1. Install `bcrypt` or `bcryptjs`.
2. Hash the password before insertion:
   ```javascript
   const bcrypt = require("bcrypt");
   const saltRounds = 10;
   const hashedPassword = await bcrypt.hash(password, saltRounds);
   db.run("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", [name, email, hashedPassword], ...);
   ```
