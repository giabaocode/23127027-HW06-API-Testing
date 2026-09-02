# [DEF-FR07-01] High: Adding Duplicate Product to Cart Appends New Row Instead of Accumulating Quantity

- **Defect ID:** `DEF-FR07-01`
- **Feature Area:** FR-07 (Shopping Cart Management)
- **Endpoint:** `POST /api/cart`
- **Severity:** **High** (Business Logic Defect / Cart Integrity Failure)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED DEFECT**
- **Associated Test Cases:** `FR07-AI-009`, `FR07-AI-010`, `FR07-AI-011`, `FR07-STU-004`

---

## 1. Description

When an authenticated customer adds a product to their shopping cart that is already present in the cart, the SUT appends a completely new row into the cart array rather than locating the existing item and incrementing its quantity.

This directly violates the mandatory business requirement specified in `README.md` (Line 96):
> *"Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới."*

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

The handler unconditionally executes `userCarts[userId].push(req.body)`. It performs zero checks to see whether an entry with matching `id` already exists in `userCarts[userId]`. Consequently, each POST request appends an independent object to the array, resulting in duplicate product rows and fragmented quantities.

---

## 3. Steps to Reproduce

1. Start backend server (`node server.js` on port 3000).
2. Obtain a valid JWT Bearer token for user A.
3. Send first addition request:
   ```bash
   curl -X POST http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}'
   ```
4. Send second addition request for the same product ID:
   ```bash
   curl -X POST http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3}'
   ```
5. Inspect cart state via `GET /api/cart`:
   ```bash
   curl -X GET http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "X-Student-Id: 23127027"
   ```

---

## 4. Expected vs. Actual Behavior

- **Expected Behavior:**
  - Cart contains exactly ONE item: `[{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 5}]`.
  - Quantity is accumulated ($2 + 3 = 5$).
- **Actual Behavior (Runtime Observed):**
  - Cart contains TWO separate items:
    ```json
    [
      {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
      {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3}
    ]
    ```

---

## 5. Test Automation Evidence

- **Failing Newman Assertions:**
  - `FR07-AI-009 (Step 3)`: `expected 2 to deeply equal 1` (duplicate rows) and `expected 2 to deeply equal 5` (unaccumulated quantity).
  - `FR07-AI-010 (Step 4)`: `expected 3 to deeply equal 2` (duplicate rows) and `expected 1 to deeply equal 5`.
  - `FR07-AI-011 (Step 3)`: `expected 2 to deeply equal 1` and `expected 1 to deeply equal 2`.
  - `FR07-STU-004 (Step 3)`: `expected 2 to deeply equal 1` and `expected 2 to deeply equal 5`.
- **Newman Log Reference:** `hw06/newman/fr07/fr07-cli-output.txt` Lines 420–451 and Lines 497–506.

---

## 6. Proposed Remediation

In `backend/server.js`, locate the existing item in `userCarts[userId]` by `id`. If found, increment its `quantity`; otherwise, push the new item:
```javascript
app.post("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  
  const existingItem = userCarts[userId].find(item => item.id === req.body.id);
  if (existingItem) {
    existingItem.quantity += Number(req.body.quantity);
  } else {
    userCarts[userId].push(req.body);
  }
  res.json({ message: "Added to cart" });
});
```
