# [DEF-FR12-01] Critical: Missing Administrator Role Verification on Administrative Endpoints (/api/admin/*)

- **Defect ID:** `DEF-FR12-01`
- **GitHub Issue:** [#8](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/8)
- **Feature Area:** FR-12 (Access Control / Kiểm soát truy cập)
- **Endpoints:**
  - `GET /api/admin/users`
  - `DELETE /api/admin/users/:id`
  - `GET /api/admin/orders`
  - `PUT /api/admin/orders/:id/status`
  - `POST /api/admin/import-products`
  - `POST /api/admin/coupons`
  - `DELETE /api/admin/coupons/:id`
- **Severity:** **Critical** (Privilege Escalation / Broken Object Level & Function Level Access Control)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED DEFECT**
- **Associated Test Cases:** `FR12-AI-001` .. `FR12-AI-007`, `FR12-AI-037`, `FR12-AI-038`, `FR12-STU-003` .. `FR12-STU-005` (21 Newman assertion failures)

---

## 1. Description

All administrative endpoints prefixed with `/api/admin/*` in the SUT are accessible to standard authenticated users (`role = 'user'`), users with omitted role claims, users with whitespace-padded role claims (`role = ' admin '`), and callers providing request-body overrides (`"role": "admin"`). 

The SUT returns HTTP `200 OK` and executes administrative actions, allowing standard authenticated users (with role='user') to:
1. Extract all registered user accounts (`GET /api/admin/users`).
2. Permanently delete user accounts (`DELETE /api/admin/users/:id`).
3. View all user order records across the platform (`GET /api/admin/orders`).
4. Modify order fulfillment statuses (`PUT /api/admin/orders/:id/status`).
5. Perform bulk product imports (`POST /api/admin/import-products`).
6. Create system-wide promotional coupons (`POST /api/admin/coupons`).
7. Delete promotional coupons (`DELETE /api/admin/coupons/:id`).

This directly violates the mandatory course security specification in `README.md` (Section 9, Line 280, `SEC-03`):
> *"Admin API: Token phải có role === 'admin'. User thường không được truy cập."*

And `api_specification.md` Section 5.2 (Line 167):
> *"Kiểm soát truy cập: Chỉ admin mới có quyền thực hiện các thao tác quản trị."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 199, 457, 483, 494, 504, 510, 525):
```javascript
app.get("/api/admin/users", authenticateToken, (req, res) => { ... });
app.delete("/api/admin/users/:id", authenticateToken, (req, res) => { ... });
app.get("/api/admin/orders", authenticateToken, (req, res) => { ... });
app.put("/api/admin/orders/:id/status", authenticateToken, (req, res) => { ... });
app.post("/api/admin/import-products", authenticateToken, (req, res) => { ... });
app.post("/api/admin/coupons", authenticateToken, (req, res) => { ... });
app.delete("/api/admin/coupons/:id", authenticateToken, (req, res) => { ... });
```

While each administrative route mounts the `authenticateToken` middleware, `authenticateToken` only checks cryptographic signature validity and assigns `req.user = user`. **No role check (`req.user.role === 'admin'`) is ever performed**, either inside `authenticateToken` or within the handler functions.

---

## 3. Steps to Reproduce

1. Start backend server: `node backend/server.js` on port 3000.
2. Authenticate as a standard non-admin user (`role = 'user'`) using email `customer@example.com` / `customer123`.
3. Extract the issued JWT token (`role = 'user'`).
4. Send an administrative query with the standard-user token:
   ```bash
   curl -i http://localhost:3000/api/admin/users \
     -H "Authorization: Bearer <STANDARD_USER_TOKEN>" \
     -H "X-Student-Id: 23127027"
   ```
5. **Observed Behavior:** SUT responds with `HTTP/1.1 200 OK` and returns JSON array containing all registered users, passwords, and sensitive fields.
6. **Expected Behavior:** SUT must reject the request with semantic access denial (`HTTP 403 Forbidden`).

---

## 4. Remediation Recommendation

Introduce a dedicated `authorizeAdmin` middleware and apply it to all `/api/admin/*` routes:
```javascript
const authorizeAdmin = (req, res, next) => {
  if (!req.user || req.user.role !== "admin") {
    return res.status(403).json({ error: "Forbidden: Admin role required" });
  }
  next();
};

app.use("/api/admin", authenticateToken, authorizeAdmin);
```
