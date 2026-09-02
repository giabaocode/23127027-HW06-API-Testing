# [DEF-FR01-05] Medium: Missing Email Format Syntax Validation (FR-01 Violation)

- **Defect ID:** `DEF-FR01-05`
- **Feature Area:** FR-01 (Account Registration — Email Syntax)
- **Endpoint:** `POST /api/register`
- **Severity:** **Medium** (Input Validation / Specification Compliance)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Associated Test Cases:** `FR01-AI-013`, `FR01-AI-014`

---

## 1. Description

The registration endpoint accepts syntactically malformed email addresses that lack an at-symbol (`@`) or omit the domain portion entirely. The SUT responds with `HTTP 200 OK` and saves the malformed string directly into the database.

This directly violates requirement **`FR-01`** stated in `README.md` (Line 33):
> *"Email hợp lệ (user@domain.com)."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 20–30), there is no email format validation check before the database query is executed. Any string supplied under the `email` key is stored directly.

---

## 3. Steps to Reproduce

Send registration requests with malformed email strings:
1. **Missing At-Symbol (`@`):**
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name":"Invalid Email","email":"invalidemaildomain.com","password":"Password123!"}'
   ```
2. **Missing Domain Portion:**
   ```bash
   curl -X POST http://localhost:3000/api/register \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name":"Invalid Email","email":"user@","password":"Password123!"}'
   ```

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  The server must validate the email syntax against standard RFC email patterns (e.g. `user@domain.com`) and return `HTTP 400 Bad Request` (`{"error": "Invalid email format"}`).
- **Actual Behavior:**
  Both requests return `HTTP 200 OK` (`"message": "User registered successfully"`).

---

## 5. Automated Evidence

- **Newman Test Results:**
  - `FR01-AI-013 — Malformed Email Missing At-Symbol (@) Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-014 — Malformed Email Missing Domain Part Rejection`: `AssertionError: expected 200 to not equal 200`

---

## 6. Suggested Remediation

Add RFC 5322 regex validation in the route handler:
```javascript
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!EMAIL_REGEX.test(email)) {
  return res.status(400).json({ error: "Invalid email format" });
}
```
