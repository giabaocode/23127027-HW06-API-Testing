# [DEF-FR12-04] Medium: Missing Administrator Role Check on Master Coupon Listing (GET /api/coupons)

- **Defect ID:** `DEF-FR12-04`
- **GitHub Issue:** [#11](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/11)
- **Feature Area:** FR-12 (Access Control) / SEC-03
- **Endpoint:** `GET /api/coupons`
- **Severity:** **Medium** (Information Disclosure / Sensitive Promotional Strategy Leak)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED DEFECT**
- **Associated Test Cases:** `FR12-AI-014` (2 Newman assertion failures)

---

## 1. Description

The endpoint `GET /api/coupons` provides a comprehensive listing of all active, inactive, and unreleased promotional coupons, including discount percentages, minimum order thresholds, expiry dates, and usage limits. While anonymous requests are rejected with 401, standard authenticated users (`role = 'user'`) can call `GET /api/coupons` and receive the entire master coupon table.

Standard users should only be able to validate specific coupon codes at checkout (`POST /api/cart/apply-coupon`), rather than scraping all administrative coupon codes and business promotion rules.

This violates `README.md` Section 9, Line 280 (`SEC-03`):
> *"Admin API: Token phải có role === 'admin'. User thường không được truy cập."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 355–360):
```javascript
app.get("/api/coupons", authenticateToken, (req, res) => {
  db.all("SELECT * FROM coupons", [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});
```

The route mounts `authenticateToken` but does not enforce administrative privileges (`req.user.role === 'admin'`).

---

## 3. Steps to Reproduce

1. Start backend server: `node backend/server.js` on port 3000.
2. Authenticate as a non-admin user (`role = 'user'`) using email `customer@example.com` / `customer123`.
3. Send a GET request to `/api/coupons`:
   ```bash
   curl -i http://localhost:3000/api/coupons \
     -H "Authorization: Bearer <STANDARD_USER_TOKEN>" \
     -H "X-Student-Id: 23127027"
   ```
4. **Observed Behavior:** SUT responds with `HTTP/1.1 200 OK` and returns all coupons in the system.
5. **Expected Behavior:** SUT must restrict this overview to administrators with semantic denial (`HTTP 403 Forbidden`).

---

## 4. Remediation Recommendation

Require administrator authorization:
```javascript
app.get("/api/coupons", authenticateToken, authorizeAdmin, (req, res) => {
  db.all("SELECT * FROM coupons", [], (err, rows) => { ... });
});
```
