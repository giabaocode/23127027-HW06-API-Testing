# HW06 Manual Action & Human Gate Register (MANUAL_TODO.md)

> **Student ID:** 23127027 | **GitHub:** giabaocode | **Role:** SUT Tester & Evaluator
> **Principle:** Automate everything that AI/tools can legitimately perform. Preserve strict human gates for tasks requiring human judgment, student authorship, personal design decisions, and authentic manual evidence.

---

## 1. Feature Selection & Group Deduplication

- [x] **1.1 Final Feature Selection Confirmed:**
  - Pool A Feature: **FR-01 — Account Registration** (`POST /api/register`)
  - Pool B Feature: **FR-07 — Shopping Cart** (`GET /api/cart`, `POST /api/cart`)
  - Pool C Feature: **FR-12 — Access Control** (Admin endpoints & data mutation endpoints)
- [x] **1.2 Group Deduplication Verified:**
  - The student has personally confirmed that this exact combination (`FR-01 + FR-07 + FR-12`) does NOT duplicate another member's selection in their group.

---

## 2. Human Audit of AI-Generated Test Cases (Mandatory Checkpoint 2)

> *Rule:* AI drafts $\ge 35$ test cases per feature leaving review fields empty. The student must personally evaluate and fill each record.

- [x] **2.1 FR-01 Audit (≥ 35 AI Test Cases):**
  - Personally review each AI-generated test case.
  - Fill fields: `Student Verdict` (`VALID` / `INVALID` / `INCOMPLETE`), `Student Reasoning`, `Student Correction`, `Student Reviewed At`.
  - *Completed and committed locally (`189814b`).*
- [x] **2.2 FR-07 Audit (≥ 35 AI Test Cases):**
  - Personally review each AI-generated test case.
  - Fill fields: `Student Verdict`, `Student Reasoning`, `Student Correction`, `Student Reviewed At`.
  - *Completed and committed locally (`c98513e`).*
- [x] **2.3 FR-12 Audit (≥ 35 AI Test Cases):**
  - Personally review each AI-generated test case.
  - Fill fields: `Student Verdict`, `Student Reasoning`, `Student Correction`, `Student Reviewed At`.
  - *Completed and committed locally (`dea0e48`).*

---

## 3. Student-Authored Original Test Cases (Mandatory Checkpoint 3)

> *Rule:* The student must personally design and author $\ge 5$ original test cases per feature exploring coverage gaps that AI missed. AI provides only broad category prompts and blank templates.

- [ ] **3.1 FR-01 Extensions (≥ 5 Student-Authored Tests):**
  - Author $\ge 5$ original tests (e.g., duplicate registration race/lifecycle, domain boundary, DB-layer password hashing).
  - Provide explanation: Why did AI miss these test cases?
  - *Note: 5 extension tests formalized and committed (`72bed5d`); requirement kept open until separate student-scratch items are confirmed.*
- [x] **3.2 FR-07 Extensions (≥ 5 Student-Authored Tests):**
  - Author $\ge 5$ original tests (e.g., malformed raw JSON, wrong Content-Type, expired JWT, conflicting metadata, read idempotency).
  - Provide explanation: Why did AI miss these test cases?
  - *Note: 5 extension tests formalized and committed (`ce50600`).*
- [x] **3.3 FR-12 Extensions (≥ 5 Student-Authored Tests):**
  - Author $\ge 5$ original tests (e.g., `alg=none` token, future `nbf` token, whitespace role `" admin "`, array role `["admin"]`, body `"role": "admin"` override).
  - Provide explanation: Why did AI miss these test cases?
  - *Completed and committed locally (`fe31f17`).*

---

## 4. Execution & Human Evidence Gathering

> *Note on Execution:* SUT startup, Postman collection generation, and Newman CLI / HTML execution will be automated via AI tools in the workspace. The student must provide and verify attributable human evidence.

- [x] **4.1 Real Postman Console Screenshot for FR-01 (`X-Student-Id`):**
  - Open Postman desktop app, execute a request from the collection.
  - Capture real screenshot of Postman Console showing request sending `X-Student-Id: 23127027` header.
  - Saved image to `hw06/screenshots/fr01-x-student-id.png` (and `fr01-x-student-id.jpg`).
- [x] **4.2 Real Postman Console Screenshot for FR-07 (`X-Student-Id`):**
  - Open Postman desktop app, import `hw06/postman/collections/fr07-shopping-cart.postman_collection.json` and `hw06/postman/environments/fr07-environment.json`.
  - Execute request (e.g. `FR07-AI-001 — Retrieve Empty Cart Baseline`).
  - Capture Postman Console showing `X-Student-Id: 23127027` and real 200 OK response.
  - Saved image to `hw06/screenshots/fr07-x-student-id.png` (and `fr07-x-student-id.jpg`).
- [x] **4.3 Real Postman Console Screenshot for FR-12 (`X-Student-Id`):**
  - Open Postman desktop app, import `hw06/postman/collections/fr12-access-control.postman_collection.json` and `hw06/postman/environments/fr12-environment.json`.
  - Execute request `FR12-AI-015 — Admin GET /api/admin/users`.
  - Capture Postman Console showing `X-Student-Id: 23127027` and real 200 OK response.
  - Verified and saved image to `hw06/screenshots/fr12-x-student-id.png` (and `fr12-x-student-id.jpg`).
