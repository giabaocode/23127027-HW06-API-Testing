# AI Audit Report (Báo cáo Sử dụng AI)

> **Student Information:**
> - Full Name: Pham Ngoc Gia Bao
> - Student ID: `23127027`
> - GitHub Username: `giabaocode`
> - Course: Software Testing (Kiểm thử Phần mềm) - HCMUS
> - Exercise: HW06 – API Testing (HW06-AI)
> - Academic Year: 2025–2026

---

## 1. AI Tool Usage Declaration

As required by the Course Policy on AI Usage (Open Policy with Mandatory Audit Report):
- I declare that AI tools are used as disciplined assistants throughout the defined phases of this assignment.
- All AI-generated outputs (test specifications, test cases, code, scripts, configurations) are subject to systematic human review, audit, correction, and extension by the student.
- The student maintains full responsibility for all final deliverables submitted.

---

## 2. Interaction Log (Antigravity / Gemini Session)

### Index of Verbatim Interaction Transcripts

To ensure total transparency without truncating large conversational turns, full verbatim records (both Student Prompt and Conversational AI Output) are preserved in individual transcript documents under [`hw06/docs/ai-transcripts/`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/):

| Interaction ID | Timestamp (ISO/Local) | Phase | Focus / Topic | Full Transcript File |
| :---: | :---: | :---: | :--- | :--- |
| **GEMINI-001** | 2026-09-02T10:47:40+07:00 | Phase 0 | Initial Setup, Reconnaissance & API Pool Comparison | [`hw06/docs/ai-transcripts/GEMINI-001.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-001.md) |
| **GEMINI-002** | 2026-09-02T10:57:18+07:00 | Phase 0 | Feature Selection Lock-in (FR-01, FR-07, FR-12) & Scope Setup | [`hw06/docs/ai-transcripts/GEMINI-002.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-002.md) |
| **GEMINI-003** | 2026-09-02T11:06:25+07:00 | Phase 0 | Compliance Corrections, Security Matrix & Classification Cleanup | [`hw06/docs/ai-transcripts/GEMINI-003.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-003.md) |
| **GEMINI-004** | 2026-09-02T11:35:35+07:00 | Phase 0 | Final Phase 0 Hardening, Defect Candidates & Commit Execution | [`hw06/docs/ai-transcripts/GEMINI-004.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-004.md) |
| **GEMINI-005** | 2026-09-02T11:40:33+07:00 | Phase 1 | FR-01 Specification Analysis & Planned Coverage Matrix | [`hw06/docs/ai-transcripts/GEMINI-005.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-005.md) |
| **GEMINI-006** | 2026-09-02T11:47:13+07:00 | Phase 1 | Human Review Corrections for FR-01 Spec Analysis | [`hw06/docs/ai-transcripts/GEMINI-006.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-006.md) |
| **GEMINI-007** | 2026-09-02T11:51:45+07:00 | Phase 1 | Human Review Checkpoint 1B Finalization & Coverage Count Calibration | [`hw06/docs/ai-transcripts/GEMINI-007.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-007.md) |
| **GEMINI-008** | 2026-09-02T11:56:35+07:00 | Phase 1 | Consistency Calibration & Local Commit of FR-01 Specification Analysis | [`hw06/docs/ai-transcripts/GEMINI-008.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-008.md) |
| **GEMINI-009** | 2026-09-02T12:00:10+07:00 | Phase 2 | AI Test Case Generation for FR-01 (38 Test Cases) | [`hw06/docs/ai-transcripts/GEMINI-009.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-009.md) |
| **GEMINI-010** | 2026-09-02T13:28:39+07:00 | Phase 2 | Human Audit Phase: Record ChatGPT Reference Review & Prepare Compact Review | [`hw06/docs/ai-transcripts/GEMINI-010.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-010.md) |

---

### Interaction GEMINI-001

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T10:47:40+07:00
- **Phase:** Phase 0 — Setup & Reconnaissance
- **Files Affected:**
  - `hw06/docs/ai-audit.md` (created)
  - `hw06/MANUAL_TODO.md` (created)
  - `implementation_plan.md` (created in brain artifacts)
