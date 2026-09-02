# [FR07-BUG-001] Adding Duplicate Product to Cart Appends New Row Instead of Accumulating Quantity

- **Bug ID:** `FR07-BUG-001` (Internal Ref: `DEF-FR07-01`)
- **GitHub Issue:** [#6 (Issue #6)](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/6)
- **Feature:** Pool B — FR-07 (Shopping Cart Management)
- **Endpoint:** `POST /api/cart`
- **Severity:** **High** (Business Logic Defect / Shopping Cart State Integrity Failure)
- **Priority:** **High** (Core E-Commerce Purchase Flow)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED SUT DEFECT**

---

## 1. Official Requirement & Reference

- **Primary Course Specification:** `README.md` Line 96
  > *"Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới."*
- **API Specification:** `api_specification.md` Line 119 (`POST /api/cart`)

---

## 2. Related Test Cases

- `FR07-AI-009` (Sequential Duplicate Addition: $q_1=2, q_2=3 \implies q=5$)
- `FR07-AI-010` (Interleaved Duplicate Addition: Product 1, Product 2, Product 1)
- `FR07-AI-011` (Unit Increment Accumulation: $q_1=1, q_2=1 \implies q=2$)
- `FR07-STU-004` (Duplicate Addition with Conflicting Client Metadata)

---

## 3. Preconditions

1. Local SUT backend running on `http://localhost:3000`.
2. Test user registered and authenticated with a valid JWT Bearer token.
3. User's cart is initially empty (`GET /api/cart` returns `[]`).

---

## 4. Exact Reproduction Steps

1. Obtain a valid customer JWT token via `POST /api/login`.
2. Send first request to add product ID `1` (quantity = 2):
   ```bash
   curl -X POST http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}'
   ```
3. Send second request to add the same product ID `1` (quantity = 3):
   ```bash
   curl -X POST http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3}'
   ```
4. Query the cart state via `GET /api/cart`:
   ```bash
   curl -X GET http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "X-Student-Id: 23127027"
   ```

---

## 5. Expected vs. Actual Result

- **Expected Result:**
  - `GET /api/cart` returns a JSON array containing **exactly 1 item**.
  - That item represents product ID `1` with accumulated quantity $5$ ($2 + 3$):
    ```json
    [
      { "id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 5 }
    ]
    ```
- **Actual Result (Runtime Observed):**
  - `GET /api/cart` returns an array containing **2 separate rows** for the same product ID:
    ```json
    [
      { "id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2 },
      { "id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3 }
    ]
    ```

---

## 6. Reproducibility & Environment

- **Reproducibility:** 100% deterministic (reproduced on every run across 4 distinct test suites).
- **Environment:**
  - Operating System: macOS
  - Runtime: Node.js v20.20.2 / Express v5.2.1
  - SUT Base URL: `http://localhost:3000`
  - In-memory cart store: `const userCarts = {};` (`backend/server.js` Line 14)

---

## 7. Real Test Execution Evidence

- **Newman CLI Execution Log:** [`hw06/newman/fr07/fr07-cli-output.txt`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/fr07/fr07-cli-output.txt) (Lines 420–451, 497–506)
- **Newman Interactive HTML Report:** [`hw06/newman/fr07/fr07-report.html`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/fr07/fr07-report.html)
- **Real Execution Report:** [`hw06/docs/fr07-execution-report.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/fr07-execution-report.md)
- **Postman Console Authentication & Student Evidence:** [`hw06/screenshots/fr07-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr07-x-student-id.png)
- **Failing Assertion Details:**
  - `FR07-AI-009 (Step 3)`: `expected 2 to deeply equal 1` (duplicate rows); `expected 2 to deeply equal 5` (unaccumulated quantity).
  - `FR07-AI-010 (Step 4)`: `expected 3 to deeply equal 2`; `expected 1 to deeply equal 5`.
  - `FR07-AI-011 (Step 3)`: `expected 2 to deeply equal 1`; `expected 1 to deeply equal 2`.
  - `FR07-STU-004 (Step 3)`: `expected 2 to deeply equal 1`; `expected 2 to deeply equal 5`.

---

## 8. Impact Analysis

- **Business Impact:** Distorts cart presentation in checkout; users see multiple fragmented entries for the same item instead of consolidated quantity. Can cause downstream billing, stock decrement, and order fulfillment errors when orders are placed.
- **Data Integrity Impact:** Violates the fundamental aggregate entity model of e-commerce shopping carts.

---

## 9. Suggested Engineering Direction

In `backend/server.js` (Lines 290–295), replace unconditional array push with duplicate checking:
```javascript
app.post("/api/cart", authenticateToken, (req, res) => {
  const userId = req.user.id;
  if (!userCarts[userId]) userCarts[userId] = [];
  
  const existingItem = userCarts[userId].find(item => item.id === req.body.id);
  if (existingItem) {
    existingItem.quantity = (Number(existingItem.quantity) || 0) + (Number(req.body.quantity) || 1);
  } else {
    userCarts[userId].push(req.body);
  }
  res.json({ message: "Added to cart" });
});
```
