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
| **GEMINI-011** | 2026-09-02T13:39:28+07:00 | Phase 2 | Human Audit: External Transcripts Setup, Compact Review Polish & Batch 1 Initiation | [`hw06/docs/ai-transcripts/GEMINI-011.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-011.md) |
| **GEMINI-012** | 2026-09-02T13:46:21+07:00 | Phase 2 | Student Human Audit Execution: All 38 FR-01 Cases Reviewed & Validated | [`hw06/docs/ai-transcripts/GEMINI-012.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-012.md) |
| **GEMINI-013** | 2026-09-02T13:50:14+07:00 | Phase 2 | Phase 2 Completion & Local Commit of Student Human Audit | [`hw06/docs/ai-transcripts/GEMINI-013.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-013.md) |
| **GEMINI-014** | 2026-09-02T13:54:44+07:00 | Phase 3 | Phase 3A: Reviewed AI Final Set Creation & Student Extension Template Setup | [`hw06/docs/ai-transcripts/GEMINI-014.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-014.md) |
| **GEMINI-015** | 2026-09-02T14:08:03+07:00 | Phase 3 | Phase 3B: Formalize 5 Student-Selected Registration Extension Tests | [`hw06/docs/ai-transcripts/GEMINI-015.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-015.md) |
| **GEMINI-016** | 2026-09-02T14:11:56+07:00 | Phase 4 & 5 | FR-01 Postman Automation, Local SUT Startup & Real Newman Execution | [`hw06/docs/ai-transcripts/GEMINI-016.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-016.md) |
| **GEMINI-017** | 2026-09-02T14:28:33+07:00 | Environment | Terminate Background SUT Process to Free Port 3000 | [`hw06/docs/ai-transcripts/GEMINI-017.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-017.md) |
| **GEMINI-018** | 2026-09-02T15:57:48+07:00 | Phase 5 & 6 | Session Resumption: SUT Status, Screenshot Verification & Defect Reporting | [`hw06/docs/ai-transcripts/GEMINI-018.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-018.md) |
| **GEMINI-019** | 2026-09-02T16:00:33+07:00 | Phase 5 | SUT Server Relaunch & Postman Console Screenshot Guidance | [`hw06/docs/ai-transcripts/GEMINI-019.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-019.md) |
| **GEMINI-020** | 2026-09-02T16:33:27+07:00 | Phase 5 & 6 | Screenshot Verification, Defect Documentation & GitHub Issues #1..#5 Created | [`hw06/docs/ai-transcripts/GEMINI-020.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-020.md) |
| **GEMINI-021** | 2026-09-02T16:47:27+07:00 | Phase 1 (FR-07) | FR-07 Shopping Cart Specification Analysis & Equivalence Partitioning | [`hw06/docs/ai-transcripts/GEMINI-021.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-021.md) |
| **GEMINI-022** | 2026-09-02T16:54:22+07:00 | Phase 6 | GitHub Issues Clarification & Student Workflow Verification | [`hw06/docs/ai-transcripts/GEMINI-022.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-022.md) |
| **GEMINI-023** | 2026-09-02T16:55:50+07:00 | Phase 1 (FR-07) | Human-Review Correction Pass of Shopping Cart Specification Analysis | [`hw06/docs/ai-transcripts/GEMINI-023.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-023.md) |
| **GEMINI-024** | 2026-09-02T17:01:20+07:00 | Phase 1 (FR-07) | SEC Definitions Alignment, Contradiction Resolution & Grounded Calibration | [`hw06/docs/ai-transcripts/GEMINI-024.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-024.md) |
| **GEMINI-025** | 2026-09-02T20:11:40+07:00 | Phase 2 (FR-07) | AI Test Case Generation (38 Tests) & Worksheet Preparation | [`hw06/docs/ai-transcripts/GEMINI-025.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-025.md) |
| **GEMINI-026** | 2026-09-02T20:21:28+07:00 | Phase 2 (FR-07) | External AI Reference Review (ChatGPT) & Design Flaw Documentation | [`hw06/docs/ai-transcripts/GEMINI-026.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-026.md) |
| **GEMINI-027** | 2026-09-02T20:55:44+07:00 | Phase 3 (FR-07) | Human Audit Formalization & Reviewed Final Test Suite | [`hw06/docs/ai-transcripts/GEMINI-027.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-027.md) |
| **GEMINI-028** | 2026-09-02T21:09:49+07:00 | Phase 3 & 4 (FR-07) | Student Extensions Formalization, Postman Automation & Newman Execution | [`hw06/docs/ai-transcripts/GEMINI-028.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-028.md) |
| **GEMINI-029** | 2026-09-02T21:45:06+07:00 | Phase 4 (FR-07) | Human Evidence Verification & FR-07 Evidence Closure | [`hw06/docs/ai-transcripts/GEMINI-029.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-029.md) |
| **GEMINI-030** | 2026-09-02T21:51:52+07:00 | Phase 6 (FR-07) | Defect Closure, Push Readiness, GitHub Issues & Final FR-07 Sign-off | [`hw06/docs/ai-transcripts/GEMINI-030.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-030.md) |
| **GEMINI-031** | 2026-09-02T22:01:02+07:00 | Phase 6 (FR-07) / Phase 1 (FR-12) | FR-07 Evidence Complete & FR-12 Access Control Specification Analysis | [`hw06/docs/ai-transcripts/GEMINI-031.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-031.md) |
| **GEMINI-032** | 2026-09-02T22:17:30+07:00 | Phase 1 (FR-12) | Specification Analysis Calibration, Role & Coupon Reconciliation | [`hw06/docs/ai-transcripts/GEMINI-032.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-032.md) |
| **GEMINI-033** | 2026-09-02T22:22:27+07:00 | Phase 1 (FR-12) | Admin Success Status Calibration & Spec-Analysis Finalization | [`hw06/docs/ai-transcripts/GEMINI-033.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-033.md) |
| **GEMINI-034** | 2026-09-02T22:38:41+07:00 | Phase 2 (FR-12) | AI Test Case Generation (38 Tests) & Worksheet Preparation | [`hw06/docs/ai-transcripts/GEMINI-034.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-034.md) |
| **GEMINI-035** | 2026-09-02T22:56:23+07:00 | Phase 2 (FR-12) | Mechanical Consistency Correction & ChatGPT Review Packet Preparation | [`hw06/docs/ai-transcripts/GEMINI-035.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-035.md) |
| **GEMINI-036** | 2026-09-02T23:10:44+07:00 | Phase 2 (FR-12) | External AI Reference Review (ChatGPT) & Reference Audit Documentation | [`hw06/docs/ai-transcripts/GEMINI-036.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-036.md) |
| **GEMINI-037** | 2026-09-02T23:26:42+07:00 | Phase 3 (FR-12) | Human Audit Formalization & Reviewed Final Test Suite | [`hw06/docs/ai-transcripts/GEMINI-037.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-037.md) |
| **GEMINI-038** | 2026-09-02T23:32:36+07:00 | Phase 3 & 4 (FR-12) | Student Extensions Formalization, Postman Automation & Newman Execution | [`hw06/docs/ai-transcripts/GEMINI-038.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-038.md) |
| **GEMINI-039** | 2026-09-03T00:07:40+07:00 | Phase 4 & 6 (FR-12) | Real Evidence Verification, Defect Reporting & GitHub Issues Creation | [`hw06/docs/ai-transcripts/GEMINI-039.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-039.md) |
| **GEMINI-040** | 2026-09-03T00:30:17+07:00 | Phase 6 & 7 (FR-12) | GitHub Issue Screenshot Verification, Terminology Consistency & Safety Audit | [`hw06/docs/ai-transcripts/GEMINI-040.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-040.md) |
| **GEMINI-041** | 2026-09-03T01:03:00+07:00 | Phase 7 & Master | Master Excel, Master Postman, CI/CD Runs A & B, Agent Skill, and Submission Packaging | [`hw06/docs/ai-transcripts/GEMINI-041.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-041.md) |

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
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-010.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-010.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-011

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T13:39:28+07:00
- **Phase:** Phase 2 — Human Audit Phase (External Transcripts Setup, Compact Review Polish & Batch 1 Initiation)
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-010.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-011.md` (created with retrospective placeholder)
  - `hw06/docs/external-ai-transcripts/CHATGPT-001.md` (created)
  - `hw06/docs/external-ai-transcripts/CHATGPT-002.md` (created with verbatim external review)
  - `hw06/testcases/fr01/human-review-compact.md` (polished without text truncation)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-010.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-011.md`
  - `write_to_file hw06/docs/external-ai-transcripts/CHATGPT-001.md`
  - `write_to_file hw06/docs/external-ai-transcripts/CHATGPT-002.md`
  - `write_to_file hw06/testcases/fr01/human-review-compact.md`
- **Git Actions:** None (Commit deferred until all 38 human reviews are complete).
- **Human Checkpoint:** Checkpoint 2B — Student Human Audit in Progress (Batch 1 / 8).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-011.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-011.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-011.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-011.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-012

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T13:46:21+07:00
- **Phase:** Phase 2 — Student Human Audit Execution (All 38 FR-01 Cases Reviewed)
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-011.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-012.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/human-audit.md` (populated with all 38 verified student verdicts)
  - `hw06/testcases/fr01/human-review-compact.md` (updated with student decisions)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-011.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-012.md`
  - `write_to_file hw06/testcases/fr01/human-audit.md`
  - `write_to_file hw06/testcases/fr01/human-review-compact.md`
  - `python3 -c "..."` (validated 38 rows, non-empty reasoning, corrections, review timestamps, generated-ai-original.md unchanged)
  - `git status`
- **Git Actions:** None (Commit deferred pending student review and confirmation).
- **Human Checkpoint:** Checkpoint 2C — Student Human Audit Complete (38/38 Reviewed; Awaiting confirmation to commit).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-012.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-012.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-012.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-012.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-013

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T13:50:14+07:00
- **Phase:** Phase 2 Completion & Local Commit of Student Human Audit
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-012.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-013.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/human-audit.md` (committed with 38 student verdicts)
  - `hw06/testcases/fr01/human-review-compact.md` (committed with 38 student verdicts)
  - `hw06/docs/external-ai-transcripts/CHATGPT-001.md` (committed)
  - `hw06/docs/external-ai-transcripts/CHATGPT-002.md` (committed)
  - `hw06/docs/ai-audit.md` (updated & committed)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-012.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-013.md`
  - `git add hw06/`
  - `git commit -m "test(fr01): complete student audit of AI-generated registration tests"`
  - `git status`
- **Git Actions:** Executed local commit on branch `main` (`test(fr01): complete student audit of AI-generated registration tests`).
- **Human Checkpoint:** Phase 2 Complete (Student human audit committed locally). Ready for Phase 3 preparation.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-013.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-013.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-013.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-013.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-014

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T13:54:44+07:00
- **Phase:** Phase 3A — Reviewed AI Final Set Creation & Student Extension Blank Template Setup
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-013.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-014.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/reviewed-ai-final.md` (created with all 38 reviewed and corrected cases)
  - `hw06/testcases/fr01/student-extensions.md` (created with empty student templates and ineligible gap banner)
  - `hw06/docs/ai-audit.md` (updated & committed)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-013.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-014.md`
  - `write_to_file hw06/testcases/fr01/student-extensions.md`
  - `write_to_file hw06/testcases/fr01/reviewed-ai-final.md`
  - `python3 -c "..."` (validated 38 reviewed test cases, counts, SEC-01 oracle, FR01-AI-019 redesign, and empty student templates)
  - `git add hw06/`
  - `git commit -m "test(fr01): apply human audit corrections to registration tests"`
  - `git status`
- **Git Actions:** Executed local commit on branch `main` (`test(fr01): apply human audit corrections to registration tests`).
- **Human Checkpoint:** Checkpoint 3A — Human Gate: Student Must Provide 5 Original Test Ideas.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-014.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-014.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-014.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-014.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-015

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T14:08:03+07:00
- **Phase:** Phase 3B — Student-Selected Registration Extension Tests Formalization
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-014.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-015.md` (created with retrospective placeholder)
  - `hw06/testcases/fr01/student-extensions.md` (formalized 5 student-selected extension tests)
  - `hw06/docs/ai-audit.md` (updated & committed)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-014.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-015.md`
  - `write_to_file hw06/testcases/fr01/student-extensions.md`
  - `python3 -c "..."` (validated 5 distinct tests, truthful provenance, and automation readiness)
  - `git add hw06/`
  - `git commit -m "test(fr01): formalize selected registration extension tests"`
  - `git status`
- **Git Actions:** Executed local commit on branch `main` (`test(fr01): formalize selected registration extension tests`).
- **Truthful Authorship & Provenance Record:** The 5 test ideas formalized in this step were originally surfaced during AI brainstorming, selected and confirmed by the student, and mechanically formalized by Gemini. In strict adherence to course academic integrity requirements, they are recorded as student-selected rather than invented from scratch.
- **Human Checkpoint:** Phase 3B Complete (Extension tests formalized and committed locally). Ready for Postman Automation.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-015.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-015.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-015.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-015.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-016

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T14:11:56+07:00
- **Phase:** Phase 4 & Phase 5 — FR-01 Postman Automation, Local SUT Startup & Real Newman Execution
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-015.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-016.md` (created with retrospective placeholder)
  - `hw06/postman/collections/fr01-registration.postman_collection.json` (created with 42 API requests)
  - `hw06/postman/environments/eshop-local.postman_environment.json` (created)
  - `hw06/postman/scripts/generate_collection.py` (created)
  - `hw06/postman/scripts/validate_collection.py` (created)
  - `hw06/postman/scripts/verify-sec01-plaintext.js` (created)
  - `hw06/postman/README.md` (created)
  - `hw06/docs/postman-features.md` (created)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-015.md`
  - `write_to_file hw06/docs/ai-transcripts/GEMINI-016.md`
  - `python3 hw06/postman/scripts/generate_collection.py`
  - `python3 hw06/postman/scripts/validate_collection.py`
  - `node hw06/postman/scripts/verify-sec01-plaintext.js`
  - `npx -y -p newman -p newman-reporter-htmlextra newman run ...`
- **Git Actions:** Executed local commits on branch `main` (`test(fr01): add Postman automation for registration suite`, followed by `test(fr01): record real registration test execution`).
- **Human Checkpoint:** Checkpoint 5A — Human Screenshot Gate (Student must capture real Postman Console screenshot).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-016.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-016.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-016.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-016.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-017

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T14:28:33+07:00
- **Phase:** Environment Support — Process Termination & Port Management
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-017.md` (created)
- **Commands Executed:**
  - `manage_task Action="list"`
  - `manage_task Action="kill" TaskId="task-550"`
  - `kill -9 52187 2>/dev/null || true; lsof -i :3000 || true`
  - `lsof -i :3000 || true`
- **Result:** SUT backend process terminated and port 3000 released for student's concurrent HW05 session.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-017.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-017.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-017.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-017.md)

---

### Interaction GEMINI-018

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T15:57:48+07:00
- **Phase:** Phase 5 & 6 — Session Resumption: SUT Relaunch, Human Screenshot Guidance & GitHub Issues Defect Filing
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-016.md` (finalized with complete verbatim response)
  - `hw06/docs/ai-transcripts/GEMINI-017.md` (created)
  - `hw06/docs/ai-transcripts/GEMINI-018.md` (created with retrospective placeholder)
  - `hw06/docs/ai-audit.md` (updated)
- **Commands Executed:**
  - `ls -la hw06/screenshots/`
  - `lsof -i :3000 || true`
- **Human Checkpoint:** Checkpoint 5A — Human Screenshot Evidence (`hw06/screenshots/fr01-x-student-id.png`).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-018.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-018.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-018.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-018.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-019

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T16:00:33+07:00
- **Phase:** Phase 5 — SUT Server Relaunch & Postman Console Screenshot Guidance
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-019.md` (created)
- **Commands Executed:**
  - `lsof -i :3000 || true`
  - `node server.js` (background daemon `task-643`)
  - `curl -s -i http://localhost:3000/api/register ...`
- **Result:** SUT server verified live on port 3000; detailed instructions provided for Postman Console header capture.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-019.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-019.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-019.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-019.md)

