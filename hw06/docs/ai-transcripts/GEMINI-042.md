# Verbatim AI Transcript — Interaction GEMINI-042

- **Session / Interaction ID:** GEMINI-042
- **Date & Time:** 2026-09-03T01:20:00+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Submission Packaging & Requirement Calibration — Oral Defense Notes Reclassified as Optional Study Aid

---

## 1. Verbatim Student Prompt

```text
Remove Oral Defense Notes from the mandatory submission requirements.

I am submitting the homework artifacts to the lecturer; I do not want
hw06/docs/oral-defense-notes.md treated as a required deliverable unless the
OFFICIAL HW06 PDF explicitly requires such a file.

Please re-read the official assignment PDF.

If the PDF does NOT explicitly require an oral-defense-notes file:

1. Mark:
   hw06/docs/oral-defense-notes.md
   as OPTIONAL / STUDY AID ONLY.

2. Remove it from:
   - mandatory submission checklist
   - completion gates
   - final required-deliverables count
   - any validator rule that fails when it is absent

3. Do NOT rewrite git history just to remove the already-created file.
   If already committed, it may remain as an optional helper artifact.

4. Update:
   - hw06/submission-checklist.md
   - hw06/MANUAL_TODO.md
   - hw06/docs/main-report.md
   - hw06/README.md
   - hw06/validate_submission.py
   only where necessary.

5. Do NOT remove any artifact that the official PDF actually requires.

Also remove any assumption that I must prepare oral-defense material before
submission.

Then show:

=== OFFICIAL PDF REQUIREMENT CHECK ===
Oral Defense Notes required by PDF: YES / NO
Exact source if YES.

=== SUBMISSION REQUIREMENTS AFTER CORRECTION ===

=== REMAINING HUMAN ACTIONS ===
```

---

## 2. Verbatim Conversational AI Response

=== OFFICIAL PDF REQUIREMENT CHECK ===

**Oral Defense Notes required by PDF: NO**

### Exact Source from the Official HW06 PDF:
- **Section 13 (Page 7) — Oral Defense Context:**
  > *"13. Oral Defense: A randomly selected 30% of students may be invited to a 5–7-minute oral defense during the week following the deadline, to explain how they completed this homework."*
- **Section 14 (Pages 7–8) — Official Submission Contents of `.zip`:**
  > *"Required contents of the .zip:*
  > 1. *Main report (Markdown + PDF), including the API-testing report and your AI audit.*
  > 2. *The public GitHub repository link (collections, scripts, and reports).*
  > 3. *The Postman collection (.json) and the Newman report (HTML), plus the list of Postman features you used.*
  > 4. *A short CI/CD report: the pipeline configuration and the two sample pipeline runs (one all-passing, one with a failing test case), with screenshots and links.*
  > 5. *The Excel test cases and test summary.*
  > 6. *The AI test-generator diagram and pseudocode (PNG / Mermaid + .md / .py).*
  > 7. *Optionally, the API specification converted to OpenAPI (.yaml / .json); if AI-generated, audit it as well.*
  > 8. *Bug report, with screenshots of the bugs on the GitHub Issues page.*
  > 9. *AI Critique and AI Audit Report (Markdown + PDF).*
  > 10. *Git commit log (text file).*
  > 11. *A README.md containing the self-assessment table (below) and a test summary report: number of APIs; test cases generated, added, executed, passed, and failed; and number of bugs.*
  > 12. *Any other supporting materials."*

**Conclusion:** The official assignment PDF establishes the Oral Defense as an **oral viva examination** conducted for a randomly selected 30% of students *during the week following the deadline*. It does **NOT** mandate an oral-defense-notes document as a required submission artifact.

---

=== SUBMISSION REQUIREMENTS AFTER CORRECTION ===

