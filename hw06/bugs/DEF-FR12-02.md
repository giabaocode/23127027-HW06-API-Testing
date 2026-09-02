# [DEF-FR12-02] Critical: Complete Absence of Authentication on Product Catalog Mutations (/api/products)

- **Defect ID:** `DEF-FR12-02`
- **GitHub Issue:** [#9](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/9)
- **Feature Area:** FR-12 (Access Control) / SEC-02 & SEC-03
- **Endpoints:**
  - `POST /api/products` (Create Product)
  - `PUT /api/products/:id` (Update Product)
  - `DELETE /api/products/:id` (Delete Product)
- **Severity:** **Critical** (Unauthenticated Public Catalog Mutation / Data Integrity Vulnerability)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED DEFECT**
- **Associated Test Cases:** `FR12-AI-008` .. `FR12-AI-010`, `FR12-AI-029` .. `FR12-AI-031` (10 Newman assertion failures)

---

## 1. Description

The product mutation endpoints (`POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id`) completely omit authentication middleware. Anonymous callers without any `Authorization` header and standard non-administrative users (`role = 'user'`) can create new products, overwrite existing product prices/descriptions, and permanently delete products from the public catalog.

This directly violates:
- `README.md` Section 9, Line 275 (`SEC-02`):
  > *"Protected API: Phải có header Authorization: Bearer <token>. Không có token -> 401 Unauthorized."*
- `README.md` Section 9, Line 280 (`SEC-03`):
  > *"Admin API: Token phải có role === 'admin'. User thường không được truy cập."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 167–196):
```javascript
app.post("/api/products", (req, res) => {
  const { name, price, description, imageUrl, category_id } = req.body;
  db.run("INSERT INTO products ...", [...], function (err) { ... });
});

app.put("/api/products/:id", (req, res) => {
  const { name, price, description, imageUrl, category_id } = req.body;
  db.run("UPDATE products ...", [...], function (err) { ... });
});

app.delete("/api/products/:id", (req, res) => {
  db.run("DELETE FROM products WHERE id = ?", [req.params.id], function (err) { ... });
});
```

Neither `authenticateToken` nor any role authorization middleware is mounted on these mutation routes. The handlers execute directly for any incoming HTTP request.

---

## 3. Steps to Reproduce

1. Start backend server: `node backend/server.js` on port 3000.
2. Send an anonymous POST request with no Authorization header:
   ```bash
   curl -i -X POST http://localhost:3000/api/products \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"name": "Vandalized Product", "price": 1000, "description": "Hacked", "category_id": 1}'
   ```
3. **Observed Behavior:** SUT responds with `HTTP/1.1 200 OK` (`{"message": "Product created", "id": ...}`) and commits the item to the database.
4. **Expected Behavior:** SUT must reject the unauthenticated request with `HTTP 401 Unauthorized`.

---

## 4. Remediation Recommendation

Bind both `authenticateToken` and admin role authorization to all mutation routes:
```javascript
app.post("/api/products", authenticateToken, authorizeAdmin, (req, res) => { ... });
app.put("/api/products/:id", authenticateToken, authorizeAdmin, (req, res) => { ... });
app.delete("/api/products/:id", authenticateToken, authorizeAdmin, (req, res) => { ... });
```