---

### Interaction GEMINI-020

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T16:33:27+07:00
- **Phase:** Phase 5 & 6 — Screenshot Verification, Defect Documentation & GitHub Issues #1..#5 Created
- **Files Affected:**
  - `hw06/screenshots/fr01-x-student-id.jpg` / `.png` (human evidence verified)
  - `hw06/MANUAL_TODO.md` (updated)
  - `hw06/bugs/DEF-FR01-01.md` through `DEF-FR01-05.md` (created)
  - `hw06/bugs/README.md` (created)
- **Commands Executed:**
  - `view_file hw06/screenshots/fr01-x-student-id.jpg` (verified authentic Postman Console view)
  - `gh issue create ...` (created Issues #1, #2, #3, #4, #5 on GitHub)
- **Git Actions:** Executed commits `8439f1f`, `7f7c771`, and `9f8c6cf`.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-020.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-020.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-020.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-020.md)

---

### Interaction GEMINI-021

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T16:47:27+07:00
- **Phase:** Phase 1 (FR-07) — Shopping Cart Specification Analysis & Equivalence Partitioning
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-021.md` (created with retrospective placeholder)
  - `hw06/testcases/fr07/spec-analysis.md` (created)
  - `hw06/testcases/fr07/coverage-matrix.md` (created)
  - `hw06/docs/ai-audit.md` (updated)
- **Human Checkpoint:** Checkpoint 1 (FR-07) — Student Human Review of Shopping Cart Specification Analysis.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-021.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-021.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-021.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-021.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-022

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T16:54:22+07:00
- **Phase:** Phase 6 — GitHub Issues Clarification & Student Workflow Verification
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-022.md` (created)
- **Result:** Clarified that Issues #1 through #5 were automatically filed on `giabaocode/23127027-HW06-API-Testing` via GitHub CLI; student only needs to capture optional browser screenshots for `hw06/bugs/evidence/`.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-022.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-022.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-022.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-022.md)