- **Commands Executed:**
  - `list_dir /Users/phamngocgiabao/eshop-sut`
  - `view_file 2026.HW06.API Testing_En.pdf`
  - `view_file api_specification.md`
  - `grep_search SEC-`
  - `view_file README.md`
  - `view_file run_servers.sh`
  - `view_file setup_guide.md`
  - `git status && git branch --show-current && git remote -v && git log --oneline -10`
  - `list_dir backend`
  - `view_file backend/package.json`
  - `node -v && npm -v`
  - `which newman`
  - `grep_search app. in backend/server.js`
- **Git Actions:** None (Inspection only)
- **Human Checkpoint:** Checkpoint 0 — Initial reconnaissance and candidate selection comparison table presented for student review.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-001.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-001.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-001.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-001.md)
- Presented complete current state, files created, learning points from the assignment PDF (Section 1–17) and API specification (`api_specification.md`), Git remote status (`origin` pointing to `giabaocode/23127027-HW06-API-Testing.git`), Pool A/B/C candidate comparison matrix, and proposed next steps.

---

### Interaction GEMINI-002

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T10:57:18+07:00
- **Phase:** Phase 0 — Feature Confirmation & Scope Definition
- **Files Affected:**
  - `hw06/docs/ai-audit.md` (updated)
  - `hw06/MANUAL_TODO.md` (updated)
  - `hw06/submission-checklist.md` (created)
  - `implementation_plan.md` (updated)
- **Commands Executed:**
  - `view_file backend/server.js:1-60` (inspected register implementation)
  - `view_file backend/server.js:95-140` (inspected authenticateToken & profile update)
  - `view_file backend/server.js:280-320` (inspected cart & checkout)
  - `view_file backend/server.js:160-210` (inspected product admin endpoints)
  - `view_file backend/server.js:235-275` (inspected category endpoints)
  - `view_file backend/server.js:480-550` (inspected admin user & order status endpoints)
  - `git status`
- **Git Actions:** None (Inspection only)
- **Human Checkpoint:** Checkpoint 0 — Confirmed feature selection (FR-01, FR-07, FR-12) recorded; stopped before Phase 1.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-002.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-002.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-002.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-002.md)
- Output structured sections: `=== CURRENT STATE ===`, `=== OFFICIAL PDF REQUIREMENTS UNDERSTOOD ===`, `=== SELECTED FEATURES ===`, `=== EXACT ENDPOINTS FOUND ===`, `=== SEC MAPPING ===`, `=== SPECIFIED / INFERRED / UNKNOWN ITEMS ===`, `=== GIT STATUS ===`, `=== FILES CREATED / CHANGED ===`, `=== PROPOSED GIT COMMIT ===`, and `=== NEXT STEP ===`.

---

### Interaction GEMINI-003

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T11:06:25+07:00
- **Phase:** Phase 0 — Compliance Corrections & Audit Standardization
- **Files Affected:**
  - `hw06/docs/ai-audit.md` (updated)
  - `hw06/docs/implementation-plan.md` (created in docs)
  - `hw06/MANUAL_TODO.md` (updated)
  - `hw06/submission-checklist.md` (updated)
  - `hw06/docs/ai-transcripts/GEMINI-001.md` (created)
  - `hw06/docs/ai-transcripts/GEMINI-002.md` (created)
  - `hw06/docs/ai-transcripts/GEMINI-003.md` (created)
- **Commands Executed:**
  - `view_file .gitignore` (checked gitignore existence)
  - `view_file implementation_plan.md` (reviewed existing plan)
- **Git Actions:** None (Commit withheld as requested; PDF excluded from proposed commit)
- **Human Checkpoint:** Checkpoint 0 — Compliance adjustments submitted; awaiting approval to commit Phase 0 and start Phase 1.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-003.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-003.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-003.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-003.md)
- Reported: `=== AI AUDIT FORMAT FIXED ===`, `=== SECURITY APPLICABILITY MATRIX ===`, `=== SPEC/INFERENCE CORRECTIONS ===`, `=== FR-12 SCOPE ===`, `=== MANUAL_TODO CHANGES ===`, `=== CORRECTED PHASE 0 COMMIT ===`, `=== GIT STATUS ===`, and `=== READY FOR HUMAN REVIEW ===`.

---

