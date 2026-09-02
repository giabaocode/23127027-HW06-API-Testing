# [DEF-FR07-02] High: POST /api/cart Accepts Invalid, Negative, Zero, and Fractional Quantities Without Validation

- **Defect ID:** `DEF-FR07-02`
- **GitHub Issue:** [#7](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/7)
- **Feature Area:** FR-07 (Shopping Cart Management)
- **Endpoint:** `POST /api/cart`
- **Severity:** **High** (Input Validation Defect / Business Rule Violation)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED DEFECT**
- **Associated Test Cases:** `FR07-AI-014`, `FR07-AI-015`, `FR07-AI-016`, `FR07-AI-017`, `FR07-AI-018`, `FR07-AI-020`, `FR07-AI-021`, `FR07-AI-023`, `FR07-AI-024`

---

## 1. Description

The `POST /api/cart` endpoint fails to perform any validation on the `quantity` parameter. It accepts zero ($q=0$), negative integers ($q=-1, -100$), fractional floating-point numbers ($q=1.5, 0.5$), non-numeric strings ($q="abc", "@#$"`), and completely omitted or null quantities, returning HTTP `200 OK` with `{"message":"Added to cart"}` and storing corrupted item entries in the user's cart.

This directly violates the mandatory business specification in `README.md` (Line 86):
> *"Có ô nhập Số lượng (chỉ nhận số nguyên dương, tối thiểu là 1)."*

---

## 2. Root Cause Analysis

In `backend/server.js` (Lines 290–295):
```javascript
app.post("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  userCarts[userId].push(req.body);
  res.json({ message: "Added to cart" });
});
```

There is zero validation logic for `req.body.quantity`. No check verifies that:
1. `quantity` exists and is non-null.
2. `quantity` is an integer (`Number.isInteger(q)`).
3. `quantity` is strictly positive ($\ge 1$).

Any arbitrary payload sent by a client is accepted and pushed directly into `userCarts[userId]`.

---

## 3. Steps to Reproduce

1. Start backend server (`node server.js` on port 3000).
2. Obtain a valid JWT Bearer token for an authenticated user.
3. Send a POST request with invalid negative quantity:
   ```bash
   curl -X POST http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -5}'
   ```
4. Check response status and body:
   - Status: `200 OK`
   - Body: `{"message":"Added to cart"}`
5. Inspect cart via `GET /api/cart`:
   - Returns: `[{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -5}]`

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  - **Expected Semantic Behavior:**
    - `quantity` must satisfy positive integer $\ge 1$ (`README.md` Line 86).
    - Invalid quantity values must NOT be accepted as valid cart mutations.
    - Cart state must remain completely unmodified by the invalid item (cart remains empty `[]`).
  - **Expected HTTP Status:** `UNKNOWN by official specification` (Controlled semantic rejection expected; exact HTTP status code such as 400 or 422 is unspecified and not required as formal contract oracle).
- **Actual Behavior (Runtime Observed):**
  - HTTP `200 OK` returned.
  - Invalid item with negative, zero, or corrupted quantity is saved into the shopping cart array.

---

## 5. Test Automation Evidence

- **Failing Newman Assertions (9 Boundary & Equivalence Partitions):**
  - `FR07-AI-014` ($q=0$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-015` ($q=-1$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-016` ($q=-100$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-017` ($q=1.5$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-018` ($q=0.5$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-020` ($q="abc"$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-021` ($q="@#$"$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-023` (omitted $q$): `expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-024` (null $q$): `expected 200 to be one of [ 400, 422 ]`
- **Newman Log Reference:** `hw06/newman/fr07/fr07-cli-output.txt` Lines 452–496.

---

## 6. Proposed Remediation

Validate `quantity` in `backend/server.js` before modifying cart state:
```javascript
app.post("/api/cart", authenticateToken, (req, res) => {
  const { id, name, price, quantity } = req.body;
  const q = Number(quantity);
  
  if (!Number.isInteger(q) || q < 1) {
    return res.status(400).json({ error: "Quantity must be a positive integer (minimum 1)" });
  }

  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  
  const existingItem = userCarts[userId].find(item => item.id === id);
  if (existingItem) {
    existingItem.quantity += q;
  } else {
    userCarts[userId].push({ id, name, price, quantity: q });
  }
  res.json({ message: "Added to cart" });
});
```