---

### Interaction GEMINI-023

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T16:55:50+07:00
- **Phase:** Phase 1 (FR-07) — Human-Review Corrections & Specification Analysis Calibration
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-022.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-023.md` (created with retrospective placeholder)
  - `hw06/testcases/fr07/spec-analysis.md` (corrected and updated)
  - `hw06/testcases/fr07/coverage-matrix.md` (corrected and updated)
  - `hw06/submission-checklist.md` (updated with verified X-Student-Id evidence)
  - `hw06/docs/ai-audit.md` (updated)
- **Factually Recorded AI Mistakes Corrected by Human Review:**
  1. *Invented Overflow Boundary:* AI initially labeled $q = 10^9$ as an "overflow boundary"; corrected to `ROBUSTNESS / UNKNOWN UPPER BOUND` because no maximum numeric bound is specified.
  2. *Misclassifying In-Memory Storage as Defect:* AI initially suggested in-memory storage was a potential bug; corrected to `IMPLEMENTATION DETAIL — NOT A REQUIREMENT` because specification contains no persistence requirement.
  3. *Overstating Exact Status Codes:* AI initially labeled 401/403 as specified; corrected to `INFERRED FROM MIDDLEWARE` because exact status codes are omitted from specification text.
  4. *Overstating Inferred Field Rules:* AI initially treated catalog price/ID lookup as specified contract rules; corrected to `ROBUSTNESS / INTEGRITY PROBES` because product fields are derived solely from JSON examples.
- **Human Checkpoint:** Checkpoint 1B (FR-07) — Student Human Review of Corrected Shopping Cart Specification Analysis.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-023.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-023.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-023.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-023.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-024

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T17:01:20+07:00
- **Phase:** Phase 1 (FR-07) — SEC Definitions Alignment, Contradiction Resolution & Grounded Calibration
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-023.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-024.md` (created with retrospective placeholder)
  - `hw06/testcases/fr07/spec-analysis.md` (fully updated & grounded)
  - `hw06/testcases/fr07/coverage-matrix.md` (fully updated & grounded)
  - `hw06/docs/ai-audit.md` (updated)
