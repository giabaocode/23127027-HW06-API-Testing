# FR-07: Shopping Cart — Student Human Audit Worksheet

> **Instructions for Student Reviewer:**
> - Review each of the 38 AI-generated test cases independently against the reviewed specification.
> - Assign `Student Verdict` as one of: **`VALID`**, **`INVALID`**, or **`INCOMPLETE`**.
> - Provide your personal `Student Reasoning` and required `Student Correction` where applicable.
> - **Academic Integrity Rule:** All student fields start strictly BLANK. Do NOT accept pre-filled verdicts.

---

## Human Audit Table

| Test ID | Coverage ID | Short Test Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **`FR07-AI-001`** | `COV-FR07-01` | Verify newly registered user starts with an empty shopping cart | | | | |
| **`FR07-AI-002`** | `COV-FR07-02` | Verify GET /api/cart correctly reflects a single added product item | | | | |
| **`FR07-AI-003`** | `COV-FR07-02` | Verify GET /api/cart correctly reflects multiple distinct added products | | | | |
| **`FR07-AI-004`** | `COV-FR07-03` | Verify GET /api/cart rejects request when Authorization header is completely omitted | | | | |
| **`FR07-AI-005`** | `COV-FR07-04` | Verify GET /api/cart rejects request with forged or tamper-corrupted JWT signature | | | | |
| **`FR07-AI-006`** | `COV-FR07-04` | Verify GET /api/cart rejects Authorization header lacking the 'Bearer ' scheme prefix | | | | |
| **`FR07-AI-007`** | `COV-FR07-05` | Verify POST /api/cart succeeds when adding a valid product item matching the specification example | | | | |
| **`FR07-AI-008`** | `COV-FR07-05` | Verify POST /api/cart succeeds when adding a second distinct product item | | | | |
| **`FR07-AI-009`** | `COV-FR07-06` | Verify adding the same product ID twice increments quantity and does not create duplicate rows | | | | |
| **`FR07-AI-010`** | `COV-FR07-06` | Verify duplicate product accumulation succeeds when interleaved with a different product | | | | |
| **`FR07-AI-011`** | `COV-FR07-06` | Verify duplicate accumulation when adding single-unit increments (q=1 then q=1) | | | | |
| **`FR07-AI-012`** | `COV-FR07-07` | Verify POST /api/cart successfully accepts quantity at exact minimum valid boundary (quantity = 1) | | | | |
| **`FR07-AI-013`** | `COV-FR07-08` | Verify POST /api/cart successfully accepts quantity at min + 1 boundary (quantity = 2) | | | | |
| **`FR07-AI-014`** | `COV-FR07-09` | Verify POST /api/cart rejects request when quantity is 0 (min - 1 boundary violation) | | | | |
| **`FR07-AI-015`** | `COV-FR07-10` | Verify POST /api/cart rejects request when quantity is -1 (immediate negative boundary) | | | | |
| **`FR07-AI-016`** | `COV-FR07-10` | Verify POST /api/cart rejects request when quantity is a large negative integer (-100) | | | | |
| **`FR07-AI-017`** | `COV-FR07-11` | Verify POST /api/cart rejects fractional/decimal quantity (quantity = 1.5) | | | | |
| **`FR07-AI-018`** | `COV-FR07-11` | Verify POST /api/cart rejects decimal quantity between 0 and 1 (quantity = 0.5) | | | | |
| **`FR07-AI-019`** | `COV-FR07-12` | Characterize SUT behavior when quantity is supplied as a string-encoded integer ('2') | | | | |
| **`FR07-AI-020`** | `COV-FR07-13` | Verify POST /api/cart rejects request when quantity is an alphabetic string ('abc') | | | | |
| **`FR07-AI-021`** | `COV-FR07-13` | Verify POST /api/cart rejects request when quantity is special symbols ('@#$') | | | | |
| **`FR07-AI-022`** | `COV-FR07-14` | Characterize server handling of extreme large quantity (10^9) without crash or corrupted memory | | | | |
| **`FR07-AI-023`** | `COV-FR07-15` | Verify POST /api/cart rejects request when the mandatory quantity property is completely omitted | | | | |
| **`FR07-AI-024`** | `COV-FR07-15` | Verify POST /api/cart rejects request when quantity is explicitly passed as null | | | | |
| **`FR07-AI-025`** | `COV-FR07-16` | Probe SUT behavior when adding a product ID that does not exist in database catalog (id = 999999) | | | | |
| **`FR07-AI-026`** | `COV-FR07-17` | Probe SUT handling of a negative integer product identifier (id = -1) | | | | |
| **`FR07-AI-027`** | `COV-FR07-18` | Probe SUT handling when the product ID property is completely omitted from body | | | | |
| **`FR07-AI-028`** | `COV-FR07-18` | Probe SUT handling when product ID is passed as a string ('one') | | | | |
| **`FR07-AI-029`** | `COV-FR07-19` | Probe whether POST /api/cart trusts client-submitted price (e.g. price: 1) or looks up catalog price | | | | |
| **`FR07-AI-030`** | `COV-FR07-20` | Probe SUT handling when price is supplied as a negative number (-50000) | | | | |
| **`FR07-AI-031`** | `COV-FR07-21` | Verify POST /api/cart rejects addition when Authorization header is completely omitted | | | | |
| **`FR07-AI-032`** | `COV-FR07-22` | Verify POST /api/cart rejects request carrying forged JWT signature | | | | |
| **`FR07-AI-033`** | `COV-FR07-22` | Verify POST /api/cart rejects Authorization header using Basic scheme instead of Bearer | | | | |
| **`FR07-AI-034`** | `COV-FR07-23` | Verify User A adding items to their cart leaves User B's cart completely empty | | | | |
| **`FR07-AI-035`** | `COV-FR07-23` | Verify User A's additions do not mutate or overwrite User B's existing populated cart | | | | |
| **`FR07-AI-036`** | `COV-FR07-23` | Verify accumulation of the same product ID operates independently across distinct users | | | | |
| **`FR07-AI-037`** | `COV-FR07-24` | Verify POST /api/cart handles empty JSON body ({}) safely without server crash | | | | |
| **`FR07-AI-038`** | `COV-FR07-24` | Verify POST /api/cart safely handles extra unexpected properties in request payload | | | | |
