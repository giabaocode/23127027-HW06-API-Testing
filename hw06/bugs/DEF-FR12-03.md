# [DEF-FR12-03] High: Missing Administrator Role Check on Category Mutations (/api/categories)

- **Defect ID:** `DEF-FR12-03`
- **GitHub Issue:** [#10](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/10)
- **Feature Area:** FR-12 (Access Control) / SEC-03
- **Endpoints:**
  - `POST /api/categories` (Create Category)
  - `PUT /api/categories/:id` (Update Category)
  - `DELETE /api/categories/:id` (Delete Category)
- **Severity:** **High** (Broken Function Level Access Control / Unauthorized Taxonomy Mutation)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED DEFECT**
- **Associated Test Cases:** `FR12-AI-011` .. `FR12-AI-013` (6 Newman assertion failures)

---

## 1. Description

While category mutations (`POST /api/categories`, `PUT /api/categories/:id`, `DELETE /api/categories/:id`) require authentication (rejecting anonymous callers with 401), they do not verify that the authenticated caller holds the administrator role (`role === 'admin'`). Standard authenticated users (`role = 'user'`) are permitted to add new categories, rename existing categories, and delete categories from the store taxonomy.

This violates `README.md` Section 9, Line 280 (`SEC-03`):
> *"Admin API: Token phải có role === 'admin'. User thường không được truy cập."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 249–270):
```javascript
app.post("/api/categories", authenticateToken, (req, res) => {
  const { name } = req.body;
  db.run("INSERT INTO categories (name) VALUES (?)", [name], function (err) { ... });
});

app.put("/api/categories/:id", authenticateToken, (req, res) => {
  const { name } = req.body;
  db.run("UPDATE categories SET name = ? WHERE id = ?", [name, req.params.id], function (err) { ... });
});

app.delete("/api/categories/:id", authenticateToken, (req, res) => {
  db.run("DELETE FROM categories WHERE id = ?", [req.params.id], function (err) { ... });
});
```

The handlers mount `authenticateToken`, which validates JWT token authenticity, but omit checking `req.user.role === 'admin'`.

---

## 3. Steps to Reproduce

1. Start backend server: `node backend/server.js` on port 3000.
2. Authenticate as a non-admin user (`role = 'user'`) using email `customer@example.com` / `customer123`.
3. Send a category creation request:
   ```bash
   curl -i -X POST http://localhost:3000/api/categories \
     -H "Authorization: Bearer <STANDARD_USER_TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name": "Unauthorized Category"}'
   ```
4. **Observed Behavior:** SUT responds with `HTTP/1.1 200 OK` (`{"message": "Category created", "id": ...}`) and creates the category.
5. **Expected Behavior:** SUT must reject the standard user request with semantic denial (`HTTP 403 Forbidden`).

---

## 4. Remediation Recommendation

Require administrator clearance for all category mutations:
```javascript
app.post("/api/categories", authenticateToken, authorizeAdmin, (req, res) => { ... });
app.put("/api/categories/:id", authenticateToken, authorizeAdmin, (req, res) => { ... });
app.delete("/api/categories/:id", authenticateToken, authorizeAdmin, (req, res) => { ... });
```
