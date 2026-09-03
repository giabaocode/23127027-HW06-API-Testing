# HW06 — Final Submission Manifest & Artifact Registry

> **Student Metadata:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Course:** Software Testing (Kiểm thử Phần mềm) — API Testing HW06
> - **Public GitHub Repository:** [`https://github.com/giabaocode/23127027-HW06-API-Testing`](https://github.com/giabaocode/23127027-HW06-API-Testing)

---

## 1. Submission Identity & Commit Registry

| Attribute | Certified Value |
| :--- | :--- |
| **Official Submission Archive** | `23127027_HW06_AI_API_093.zip` (6.14 MB) |
| **Archive Validation Status** | **Local artifact validation passes; archive size/count refreshed by `package_submission.py`** |
| **Final Git Commit Hash** | `a0ff9dd` at the start of the 2026-09-03 Codex audit; subsequent local corrections require commit/push |
| **Git Remote Sync Status** | **Local audit corrections pending commit/push** |
| **Public GitHub Repository URL** | [`https://github.com/giabaocode/23127027-HW06-API-Testing`](https://github.com/giabaocode/23127027-HW06-API-Testing) |
| **CI/CD Run A (Success) URL** | [`https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665114685`](https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665114685) |
| **CI/CD Run B (Failure Demo) URL**| [`https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665296154`](https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665296154) |
| **Total Logical Test Case Designs**| **129** (43 FR-01 + 43 FR-07 + 43 FR-12) |
| **Total Confirmed SUT Bugs** | **11 Defects** (Issues #1 through #11 filed on GitHub) |
| **Comprehensive Self-Assessed Score**| **93 / 100** — conservative deduction for missing independent student-original extensions, declared historical audit gaps, and remaining student-only confirmations |

---

## 2. Mandatory Deliverables Checklist (PDF Section 14)

| # | Mandatory Item (PDF Section 14) | File Path in Archive | Format & Verification | Status |
| :-: | :--- | :--- | :--- | :---: |
| 1 | **Main Report** | `hw06/docs/main-report.md`<br>`hw06/docs/main-report.pdf` | Markdown + Valid 4-page PDF | **VERIFIED** |
| 2 | **Public GitHub Repository Link** | Documented in `README.md` & reports | `https://github.com/giabaocode/23127027-HW06-API-Testing` | **VERIFIED** |
| 3 | **Master Postman Collection** | `hw06/postman/eshop-hw06-collection.json` | JSON (3 feature folders, central `X-Student-Id`) | **VERIFIED** |
| 4 | **Newman Test Reports** | `hw06/newman/*/fr*-report.html`<br>`hw06/newman/*/fr*-cli-output.txt` | HTML Extra Interactive Dashboards & CLI logs | **VERIFIED** |
| 5 | **List of Postman Features Used** | `hw06/docs/postman-features.md` | Comprehensive technical feature guide | **VERIFIED** |
| 6 | **CI/CD Pipeline Report** | `hw06/docs/cicd-report.md`<br>`hw06/docs/cicd-report.pdf` | Markdown + Valid 3-page PDF | **VERIFIED** |
| 7 | **CI/CD Run 1 Evidence (Passing)** | `hw06/screenshots/cicd-run-01-success.png` | Real browser screenshot (Run ID `33665114685`) | **VERIFIED** |
| 8 | **CI/CD Run 2 Evidence (Failure)** | `hw06/screenshots/cicd-run-02-failure.png` | Real browser screenshot (Run ID `33665296154`) | **VERIFIED** |
| 9 | **Master Test Cases Excel** | `hw06/testcases/testcases-master.xlsx` | 7-sheet styled Excel workbook, exactly 129 rows | **VERIFIED** |
| 10 | **AI Test-Generator Diagram** | `hw06/agent-skill/student-diagram.png` | Readable diagram carrying student identity; authorship cannot be programmatically proven | **STUDENT CONFIRMATION REQUIRED** |
| 11 | **Agent Skill Pseudocode & Code** | `hw06/agent-skill/pseudocode.md`<br>`hw06/agent-skill/test_generator.py` | Design decisions, pseudocode, functional CLI tool | **VERIFIED** |
| 12 | **Bug Reports & GitHub Issues** | `hw06/bugs/README.md`<br>`hw06/bugs/DEF-*.md` (11 reports) | 11 markdown reports and 11 live GitHub Issues verified | **VERIFIED** |
| 13 | **Screenshot attached to each GitHub Issue** | GitHub Issues #1–#11 | Embedded image found in the body or comments of all 11 issues through GitHub API verification | **VERIFIED 2026-09-03** |
| 14 | **Console Screenshot (`X-Student-Id`)** | `hw06/screenshots/fr01-x-student-id.png`<br>`hw06/screenshots/fr07-x-student-id.png`<br>`hw06/screenshots/fr12-x-student-id.png` | Authentic Postman Console captures showing ID | **VERIFIED** |
| 15 | **AI Critique** | `hw06/docs/ai-critique.md`<br>`hw06/docs/ai-critique.pdf` | Markdown + 1-page PDF (exactly 252 words) | **VERIFIED** |
| 16 | **AI Audit Report** | `hw06/docs/ai-audit.md`<br>`hw06/docs/ai-audit.pdf` | Current Codex interaction recorded; unavailable historical prompt/output text is explicitly disclosed | **UPDATED WITH DECLARED HISTORICAL GAPS** |
| 17 | **Git Commit Log** | `hw06/docs/git-commit-log.txt` | Complete text export of authentic git log | **VERIFIED** |
| 18 | **README with Self-Assessment** | `hw06/README.md` | Complete repository guide and grading rubric | **VERIFIED** |
| — | **GitHub Actions Workflow** | `.github/workflows/api-tests.yml` | Live automated CI/CD pipeline | **VERIFIED** |
| — | *(Optional Study Aid)* | `hw06/docs/oral-defense-notes.md` | Preserved in git repository only (excluded from zip) | **OPTIONAL** |

---

## 3. Submission Integrity Status

- **No evidence was fabricated during the 2026-09-03 audit.** Existing screenshots, Newman reports, CI/CD runs, and GitHub Issues were cross-checked where possible.
- **Specification Assertions Uncompromised:** No tests were inverted or suppressed to hide SUT defects.
- **Clean Archive Scope:** no `.env` files, `node_modules`, database backups, or course prompt PDFs are packaged. Postman environments intentionally retain local-only test JWT fixtures required to replay the suites; these are not production credentials.
- **Student Extension Coverage:** All 15 student extension test cases formalized with explicit root-cause analysis on why AI missed them (Prompt Quality, Model Limitations, SUT Characteristics per PDF Section 6.3).