- [x] **4.4 Real Newman Execution Verification (FR-01, FR-07, FR-12):**
  - Verify that the automated Newman run output reflects local hostname (`localhost:3000` / `127.0.0.1`).
  - Generated genuine `hw06/newman/fr01/`, `hw06/newman/fr07/`, and `hw06/newman/fr12/` CLI output and HTML extra reports.
- [x] **4.5 Postman Advanced Feature Verification:**
  - Documented features in `hw06/docs/postman-features.md` and automated in collections.

---

## 5. Bug Reporting & GitHub Issues

- [x] **5.1 File Genuine Bugs on GitHub Issues:**
  - Created genuine issues on `https://github.com/giabaocode/23127027-HW06-API-Testing/issues`:
    - Issue #1: [`[DEF-FR01-01] Critical: Plaintext Passwords`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/1)
    - Issue #2: [`[DEF-FR01-02] High: Duplicate Email Registration`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/2)
    - Issue #3: [`[DEF-FR01-03] High: Missing Password Policy`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/3)
    - Issue #4: [`[DEF-FR01-04] High: Missing Mandatory Fields`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/4)
    - Issue #5: [`[DEF-FR01-05] Medium: Missing Email Syntax Validation`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/5)
    - Issue #6: [`[FR-07] High: Adding Duplicate Product to Cart Appends New Row`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/6)
    - Issue #7: [`[FR-07] High: Missing Quantity Domain Validation on POST /api/cart`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/7)
    - Issue #8: [`[FR-12] Critical: Missing Administrator Role Verification on Administrative Endpoints (/api/admin/*)`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/8)
    - Issue #9: [`[FR-12] Critical: Complete Absence of Authentication on Product Catalog Mutations (/api/products)`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/9)
    - Issue #10: [`[FR-12] High: Missing Administrator Role Check on Category Mutations (/api/categories)`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/10)
    - Issue #11: [`[FR-12] Medium: Missing Administrator Role Check on Master Coupon Listing (GET /api/coupons)`](https://github.com/giabaocode/23127027-HW06-API-Testing/issues/11)
- [x] **5.2 FR-07 GitHub Issue Browser Screenshot:**
  - Student captured authentic browser screenshot of live GitHub Issue #6.
  - Verified and committed at `hw06/screenshots/fr07-bug-issue-001.png` (and `fr07-bug-issue-001.jpg`).
- [ ] **5.3 FR-12 GitHub Issue Browser Screenshot:**
  - Student captures authentic browser screenshot of live GitHub Issue #8 (`[FR-12] Critical: Missing Administrator Role Verification on Administrative Endpoints (/api/admin/*)`).
  - Target save path: `hw06/screenshots/fr12-bug-issue-001.png`.
- [ ] **5.4 Link Issues in Main Report:**
  - Update `hw06/docs/main-report.md` bug register with Issue #, Title, Severity, and screenshot links.

---

## 6. CI/CD Pipeline (GitHub Actions)

- [ ] **6.1 Pipeline Execution Verification:**
  - Push collection & workflow (`.github/workflows/api-tests.yml`) to GitHub repository.
  - Verify Run A (all tests pass) and capture screenshot + Run URL.
  - Create isolated demonstration commit for Run B (1 intentional failing test) and capture screenshot + Run URL.

---

## 7. Agent Skill (AI Test Generator)

- [ ] **7.1 Architectural & Design Decisions:**
  - Student personally specifies design choices: pipeline components, Intermediate Representation (IR), partition strategy, validation gates.
  - Record in `hw06/agent-skill/design-decisions.md`.
- [ ] **7.2 Self-Drawn Diagram (STRICT: NO AI-GENERATED DIAGRAMS):**
  - Student must hand-draw or construct the architecture diagram in Draw.io / Excalidraw / tool of choice.
  - Export diagram as `hw06/agent-skill/student-diagram.png`.
- [ ] **7.3 (Optional / Encouraged) Demo Video:**
  - Record and upload demonstration video (YouTube link) showing automated generation for 1 API.

---

## 8. AI Critique & External AI Declarations

- [ ] **8.1 External AI Session Declarations:**
  - Populate Section 3 of `hw06/docs/ai-audit.md` with the ChatGPT session used to prepare the initial master prompt and any other external AI interactions.
- [ ] **8.2 Author & Personalize AI Critique (200–300 words):**
  - Personalize critique in `hw06/docs/ai-critique.md` reflecting on real errors from the audit, what AI missed, and principles learned.

---

## 9. Final Packaging & Submission Verification

- [ ] **9.1 Git Commit Log:**
  - Generate clean text commit log: `git log --pretty=format:"%h - %cd : %s" --date=short > hw06/docs/git-commit-log.txt`.
- [ ] **9.2 Self-Assessed Grade:**
  - Student personally completes the evaluation table in `hw06/README.md` (Total out of 100).
- [ ] **9.3 Zip Archive Creation:**
  - Bundle into `23127027_HW06_AI_API_<SelfAssessedGrade>.zip` verifying all 14 mandatory PDF deliverables.
- [ ] **9.4 Submit to Moodle** before deadline.
