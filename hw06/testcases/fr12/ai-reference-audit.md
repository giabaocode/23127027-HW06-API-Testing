# FR-12: Access Control — External AI Reference Audit (ChatGPT)

> [!WARNING]
> **External Secondary AI Reference Material:**
> This document contains an external secondary AI review produced by ChatGPT. It is reference material for student review and does not itself constitute the student human audit.
> Student-owned audit decisions, reasoning, and formal adoptions are maintained independently in [`hw06/testcases/fr12/human-audit.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/fr12/human-audit.md).

---

## 1. Reference Verdict Distribution

| Reference Verdict Category | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **VALID** | **28** | 73.68% | Test case is logically coherent, correctly mapped to FR-12/SEC-02/SEC-03, has realistic oracles, and preserves test isolation. |
| **INCOMPLETE** | **10** | 26.32% | Test case has technical merit but requires calibrated headers, direct state verification, cleanup safety on defect paths, or oracle clarification. |
| **INVALID** | **0** | 0.00% | No test case was found to be fundamentally flawed, targeting non-existent endpoints, or violating specification boundaries. |
| **TOTAL** | **38** | **100.0%** | Programmatically verified: $28 + 10 + 0 = 38$. |

---

## 2. Complete Reference Verdict Table (All 38 Test Cases)

| Test ID | Coverage ID | Method & Target Endpoint | Caller & Subject Condition | Reference Verdict | Key Reason / Focus Area |
| :---: | :---: | :--- | :--- | :---: | :--- |
| `FR12-AI-001` | `COV-FR12-02` | `GET /api/admin/users` | Standard User (`role: 'user'`) | **VALID** | Correctly maps standard-user denial to SEC-03. |
| `FR12-AI-002` | `COV-FR12-04` | `DELETE /api/admin/users/:id` | Standard User (`role: 'user'`) | **VALID** | Enforces dual-assertion; verifies target user still exists via login probe. |
| `FR12-AI-003` | `COV-FR12-07` | `GET /api/admin/orders` | Standard User (`role: 'user'`) | **VALID** | Correctly restricts system-wide customer order history to admin. |
| `FR12-AI-004` | `COV-FR12-09` | `PUT /api/admin/orders/:id/status` | Standard User (`role: 'user'`) | **INCOMPLETE** | Transition `pending -> delivered` risks rejection by business validation, masking authorization defect. |
| `FR12-AI-005` | `COV-FR12-12` | `POST /api/admin/import-products` | Standard User (`role: 'user'`) | **INCOMPLETE** | Side-effect check relies on unestablished `?search=` query semantics rather than direct absence verification. |
| `FR12-AI-006` | `COV-FR12-18` | `POST /api/admin/coupons` | Standard User (`role: 'user'`) | **INCOMPLETE** | Verifying non-creation via checkout application is coupled to unrelated business rules; use admin coupon list. |
| `FR12-AI-007` | `COV-FR12-20` | `DELETE /api/admin/coupons/:id` | Standard User (`role: 'user'`) | **INCOMPLETE** | Verification phrasing is ambiguous; verify disposable coupon directly through admin coupon listing. |
| `FR12-AI-008` | `COV-FR12-22` | `POST /api/products` | Standard User (`role: 'user'`) | **INCOMPLETE** | Product non-creation check relies on ungrounded `?search=` query semantics. |
| `FR12-AI-009` | `COV-FR12-25` | `PUT /api/products/:id` | Standard User (`role: 'user'`) | **VALID** | Side-effect check verifies original price remains unchanged after unauthorized PUT probe. |
| `FR12-AI-010` | `COV-FR12-28` | `DELETE /api/products/:id` | Standard User (`role: 'user'`) | **VALID** | Side-effect check verifies product still exists via GET probe after unauthorized DELETE probe. |
| `FR12-AI-011` | `COV-FR12-30` | `POST /api/categories` | Standard User (`role: 'user'`) | **VALID** | Category non-creation is verified by absence in category list after standard-user POST probe. |
| `FR12-AI-012` | `COV-FR12-32` | `PUT /api/categories/:id` | Standard User (`role: 'user'`) | **VALID** | Category modification denial verified by category name remaining unchanged in database. |
| `FR12-AI-013` | `COV-FR12-33` | `DELETE /api/categories/:id` | Standard User (`role: 'user'`) | **VALID** | Category deletion denial verified by category continuing to exist in database. |
| `FR12-AI-014` | `COV-FR12-15` | `GET /api/coupons` | Standard User (`role: 'user'`) | **VALID** | Standard user denied access to administrative coupon master list via SEC-03. |
| `FR12-AI-015` | `COV-FR12-03` | `GET /api/admin/users` | Admin User (`role: 'admin'`) | **VALID** | Admin access correctly defines authorization clearance as primary oracle with 200 as inferred SUT behavior. |
| `FR12-AI-016` | `COV-FR12-05` | `DELETE /api/admin/users/:id` | Admin User (`role: 'admin'`) | **INCOMPLETE** | Side-effect verifier requires exact downstream login status 401; should assert user no longer exists/cannot login. |
| `FR12-AI-017` | `COV-FR12-08` | `GET /api/admin/orders` | Admin User (`role: 'admin'`) | **VALID** | Admin access to GET /api/admin/orders verifies administrative clearance unhindered. |
| `FR12-AI-018` | `COV-FR12-10` | `PUT /api/admin/orders/:id/status` | Admin User (`role: 'admin'`) | **VALID** | Admin order status update correctly verifies administrative capability on disposable order. |
| `FR12-AI-019` | `COV-FR12-13` | `POST /api/admin/import-products` | Admin User (`role: 'admin'`) | **VALID** | Admin product import verifies administrative capability with valid disposable payload. |
| `FR12-AI-020` | `COV-FR12-19` | `POST /api/admin/coupons` | Admin User (`role: 'admin'`) | **VALID** | Admin coupon creation verifies administrative capability with valid disposable coupon code. |
| `FR12-AI-021` | `COV-FR12-21` | `DELETE /api/admin/coupons/:id` | Admin User (`role: 'admin'`) | **VALID** | Admin coupon deletion operates on disposable coupon and verifies deletion. |
| `FR12-AI-022` | `COV-FR12-23` | `POST /api/products` | Admin User (`role: 'admin'`) | **VALID** | Admin product creation verifies administrative capability with valid disposable product body. |
| `FR12-AI-023` | `COV-FR12-26` | `PUT /api/products/:id` | Admin User (`role: 'admin'`) | **VALID** | Admin product update operates on disposable product and updates price/description. |
| `FR12-AI-024` | `COV-FR12-27` | `DELETE /api/products/:id` | Admin User (`role: 'admin'`) | **VALID** | Admin product deletion operates on disposable product and removes it from catalog. |
| `FR12-AI-025` | `COV-FR12-31` | `POST /api/categories` | Admin User (`role: 'admin'`) | **VALID** | Admin category creation verifies administrative capability with valid category body. |
| `FR12-AI-026` | `COV-FR12-32` | `PUT /api/categories/:id` | Admin User (`role: 'admin'`) | **VALID** | Admin category update operates on disposable category and updates name. |
| `FR12-AI-027` | `COV-FR12-34` | `DELETE /api/categories/:id` | Admin User (`role: 'admin'`) | **VALID** | Admin category deletion operates on disposable category and removes it from database. |
| `FR12-AI-028` | `COV-FR12-16` | `GET /api/coupons` | Admin User (`role: 'admin'`) | **VALID** | Admin coupon listing verifies administrative capability on GET /api/coupons. |
| `FR12-AI-029` | `COV-FR12-21` | `POST /api/products` | Anonymous Caller (No Token) | **INCOMPLETE** | Product-absence verification must not rely on unestablished search-query behavior; inspect list directly. |
| `FR12-AI-030` | `COV-FR12-24` | `PUT /api/products/:id` | Anonymous Caller (No Token) | **VALID** | Anonymous product update denial correctly asserts SEC-02 and verifies product unchanged. |
| `FR12-AI-031` | `COV-FR12-27` | `DELETE /api/products/:id` | Anonymous Caller (No Token) | **VALID** | Anonymous product deletion denial correctly asserts SEC-02 and verifies product still exists. |
| `FR12-AI-032` | `COV-FR12-01` | `GET /api/admin/users` | Anonymous Caller (No Token) | **VALID** | Anonymous user list denial correctly asserts SEC-02 and prevents user data exposure. |
| `FR12-AI-033` | `COV-FR12-29` | `POST /api/categories` | Anonymous Caller (No Token) | **INCOMPLETE** | Missing cleanup step if expected access-control defect occurs and category is created. |
| `FR12-AI-034` | `COV-FR12-14` | `GET /api/coupons` | Anonymous Caller (No Token) | **VALID** | Anonymous coupon overview denial correctly asserts SEC-02 and prevents coupon data exposure. |
| `FR12-AI-035` | `COV-FR12-35` | `GET /api/admin/users` | Expired Admin Token | **INCOMPLETE** | Wording incorrectly equates expiration with cryptographic signature failure; signature is valid but exp is past. |
| `FR12-AI-036` | `COV-FR12-36` | `GET /api/admin/orders` | Forged Signature Token | **VALID** | Forged cryptographic signature rejection correctly asserts SEC-02 integrity failure. |
| `FR12-AI-037` | `COV-FR12-37` | `POST /api/admin/coupons` | Missing Role Claim Token | **INCOMPLETE** | Missing cleanup step if SEC-03 defect allows coupon creation; verify absence via admin GET /api/coupons. |
| `FR12-AI-038` | `COV-FR12-38` | `DELETE /api/admin/users/:id` | Uppercase Role Token (`'ADMIN'`) | **VALID** | Uppercase role 'ADMIN' probe correctly asserts SEC-03 exact-match case sensitivity. |

---

## 3. Exact Reference Corrections for Incomplete Cases (10 Cases)

### `FR12-AI-004` (PUT /api/admin/orders/:id/status — Standard User)
- **Reason:** The access-control objective is valid, but attempting `pending -> delivered` may be rejected by downstream order-state validation even if authorization is broken, masking the SEC-03 defect.
- **Correction:** Use a valid disposable-order transition such as `pending -> confirmed` so authorization is isolated from order status state machine rules.

### `FR12-AI-005` (POST /api/admin/import-products — Standard User)
- **Reason:** The side-effect oracle depends on `GET /api/products?search=...` returning an empty list, but this packet does not establish server-side search semantics.
- **Correction:** Fetch the product list and assert that the unique marker `ImportProbe_23127027` is absent, or use another source-confirmed lookup.

### `FR12-AI-006` (POST /api/admin/coupons — Standard User)
- **Reason:** Using coupon application/checkout behavior as the persistence verifier can be affected by unrelated coupon/order business conditions.
- **Correction:** Use an authenticated admin `GET /api/coupons` state check and assert that `HACK23127027` does not exist.

### `FR12-AI-007` (DELETE /api/admin/coupons/:id — Standard User)
- **Reason:** "query or application succeeds" is ambiguous, and coupon application can fail for unrelated business reasons.
- **Correction:** Verify the disposable coupon directly through admin coupon listing and assert its ID/code remains present.

### `FR12-AI-008` (POST /api/products — Standard User)
- **Reason:** The product non-creation verifier depends on ungrounded server-side `?search=` semantics.
- **Correction:** Fetch product data and explicitly assert that the unique `UnauthorizedProduct_23127027` marker is absent.

### `FR12-AI-016` (DELETE /api/admin/users/:id — Admin User)
- **Reason:** The main authorization test is sound, but the side-effect verifier requires an exact downstream login status 401 that is not an FR-12 contract oracle.
- **Correction:** Require that the deleted disposable user can no longer authenticate / no longer exists. Treat exact login failure status as endpoint-specific INFERRED/UNKNOWN.

### `FR12-AI-029` (POST /api/products — Anonymous Caller)
- **Reason:** The anonymous POST product test is valid, but its product-absence verification must not rely on unestablished search-query behavior.
- **Correction:** Fetch the product list and explicitly check that `AnonProduct_23127027` is absent.

### `FR12-AI-033` (POST /api/categories — Anonymous Caller)
- **Reason:** If the expected access-control defect occurs, anonymous category creation may leave a real category in the test environment, but cleanup is None.
- **Correction:** If `AnonCategory_23127027` exists after execution, delete it using legitimate admin credentials.

### `FR12-AI-035` (GET /api/admin/users — Expired Token)
- **Reason:** The semantic expired-JWT test is valid, but the wording incorrectly describes expiration as a cryptographic signature failure.
- **Correction:** State that the signature may remain valid while JWT validity fails because the `exp` claim is in the past. Preserve SEC-02 semantic denial. Exact 403 remains INFERRED.

### `FR12-AI-037` (POST /api/admin/coupons — Missing Role Claim)
- **Reason:** Missing-role authorization probe is valid, but if SEC-03 is broken the coupon can actually be created and cleanup is currently None.
- **Correction:** Verify absence/presence through admin `GET /api/coupons`. If `NOROLE_CPN_23127027` was created, delete it using admin credentials.

---

## 4. Systematic Engineering Lessons from External AI Critique

1. **Access-Control Isolation:** Use valid downstream business inputs so business validation (e.g. order state machine transitions) cannot mask a missing authorization check.
2. **State Verification Directness:** Prefer direct, source-grounded resource verification (such as admin listing endpoints) over unrelated downstream business flows (such as promotional checkout calculations).
3. **Cleanup on Expected Defect Paths:** Negative security tests probing static defect candidates must include fallback cleanup steps for the scenario where the SUT is actually vulnerable and performs the unauthorized mutation.
4. **JWT Terminology Precision:** Maintain strict separation between temporal claim invalidation (expired tokens) and cryptographic integrity failures (forged signatures).
5. **HTTP Oracle Calibration:** Never promote downstream endpoint-specific verifier response codes (such as login failure status) into formal FR-12 specification requirements.