### Interaction GEMINI-004

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T11:35:35+07:00
- **Phase:** Phase 0 — Final Compliance Hardening & Local Commit
- **Files Affected:**
  - `hw06/docs/ai-audit.md` (updated with transcript index & interaction 4)
  - `hw06/docs/implementation-plan.md` (updated security mapping, defect candidates, and FR-12 scope rule)
  - `implementation_plan.md` (brain artifact synchronized)
  - `hw06/MANUAL_TODO.md` (updated to clarify synthetic test data is allowed)
  - `hw06/docs/ai-transcripts/GEMINI-004.md` (created)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-001.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-002.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-003.md`
  - `write_to_file hw06/docs/implementation-plan.md`
  - `write_to_file hw06/docs/ai-audit.md`
  - `git status`
  - `git add hw06/`
  - `git commit -m "feat(hw06): initialize Phase 0 setup, feature selection, and audit registers"`
- **Git Actions:** Executed local Phase 0 commit (excluding assignment PDF; zero remote push).
- **Human Checkpoint:** Checkpoint 0 — Phase 0 successfully committed locally. Awaiting explicit student approval before starting Phase 1.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-004.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-004.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-004.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-004.md)

---

### Interaction GEMINI-005

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T11:40:33+07:00
- **Phase:** Phase 1 — Specification Analysis for FR-01 (Account Registration)
- **Files Affected:**
  - `hw06/testcases/fr01/spec-analysis.md` (created)
  - `hw06/testcases/fr01/coverage-matrix.md` (created)
  - `hw06/docs/ai-transcripts/GEMINI-005.md` (created)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `view_file backend/database.js:1-45`
  - `view_file backend/database.js:46-90`
  - `view_file backend/database.js:90-120`
  - `write_to_file hw06/testcases/fr01/spec-analysis.md`
  - `write_to_file hw06/testcases/fr01/coverage-matrix.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-005.md`
  - `git status`
- **Git Actions:** None (Commit withheld; stopping at Checkpoint 1 for student review).
- **Human Checkpoint:** Checkpoint 1 — Student Review of FR-01 Specification Analysis & Planned Coverage Matrix.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-005.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-005.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-005.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-005.md)

---

### Interaction GEMINI-006

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T11:47:13+07:00
- **Phase:** Phase 1 — Human Review Corrections for FR-01 Specification Analysis
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-005.md` (updated with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-006.md` (created)
  - `hw06/testcases/fr01/spec-analysis.md` (updated with human review corrections)
  - `hw06/testcases/fr01/coverage-matrix.md` (updated with recalculated 48 planned tests)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-005.md`
  - `write_to_file hw06/testcases/fr01/spec-analysis.md`
  - `write_to_file hw06/testcases/fr01/coverage-matrix.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-006.md`
  - `git status`
- **Git Actions:** None (Commit withheld; stopping at Checkpoint 1B for student second review).
- **Human Checkpoint:** Checkpoint 1B — Student Second Review of FR-01 Specification Analysis.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-006.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-006.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-006.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-006.md)

---

