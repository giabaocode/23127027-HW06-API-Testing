# [FR07-BUG-002] Missing Quantity Domain Validation on POST /api/cart Accepts Zero, Negative, and Fractional Values

- **Bug ID:** `FR07-BUG-002` (Internal Ref: `DEF-FR07-02`)
- **GitHub Issue:** [#7 (Issue #7)](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/7)
- **Feature:** Pool B — FR-07 (Shopping Cart Management)
- **Endpoint:** `POST /api/cart`
- **Severity:** **High** (Input Validation Defect / Business Invariant Violation)
- **Priority:** **High** (Inventory & Payment Integrity)
- **Reported By:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
- **Status:** **RUNTIME-CONFIRMED SUT DEFECT**

---

## 1. Official Requirement & Reference

- **Primary Course Specification:** `README.md` Line 86
  > *"Có ô nhập Số lượng (chỉ nhận số nguyên dương, tối thiểu là 1)."*
- **API Specification:** `api_specification.md` Line 119 (`POST /api/cart`)

---

## 2. Related Test Cases

- `FR07-AI-014` (Boundary: Zero Quantity $q=0$)
- `FR07-AI-015` (Negative Boundary: Immediate Negative $q=-1$)
- `FR07-AI-016` (Negative Domain: Large Negative Integer $q=-100$)
- `FR07-AI-017` (Type Robustness: Positive Decimal $q=1.5$)
- `FR07-AI-018` (Type Robustness: Sub-Unit Decimal $q=0.5$)
- `FR07-AI-020` (Type Robustness: Non-Numeric Alphabetic String $q="abc"$)
- `FR07-AI-021` (Type Robustness: Special Symbol String $q="@#$"$)
- `FR07-AI-023` (Schema Completeness: Omitted Mandatory Quantity Field)
- `FR07-AI-024` (Schema Robustness: Explicit Null Quantity $q=null$)

---

## 3. Preconditions

1. Local SUT backend running on `http://localhost:3000`.
2. Test user registered and authenticated with a valid JWT Bearer token.
3. User's cart is initially empty.

---

## 4. Exact Reproduction Steps

1. Obtain a valid customer JWT Bearer token.
2. Transmit `POST /api/cart` with negative quantity ($q=-5$):
   ```bash
   curl -X POST http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "Content-Type: application/json" \
     -H "X-Student-Id: 23127027" \
     -d '{"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -5}'
   ```
3. Inspect HTTP response code and response body.
4. Verify cart mutation by sending:
   ```bash
   curl -X GET http://localhost:3000/api/cart \
     -H "Authorization: Bearer <TOKEN>" \
     -H "X-Student-Id: 23127027"
   ```

---

## 5. Expected vs. Actual Result

- **Expected Result:**
  - **Expected Semantic Behavior:**
    - `quantity` must satisfy positive integer $\ge 1$ (`README.md` Line 86).
    - Invalid quantity values must NOT be accepted as valid cart mutations.
    - Cart state must remain completely unmodified by the invalid item (cart remains empty `[]`).
  - **Expected HTTP Status:** `UNKNOWN by official specification` (Controlled semantic rejection expected; exact HTTP status code such as 400 or 422 is unspecified and not required as formal contract oracle).
- **Actual Result (Runtime Observed):**
  - HTTP Status: `200 OK`.
  - Response Body: `{"message":"Added to cart"}`.
  - Cart State: The negative/invalid item is saved into the shopping cart array:
    ```json
    [
      { "id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -5 }
    ]
    ```

---

## 6. Reproducibility & Environment

- **Reproducibility:** 100% deterministic (reproduced across 9 distinct boundary, equivalence, and robustness test cases).
- **Environment:**
  - Operating System: macOS
  - Runtime: Node.js v20.20.2 / Express v5.2.1
  - SUT Base URL: `http://localhost:3000`

---

## 7. Real Test Execution Evidence

- **Newman CLI Execution Log:** [`hw06/newman/fr07/fr07-cli-output.txt`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/fr07/fr07-cli-output.txt) (Lines 452–496)
- **Newman Interactive HTML Report:** [`hw06/newman/fr07/fr07-report.html`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/fr07/fr07-report.html)
- **Real Execution Report:** [`hw06/docs/fr07-execution-report.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/fr07-execution-report.md)
- **Postman Console Authentication & Student Evidence:** [`hw06/screenshots/fr07-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr07-x-student-id.png)
- **Failing Assertion Details:**
  - `FR07-AI-014` ($q=0$): `SUT violation: accepted invalid quantity 0 with HTTP 200: expected 200 to be one of [ 400, 422 ]`
  - `FR07-AI-015` ($q=-1$): `SUT violation: accepted invalid quantity -1 with HTTP 200`
  - `FR07-AI-016` ($q=-100$): `SUT violation: accepted negative quantity -100`
  - `FR07-AI-017` ($q=1.5$): `SUT violation: accepted fractional quantity 1.5`
  - `FR07-AI-018` ($q=0.5$): `SUT violation: accepted sub-unit decimal 0.5`
  - `FR07-AI-020` ($q="abc"$): `SUT accepted non-numeric string quantity`
  - `FR07-AI-021` ($q="@#$"$): `SUT accepted symbol string quantity`
  - `FR07-AI-023` (omitted $q$): `SUT accepted cart addition missing quantity`
  - `FR07-AI-024` (null $q$): `SUT accepted null quantity`

---

## 8. Impact Analysis

- **Financial Impact:** Negative quantities can invert total order costs, allowing malicious actors to exploit checkout calculations (e.g. subtracting from total cart value).
- **Inventory Impact:** Zero or fractional quantities corrupt stock reservations and inventory decrements upon checkout.
- **Robustness Impact:** Omitted or string quantities cause `NaN` propagation during numeric summation in checkout calculation.

---

## 9. Suggested Engineering Direction

In `backend/server.js` (Line 290), add rigorous input validation:
```javascript
app.post("/api/cart", authenticateToken, (req, res) => {
  const { id, name, price, quantity } = req.body;
  const q = Number(quantity);

  if (quantity === undefined || quantity === null || !Number.isInteger(q) || q < 1) {
    return res.status(400).json({ error: "Quantity must be a positive integer >= 1" });
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
