# FR-07: Shopping Cart — Compact Review Sheet

> **Document Status:** Student Final Reviewed Tracking Sheet
> **Student Reviewer:** Phạm Ngọc Gia Bảo (`23127027`)
> **Audit Date:** 2026-09-02

| Test ID | Coverage ID | One-Sentence Condition | Expected Oracle | Student Final Verdict | Student Note |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **`FR07-AI-001`** | `COV-FR07-01` | Authenticated user with no prior cart additions sends GET /api/cart | Return empty collection representing absence of items in user cart | **`VALID`** | Approved |
| **`FR07-AI-002`** | `COV-FR07-02` | Add 1 product (id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2) then retrieve cart | Cart returns an array containing exactly the single added item with matching properties | **`VALID`** | Approved |
| **`FR07-AI-003`** | `COV-FR07-02` | Add Product 1 (q=1) and Product 2 (q=3) then retrieve cart | Cart returns an array containing both distinct product items with their respective quantities | **`VALID`** | Approved |
| **`FR07-AI-004`** | `COV-FR07-03` | Send GET /api/cart with no Authorization header | Access denied; cart information not exposed to unauthenticated callers | **`VALID`** | Approved |
| **`FR07-AI-005`** | `COV-FR07-04` | Send GET /api/cart with JWT token having an invalid HMAC signature | Access denied; forged or invalid token rejected | **`INCOMPLETE`** | Calibrated: Keep exact error envelope UNKNOWN or IMPLEMENTATION-OBSERVED |
| **`FR07-AI-006`** | `COV-FR07-04` | Send GET /api/cart with raw token string without 'Bearer ' prefix | Access denied; non-Bearer scheme rejected cleanly | **`VALID`** | Approved |
| **`FR07-AI-007`** | `COV-FR07-05` | Send POST /api/cart with valid body { id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2 } | Item accepted and added to user's shopping cart session | **`VALID`** | Approved |
| **`FR07-AI-008`** | `COV-FR07-05` | Add product 1 then add product 2 | Second item accepted without removing or corrupting first item | **`VALID`** | Approved |
| **`FR07-AI-009`** | `COV-FR07-06` | POST product id: 1 with q=2, then POST product id: 1 with q=3, then GET cart | Cart must contain exactly ONE entry for product id: 1 with accumulated quantity === 5 (2 + 3) | **`VALID`** | Approved |
| **`FR07-AI-010`** | `COV-FR07-06` | POST product 1 (q=1) -> POST product 2 (q=2) -> POST product 1 (q=4) -> GET cart | Cart has exactly 2 lines: product 1 with quantity === 5 (1 + 4), product 2 with quantity === 2 | **`VALID`** | Approved |
| **`FR07-AI-011`** | `COV-FR07-06` | POST product id: 1 with q=1, then POST product id: 1 with q=1, then GET cart | Cart has exactly 1 entry for product 1 with quantity === 2 (1 + 1) | **`VALID`** | Approved |
| **`FR07-AI-012`** | `COV-FR07-07` | Send POST /api/cart with quantity: 1 | Item accepted with quantity 1 | **`INCOMPLETE`** | Calibrated: Semantic acceptance = SPECIFIED; Status = 200 OK (INFERRED) |
| **`FR07-AI-013`** | `COV-FR07-08` | Send POST /api/cart with quantity: 2 | Item accepted with quantity 2 | **`INCOMPLETE`** | Calibrated: Semantic validity = SPECIFIED; 200 OK = INFERRED |
| **`FR07-AI-014`** | `COV-FR07-09` | Send POST /api/cart with quantity: 0 | Server must reject request; zero quantity violates minimum 1 rule | **`INCOMPLETE`** | Calibrated: Expected status = UNKNOWN; primary oracle = semantic rejection/no mutation |
| **`FR07-AI-015`** | `COV-FR07-10` | Send POST /api/cart with quantity: -1 | Server must reject request; negative quantity violates positive integer requirement | **`INCOMPLETE`** | Calibrated: Keep status UNKNOWN; verify zero cart mutation |
| **`FR07-AI-016`** | `COV-FR07-10` | Send POST /api/cart with quantity: -100 | Server must reject request; negative integer is forbidden | **`INCOMPLETE`** | Calibrated: HTTP status UNKNOWN; semantic rejection is authoritative |
| **`FR07-AI-017`** | `COV-FR07-11` | Send POST /api/cart with quantity: 1.5 | Server must reject request; fractional values violate integer requirement | **`INCOMPLETE`** | Calibrated: Status UNKNOWN; verify semantic rejection and no mutation |
| **`FR07-AI-018`** | `COV-FR07-11` | Send POST /api/cart with quantity: 0.5 | Server must reject request; sub-unit decimal violates both integer and minimum 1 constraints | **`INCOMPLETE`** | Calibrated: Keep status UNKNOWN; assert rejection and no mutation |
| **`FR07-AI-019`** | `COV-FR07-12` | Send POST /api/cart with quantity: '2' | Characterize whether server strictly rejects non-number type or coerces string integer safely without crash | **`VALID`** | Approved |
| **`FR07-AI-020`** | `COV-FR07-13` | Send POST /api/cart with quantity: 'abc' | Server must reject request; non-numeric string violates integer constraint | **`INCOMPLETE`** | Calibrated: Status UNKNOWN; semantic rejection/no mutation is main oracle |
| **`FR07-AI-021`** | `COV-FR07-13` | Send POST /api/cart with quantity: '@#$' | Server must reject request; special character string cannot represent integer quantity | **`INCOMPLETE`** | Calibrated: Use UNKNOWN HTTP status and semantic rejection |
| **`FR07-AI-022`** | `COV-FR07-14` | Send POST /api/cart with quantity: 1000000000 | Server handles large integer safely with controlled response and no process crash | **`VALID`** | Approved |
| **`FR07-AI-023`** | `COV-FR07-15` | Send POST /api/cart with body omitting 'quantity': { id: 1, name: 'Sản phẩm A', price: 100000 } | Server must reject request; quantity is a required input for cart additions | **`INCOMPLETE`** | Calibrated: Status UNKNOWN; verify no undefined-quantity item added |
| **`FR07-AI-024`** | `COV-FR07-15` | Send POST /api/cart with quantity: null | Server must reject request; null quantity cannot satisfy positive integer requirement | **`INCOMPLETE`** | Calibrated: Status UNKNOWN; assert semantic rejection and no mutation |
| **`FR07-AI-025`** | `COV-FR07-16` | Send POST /api/cart with non-existent id: 999999 | Characterize whether cart checks database catalog or blindly pushes unverified product IDs | **`VALID`** | Approved |
| **`FR07-AI-026`** | `COV-FR07-17` | Send POST /api/cart with id: -1 | Probe whether server handles negative ID safely without unexpected state corruption | **`VALID`** | Approved |
| **`FR07-AI-027`** | `COV-FR07-18` | Send POST /api/cart with body lacking 'id': { name: 'No ID Item', price: 50000, quantity: 1 } | Probe whether server requires an item ID or blindly stores ID-less cart entries | **`VALID`** | Approved |
| **`FR07-AI-028`** | `COV-FR07-18` | Send POST /api/cart with id: 'one' | Probe whether server coerces string ID, rejects it, or allows string key | **`VALID`** | Approved |
| **`FR07-AI-029`** | `COV-FR07-19` | Send POST /api/cart for known 100000 VND product with tampered price: 1, then GET cart | Characterize whether cart stores arbitrary client price or overrides it with official catalog price | **`VALID`** | Approved |
| **`FR07-AI-030`** | `COV-FR07-20` | Send POST /api/cart with price: -50000 | Characterize handling of negative price without server crash | **`VALID`** | Approved |
| **`FR07-AI-031`** | `COV-FR07-21` | Send POST /api/cart with valid body but without Authorization header | Cart mutation denied; unauthenticated user cannot mutate any cart | **`VALID`** | Approved |
| **`FR07-AI-032`** | `COV-FR07-22` | Send POST /api/cart with valid body and forged HMAC signature | Cart mutation denied; token signature verification fails | **`INCOMPLETE`** | Calibrated: Keep exact error envelope UNKNOWN / IMPLEMENTATION-OBSERVED |
| **`FR07-AI-033`** | `COV-FR07-22` | Send POST /api/cart with Authorization: Basic dXNlcjpwYXNz | Access denied; non-Bearer scheme rejected | **`VALID`** | Approved |
| **`FR07-AI-034`** | `COV-FR07-23` | User A adds product 1 -> User B (fresh login) retrieves GET /api/cart | User B's cart remains completely empty ([]); User A's items are strictly isolated | **`VALID`** | Approved |
| **`FR07-AI-035`** | `COV-FR07-23` | User B adds product 2 -> User A adds product 1 -> User B retrieves cart | User B's cart still contains only product 2 with quantity 1; completely unaffected by User A | **`VALID`** | Approved |
| **`FR07-AI-036`** | `COV-FR07-23` | User A adds product 1 (q=2) -> User B adds product 1 (q=3) -> User A GET cart | User A's cart quantity for product 1 is strictly 2; not contaminated by User B's addition of product 1 | **`VALID`** | Approved |
| **`FR07-AI-037`** | `COV-FR07-24` | Send POST /api/cart with empty body {} | Server safely handles empty object with controlled response; does not crash process | **`INCOMPLETE`** | Calibrated: Use controlled-response/no-crash oracle; no mutation |
| **`FR07-AI-038`** | `COV-FR07-24` | Send POST /api/cart with valid item plus extra fields: { id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2, adminNote: 'hack', discountBypass: true } | Server handles extra properties safely without crashing or corrupting cart state | **`INCOMPLETE`** | Calibrated: Base oracle: controlled handling/no crash; report security fail only if effect shown |
