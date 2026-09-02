# FR-07: Shopping Cart — Student Human Audit Worksheet

> **Document Status:** Official Student Human Audit Record
> **Feature ID:** Pool B — `FR-07` (Shopping Cart)
> **Student Reviewer:** Phạm Ngọc Gia Bảo (`23127027`)
> **Audit Review Date:** 2026-09-02
> **Audit Provenance:** Student evaluated all 38 original AI cases with reference to external ChatGPT second-AI critique; adopted calibrated decisions.

---

## 1. Audit Summary Distribution

| Verdict | Count | Percentage | Student Action |
| :---: | :---: | :---: | :--- |
| **`VALID`** | **23** | 60.5% | Approved directly into reviewed final test suite. |
| **`INCOMPLETE`** | **15** | 39.5% | Adopted with formal calibration (status decouple, safe envelope). |
| **`INVALID`** | **0** | 0.0% | Zero test cases rejected. |
| **TOTAL** | **38** | **100.0%** | **38 Total AI Test Cases Audited** |

---

## 2. Human Audit Table

| Test ID | Coverage ID | Short Test Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **`FR07-AI-001`** | `COV-FR07-01` | Verify newly registered user starts with an empty shopping cart | **`VALID`** | Empty-cart test correctly classified as INFERRED / IMPLEMENTATION-OBSERVED. | None required | 2026-09-02 |
| **`FR07-AI-002`** | `COV-FR07-02` | Verify GET /api/cart correctly reflects a single added product item | **`VALID`** | Add-then-GET state verification is coherent; result oracle remains INFERRED. | None required | 2026-09-02 |
| **`FR07-AI-003`** | `COV-FR07-02` | Verify GET /api/cart correctly reflects multiple distinct added products | **`VALID`** | Multi-item state characterization is meaningful and does not overstate response contract. | None required | 2026-09-02 |
| **`FR07-AI-004`** | `COV-FR07-03` | Verify GET /api/cart rejects request when Authorization header is completely omitted | **`VALID`** | Missing JWT correctly requires semantic denial; 401 correctly labeled middleware-inferred. | None required | 2026-09-02 |
| **`FR07-AI-005`** | `COV-FR07-04` | Verify GET /api/cart rejects request with forged or tamper-corrupted JWT signature | **`INCOMPLETE`** | Rejection valid, but exact body {error:'Forbidden'} is not specified by contract. | Keep exact error envelope UNKNOWN or IMPLEMENTATION-OBSERVED | 2026-09-02 |
| **`FR07-AI-006`** | `COV-FR07-04` | Verify GET /api/cart rejects Authorization header lacking the 'Bearer ' scheme prefix | **`VALID`** | Non-Bearer scheme violates SEC-02 authentication; exact status remains inferred. | None required | 2026-09-02 |
| **`FR07-AI-007`** | `COV-FR07-05` | Verify POST /api/cart succeeds when adding a valid product item matching the specification example | **`VALID`** | Standard POST matching documented example is meaningful positive test; behavior INFERRED. | None required | 2026-09-02 |
| **`FR07-AI-008`** | `COV-FR07-05` | Verify POST /api/cart succeeds when adding a second distinct product item | **`VALID`** | Adding second distinct item provides useful state coverage with inferred status. | None required | 2026-09-02 |
| **`FR07-AI-009`** | `COV-FR07-06` | Verify adding the same product ID twice increments quantity and does not create duplicate rows | **`VALID`** | Directly verifies explicit duplicate-product accumulation rule (q1+q2, single row). | None required | 2026-09-02 |
| **`FR07-AI-010`** | `COV-FR07-06` | Verify duplicate product accumulation succeeds when interleaved with a different product | **`VALID`** | Meaningful interleaved state variation of the explicit accumulation rule. | None required | 2026-09-02 |
| **`FR07-AI-011`** | `COV-FR07-06` | Verify duplicate accumulation when adding single-unit increments (q=1 then q=1) | **`VALID`** | Tests explicit accumulation rule using minimum valid unit increments (1+1). | None required | 2026-09-02 |
| **`FR07-AI-012`** | `COV-FR07-07` | Verify POST /api/cart successfully accepts quantity at exact minimum valid boundary (quantity = 1) | **`INCOMPLETE`** | quantity=1 is SPECIFIED valid, but HTTP 200 is only INFERRED for endpoint. | Semantic acceptance = SPECIFIED; Status = 200 OK (INFERRED) | 2026-09-02 |
| **`FR07-AI-013`** | `COV-FR07-08` | Verify POST /api/cart successfully accepts quantity at min + 1 boundary (quantity = 2) | **`INCOMPLETE`** | quantity=2 satisfies positive integer domain, but incorrectly strengthens HTTP status. | Semantic validity = SPECIFIED; 200 OK = INFERRED | 2026-09-02 |
| **`FR07-AI-014`** | `COV-FR07-09` | Verify POST /api/cart rejects request when quantity is 0 (min - 1 boundary violation) | **`INCOMPLETE`** | quantity=0 violates minimum 1, but status!=200 / 400 over-specifies undocumented status. | Expected status = UNKNOWN; primary oracle = semantic rejection/no mutation | 2026-09-02 |
| **`FR07-AI-015`** | `COV-FR07-10` | Verify POST /api/cart rejects request when quantity is -1 (immediate negative boundary) | **`INCOMPLETE`** | quantity=-1 must be rejected semantically, but exact non-200 status is undocumented. | Keep status UNKNOWN; verify zero cart mutation | 2026-09-02 |
| **`FR07-AI-016`** | `COV-FR07-10` | Verify POST /api/cart rejects request when quantity is a large negative integer (-100) | **`INCOMPLETE`** | quantity=-100 violates positive-integer requirement, but over-specifies HTTP outcome. | HTTP status UNKNOWN; semantic rejection is authoritative | 2026-09-02 |
| **`FR07-AI-017`** | `COV-FR07-11` | Verify POST /api/cart rejects fractional/decimal quantity (quantity = 1.5) | **`INCOMPLETE`** | quantity=1.5 violates integer requirement, but incorrectly strengthens HTTP oracle. | Status UNKNOWN; verify semantic rejection and no mutation | 2026-09-02 |
| **`FR07-AI-018`** | `COV-FR07-11` | Verify POST /api/cart rejects decimal quantity between 0 and 1 (quantity = 0.5) | **`INCOMPLETE`** | quantity=0.5 violates integer and minimum constraints, but failure status undocumented. | Keep status UNKNOWN; assert rejection and no mutation | 2026-09-02 |
| **`FR07-AI-019`** | `COV-FR07-12` | Characterize SUT behavior when quantity is supplied as a string-encoded integer ('2') | **`VALID`** | String quantity '2' correctly treated as TYPE ROBUSTNESS / CHARACTERIZATION. | None required | 2026-09-02 |
| **`FR07-AI-020`** | `COV-FR07-13` | Verify POST /api/cart rejects request when quantity is an alphabetic string ('abc') | **`INCOMPLETE`** | 'abc' violates integer requirement, but status!=200 / 400 is stronger than spec. | Status UNKNOWN; semantic rejection/no mutation is main oracle | 2026-09-02 |
| **`FR07-AI-021`** | `COV-FR07-13` | Verify POST /api/cart rejects request when quantity is special symbols ('@#$') | **`INCOMPLETE`** | Special-character string cannot represent integer, but test over-specifies HTTP outcome. | Use UNKNOWN HTTP status and semantic rejection | 2026-09-02 |
| **`FR07-AI-022`** | `COV-FR07-14` | Characterize server handling of extreme large quantity (10^9) without crash or corrupted memory | **`VALID`** | 10^9 correctly treated as ROBUSTNESS / UNKNOWN UPPER BOUND without invented boundary. | None required | 2026-09-02 |
| **`FR07-AI-023`** | `COV-FR07-15` | Verify POST /api/cart rejects request when the mandatory quantity property is completely omitted | **`INCOMPLETE`** | Missing quantity is inferred rejection, but test over-specifies !=200 / 400. | Status UNKNOWN; verify no undefined-quantity item added | 2026-09-02 |
| **`FR07-AI-024`** | `COV-FR07-15` | Verify POST /api/cart rejects request when quantity is explicitly passed as null | **`INCOMPLETE`** | null quantity violates integer requirement, but exact non-200 status unspecified. | Status UNKNOWN; assert semantic rejection and no mutation | 2026-09-02 |
| **`FR07-AI-025`** | `COV-FR07-16` | Probe SUT behavior when adding a product ID that does not exist in database catalog (id = 999999) | **`VALID`** | Non-existent ID correctly kept as robustness probe rather than specified rule. | None required | 2026-09-02 |
| **`FR07-AI-026`** | `COV-FR07-17` | Probe SUT handling of a negative integer product identifier (id = -1) | **`VALID`** | Negative product ID behavior correctly treated as UNKNOWN robustness probe. | None required | 2026-09-02 |
| **`FR07-AI-027`** | `COV-FR07-18` | Probe SUT handling when the product ID property is completely omitted from body | **`VALID`** | Omitted product ID correctly treated as schema robustness probe. | None required | 2026-09-02 |
| **`FR07-AI-028`** | `COV-FR07-18` | Probe SUT handling when product ID is passed as a string ('one') | **`VALID`** | String product ID is legitimate type-characterization probe with safe oracle. | None required | 2026-09-02 |
| **`FR07-AI-029`** | `COV-FR07-19` | Probe whether POST /api/cart trusts client-submitted price (e.g. price: 1) or looks up catalog price | **`VALID`** | Price tampering explicitly treated as integrity probe, not formal cart rule. | None required | 2026-09-02 |
| **`FR07-AI-030`** | `COV-FR07-20` | Probe SUT handling when price is supplied as a negative number (-50000) | **`VALID`** | Negative price correctly classified as robustness; positive rule is in FR-15. | None required | 2026-09-02 |
| **`FR07-AI-031`** | `COV-FR07-21` | Verify POST /api/cart rejects addition when Authorization header is completely omitted | **`VALID`** | SEC-02 requires authentication for POST mutation; 401 identified as middleware-inferred. | None required | 2026-09-02 |
| **`FR07-AI-032`** | `COV-FR07-22` | Verify POST /api/cart rejects request carrying forged JWT signature | **`INCOMPLETE`** | Forged JWT must be denied, but exact error object {error:'Forbidden'} unspecified. | Keep exact error envelope UNKNOWN / IMPLEMENTATION-OBSERVED | 2026-09-02 |
| **`FR07-AI-033`** | `COV-FR07-22` | Verify POST /api/cart rejects Authorization header using Basic scheme instead of Bearer | **`VALID`** | Basic auth violates Bearer contract; exact status remains middleware-inferred. | None required | 2026-09-02 |
| **`FR07-AI-034`** | `COV-FR07-23` | Verify User A adding items to their cart leaves User B's cart completely empty | **`VALID`** | User isolation testing is useful; clearly classified as INFERRED from SEC-02. | None required | 2026-09-02 |
| **`FR07-AI-035`** | `COV-FR07-23` | Verify User A's additions do not mutate or overwrite User B's existing populated cart | **`VALID`** | Cross-user non-interference is meaningful inferred state/security characterization. | None required | 2026-09-02 |
| **`FR07-AI-036`** | `COV-FR07-23` | Verify accumulation of the same product ID operates independently across distinct users | **`VALID`** | Same product IDs independently scoped across distinct users; classified INFERRED. | None required | 2026-09-02 |
| **`FR07-AI-037`** | `COV-FR07-24` | Verify POST /api/cart handles empty JSON body ({}) safely without server crash | **`INCOMPLETE`** | Classified as ROBUSTNESS but requires non-200 status despite formal behavior UNKNOWN. | Use controlled-response/no-crash oracle; no mutation | 2026-09-02 |
| **`FR07-AI-038`** | `COV-FR07-24` | Verify POST /api/cart safely handles extra unexpected properties in request payload | **`INCOMPLETE`** | Extra-property behavior UNKNOWN; tampering assertion too vague without mechanism. | Base oracle: controlled handling/no crash; report security fail only if effect shown | 2026-09-02 |