- **Factually Recorded AI Errors & Contradictions Corrected:**
  1. *Critical SEC Numbering Error:* AI previously erroneously mapped `Authorization: Bearer <token>` to `SEC-07` (which is actually password reset OTP) instead of `SEC-02` (`Các API có tính bảo mật phải yêu cầu JWT Token hợp lệ`). Rebuilt the security matrix strictly against official `SEC-01` through `SEC-07` definitions (`README.md` Lines 276–285).
  2. *Misattributed User Cart Isolation:* AI previously labeled user isolation as "INFERRED FROM SEC-07". Corrected to **`INFERRED FROM AUTHENTICATED-USER CART SEMANTICS & SEC-02`** because `README.md` does not contain explicit isolation text and SEC-07 is unrelated.
  3. *Cross-Feature Price Rule Contradiction:* AI previously claimed `price > 0` was `SPECIFIED` for FR-07 by conflating it with `FR-15` (Product CRUD Line 196: *"Giá: bắt buộc, phải là số dương (> 0)"*). Official repository inspection confirms FR-07 contains no textual price rule; `price` appears solely in the JSON example, making negative price testing a **`ROBUSTNESS / SECURITY PROBE`** rather than a contract violation.
  4. *Quantity String Typing Clarification:* Clarified that while the semantic domain is strictly positive integer $\ge 1$ (`SPECIFIED`), string representations like `$q="2"` are non-integer types whose coercion vs rejection behavior is classified as `TYPE ROBUSTNESS / CHARACTERIZATION`.
- **Human Checkpoint:** Checkpoint 1B (FR-07) — Final Grounded Verification & Execution of Local Correction Commit.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-024.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-024.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-024.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-024.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-025

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T20:11:40+07:00
- **Phase:** Phase 2 (FR-07) — AI Test Case Generation (38 Tests) & Worksheet Preparation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-024.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-025.md` (created with retrospective placeholder)
  - `hw06/testcases/fr07/generated-ai-original.md` (created: exactly 38 test cases)
  - `hw06/testcases/fr07/human-audit.md` (created: 38 rows with student fields blank)
  - `hw06/testcases/fr07/human-review-compact.md` (created: 38 rows with student fields blank)
  - `hw06/docs/ai-audit.md` (updated)
- **Result:** Successfully allocated 38 test cases across the 24 reviewed Coverage IDs, generated `generated-ai-original.md`, prepared blank human audit worksheets, programmatically validated all 13 quality rules, and committed locally in `test(fr07): generate 38 AI cart test cases`.
- **Human Checkpoint:** Checkpoint 2 (FR-07) — Student Human Audit Required.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-025.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-025.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-025.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-025.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-026

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T20:21:28+07:00
- **Phase:** Phase 2 (FR-07) — External AI Reference Review (ChatGPT) & Design Flaw Documentation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-025.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-026.md` (created with retrospective placeholder)
  - `hw06/docs/external-ai-transcripts/CHATGPT-003.md` (created)
  - `hw06/testcases/fr07/ai-reference-audit.md` (created)
  - `hw06/docs/ai-audit.md` (updated)