### Actions Taken:
1. **Reclassified [`hw06/docs/oral-defense-notes.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/oral-defense-notes.md):**
   - Explicitly marked with an official disclaimer at the top as **`OPTIONAL STUDY AID ONLY — NOT A MANDATORY SUBMISSION DELIVERABLE`**.
   - Preserved in the repository strictly as an optional helper for student preparation without rewriting git history.
2. **Removed from Mandatory Gates & Lists:**
   - Excluded from mandatory submission deliverables in [`hw06/submission-checklist.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/submission-checklist.md) and [`hw06/MANUAL_TODO.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/MANUAL_TODO.md).
   - Removed from required-deliverables list in [`hw06/README.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/README.md) (annotated as optional study aid).
   - Updated [`hw06/validate_submission.py`](file:///Users/phamngocgiabao/eshop-sut/hw06/validate_submission.py) so validation **never fails** if oral defense notes are absent.

### Authoritative Mandatory Submission Inventory (PDF Section 14):

| # | Required Deliverable | Repository Path | Completion Status |
| :-: | :--- | :--- | :---: |
| 1 | **Main Report (Markdown + PDF)** | [`hw06/docs/main-report.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/main-report.md) | **COMPLETE (Markdown)** |
| 2 | **Public GitHub Repository Link** | `https://github.com/giabaocode/23127027-HW06-API-Testing` | **COMPLETE** |
| 3 | **Postman Collection (`.json`)** | [`hw06/postman/eshop-hw06-collection.json`](file:///Users/phamngocgiabao/eshop-sut/hw06/postman/eshop-hw06-collection.json) | **COMPLETE** |
| 4 | **Newman Reports (HTML & CLI)** | [`hw06/newman/*/fr*-report.html`](file:///Users/phamngocgiabao/eshop-sut/hw06/newman/) | **COMPLETE** |
| 5 | **List of Postman Features Used** | [`hw06/docs/postman-features.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/postman-features.md) | **COMPLETE** |
| 6 | **CI/CD Pipeline Report** | [`hw06/docs/cicd-report.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/cicd-report.md) | **COMPLETE (Markdown)** |
| 7 | **CI/CD Run 1 (Passing Smoke Run)** | Real Run ID `33665114685` verified on GitHub Actions | **Run Complete (Screenshot Gate)** |
| 8 | **CI/CD Run 2 (Failing Test Demo)** | Real Run ID `33665296154` verified on GitHub Actions | **Run Complete (Screenshot Gate)** |
| 9 | **Excel Test Cases & Summary** | [`hw06/testcases/testcases-master.xlsx`](file:///Users/phamngocgiabao/eshop-sut/hw06/testcases/testcases-master.xlsx) (129 rows) | **COMPLETE** |
| 10 | **AI Test-Generator Diagram** | `hw06/agent-skill/student-diagram.png` | **Pending Student Drawing** |
| 11 | **Agent Skill Pseudocode & Code** | [`hw06/agent-skill/pseudocode.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/agent-skill/pseudocode.md)<br>[`hw06/agent-skill/test_generator.py`](file:///Users/phamngocgiabao/eshop-sut/hw06/agent-skill/test_generator.py) | **COMPLETE** |
| 12 | **Bug Reports with GitHub Issues** | [`hw06/bugs/README.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/bugs/README.md)<br>Issues #1 to #11 on GitHub | **COMPLETE** |
| 13 | **Bug Issue Browser Screenshots** | [`hw06/screenshots/fr07-bug-issue-001.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr07-bug-issue-001.png)<br>[`hw06/screenshots/fr12-bug-issue-001.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr12-bug-issue-001.png) | **COMPLETE** |
| 14 | **Console Screenshot (`X-Student-Id`)** | [`hw06/screenshots/fr01-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr01-x-student-id.png)<br>[`hw06/screenshots/fr07-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr07-x-student-id.png)<br>[`hw06/screenshots/fr12-x-student-id.png`](file:///Users/phamngocgiabao/eshop-sut/hw06/screenshots/fr12-x-student-id.png) | **COMPLETE** |
| 15 | **AI Critique (200–300 words)** | [`hw06/docs/ai-critique.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-critique.md) (252 words) | **COMPLETE (Draft for Review)** |
| 16 | **AI Audit Report (Markdown)** | [`hw06/docs/ai-audit.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-audit.md) | **COMPLETE** |
| 17 | **Git Commit Log (Text File)** | [`hw06/docs/git-commit-log.txt`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/git-commit-log.txt) | **COMPLETE** |
| 18 | **README.md (Self-Assessment Table)** | [`hw06/README.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/README.md) | **COMPLETE** |
| — | *(Optional Study Aid)* | [`hw06/docs/oral-defense-notes.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/oral-defense-notes.md) | **OPTIONAL / STUDY AID ONLY** |

---

=== REMAINING HUMAN ACTIONS ===

There are **zero oral defense preparation requirements** before submission. The only genuine physical human actions remaining are:

### 1. Capture 2 Real Browser Screenshots of GitHub Actions Runs:
- **Run A (Passing Smoke Run):**
  - Open: https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665114685
  - Capture clean browser screenshot showing green checkmark and job summary.
  - Save to: `hw06/screenshots/cicd-run-01-success.png`
- **Run B (Intentional Failure Demo):**
  - Open: https://github.com/giabaocode/23127027-HW06-API-Testing/actions/runs/33665296154
  - Capture clean browser screenshot showing red cross and test step failure.
  - Save to: `hw06/screenshots/cicd-run-02-failure.png`

### 2. Draw Agent Skill Architecture Diagram (Student-Created):
- Follow the guide and checklist in [`hw06/agent-skill/student-diagram-checklist.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/agent-skill/student-diagram-checklist.md).
- Hand-draw or construct the diagram in Draw.io / Excalidraw / tool of choice (showing Input $\rightarrow$ EP/BVA $\rightarrow$ Security $\rightarrow$ Oracle Calibration $\rightarrow$ Export $\rightarrow$ Newman Loop).
- Include Student Name & ID (`Phạm Ngọc Gia Bảo - 23127027`).
- Save to: `hw06/agent-skill/student-diagram.png`

### 3. Review AI Critique & Fill Self-Assessed Score:
- Review the 252-word critique in [`hw06/docs/ai-critique.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-critique.md).
- Enter your personal self-assessed grade in [`hw06/README.md`](file:///Users/phamngocgiabao/eshop-sut/hw06/README.md).

