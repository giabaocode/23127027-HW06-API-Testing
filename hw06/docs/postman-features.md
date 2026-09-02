# HW06 — Postman Advanced Features & Engineering Documentation

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Scope:** Master Test Suite — FR-01 (Account Registration), FR-07 (Shopping Cart), FR-12 (Access Control)
> - **Unified Collection:** [`hw06/postman/eshop-hw06-collection.json`](file:///Users/phamngocgiabao/eshop-sut/hw06/postman/eshop-hw06-collection.json)

---

## 1. Architectural Overview & Postman Inventory

The automated test framework utilizes Postman and Newman v6 to execute 129 logical test cases across 3 feature subsystems. No Postman feature is used cosmetically; every construct fulfills a concrete quality assurance or security testing requirement:

| Postman Feature | Scope / Where Used | Engineering Rationale & Purpose | Evidence / File Reference |
| :--- | :--- | :--- | :--- |
| **Hierarchical Folders** | Collections for FR-01, FR-07, FR-12 & Master Suite | Partitions tests into clean logical categories: Positive Happy Path, Negative Validation, Boundary Limits, Security Authorization, Robustness, and Student Extensions. | `eshop-hw06-collection.json` (`item[]`) |
| **Environment Decoupling** | `eshop-local`, `fr07-environment`, `fr12-environment` | Isolates target endpoints (`baseUrl`), tokens, and credentials from test scripts, enabling portability between localhost, Docker, and GitHub Actions CI. | `hw06/postman/environments/*.json` |
| **Central Pre-Request Hook** | Collection Root (`event[listen="prerequest"]`) | **Attribution Enforcement:** Automatically injects `X-Student-Id: 23127027` into every HTTP request before transmission across all 129 test designs. | Root `event[0].script.exec` |
| **Central Assertion Hook** | Collection Root (`event[listen="test"]`) | Verifies that the outbound header `X-Student-Id` strictly matches `23127027` and asserts basic HTTP server resilience (`oneOf([200..500])`). | Root `event[1].script.exec` |
| **Request Chaining (`pm.sendRequest`)** | Sequential duplicate tests, Pre-seed carts | Executes setup HTTP calls prior to the main assertion probe (e.g. creating a disposable user or clearing a cart). | `FR01-AI-017`, `FR07-STU-005` |
| **Multi-Token Auth Matrix** | FR-12 Access Control Suite | Mounts 10 distinct JWT tokens into environment variables (`adminToken`, `userToken`, `expiredAdminToken`, `forgedToken`, `missingRoleToken`, `uppercaseRoleToken`, `unsignedAlgNoneToken`, `futureNbfToken`, `whitespaceRoleToken`, `arrayRoleToken`). | `fr12-environment.json` |
| **Dynamic Interpolation (`{{$timestamp}}`)** | User registration, cart probes, coupon codes | Synthesizes unique email addresses and probe names (`Probe_{{$timestamp}}`) to prevent collisions across repeated test runs. | Request body templates |
| **Raw Unparsed Body Mode** | FR-01 & FR-07 Student Extensions | Bypasses Postman GUI sanitization to send raw malformed JSON strings and duplicate object keys to test parser robustness. | `FR01-STU-001`, `FR07-STU-001` |
| **Header Overrides** | MIME-type tests (`Content-Type: text/plain`) | Verifies strict server content negotiation and rejection of non-JSON payloads on REST endpoints. | `FR01-STU-002`, `FR07-STU-002` |
| **Side-Effect Verification Probes** | FR-07 & FR-12 Dual-Assertion Probes | For every negative/mutation probe, triggers a subsequent query probe asserting that the database/cart state was NOT mutated. | 16 verification probes in FR-12 |
| **HTML Extra Dashboard** | Newman execution reports | Generates rich, interactive HTML reports with collapsible folder trees, response timings, headers, and visual pass/fail graphs. | `hw06/newman/*/fr*-report.html` |

---

## 2. Authentication Handling & Multi-Role Token Management

In accordance with course security requirements (`SEC-02` and `SEC-03`), authentication is decoupled into an environment-driven token matrix:

1. **Role Separation:**
   - `adminToken`: Signed with SUT secret key, payload contains `id: 1, role: 'admin'`.
   - `userToken`: Signed with SUT secret key, payload contains `id: 2, role: 'user'` (standard non-admin user).
2. **Cryptographic Boundary Probes:**
   - `expiredAdminToken`: Token whose `exp` claim is in the past ($t - 3600$s).
   - `forgedToken`: Valid JWT payload signed with an incorrect cryptographic key (`wrong_secret_key`).
   - `unsignedAlgNoneToken`: JWT with header `{"alg": "none"}` and unverified `admin` payload (`FR12-STU-001`).
   - `futureNbfToken`: Valid token with `nbf` (Not Before) set to $t + 3600$s (`FR12-STU-002`).
3. **Role Validation Boundary Probes:**
   - `missingRoleToken`: Valid signature but `role` attribute completely omitted (`FR12-AI-037`).
   - `uppercaseRoleToken`: Valid signature with `role: 'ADMIN'` to test case sensitivity (`FR12-AI-038`).
   - `whitespaceRoleToken`: Valid signature with untrimmed `role: ' admin '` (`FR12-STU-003`).
   - `arrayRoleToken`: Valid signature with type confusion payload `role: ['admin']` (`FR12-STU-004`).

---

## 3. Pre-Request & Dynamic Data Generation

- **Zero Hardcoded Timestamps:** Any test creating disposable records dynamically embeds `Date.now()` or `{{$timestamp}}` into probe keys (e.g. `HACK23127027`, `ImportProbe_23127027`, `UserCategory_23127027`).
- **State Isolation in Pre-Request Scripts:**
  - Where a test requires a clean cart, the pre-request script clears the cart state.
  - Where a duplicate record is tested, the pre-request script performs the baseline registration to ensure state determinism regardless of run sequence.

---

## 4. Assertion Strategy & Oracles Separation

Every test script strictly adheres to the principle of separating **Semantic Access-Control Outcome** from **Inferred HTTP Status**:
1. **Primary Oracle (Semantic Contract):**
   - For positive operations: Operation succeeds, state is committed.
   - For negative/unauthorized operations: Operation denied, no state modification occurs.
2. **Dual-Assertion Pattern (Action + Side-Effect):**
   - When testing `DELETE /api/admin/users/:id` with standard-user credentials, Assertion 1 checks that HTTP response is `403 Forbidden` (or denied). Assertion 2 performs a subsequent login or retrieval probe to confirm that the user account was **not actually deleted**.
   - This pattern directly uncovered that SUT returns `200 OK` AND executes state destruction despite unauthorized caller credentials (`DEF-FR12-01`).

---

## 5. Teardown & Defect-Path Cleanup Strategy

To prevent test suite side-effects from polluting subsequent test runs:
- **Dedicated Seeding Scripts:** `hw06/postman/scripts/seed_fr12_fixtures.js` cleans up all probe items (`id >= 50` or matching student ID marker `23127027`) before reseeding isolated baseline fixtures.
- **Defect-Path Recovery:** For tests like `FR12-STU-003` and `FR12-STU-005` that trigger SUT vulnerabilities resulting in unauthorized coupon creation, post-assertion scripts delete the illegally created coupon using legitimate admin credentials to keep the database clean.

---

## 6. Newman Reporters & CI Execution

The suite is designed for dual-channel execution:
1. **Command-Line Interface (`cli`):** Outputs real-time request status, response times, and failure backtraces suitable for terminal logs and CI/CD console output.
2. **HTML Extra Reporter (`htmlextra`):** Generates self-contained, interactive dashboards (`hw06/newman/*/fr*-report.html`) containing:
   - Aggregated run metrics (iterations, requests, script counts, assertion passes/failures).
   - Filterable test lists by pass/fail status.
   - Exact request payloads, response bodies, and headers (verifying `X-Student-Id`).

---

## 7. Known Limitations & SUT In-Memory Caveats

- **In-Memory Shopping Carts:** In the current SUT implementation (`backend/server.js`), carts are stored in memory (`userCarts = {}`) rather than SQLite. Server restarts clear cart state, which requires test runs to be self-contained or to run against an active daemon server instance.
- **Synchronous SQLite Calls:** The SUT SQLite database uses asynchronous callbacks. In high-concurrency Newman runs, sequential requests are paced with Newman `--delay-request 50` if needed to prevent SQLite locking.