- **External AI Critique Summary:**
  - Source: ChatGPT (OpenAI) supplied by student as external reference material.
  - Distribution: **23 VALID / 15 INCOMPLETE / 0 INVALID (Total: 38)**.
  - Factual AI Flaws Recorded:
    1. `AI-ERR-FR07-STATUS-ORACLE`: Internal oracle contradiction where exact failure status was noted as UNKNOWN by spec, but assertions required `status != 200` or `400 Bad Request expected`.
    2. `AI-ERR-FR07-ERROR-ENVELOPE`: Hard-coding `{ error: 'Forbidden' }` when error response body schema is officially unspecified.
- **Academic Integrity Guard:** `generated-ai-original.md` remains 100% immutable; all student fields in `human-audit.md` and `human-review-compact.md` remain strictly blank.
- **Human Checkpoint:** Checkpoint 2A (FR-07) — Student Final Review & Audit Decision.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-026.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-026.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-026.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-026.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-027

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T20:55:44+07:00
- **Phase:** Phase 3 (FR-07) — Human Audit Formalization & Reviewed Final Test Suite
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-026.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-027.md` (created with retrospective placeholder)
  - `hw06/testcases/fr07/human-audit.md` (populated: 38 rows with student adopted decisions)
  - `hw06/testcases/fr07/human-review-compact.md` (populated: 38 rows)
  - `hw06/testcases/fr07/reviewed-ai-final.md` (created: 38 tests with 15 calibrations applied)
  - `hw06/testcases/fr07/student-extensions.md` (created: 5 blank template slots)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - The initial critique and correction suggestions originated from ChatGPT external reference review (`CHATGPT-003`).
  - Student personally reviewed, validated, and formally adopted the final 23 VALID / 15 INCOMPLETE / 0 INVALID decisions.
  - Gemini mechanically populated the audit worksheets and constructed the calibrated final test suite `reviewed-ai-final.md`.
- **Integrity Status:** `generated-ai-original.md` remains 100% byte-for-byte unchanged.
- **Human Checkpoint:** Human Gate — FR-07 Student Extension Ideas.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-027.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-027.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-027.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-027.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-028

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T21:09:49+07:00
- **Phase:** Phase 3 & Phase 4 (FR-07) — Student Extensions Formalization, Postman Automation & Newman Execution
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-027.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-028.md` (created with retrospective placeholder)
  - `hw06/testcases/fr07/student-extensions.md` (formalized: 5 student-selected extensions)
  - `hw06/postman/fr07/` (Postman collection & environment for FR-07)
  - `hw06/newman/fr07/` (Newman CLI & HTML reports)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Provenance Statement:**
  - The 5 student extension ideas (`FR07-STU-001` through `005`) were surfaced during external AI brainstorming and selected and confirmed by the student (`Student Selection: CONFIRMED`).
  - Gemini performed mechanical specification formalization, Postman script authoring, and Newman execution orchestration.
- **Human Checkpoint:** Postman Console Screenshot Evidence Required.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-028.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-028.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-028.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-028.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-029

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T21:45:06+07:00
- **Phase:** Phase 4 (FR-07) — Human Evidence Verification & FR-07 Evidence Closure
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-028.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-029.md` (created with retrospective placeholder)
  - `hw06/screenshots/fr07-x-student-id.jpg` (verified real Postman Console screenshot)
  - `hw06/screenshots/fr07-x-student-id.png` (synchronized image)
  - `hw06/MANUAL_TODO.md` (checked off FR-07 screenshot)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - The student personally executed the Postman request against the live local SUT (`http://localhost:3000/api/cart`), expanded the Postman Console, and captured authentic screenshot evidence visibly demonstrating `X-Student-Id: "23127027"` and real `200 OK` response.
  - Zero synthetic or mock image generation occurred.
- **Human Checkpoint:** Checkpoint 4 (FR-07) — COMPLETED.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-029.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-029.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-029.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-029.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-030

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T21:51:52+07:00
- **Phase:** Phase 6 (FR-07) — Defect Closure, Push Readiness, GitHub Issues & Final FR-07 Sign-off
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-029.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-030.md` (created with retrospective placeholder)
  - `hw06/bugs/fr07/` (formal defect reports created)
  - `hw06/bugs/README.md` (indexed with live GitHub issue links)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Gemini verified real execution artifacts, performed repository safety analysis, pushed legitimate commits to GitHub origin, and orchestrated defect documentation.
  - Zero fabricated results or synthetic screenshots.
- **Human Checkpoint:** Human Gate — GitHub Issue Screenshot.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-030.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-030.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-030.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-030.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-031

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T22:01:02+07:00
- **Phase:** Phase 6 (FR-07) Closure & Phase 1 (FR-12) Access Control Specification Analysis
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-030.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-031.md` (created with retrospective placeholder)
  - `hw06/screenshots/fr07-bug-issue-001.png` (verified real browser screenshot)
  - `hw06/bugs/fr07/FR07-BUG-002-missing-quantity-validation.md` (calibrated expected oracle)
  - `hw06/bugs/DEF-FR07-02.md` (calibrated expected oracle)
  - GitHub Issue #7 (body calibrated on remote)
  - `hw06/MANUAL_TODO.md` (updated)
  - `hw06/submission-checklist.md` (updated)
  - `hw06/testcases/fr12/spec-analysis.md` (Phase 1 specification analysis)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - The student personally captured and placed the real GitHub browser screenshot for Issue #6.
  - Gemini verified the file, updated GitHub Issue #7 contract oracle, synchronized documentation, and conducted Phase 1 specification analysis for Pool C Feature FR-12.
