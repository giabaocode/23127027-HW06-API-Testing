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

## 3. Previous / External AI Interactions — Student Must Add

> [!IMPORTANT]
> **Mandatory Action for Student (Pham Ngoc Gia Bao):** The prompt used to initiate this session was engineered using ChatGPT. As required by the course guidelines, please record that interaction (and any other external AI interactions) below with the exact prompt, date, tool name, and summary.

| # | Date & Time | AI Tool | Task / Topic | Student Prompt Summary | Summary of AI Output | How Output Was Used / Verified |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | *[Student to fill date]* | ChatGPT (OpenAI) | Prompt Engineering / HW06 Setup | Formulated comprehensive instructions and constraints for Antigravity AI pair programming. | Generated structured master prompt template with phase gating and anti-cheat rules. | Used to guide Phase 0 session initialization and policy compliance. |
| 2 | *[Student to fill if any]* | | | | | |

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
