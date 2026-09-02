# HW06 Submission Checklist & Quality Gate (submission-checklist.md)

> **Student ID:** `23127027` | **GitHub:** `giabaocode`
> **Archive Name Format:** `23127027_HW06_AI_API_<SelfAssessedGrade>.zip`
> **Target Course:** Software Testing (Kiểm thử Phần mềm) — HCMUS
> **Exercise:** HW06 – API Testing (HW06-AI)

---

## 1. Feature Selection & Academic Integrity

- [x] **Pool A Selection:** FR-01 — Account Registration (`POST /api/register`)
- [x] **Pool B Selection:** FR-07 — Shopping Cart (`GET /api/cart`, `POST /api/cart`)
- [x] **Pool C Selection:** FR-12 — Access Control (Admin endpoints & data mutation endpoints)
- [x] **Group Deduplication Confirmed:** The student has personally verified that no other member in the study group selected the exact combination `FR-01 + FR-07 + FR-12`.
- [x] **PDF Authority Recognized:** Confirmed that `2026.HW06.API Testing_En.pdf` overrides any secondary prompt instructions.

---

## 2. Deliverables Matrix (PDF Section 14)

| # | Item Required by PDF | Target File Path | Current Status | Notes / Evidence |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Main Report (Markdown + PDF)** | `hw06/docs/main-report.md`<br>`hw06/docs/main-report.pdf` | **COMPLETED (Markdown)** | Comprehensive report covering FR-01, FR-07, FR-12 |
| 2 | **Public GitHub Repository Link** | `https://github.com/giabaocode/23127027-HW06-API-Testing` | **COMPLETED** | Verified public repository |
| 3 | **Postman Collection (`.json`)** | `hw06/postman/eshop-hw06-collection.json` | **COMPLETED** | Unified master collection with central `X-Student-Id` injection |
| 4 | **Newman HTML Report** | `hw06/newman/*/fr*-report.html` | **COMPLETED** | Authentic Newman execution reports for FR-01, FR-07, FR-12 |
| 5 | **List of Postman Features Used** | `hw06/docs/postman-features.md` | **COMPLETED** | Comprehensive engineering documentation of Postman features |
| 6 | **CI/CD Report (MD + PDF)** | `hw06/docs/cicd-report.md` | **COMPLETED (Markdown)** | Pipeline setup, real run IDs 33665114685 & 33665296154 |
| 7 | **CI/CD Run 1: All-Passing Evidence** | Screenshots & Links in report | **Run Executed (Screenshot Gate)** | Real run 33665114685 passed; screenshot pending student capture |
| 8 | **CI/CD Run 2: Failing Test Demo** | Screenshots & Links in report | **Run Executed (Screenshot Gate)** | Real run 33665296154 failed as intended; screenshot pending student capture |
| 9 | **Excel Test Cases & Summary** | `hw06/testcases/testcases-master.xlsx` | **COMPLETED** | Exactly 129 logical testcase rows across 7 styled sheets |
| 10 | **AI Test-Generator Diagram** | `hw06/agent-skill/student-diagram.png` | **Pending Human Drawing** | Checklist prepared; **Must be self-drawn by student** |
| 11 | **Agent Skill Pseudocode / Code** | `hw06/agent-skill/pseudocode.md`<br>`hw06/agent-skill/test_generator.py` | **COMPLETED** | Working Python generator CLI tested with sample inputs |
| 12 | **Bug Report with GitHub Issues** | `hw06/bugs/README.md`<br>`hw06/screenshots/fr07-bug-issue-001.png`<br>`hw06/screenshots/fr12-bug-issue-001.png` | **COMPLETED (FR-01, FR-07, FR-12)** | Real issues #1–#11 created on GitHub; FR-07 & FR-12 browser screenshots verified and committed |
| 13 | **AI Critique (200–300 words)** | `hw06/docs/ai-critique.md` | **COMPLETED (Draft for Review)** | Grounded in actual AI audit errors (252 words) |
| 14 | **AI Audit Report (Markdown + PDF)** | `hw06/docs/ai-audit.md`<br>`hw06/docs/ai-audit.pdf` | In Progress | Maintained through Turn 40 with verbatim transcripts |
| 15 | **Git Commit Log (Text file)** | `hw06/docs/git-commit-log.txt` | **COMPLETED** | Exported from authentic git history |
| 16 | **README.md (Self-Assessment Table)** | `hw06/README.md` | **COMPLETED** | Complete architecture, navigation, and self-assessment rubric |
| 17 | **Console Screenshot: `X-Student-Id`** | `hw06/screenshots/fr01-x-student-id.png`<br>`hw06/screenshots/fr07-x-student-id.png`<br>`hw06/screenshots/fr12-x-student-id.png` | **COMPLETED (FR-01, FR-07 & FR-12)** | Real Postman Console captures with student ID `23127027` verified and committed |
| 18 | *(Optional)* **OpenAPI Specification** | `hw06/api-spec/openapi.yaml` | Optional | Audited if generated |

---

## 3. Anti-AI-Cheat Quality Gates

- [x] **Gate 1: True X-Student-Id Evidence (FR-01, FR-07, FR-12)**
  - Confirmed: Header `X-Student-Id: 23127027` injected and verified in real terminal/Postman logs.
  - Authentic student screenshots provided and committed at `hw06/screenshots/fr01-x-student-id.png`, `hw06/screenshots/fr07-x-student-id.png`, and `hw06/screenshots/fr12-x-student-id.png`.
  - Zero synthetic screenshots used.
- [ ] **Gate 2: Authentic Newman Run**
  - Confirmed: Hostname is `localhost` / `127.0.0.1`.
  - Zero fabricated terminal logs or reports.
- [ ] **Gate 3: Self-Drawn Agent Skill Diagram**
  - Confirmed: Hand-drawn or self-constructed by student in diagramming tool (Draw.io, Excalidraw, etc.).
  - Zero AI-generated images or AI Mermaid rendering for the final architecture diagram.
- [ ] **Gate 4: Human-in-the-Loop Audit**
  - Confirmed: Every AI test case has `Student Verdict`, `Student Reasoning`, and `Student Correction` filled personally by the student.
  - No AI hints pre-filled.
- [ ] **Gate 5: Original Student Extension Tests**
  - Confirmed: At least 5 tests per feature authored solely by the student exploring gaps AI missed.

---

## 4. Final Packaging Verification

- [ ] Archive created: `23127027_HW06_AI_API_<SelfAssessedGrade>.zip`
- [ ] File size check: within Moodle upload limit.
- [ ] Archive integrity: extracts cleanly with identical structure.
- [ ] All required files present and non-empty.
- [ ] Moodle submission completed before deadline.