- **Human Checkpoint:** Checkpoint 1 (FR-12) — Specification Analysis Review.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-031.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-031.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-031.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-031.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-032

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T22:17:30+07:00
- **Phase:** Phase 1 (FR-12) — Specification Analysis Calibration, Role & Coupon Reconciliation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-031.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-032.md` (created with retrospective placeholder)
  - `hw06/testcases/fr12/spec-analysis.md` (reconciled role, coupon scope, candidate bugs, and side-effect assertions)
  - `hw06/testcases/fr12/coverage-matrix.md` (rebuilt with real endpoints and exact role `user`)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Student identified three source discrepancies in initial FR-12 analysis: (1) normal-user role value (`user` vs `customer`), (2) coupon endpoint scope clarification, (3) missing category-mutation static candidate (`CAND-FR12-03`).
  - Gemini verified the real SUT source code (`backend/server.js`), reconciled specifications, documented factual AI error, and produced corrected Phase 1 analysis.
- **Human Checkpoint:** Checkpoint 1 (FR-12) — Specification Analysis Review (Correction Pass).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-032.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-032.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-032.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-032.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-033

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T22:22:27+07:00
- **Phase:** Phase 1 (FR-12) — Admin Success Status Calibration & Spec-Analysis Finalization
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-032.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-033.md` (created with retrospective placeholder)
  - `hw06/testcases/fr12/spec-analysis.md` (decoupled generic REST success from formal access-control oracle; added exact handler line citation for `GET /api/coupons`)
  - `hw06/testcases/fr12/coverage-matrix.md` (calibrated admin positive cases to test access-control layer clearance)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Gemini verified all 14 target operations against `api_specification.md`, classified documented vs implementation success status codes, cited exact line 356 for `GET /api/coupons` static candidate, and recorded the engineering lesson in the AI error register.
- **Human Checkpoint:** Checkpoint 1 (FR-12) — Specification Analysis Final Calibration.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-033.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-033.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-033.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-033.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-034

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T22:38:41+07:00
- **Phase:** Phase 2 (FR-12) — AI Test Case Generation (38 Tests) & Worksheet Preparation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-033.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-034.md` (created with retrospective placeholder)
  - `hw06/testcases/fr12/generated-ai-original.md` (generated 38 original AI test cases, immutable)
  - `hw06/testcases/fr12/human-audit.md` (blank 38-row audit worksheet)
  - `hw06/testcases/fr12/human-review-compact.md` (blank 38-row review worksheet)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Gemini generated exactly 38 AI test cases mapped to the 14 real exposed FR-12 operations and prepared blank human audit worksheets.
  - Zero Postman/Newman executions performed; all student audit fields left completely blank.
- **Human Checkpoint:** Checkpoint 2 (FR-12) — Human Audit Required.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-034.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-034.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-034.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-034.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-035

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T22:56:23+07:00
- **Phase:** Phase 2 (FR-12) — Mechanical Consistency Correction & ChatGPT Review Packet Preparation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-034.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-035.md` (created with retrospective placeholder)
  - `hw06/testcases/fr12/chatgpt-review-packet.md` (created 38-test external review packet for second AI)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance & Factual Generation Consistency Observations:**
  - **SEC-02 Summary Count Correction:** The GEMINI-034 turn summary inadvertently stated: *"SEC-02 (Authentication Required): 10 Test Cases (FR12-AI-029 .. FR12-AI-036)"*. This was a mathematical calculation error. `FR12-AI-029` through `FR12-AI-036` inclusive contains **8 test cases**, not 10. Direct negative `SEC-02` tests are exactly 8 (6 anonymous callers + 1 expired JWT + 1 forged signature).
  - **Token-Validity Allocation Mismatch Observation:** The initial 4-case token robustness bucket (`FR12-AI-035` .. `FR12-AI-038`) contains only two cryptographic/token-validity tests (`FR12-AI-035` expired JWT, `FR12-AI-036` forged signature). The remaining two (`FR12-AI-037` missing role claim, `FR12-AI-038` uppercase role `'ADMIN'`) possess valid cryptographic signatures and are strictly `SEC-03` role-claim authorization probes. Total `SEC-03` tests are therefore 16 ($14 \text{ standard users} + 2 \text{ role-claim probes}$).
  - **Immutable Original Artifact Verification:** `hw06/testcases/fr12/generated-ai-original.md` was verified byte-for-byte identical to local commit `6b50faa`.
  - **External Review Packet Prepared:** `hw06/testcases/fr12/chatgpt-review-packet.md` was generated with 38 neutral test sections containing zero pre-baked verdicts or hints to enable independent evaluation by a second AI (ChatGPT).
- **Human Checkpoint:** Checkpoint 2A (FR-12) — External AI Review Packet Ready.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-035.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-035.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-035.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-035.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-036

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T23:10:44+07:00
- **Phase:** Phase 2 (FR-12) — External AI Reference Review (ChatGPT) & Reference Audit Documentation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-035.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-036.md` (created with retrospective placeholder)
  - `hw06/docs/external-ai-transcripts/CHATGPT-004.md` (created verbatim ChatGPT review transcript)
  - `hw06/testcases/fr12/ai-reference-audit.md` (created external AI reference audit)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Student supplied an independent external second-AI review from ChatGPT across all 38 original FR-12 AI test cases.
  - Distribution recorded: 28 VALID, 10 INCOMPLETE, 0 INVALID (Total: 38).
  - Prominent warning attached clarifying that this document represents external AI reference material and does NOT constitute the student's human audit.
  - Original AI test set `hw06/testcases/fr12/generated-ai-original.md` remained strictly immutable and byte-for-byte unchanged.
  - Student audit worksheet `hw06/testcases/fr12/human-audit.md` student fields remained 100% blank.
- **Human Checkpoint:** Checkpoint 2B (FR-12) — Final Human Audit Decision Pending.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-036.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-036.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-036.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-036.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-037

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T23:26:42+07:00
- **Phase:** Phase 3 (FR-12) — Human Audit Formalization & Reviewed Final Test Suite
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-036.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-037.md` (created with retrospective placeholder)
  - `hw06/testcases/fr12/human-audit.md` (populated with student-adopted verdicts and reasoning)
  - `hw06/testcases/fr12/human-review-compact.md` (updated with concise review decisions)
  - `hw06/testcases/fr12/reviewed-ai-final.md` (created reviewed final test suite applying 10 corrections)
  - `hw06/testcases/fr12/student-extensions.md` (created blank 5-slot template for student extensions)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Student reviewed the 38 original AI test cases together with the external ChatGPT critique and adopted the final distribution: 28 VALID, 10 INCOMPLETE, 0 INVALID.
  - For the 10 INCOMPLETE cases, student adopted the corrections documented in `ai-reference-audit.md`.
  - Gemini mechanically populated `human-audit.md`, updated `human-review-compact.md`, formalized `reviewed-ai-final.md`, and prepared blank template `student-extensions.md`.
  - `generated-ai-original.md` remained strictly immutable and byte-for-byte unchanged.