### Interaction GEMINI-007

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T11:51:45+07:00
- **Phase:** Phase 1 — Human Review Checkpoint 1B Finalization & Coverage Count Calibration
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-006.md` (repaired with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-007.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/spec-analysis.md` (calibrated response contract & one-condition rule)
  - `hw06/testcases/fr01/coverage-matrix.md` (calibrated to exactly 38 tests verified via python script)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-006.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-007.md`
  - `python3 -c "..."` (summed and verified planned test counts)
  - `write_to_file hw06/testcases/fr01/coverage-matrix.md`
  - `write_to_file hw06/testcases/fr01/spec-analysis.md`
  - `git status`
- **Git Actions:** None (Commit withheld; stopping at Checkpoint 1C for final student review).
- **Human Checkpoint:** Checkpoint 1C — Final Student Review of FR-01 Specification Analysis.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-007.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-007.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-007.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-007.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-008

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T11:56:35+07:00
- **Phase:** Phase 1 — Consistency Calibration & Local Commit of FR-01 Specification Analysis
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-007.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-008.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/spec-analysis.md` (calibrated field types and conditional status)
  - `hw06/testcases/fr01/coverage-matrix.md` (calibrated field types and conditional status; verified 38 tests)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-007.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-008.md`
  - `write_to_file hw06/testcases/fr01/spec-analysis.md`
  - `write_to_file hw06/testcases/fr01/coverage-matrix.md`
  - `python3 -c "..."` (re-verified planned test count = 38)
  - `git status`
  - `git add hw06/`
  - `git commit -m "test(fr01): complete reviewed specification analysis and coverage plan"`
- **Git Actions:** Executed local commit on branch `main` (PDF excluded, zero remote push).
- **Human Checkpoint:** Checkpoint 1C approved; Phase 1 FR-01 Specification Analysis committed locally. Stopping before Phase 2 test generation.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-008.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-008.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-008.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-008.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-009

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T12:00:10+07:00
- **Phase:** Phase 2 — AI Test Case Generation for FR-01 (Account Registration)
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-008.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-009.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/generated-ai-original.md` (created with exactly 38 AI-generated test cases)
  - `hw06/testcases/fr01/human-audit.md` (created with 38 rows and empty student audit fields)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-008.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-009.md`
  - `write_to_file hw06/testcases/fr01/generated-ai-original.md`
  - `write_to_file hw06/testcases/fr01/human-audit.md`
  - `python3 -c "..."` (validated 38 tests, continuous IDs, coverage mapping, empty audit fields)
  - `git status`
  - `git add hw06/`
  - `git commit -m "test(fr01): generate 38 AI registration test cases"`
- **Git Actions:** Executed local commit representing AI generation step (PDF excluded, zero remote push).
- **Human Checkpoint:** Checkpoint 2 — Student Human Audit Required (Awaiting student independent review).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-009.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-009.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-009.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-009.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-010

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T13:28:39+07:00
- **Phase:** Phase 2 — Human Audit Phase (Recording ChatGPT External Reference Review & Fast Review View)
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-009.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-010.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/ai-reference-audit.md` (created with ChatGPT reference review)
  - `hw06/testcases/fr01/human-review-compact.md` (created for rapid student review)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-009.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-010.md`
  - `write_to_file hw06/testcases/fr01/ai-reference-audit.md`
  - `python3 -c "..."` (generated human-review-compact.md)
  - `python3 -c "..."` (validated reference distribution, human-audit.md empty fields, compact review rows)
  - `git status`
  - `git add hw06/`
  - `git commit -m "docs(fr01): record external AI reference review"`
- **Git Actions:** Executed local documentation commit on branch `main` (PDF excluded, zero remote push).
- **Human Checkpoint:** Checkpoint 2A — Student Final Human Judgment Required (Student review in progress).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-010.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-010.md)

#### Verbatim AI Output
*Conversational response status:* `[VERBATIM AI RESPONSE TO BE FINALIZED AT NEXT INTERACTION]` (Preserved in [`GEMINI-010.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-010.md) via retrospective logging).

---

## 3. Previous / External AI Interactions — Student Must Add

> [!IMPORTANT]
> **Mandatory Action for Student (Pham Ngoc Gia Bao):** The prompt used to initiate this session was engineered using ChatGPT. As required by the course guidelines, please record that interaction (and any other external AI interactions) below with the exact prompt, date, tool name, and summary.

| # | Date & Time | AI Tool | Task / Topic | Student Prompt Summary | Summary of AI Output | How Output Was Used / Verified |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-09-02 | ChatGPT (OpenAI) | Prompt Engineering / HW06 Setup | Formulated comprehensive instructions and constraints for Antigravity AI pair programming. | Generated structured master prompt template with phase gating and anti-cheat rules. | Used to guide Phase 0 session initialization and policy compliance. |
| 2 | 2026-09-02 | ChatGPT (OpenAI) | External Reference Review of FR-01 AI Test Cases | Student provided the 38 AI-generated FR-01 test cases to obtain an independent second-AI critique. | Produced external reference review with verdicts (25 Valid, 12 Incomplete, 1 Invalid) and reasoning/corrections. | Preserved as reference material in `ai-reference-audit.md` for student cross-reference; student audit fields remain independent. |

---

## 4. Summary of AI-Assisted vs. Human-Only Tasks

