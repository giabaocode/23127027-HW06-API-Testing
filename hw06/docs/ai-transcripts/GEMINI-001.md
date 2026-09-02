# Verbatim AI Transcript — Interaction GEMINI-001

- **Session / Interaction ID:** GEMINI-001
- **Date & Time:** 2026-09-02T10:47:40+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Phase 0 — Setup & Reconnaissance

---

## 1. Verbatim Student Prompt

```text
You are working INSIDE my already-cloned local repository of the official
HCMUS EShop SUT.

This repository contains:
- the official EShop source code,
- api_specification.md,
- functional/security requirements,
- and a PDF containing the official HW06 – API Testing assignment requirements.

Student information:

STUDENT_ID = 23127027
GITHUB_USERNAME = giabaocode

IMPORTANT:
Do NOT assume my GitHub homework repository has already been configured.
Inspect `git remote -v` first.

============================================================
PRIMARY OBJECTIVE
============================================================

Help me complete as much of HW06 – API Testing as legitimately possible using
AI-first software-engineering practices.

You should automate everything that AI/tools are legitimately allowed to do,
but STOP whenever the assignment requires:

- human judgment,
- student-authored work,
- real execution evidence,
- screenshots,
- personal design decisions,
- or any action that cannot be truthfully automated.

The assignment PDF inside this repository is the HIGHEST-PRIORITY source of
rules for this task.

The SUT API specification and requirements inside the repository are the
HIGHEST-PRIORITY technical source for API behavior.

Do NOT rely only on this prompt.

============================================================
PHASE 0 — READ BEFORE DOING ANYTHING
============================================================

Before modifying files:

1. Inspect the repository tree.

2. Locate the HW06 assignment PDF I placed in the repository.

3. Read the COMPLETE PDF.

4. Locate and read:
   - api_specification.md
   - relevant FR requirements
   - SEC-01 through SEC-07
   - README/setup instructions
   - application startup instructions

5. Inspect:
   git status
   git branch --show-current
   git remote -v
   git log --oneline -10

6. Produce a concise interpretation of:
   - required deliverables,
   - mandatory AI-first workflow,
   - human-only requirements,
   - execution evidence requirements,
   - Git requirements,
   - CI/CD requirements,
   - submission requirements.

7. Compare the PDF rules against this prompt.

If anything in this prompt conflicts with the PDF:

THE PDF WINS.

Tell me about the conflict instead of silently following this prompt.

DO NOT generate test cases yet.

============================================================
ACADEMIC INTEGRITY / HARD RULES
============================================================

The assignment requires an AI-first process, NOT a black-box process.

Therefore, never execute the entire homework from beginning to end without
human checkpoints.

You must work phase-by-phase.

After every major phase:

1. summarize what you did,
2. list files created/changed,
3. list assumptions,
4. list unresolved questions,
5. update the AI Audit,
6. propose a Git commit,
7. STOP when human approval/work is required.

------------------------------------------------------------
HUMAN AUDIT
------------------------------------------------------------

AI-generated test cases must later be reviewed by ME.

For every AI-generated test case, prepare fields for:

- Student Verdict: VALID / INVALID / INCOMPLETE
- Student Reasoning
- Student Correction
- Student Reviewed At

YOU MUST NOT fill these student-review fields.

You may provide a separate:

AI REVIEW HINT

but that must never be presented as my human audit.

------------------------------------------------------------
STUDENT-OWN TEST CASES
------------------------------------------------------------

For EACH selected API, the assignment requires at least five additional test
cases created by the student that AI missed.

Therefore:

DO NOT write those five actual test cases for me.

You may:
- detect coverage gaps,
- identify broad missing categories,
- prepare empty test-case templates.

You may NOT give me a fully specified test input + execution + expected result
that I could directly copy as one of my five student-created tests.

After I create those tests myself, you may automate and execute them.

------------------------------------------------------------
AI TEST-GENERATOR DIAGRAM
------------------------------------------------------------

The final AI-driven API test-generator diagram must be self-drawn by me.

Therefore DO NOT:

- create the final Mermaid diagram,
- create PlantUML,
- create SVG/PNG,
- generate a diagram image,
- create draw.io content representing the final design.

You may help me:
- understand architectural choices,
- create a blank checklist,
- review my diagram AFTER I create it,
- implement code/pseudocode after my design decisions are known.

------------------------------------------------------------
REAL EVIDENCE ONLY
------------------------------------------------------------

NEVER fabricate:

- screenshots,
- Postman Console evidence,
- Newman execution,
- Newman reports,
- GitHub Actions runs,
- Git commit hashes,
- GitHub Issue screenshots,
- request/response evidence,
- timestamps,
- URLs,
- bugs,
- pass/fail statistics.

If you actually run something in the terminal, preserve its real output.

If something cannot be executed:

mark it clearly as:

MANUAL ACTION REQUIRED

Never create fake evidence to make the homework appear complete.

============================================================
GIT / REPOSITORY SAFETY
============================================================

First inspect `git remote -v`.

If `origin` still points to:

https://github.com/ttbhanh/eshop-sut

DO NOT push homework modifications to the lecturer's repository.

Instead STOP and tell me that my personal repository needs to be configured.

My intended GitHub owner is:

giabaocode

Do not invent the destination repository URL if it does not exist.

When a personal repository is configured, the recommended arrangement is:

origin   -> my HW06 repository
upstream -> official ttbhanh/eshop-sut

Never force-push unless I explicitly approve it.

Never remove `.git`.

Never rewrite existing official Git history.

Before every commit:

1. show changed files,
2. propose commit message,
3. explain which HW06 phase it represents.

The assignment expects separate commits for major procedure steps.

============================================================
PROJECT ORGANIZATION
============================================================

Do NOT unnecessarily reorganize the official SUT.

Prefer creating a homework area such as:

hw06/
├── README.md
├── MANUAL_TODO.md
├── submission-checklist.md
├── docs/
│   ├── main-report.md
│   ├── ai-audit.md
│   ├── ai-critique.md
│   ├── cicd-report.md
│   ├── postman-features.md
│   ├── oral-defense-notes.md
│   └── git-commit-log.txt
├── testcases/
│   ├── api1/
│   ├── api2/
│   └── api3/
├── postman/
│   └── data/
├── newman/
├── bugs/
│   └── evidence/
├── screenshots/
└── agent-skill/
    ├── design-decisions.md
    ├── student-diagram-checklist.md
    └── pseudocode.md

Keep CI/CD workflows in the repository's normal:

.github/workflows/

directory where appropriate.

Adapt this structure if the repository already contains suitable directories.

Do not duplicate existing material unnecessarily.

============================================================
AI AUDIT
============================================================

Create and continuously maintain:

hw06/docs/ai-audit.md

For interactions during THIS Antigravity/Gemini session, record:

- AI tool
- date/time
- phase
- student prompt
- meaningful AI output/action
- files affected

Do not claim this is the complete audit of all AI usage.

Create a section:

## Previous / External AI Interactions — Student Must Add

because I may also have used ChatGPT or other AI tools.

Do not invent interactions that you cannot observe.

============================================================
MANUAL TODO REGISTER
============================================================

Create:

hw06/MANUAL_TODO.md

Track every required student/manual action.

Initial categories should include:

- confirm the three APIs selected,
- confirm no group member has the exact same selection,
- human audit of every AI-generated test,
- >=5 student-authored additional tests per API,
- explanation of why AI missed them,
- real X-Student-Id screenshot,
- real Newman evidence,
- real bug screenshots,
- real GitHub Actions links/screenshots,
- Agent Skill design decisions,
- student-created diagram,
- AI Critique personalization,
- self-assessed grade,
- previous external AI interactions,
- final submission verification.

Never silently mark something complete.

Only mark complete when real evidence exists.

============================================================
API SELECTION
============================================================

The homework requires exactly three APIs/features:

- one from Pool A,
- one from Pool B,
- one from Pool C.

Pool D is excluded.

If I have NOT selected the APIs yet:

1. inspect api_specification.md,
2. identify valid options for Pool A/B/C,
3. create a concise comparison table showing:
   - feature / FR,
   - endpoint(s),
   - complexity,
   - state-transition opportunities,
   - security-testing opportunities,
   - automation difficulty,
   - likely suitability for this homework.

Do NOT choose the final three for me.

STOP and let me choose.

I must also personally confirm that the exact selection is not duplicated by
another member of my group.

============================================================
PHASE 1 — SPECIFICATION ANALYSIS
============================================================

After I choose the APIs, analyze ONE API AT A TIME.

For each selected API extract:

- FR
- endpoint
- HTTP method
- authentication
- authorization/roles
- headers
- path parameters
- query parameters
- request body
- field types
- required/optional fields
- documented constraints
- response codes
- response schema
- state requirements
- SEC requirements
- relevant cross-field rules.

Every extracted statement must be marked:

SPECIFIED
INFERRED
UNKNOWN

Never silently turn an implementation behavior into an expected requirement.

If implementation and specification disagree:

record:

POSSIBLE DEFECT / SPEC DISCREPANCY

Do not adjust the test expectation merely to match implementation.

Then design the testing dimensions for that API:

- equivalence/domain partitions for every parameter,
- valid partitions,
- invalid partitions,
- boundary values,
- state transitions,
- authentication,
- authorization,
- SEC-01–SEC-07 where applicable,
- IDOR/role escalation/injection where relevant,
- schema validation,
- error behavior,
- cross-field behavior.

Create a coverage matrix.

DO NOT generate >=35 tests yet.

STOP:

=== CHECKPOINT 1 — STUDENT REVIEW OF SPEC ANALYSIS ===

Wait for my approval.

============================================================
PHASE 2 — AI TEST GENERATION
============================================================

Only after I approve Phase 1.

Generate tests for ONE selected API.

Target:

>= 35 meaningful AI-generated test cases PER API.

Do not meet the number by creating trivial duplicates.

Every test should contain:

- Test ID
- Origin = AI
- FR / requirement
- SEC requirement if applicable
- category
- objective
- preconditions
- initial state
- authentication/role
- method
- endpoint
- input
- equivalence partition/boundary
- execution steps
- expected HTTP status
- expected response
- schema assertions
- security assertion if applicable
- state assertion if applicable
- cleanup
- automation status.

Coverage must follow the HW06 PDF.

Generate ONE API first.

After generation:

1. save the generated set,
2. update coverage matrix,
3. prepare the human-audit worksheet,
4. update AI Audit,
5. propose Git commit,
6. STOP.

Use:

=== CHECKPOINT 2 — HUMAN AUDIT REQUIRED ===

Do not audit the tests for me.

============================================================
PHASE 3 — HUMAN AUDIT PROCESS
============================================================

After I manually fill:

VALID / INVALID / INCOMPLETE
reasoning
correction

preserve BOTH:

- original AI test,
- reviewed/final test.

Do not erase incorrect AI output.

Maintain traceability.

This evidence is important for the AI Audit and AI Critique.

============================================================
PHASE 4 — STUDENT EXTENSION
============================================================

After human audit, analyze missing coverage.

Do NOT generate the five required student-created tests.

Instead create an empty worksheet containing:

- Student Test ID
- Gap Category
- Student Objective
- Preconditions
- Input
- Steps
- Expected Result
- Requirement / SEC
- Why AI Missed It
- Student Authorship Confirmation

You may populate ONLY broad categories such as:

- authorization edge
- state-transition edge
- security boundary
- domain boundary
- schema edge
- cross-field interaction
- concurrency consideration.

STOP:

=== CHECKPOINT 3 — STUDENT MUST CREATE >=5 ORIGINAL TESTS ===

After I write them, you may validate their consistency and automate them.

============================================================
PHASE 5 — POSTMAN / NEWMAN
============================================================

After the reviewed AI tests + my additional tests exist:

Create/maintain a real Postman collection.

Use appropriate features when genuinely useful:

- collection variables,
- environments,
- pre-request scripts,
- test scripts,
- data-driven testing,
- Collection Runner,
- mock servers if useful,
- monitors if practical.

Every request must carry:

X-Student-Id: 23127027

Prefer central injection through a collection-level pre-request script or
another clearly traceable mechanism.

Do not fake the required screenshot.

Prepare a checklist telling me exactly how to capture real evidence.

Implement real assertions for:

- HTTP status
- response body
- schema
- security behavior
- state changes.

============================================================
PHASE 6 — EXECUTION
============================================================

Before Newman:

- identify the actual backend startup command,
- confirm required services,
- determine the actual base URL,
- confirm the SUT is healthy.

If you can REALLY start/run the application in this workspace, you may do so.

Then run Newman for real.

Preserve:

- commands,
- terminal output,
- timestamps,
- actual hostname,
- actual totals,
- passes/failures.

Do not modify legitimate expected results merely to make tests pass.

A test exposing a bug is valuable.

If execution cannot occur:

STOP and create exact manual commands for me.

Never generate fake Newman HTML output.

============================================================
BUG REPORTING
============================================================

A bug must be based on actual observed behavior.

For failures classify first:

- likely SUT defect
- likely test defect
- environment/configuration issue
- spec ambiguity
- requires investigation.

Only draft a bug report when justified.

Use:

- title
- API / FR / SEC
- environment
- preconditions
- steps
- expected
- actual
- severity suggestion
- evidence.

Never fabricate screenshot evidence.

Leave:

[STUDENT MUST ATTACH REAL SCREENSHOT]

when necessary.

============================================================
CI/CD
============================================================

Create a real GitHub Actions workflow for the API tests when appropriate.

The assignment requires evidence of:

1. a real run where all intended API tests pass,
2. a real demonstration run containing one failing test.

Do not fabricate either run.

If creating the intentional failure demonstration:

- make the change explicit,
- isolate it in a demonstration commit,
- do not corrupt the real final test suite,
- document why the commit intentionally fails.

Store only real run URLs and hashes.

============================================================
AGENT SKILL / TEST GENERATOR
============================================================

Help implement an AI-driven API test generator only AFTER I provide my own
design decisions.

Ask me for:

- components,
- flow,
- intermediate representation,
- test-generation strategy,
- validation stage,
- human-review point,
- outputs.

Record MY decisions.

Then you may:

- help with pseudocode,
- implement reusable code/skill,
- test it,
- prepare demo commands.

DO NOT draw the final architecture/test-generator diagram.

Create only a checklist of things I may want to include when I draw it myself.

============================================================
REPORTING
============================================================

Continuously build documentation from REAL project data.

Main report should eventually cover:

- selected APIs,
- specification analysis,
- AI generation,
- human audit,
- student extension,
- Postman automation,
- execution,
- bugs,
- Postman features,
- CI/CD,
- Agent Skill,
- test summary,
- AI Critique,
- AI Audit,
- limitations,
- evidence.

Never invent missing statistics.

Use:

[WAITING FOR REAL EXECUTION]

when evidence is not available yet.

============================================================
AI CRITIQUE
============================================================

Do not invent an artificial 200–300 word critique.

Wait until there are real examples from:

- INVALID cases,
- INCOMPLETE cases,
- tests I added,
- AI mistakes,
- bugs AI missed.

Then prepare a factual draft.

Mark it:

STUDENT MUST REVIEW AND PERSONALIZE BEFORE SUBMISSION

============================================================
QUALITY GATE
============================================================

Never say the homework is finished until you have checked:

- exactly 3 selected APIs: Pool A/B/C,
- >=35 meaningful AI-generated tests per API,
- every parameter appropriately partitioned,
- relevant state transitions covered,
- relevant SEC requirements covered,
- response schema covered,
- every AI case human-reviewed,
- >=5 student-authored additional tests/API,
- actual execution exists,
- X-Student-Id is present,
- Newman report is real,
- genuine bugs only,
- CI/CD has two genuine runs,
- AI Audit is complete,
- AI Critique is 200–300 words and student-reviewed,
- final test-generator diagram is student-created,
- Git commit log is real,
- README/test summary exists,
- all submission artifacts required by the PDF exist.

If anything is missing, report:

NOT READY FOR SUBMISSION

and list exactly what remains.

============================================================
START NOW — DO ONLY THIS
============================================================

For your FIRST response/action:

1. Inspect the repository.
2. Find and read the complete HW06 PDF.
3. Find and read api_specification.md.
4. Locate SEC-01–SEC-07.
5. Inspect git status, branch, remotes, recent commits.
6. Determine how the SUT is started.
7. Determine what HW06 files/folders already exist.
8. Create/update:
   - hw06/docs/ai-audit.md
   - hw06/MANUAL_TODO.md
9. Identify Pool A/B/C API options.
10. Tell me what information/actions you need from me.
11. DO NOT generate the >=35 tests yet.
12. DO NOT create a final diagram.
13. DO NOT execute the whole homework.
14. STOP at the first checkpoint.

At the end, show:

CURRENT STATE
FILES CREATED/CHANGED
WHAT YOU LEARNED FROM THE PDF
WHAT YOU LEARNED FROM THE API SPEC
GIT/REMOTE STATUS
MANUAL ACTIONS REQUIRED
NEXT PROPOSED STEP
```