- **Human Checkpoint:** Human Gate — FR-12 Extension Ideas (Student to select 5 extension ideas).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-037.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-037.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-037.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-037.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-038

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-02T23:32:36+07:00
- **Phase:** Phase 3 & 4 (FR-12) — Student Extensions Formalization, Postman Automation & Newman Execution
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-037.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-038.md` (created with retrospective placeholder)
  - `hw06/testcases/fr12/student-extensions.md` (formalized 5 student extensions `FR12-STU-001` .. `FR12-STU-005`)
  - `hw06/postman/scripts/seed_fr12_fixtures.js` (created disposable test fixtures seed script)
  - `hw06/postman/scripts/generate_fr12_environment.js` (created token & environment generator)
  - `hw06/postman/environments/fr12-environment.json` (generated execution environment)
  - `hw06/postman/scripts/generate_fr12_collection.py` (created collection builder)
  - `hw06/postman/collections/fr12-access-control.postman_collection.json` (automated 43 testcase designs across 59 requests)
  - `hw06/newman/fr12/fr12-cli-output.txt` (real execution CLI output log)
  - `hw06/newman/fr12/fr12-report.html` (real execution HTML dashboard export, 1.3 MB)
  - `hw06/docs/fr12-execution-report.md` (formal execution report and failure triage)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Student selected 5 extension ideas from AI brainstorming (`FR12-STU-001` .. `FR12-STU-005`); student selection confirmed.
  - Zero duplication against the 38 reviewed AI tests verified programmatically.
  - SUT executed in Newman: 59 requests executed, 187 assertions (148 passed, 39 failed).
  - 100% of the 39 failures were triaged and confirmed as genuine **RUNTIME-CONFIRMED SUT DEFECTS** across 4 vulnerability groups (`DEF-FR12-01`, `DEF-FR12-02`, `DEF-FR12-03`, `DEF-FR12-04`).
  - `generated-ai-original.md` remained strictly immutable and byte-for-byte unchanged.
- **Human Checkpoint:** Phase 4 Real Execution Complete; Human action required for manual Postman Console evidence.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-038.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-038.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-038.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-038.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-039

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-03T00:07:40+07:00
- **Phase:** Phase 4 & 6 (FR-12) — Real Evidence Verification, Defect Reporting & GitHub Issues Creation
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-038.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-039.md` (created with retrospective placeholder)
  - `hw06/screenshots/fr12-x-student-id.png` (and `.jpg`, verified authentic student screenshot from Postman Desktop)
  - `hw06/bugs/DEF-FR12-01.md` (created defect report for Issue #8)
  - `hw06/bugs/DEF-FR12-02.md` (created defect report for Issue #9)
  - `hw06/bugs/DEF-FR12-03.md` (created defect report for Issue #10)
  - `hw06/bugs/DEF-FR12-04.md` (created defect report for Issue #11)
  - `hw06/bugs/README.md` (updated bug index with FR-12 section)
  - `hw06/docs/fr12-execution-report.md` (updated with evidence and live issue links)
  - `hw06/MANUAL_TODO.md` (updated human register with completed FR-12 audit, extensions, screenshot, and bug filing)
  - `hw06/submission-checklist.md` (updated checklist rows 12, 17, and Gate 1)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Student captured authentic Postman Console screenshot `hw06/screenshots/fr12-x-student-id.png` showing `FR12-AI-015`, expanded Request Headers, and `X-Student-Id: 23127027`.
  - 4 runtime-confirmed defects from real Newman execution were grouped and formalized without fabricating any unconfirmed vulnerabilities.
  - 4 real GitHub Issues (#8, #9, #10, #11) were automatically created via GitHub CLI on `giabaocode/23127027-HW06-API-Testing`.
  - Human Gate preserved for authentic browser screenshot of live GitHub Issue #8.
- **Human Checkpoint:** Human Gate — FR-12 GitHub Issue Browser Screenshot (Student to capture browser screenshot of Issue #8 at `hw06/screenshots/fr12-bug-issue-001.png`).

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-039.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-039.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-039.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-039.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-040

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-03T00:30:17+07:00
- **Phase:** Phase 6 & 7 (FR-12) — GitHub Issue Screenshot Verification, Terminology Consistency & Safety Audit
- **Files Affected:**
  - `hw06/docs/ai-transcripts/GEMINI-039.md` (finalized)
  - `hw06/docs/ai-transcripts/GEMINI-040.md` (created with retrospective placeholder)
  - `hw06/screenshots/fr12-bug-issue-001.png` (and `.jpg`, verified authentic browser screenshot of live GitHub Issue #8)
  - `hw06/bugs/DEF-FR12-01.md`, `DEF-FR12-02.md`, `DEF-FR12-03.md`, `DEF-FR12-04.md` (corrected role terminology to `role = 'user'` / standard user)
  - `hw06/docs/fr12-execution-report.md` (updated with issue screenshot)
  - `hw06/MANUAL_TODO.md` (marked 5.3 FR-12 issue screenshot complete)
  - `hw06/submission-checklist.md` (marked bug reporting deliverable #12 fully complete across all 3 features)
  - `hw06/docs/ai-audit.md` (updated)
- **Truthful Audit Provenance:**
  - Student captured authentic browser screenshot `hw06/screenshots/fr12-bug-issue-001.png` showing live GitHub Issue #8.
  - SUT terminology rigorously reconciled: non-admin user role in database/tokens is strictly `role = 'user'`, never "customer".
  - Full pre-push safety scan executed across repository to ensure zero leaked credentials, tokens, or untracked PDFs.
- **Human Checkpoint:** FR-12 Fully Sealed; Repository Safe to Push.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-040.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-040.md)

#### Verbatim AI Output
*Full conversational response preserved in:* [`hw06/docs/ai-transcripts/GEMINI-040.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-040.md) (Finalized via retrospective logging).

---

### Interaction GEMINI-041

- **AI Tool / Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Date & Time:** 2026-09-03T01:03:00+07:00
- **Phase:** Phase 7 & Master Packaging — Master Excel (129 rows), Master Postman Collection, CI/CD Runs A & B, Agent Skill, Reports
- **Files Affected:**
  - `hw06/testcases/testcases-master.xlsx` (129 certified logical test cases across 7 sheets)
  - `hw06/postman/eshop-hw06-collection.json` (master collection with central `X-Student-Id` injection)
  - `hw06/docs/postman-features.md` (comprehensive engineering inventory)
  - `.github/workflows/api-tests.yml` (automated CI/CD pipeline with Run A and Run B)
  - `hw06/docs/cicd-report.md` (documented real Run A `33665114685` and Run B `33665296154`)
  - `hw06/agent-skill/design-decisions.md`, `pseudocode.md`, `test_generator.py` (functional CLI generator), `student-diagram-checklist.md`
  - `hw06/docs/ai-critique.md` (252-word critical reflection grounded in project errors)
  - `hw06/docs/oral-defense-notes.md` (11 core examination Q&As)
  - `hw06/docs/main-report.md` (master comprehensive testing report)
  - `hw06/README.md` (repository navigation & self-assessment table)
  - `hw06/docs/git-commit-log.txt` (clean text commit history)
  - `hw06/submission-checklist.md` & `hw06/MANUAL_TODO.md` (updated)
- **Truthful Audit Provenance:**
  - Complete mathematical reconciliation verified: $43 + 43 + 43 = 129$ logical test case designs.
  - Zero specification assertions weakened or inverted. CI/CD Run A verified real passing health suite (34 assertions passed). Run B verified isolated deliberate failure detection (Newman exit code 1).
  - Human Gate preserved for student-drawn diagram (`student-diagram.png`) and real CI/CD browser screenshots.
- **Human Checkpoint:** CI/CD Execution Verified; Human Action Required for physical screenshots and hand-drawn diagram.

#### Exact Student Prompt
*See verbatim text preserved in:* [`hw06/docs/ai-transcripts/GEMINI-041.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-041.md)

#### Verbatim AI Output
*Conversational response status:* `[VERBATIM AI RESPONSE TO BE FINALIZED AT NEXT INTERACTION]` (Preserved in [`GEMINI-041.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-transcripts/GEMINI-041.md) via retrospective logging).

---

## 3. Previous / External AI Interactions — Dedicated External Transcripts

> [!IMPORTANT]
> **Auditability Requirement for External AI Interactions:** As required by the official course guidelines, external AI prompts and outputs must be fully auditable rather than represented merely by narrative summaries. Detailed external interaction transcripts are maintained in [`hw06/docs/external-ai-transcripts/`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/).

| # | Interaction ID | Date | AI Tool | Task / Topic | Student Prompt | AI Output Transcript | Purpose & Verification |
| :-: | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | **CHATGPT-001** | 2026-09-02 | ChatGPT (OpenAI) | Master Prompt Engineering & HW06 Setup | Formulated comprehensive instructions and constraints for Antigravity AI pair programming. | [`CHATGPT-001.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/CHATGPT-001.md)<br>*(Placeholder for exact historical text)* | Used to guide Phase 0 session initialization and policy compliance. |
| 2 | **CHATGPT-002** | 2026-09-02 | ChatGPT (OpenAI) | External Reference Review of FR-01 AI Test Cases | Student provided 38 AI-generated FR-01 test cases for independent second-AI critique. | [`CHATGPT-002.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/CHATGPT-002.md)<br>*(Verbatim transcript preserved)* | Preserved as reference material in `ai-reference-audit.md` for student cross-reference; student audit fields remain independent. |
| 3 | **CHATGPT-003** | 2026-09-02 | ChatGPT (OpenAI) | External Reference Review of FR-07 AI Test Cases | Student provided 38 AI-generated FR-07 test cases for independent second-AI critique. | [`CHATGPT-003.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/CHATGPT-003.md)<br>*(Verbatim transcript preserved)* | Preserved as reference material in `hw06/testcases/fr07/ai-reference-audit.md` for student cross-reference; student audit fields remain independent. |
| 4 | **CHATGPT-004** | 2026-09-02 | ChatGPT (OpenAI) | External Reference Review of FR-12 AI Test Cases | Student provided 38 AI-generated FR-12 test cases for independent second-AI critique. | [`CHATGPT-004.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/external-ai-transcripts/CHATGPT-004.md)<br>*(Verbatim transcript preserved)* | Preserved as reference material in `hw06/testcases/fr12/ai-reference-audit.md` for student cross-reference; student audit fields remain independent. |

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

