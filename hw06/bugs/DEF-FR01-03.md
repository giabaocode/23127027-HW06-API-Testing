# [DEF-FR01-03] High: Missing Password Complexity Policy Enforcement (FR-01 Violation)

- **Defect ID:** `DEF-FR01-03`
- **Feature Area:** FR-01 (Account Registration — Password Policy)
- **Endpoint:** `POST /api/register`
- **Severity:** **High** (Security / Specification Compliance)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Associated Test Cases:** `FR01-AI-025`, `FR01-AI-026`, `FR01-AI-029`, `FR01-AI-030`, `FR01-AI-031`

---

## 1. Description

The registration endpoint accepts arbitrary weak passwords that violate the mandatory password policy. Passwords under 8 characters, passwords without uppercase letters, passwords without lowercase letters, passwords without digits, and passwords without any special symbols from `@, $, &` are accepted without error and returned with `HTTP 200 OK`.

This directly violates requirement **`FR-01`** stated in `README.md` (Line 34):
> *"Mật khẩu tối thiểu 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt (@, $, &)."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 20–30), the controller extracts `password` from `req.body` and sends it directly to SQLite without any regular expression or policy validation function:
```javascript
app.post("/api/register", (req, res) => {
  const { name, email, password } = req.body;
  db.run("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", [name, email, password], ...);
});
```
There is zero validation logic inspecting length or character set constraints.

---

## 3. Steps to Reproduce

Send registration requests with various non-compliant passwords:
1. **Missing Special Symbol:** `"password": "Password1234"`
2. **Under 8 Characters (Length 7):** `"password": "Pass1!a"`
3. **Missing Uppercase Letter:** `"password": "password123!"`
4. **Missing Lowercase Letter:** `"password": "PASSWORD123!"`
5. **Missing Numeric Digit:** `"password": "Password!@#$"`

Example curl:
```bash
curl -X POST http://localhost:3000/api/register \
  -H "Content-Type: application/json" \
  -H "X-Student-Id: 23127027" \
  -d '{"name":"Weak Pass User","email":"weak_pass@example.com","password":"123"}'
```

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  The server must reject non-compliant passwords with an error status (e.g. `400 Bad Request` or `422 Unprocessable Entity`) and return an error message detailing the unmet password policy rules.
- **Actual Behavior:**
  Every weak password is accepted with `HTTP 200 OK` (`"message": "User registered successfully"`).

---

## 5. Automated Evidence

- **Newman Test Results:**
  - `FR01-AI-025 — Missing Required Special Character from Set Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-026 — Password Length Boundary: 7 Chars (Minimum - 1) Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-029 — Missing Uppercase Letter in Password Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-030 — Missing Lowercase Letter in Password Rejection`: `AssertionError: expected 200 to not equal 200`
  - `FR01-AI-031 — Missing Numeric Digit in Password Rejection`: `AssertionError: expected 200 to not equal 200`

---

## 6. Suggested Remediation

Implement a password validation helper using regex:
```javascript
function validatePassword(pwd) {
  if (typeof pwd !== "string") return false;
  if (pwd.length < 8) return false;
  if (!/[A-Z]/.test(pwd)) return false;
  if (!/[a-z]/.test(pwd)) return false;
  if (!/[0-9]/.test(pwd)) return false;
  if (!/[@$&]/.test(pwd)) return false;
  return true;
}

if (!validatePassword(password)) {
  return res.status(400).json({ error: "Password does not meet required policy criteria" });
}
```