---

## 2. Verbatim Conversational AI Response

### CURRENT STATE

Phase 0 setup and comprehensive reconnaissance of the SUT and assignment requirements are complete. 
- All official source code, API specifications, and the assignment specification PDF have been thoroughly inspected.
- The homework workspace layout under `hw06/` has been initialized, including the mandatory [ai-audit.md](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-audit.md) and [MANUAL_TODO.md](file:///Users/phamngocgiabao/eshop-sut/hw06/MANUAL_TODO.md).
- The detailed phase-by-phase [implementation_plan.md](file:///Users/phamngocgiabao/.gemini/antigravity-ide/brain/95308b01-1bfe-414d-8483-877d83a584e0/implementation_plan.md) is established with user checkpoints.
- No test cases or diagrams have been generated, and no code has been executed yet. We are halted at **Checkpoint 1**.

---

### FILES CREATED/CHANGED

1. **[hw06/docs/ai-audit.md](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-audit.md)**: AI Audit log initialized with tool declarations, session timestamp, Phase 0 actions, external AI tracking section for the student, and clear AI vs. human responsibility boundaries.
2. **[hw06/MANUAL_TODO.md](file:///Users/phamngocgiabao/eshop-sut/hw06/MANUAL_TODO.md)**: Master register tracking all human-only requirements, evidence captures, and quality checkpoints.
3. **[implementation_plan.md](file:///Users/phamngocgiabao/.gemini/antigravity-ide/brain/95308b01-1bfe-414d-8483-877d83a584e0/implementation_plan.md)**: Complete implementation plan covering all 9 phases, API pool comparison, and verification plan.

---

### WHAT YOU LEARNED FROM THE PDF

From **`2026.HW06.API Testing_En.pdf`**:
- **Assignment ID & Nature**: HW06-AI (Individual assignment, 10 hours estimated).
- **Core Pipeline per API**: Must select exactly **three (3) APIs** (one from Pool A, one from Pool B, one from Pool C; Pool D mobile is excluded). For each API:
  1. *Generate with AI*: $\ge 35$ test cases covering domain partitions, state transitions, security (SEC-01–SEC-07), and schema validation.
  2. *Audit (Human review)*: Student must label each case `VALID` / `INVALID` / `INCOMPLETE` with reasoning and corrections.
  3. *Extend*: Student must author $\ge 5$ original test cases that AI missed (with explanations why AI missed them).
  4. *Execute*: Run via Postman + Newman with `X-Student-Id: {StudentID}` header; generate real Newman HTML report.
  5. *Report bugs*: File real bugs found on GitHub Issues with screenshots and in the markdown report.
- **Anti-AI-Cheat Constraints (Strict Verification)**:
  - Header `X-Student-Id: 23127027` evidenced by a real Postman Console screenshot.
  - Newman run output hostname must match local deployment (`localhost` / `127.0.0.1`).
  - The AI test-generator architecture diagram must be **self-drawn by the student** (no AI-generated images or direct Mermaid renders).
- **CI/CD Requirements**: GitHub Actions pipeline running Newman with two sample commits: one all-passing and one with an intentional 1-test failure demonstration.
- **AI Critique**: Mandatory 200–300 word critique analyzing where AI failed, why it failed, and principles learned.
- **Submission Deliverable**: Zip file named `<StudentID>_HW06_AI_API_<SelfAssessedGrade>.zip` (e.g. `23127027_HW06_AI_API_090.zip`) containing report (MD + PDF), Postman collection & Newman HTML report, CI/CD report, Excel test cases, diagram + pseudocode, bug reports, critique + audit, commit log, and README with self-assessment table.
- **Conflict Rule**: The PDF is the highest authority; any conflicting instructions from earlier prompts defer to the PDF.

---

### WHAT YOU LEARNED FROM THE API SPEC & REQUIREMENTS

1. **System Under Test (SUT) Architecture**:
   - Backend: Node.js + Express 5 + SQLite (`backend/server.js`, `backend/database.js`).
   - Base URL: `http://localhost:3000`.
   - Seed data command: `cd backend && node database.js` (creates `database.sqlite` with default admin `admin@eshop.com` / `Admin123!` and user `test@eshop.com` / `Test1234!`).
   - Server run command: `cd backend && node server.js`.
2. **Security Requirements (SEC-01 to SEC-07)**:
   - `SEC-01`: Password must not be stored in plaintext.
   - `SEC-02`: Secured endpoints must enforce valid JWT token in `Authorization: Bearer <token>`.
   - `SEC-03`: Admin endpoints must verify `role === 'admin'` in the token, not merely token existence.
   - `SEC-04`: User-supplied input reflected on UI must be properly sanitized/escaped.
   - `SEC-05`: Database queries must use parameterized queries (prevent SQL injection).
   - `SEC-06`: Profile update API (`PUT /api/users/me`) must not allow modification of `role`.
   - `SEC-07`: Password reset OTP must have sufficient entropy ($\ge 6$ digits), expiration, and one-time invalidation.
3. **Candidate API Pools**:
   - **Pool A (Auth, Categories, Products)**:
     - `FR-01`: `POST /api/register`
     - `FR-02`: `POST /api/login` *(Recommended: Rich lockout state machine, JWT generation, SEC-01/02)*
     - `FR-03`: `POST /api/forgot-password` & `POST /api/reset-password`
     - `FR-04`: `GET /api/users/me` & `PUT /api/users/me` (SEC-06 role escalation target)
     - `FR-05`: `GET /api/products` (Search keyword XSS / SQLi)
     - `FR-06`: `GET /api/products/:id`
   - **Pool B (Cart & Checkout)**:
     - `FR-07`: `GET /api/cart` & `POST /api/cart`
     - `FR-08`: `POST /api/checkout`
     - `FR-09`: `POST /api/apply-coupon` *(Recommended: 5 explicit business conditions C1–C5, threshold boundaries, max uses, IDOR vulnerability)*
     - `FR-10`: `PUT /api/orders/:id/cancel` (Order cancellation state rules)
     - `FR-11`: `GET /api/orders/my-orders` & `GET /api/orders/:id`
   - **Pool C (Web Admin)**:
     - `FR-14`: `GET /api/categories`, `POST /api/categories`, `PUT /api/categories/:id`, `DELETE /api/categories/:id`
     - `FR-15`: `POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id`
     - `FR-16`: `POST /api/admin/import-products` (CSV transaction rollback)
     - `FR-17`: `POST /api/admin/coupons`, `DELETE /api/admin/coupons/:id`
     - `FR-18`: `GET /api/admin/orders`, `PUT /api/admin/orders/:id/status` *(Recommended: Complete 5-state machine pending $\to$ confirmed $\to$ shipping $\to$ delivered / canceled, final state immutability, SEC-03 admin privilege verification)*
     - `FR-19`: `GET /api/admin/users`, `DELETE /api/admin/users/:id`

---

### GIT/REMOTE STATUS

- **Current Branch**: `main`
- **Remotes**:
  - `origin`: `https://github.com/giabaocode/23127027-HW06-API-Testing.git` (Already configured correctly for your GitHub account!)
  - `upstream`: `https://github.com/ttbhanh/eshop-sut.git` (Official lecturer repository)
- **Commit History**:
  - `85af3ba` first upload
  - `2f9bf2b` Initial commit
- **Local Changes**:
  - Untracked: `2026.HW06.API Testing_En.pdf`, `hw06/` directory.

---

### MANUAL ACTIONS REQUIRED (FROM YOU)

1. **Confirm API Selection**:
   Please confirm your final three APIs (one each from Pool A, B, and C). Our recommendation for maximum testing depth and alignment with assignment rubrics:
   - **API 1 (Pool A)**: `POST /api/login` (FR-02: Login, Account Lockout, JWT issuance)
   - **API 2 (Pool B)**: `POST /api/apply-coupon` (FR-09: Coupon business logic conditions C1–C5, user limits, boundaries)
   - **API 3 (Pool C)**: `PUT /api/admin/orders/:id/status` & `GET /api/admin/orders` (FR-18 & FR-10: Admin Order State Machine & Access Control)
2. **Verify Group Deduplication**:
   Confirm that no other student in your study group has chosen the exact same combination of 3 APIs.
3. **Review & Approve Implementation Plan**:
   Review the [implementation_plan.md](file:///Users/phamngocgiabao/.gemini/antigravity-ide/brain/95308b01-1bfe-414d-8483-877d83a584e0/implementation_plan.md) artifact.

---

### NEXT PROPOSED STEP

Upon your selection confirmation and approval:
1. Stage and commit Phase 0 setup:
   - Commit message: `feat(hw06): initialize Phase 0 setup, manual todo register, and AI audit log`
2. Begin **Phase 1: Specification Analysis for API 1 (Pool A)**:
   - Extract parameter constraints, HTTP codes, schemas, and security requirements.
   - Construct domain equivalence partitions (valid/invalid) and boundary values.
   - Present the Phase 1 Specification & Coverage Matrix for API 1 and pause at **Checkpoint 1** for your review before generating tests.
