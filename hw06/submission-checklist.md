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
| 1 | **Main Report (Markdown + PDF)** | `hw06/docs/main-report.md`<br>`hw06/docs/main-report.pdf` | Pending Phase 10 | Covers full pipeline for FR-01, FR-07, FR-12 |
| 2 | **Public GitHub Repository Link** | `https://github.com/giabaocode/23127027-HW06-API-Testing` | Configured | Verified in Git remotes |
| 3 | **Postman Collection (`.json`)** | `hw06/postman/eshop-hw06-collection.json` | Pending Phase 4 | Includes all test scripts and assertions |
| 4 | **Newman HTML Report** | `hw06/newman/newman-report.html` | Pending Phase 5 | Real execution against `localhost:3000` |
| 5 | **List of Postman Features Used** | `hw06/docs/postman-features.md` | Pending Phase 4 | Document variables, pre-request scripts, tests, etc. |
| 6 | **CI/CD Report (MD + PDF)** | `hw06/docs/cicd-report.md` | Pending Phase 7 | Pipeline setup, 2 runs, real URLs |
| 7 | **CI/CD Run 1: All-Passing Evidence** | Screenshots & Links in report | Pending Phase 7 | Real GitHub Actions URL & commit hash |
| 8 | **CI/CD Run 2: Failing Test Demo** | Screenshots & Links in report | Pending Phase 7 | Isolated demonstration commit with 1 failing test |
| 9 | **Excel Test Cases & Summary** | `hw06/testcases/testcases-master.xlsx` (or CSVs) | Pending Phase 3 | Formatted with human audit verdicts & traceability |
| 10 | **AI Test-Generator Diagram** | `hw06/agent-skill/student-diagram.png` | Pending Phase 8 | **Must be self-drawn by student** (NO AI generation) |
| 11 | **Agent Skill Pseudocode / Code** | `hw06/agent-skill/pseudocode.md`<br>`hw06/agent-skill/test_generator.py` | Pending Phase 8 | Code/pseudocode following student design decisions |
| 12 | **Bug Report with GitHub Issues** | `hw06/bugs/bug-report.md`<br>`hw06/bugs/evidence/*.png` | Pending Phase 6 | Genuine bugs with screenshots and GitHub issue links |
| 13 | **AI Critique (200–300 words)** | `hw06/docs/ai-critique.md` | Pending Phase 9 | Student reviewed and personalized |
| 14 | **AI Audit Report (Markdown + PDF)** | `hw06/docs/ai-audit.md`<br>`hw06/docs/ai-audit.pdf` | In Progress | Continuous maintenance with verbatim prompts |
| 15 | **Git Commit Log (Text file)** | `hw06/docs/git-commit-log.txt` | Pending Phase 10 | Generated from real `git log` |
| 16 | **README.md (Self-Assessment Table)** | `hw06/README.md` | Pending Phase 10 | Contains test summary and score breakdown (/100) |
| 17 | **Console Screenshot: `X-Student-Id`** | `hw06/screenshots/fr01-x-student-id.png` | **COMPLETED (FR-01)** | Real Postman Console capture with student ID `23127027` verified and committed (`8439f1f`) |
| 18 | *(Optional)* **OpenAPI Specification** | `hw06/api-spec/openapi.yaml` | Optional | Audited if generated |

---

## 3. Anti-AI-Cheat Quality Gates

- [x] **Gate 1: True X-Student-Id Evidence (FR-01)**
  - Confirmed: Header `X-Student-Id: 23127027` injected and verified in real terminal/Postman logs.
  - Authentic student screenshot provided and committed at `hw06/screenshots/fr01-x-student-id.png` (`8439f1f`).
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