| Category | AI Responsibility (Automatable via Tools) | Student Responsibility (Strict Human Gate) |
| :--- | :--- | :--- |
| **API Specification Analysis** | Extract parameter rules, status codes, schemas, security requirements; construct partition matrices. | Verify accuracy against business logic, identify spec discrepancies and edge cases. |
| **Test Case Generation** | Generate draft test cases (target ≥ 35 per selected API) with inputs, assertions, and boundary coverage. | Perform mandatory audit: label VALID / INVALID / INCOMPLETE with reasoning and corrections. |
| **Test Case Extension** | Identify high-level coverage gaps; provide empty templates. | Author ≥ 5 original, non-AI test cases per API (focusing on state transitions, security, business logic). |
| **Automation & Execution** | Construct Postman collection/environment, inject `X-Student-Id`, execute Newman, generate HTML report, start SUT. | Capture real console screenshot showing `X-Student-Id: 23127027`; verify Newman report authenticity. |
| **Bug Detection & Reporting** | Correlate test failures to possible defects vs. test errors. | Verify real reproducibility, file GitHub Issues with screenshots, document root causes. |
| **CI/CD Integration** | Write GitHub Actions workflow YAML (`.github/workflows/api-tests.yml`), set up sample demonstration runs. | Trigger real pipeline runs, capture screenshots and record real GitHub run URLs. |
| **Agent Skill / Architecture** | Provide architectural options, pseudocode, and implementation scaffolding. | Make architectural design decisions; self-draw test generator diagram (no AI-generated images/Mermaid diagrams). |
| **AI Critique** | Collate factual observations on AI errors and limitations during the assignment. | Author personalized 200–300 word critique and reflect on human-AI pairing principles. |

---

## 5. Factual AI Mistakes & Critique Candidates (Recorded for Phase 9)

As required by the assignment guidelines, all observable AI reasoning errors, hallucinated assumptions, and calculation discrepancies are documented truthfully here rather than silently erased. These provide authentic evidence for the student's **AI Critique (Phase 9)**:

| Candidate ID | Phase / Interaction | Category | Description of AI Error | Root Cause & Correction |
| :---: | :---: | :---: | :--- | :--- |
| **AI-ERR-01** | Phase 0 (Turn 1 & 2) | Hallucinated Schema Constraint | AI asserted that duplicate email registration would trigger a SQLite `UNIQUE` constraint error and return `500 Internal Server Error`. | **Fact:** Re-inspection of `backend/database.js` Line 53 confirmed the column is defined as `email TEXT` without a `UNIQUE` constraint. `server.js` performs no existence lookup; duplicate accounts are silently inserted into SQLite as duplicate records with status 200. |
| **AI-ERR-02** | Phase 1 (Turn 6) | Mathematical Calculation Discrepancy | AI stated `~38` in the header and `48` in the summary text of `coverage-matrix.md`, while the actual programmatic sum of the row counts was `55`. | **Fact:** AI estimated row totals mentally instead of executing programmatic summation. The matrix was recalibrated and verified via a Python script to sum to exactly **38 tests**. |
| **AI-ERR-03** | Phase 1 (Turn 6) | Premature Verbatim Claim | AI Audit logged that Turn 6 transcript contained full verbatim AI response before the turn was delivered, leaving a placeholder inside `GEMINI-006.md`. | **Fact:** A response cannot be logged before it is generated. Corrected by establishing a strict retrospective logging protocol (finalizing previous turn response at the start of next turn). |
| **AI-ERR-04** | Phase 1 (Turn 5) | Over-Constraint Inference | AI converted a single example response in `api_specification.md` into a rigid JSON Schema asserting `additionalProperties: false` and `id >= 1` as `SPECIFIED` contract rules. | **Fact:** The specification provided only an example JSON object. Corrected by classifying example attributes as `EXAMPLE-DERIVED` and `INFERRED FROM EXAMPLE`, keeping schema constraints as `UNKNOWN / NOT SPECIFIED`. |
| **AI-ERR-05** | Phase 2 (Turn 9) / `FR01-AI-019` | Test Design Flaw / False Security Probe | In `FR01-AI-019`, AI designed a test for SEC-05 (parameterized query) using email `' OR '1'='1'@domain.com`, which is syntactically malformed under email format rules. | **Fact:** An API validation layer may reject malformed emails before database interaction occurs, meaning the test cannot reliably prove whether parameterized queries protect the database. To test SEC-05 effectively, the payload must reach the SQL execution layer (e.g. via `name`). |

