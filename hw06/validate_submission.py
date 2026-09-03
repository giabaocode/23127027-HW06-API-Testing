#!/usr/bin/env python3
"""
validate_submission.py
Programmatic verification script for all HW06 requirements, quality gates,
and official PDF deliverables.
"""

import os
import sys
import json
import subprocess
import pypdf

def run_checks():
    print("=" * 65)
    print("HW06 FINAL SUBMISSION PROGRAMMATIC VERIFICATION (PHASE 14)")
    print("=" * 65)
    
    errors = []

    # 1. Master Excel Workbook & 129 Logical Test Case Designs
    excel_path = "hw06/testcases/testcases-master.xlsx"
    if not os.path.exists(excel_path):
        errors.append(f"Missing master Excel workbook: {excel_path}")
    else:
        try:
            import openpyxl
            wb = openpyxl.load_workbook(excel_path, read_only=True)
            all_cases_sheet = wb["All Test Cases"]
            rows = sum(1 for _ in all_cases_sheet.iter_rows()) - 1
            print(f"✓ Excel Master Workbook present ({os.path.getsize(excel_path)} bytes)")
            print(f"  Total logical test case rows in 'All Test Cases': {rows}")
            if rows != 129:
                errors.append(f"Excel row count is {rows}, expected exactly 129.")
            wb.close()
        except Exception as e:
            errors.append(f"Failed to parse Excel workbook: {e}")

    # 2. Master Postman Collection & Folders
    master_col = "hw06/postman/eshop-hw06-collection.json"
    if not os.path.exists(master_col):
        errors.append(f"Missing master Postman collection: {master_col}")
    else:
        with open(master_col) as f:
            d = json.load(f)
        folders = [item["name"] for item in d.get("item", [])]
        print(f"✓ Master Postman Collection present with {len(folders)} top-level feature folders")
        if len(folders) < 3:
            errors.append(f"Master Postman collection has {len(folders)} folders, expected 3.")

    # 3. GitHub Actions CI/CD Workflow
    wf_path = ".github/workflows/api-tests.yml"
    if not os.path.exists(wf_path):
        errors.append(f"Missing GitHub Actions workflow: {wf_path}")
    else:
        print(f"✓ GitHub Actions workflow present at {wf_path}")

    # 4. Authentic Screenshots (Postman Console, GitHub Issues, CI/CD Runs)
    screenshots = [
        ("hw06/screenshots/fr01-x-student-id.png", "FR-01 X-Student-Id Console"),
        ("hw06/screenshots/fr07-x-student-id.png", "FR-07 X-Student-Id Console"),
        ("hw06/screenshots/fr12-x-student-id.png", "FR-12 X-Student-Id Console"),
        ("hw06/screenshots/fr07-bug-issue-001.png", "FR-07 GitHub Issue #6"),
        ("hw06/screenshots/fr12-bug-issue-001.png", "FR-12 GitHub Issue #8"),
        ("hw06/screenshots/cicd-run-01-success.png", "CI/CD Run A Success"),
        ("hw06/screenshots/cicd-run-02-failure.png", "CI/CD Run B Failure Demo")
    ]
    for sc, desc in screenshots:
        if os.path.exists(sc):
            print(f"✓ Screenshot verified: {desc} -> {sc} ({os.path.getsize(sc)} bytes)")
        else:
            errors.append(f"Missing mandatory screenshot: {desc} ({sc})")

    # 5. Authentic Newman CLI and HTML Reports
    newman_reports = [
        "hw06/newman/fr01/fr01-report.html",
        "hw06/newman/fr07/fr07-report.html",
        "hw06/newman/fr12/fr12-report.html",
        "hw06/newman/fr01/fr01-cli-output.txt",
        "hw06/newman/fr07/fr07-cli-output.txt",
        "hw06/newman/fr12/fr12-cli-output.txt",
    ]
    for nr in newman_reports:
        if os.path.exists(nr):
            print(f"✓ Newman artifact verified: {nr} ({os.path.getsize(nr)} bytes)")
        else:
            errors.append(f"Missing Newman artifact: {nr}")

    # 6. All 11 Confirmed SUT Bug Reports
    for feat, num in [("FR01", 5), ("FR07", 2), ("FR12", 4)]:
        for i in range(1, num + 1):
            bf = f"hw06/bugs/DEF-{feat}-{i:02d}.md"
            if os.path.exists(bf):
                print(f"✓ SUT Bug report verified: {bf}")
            else:
                errors.append(f"Missing defect report: {bf}")

    # 7. Agent Skill Implementation & Student Diagram
    agent_skill_files = [
        "hw06/agent-skill/design-decisions.md",
        "hw06/agent-skill/pseudocode.md",
        "hw06/agent-skill/test_generator.py",
        "hw06/agent-skill/student-diagram.png",
        "hw06/agent-skill/student-diagram-checklist.md"
    ]
    for asf in agent_skill_files:
        if os.path.exists(asf):
            print(f"✓ Agent Skill file verified: {asf}")
        else:
            errors.append(f"Missing Agent Skill file: {asf}")

    # 8. Mandatory Markdown Documentation Deliverables (PDF Section 14)
    mandatory_docs_files = [
        "hw06/docs/main-report.md",
        "hw06/docs/ai-critique.md",
        "hw06/docs/ai-audit.md",
        "hw06/docs/cicd-report.md",
        "hw06/docs/git-commit-log.txt",
        "hw06/docs/postman-features.md",
        "hw06/README.md"
    ]
    for df in mandatory_docs_files:
        if os.path.exists(df):
            print(f"✓ Mandatory markdown document verified: {df}")
        else:
            errors.append(f"Missing mandatory documentation file: {df}")

    # 9. Mandatory Rendered PDF Deliverables (PDF Section 14)
    pdf_files = [
        "hw06/docs/main-report.pdf",
        "hw06/docs/ai-critique.pdf",
        "hw06/docs/ai-audit.pdf",
        "hw06/docs/cicd-report.pdf"
    ]
    for pf in pdf_files:
        if not os.path.exists(pf):
            errors.append(f"Missing mandatory PDF deliverable: {pf}")
        else:
            try:
                reader = pypdf.PdfReader(pf)
                pages = len(reader.pages)
                print(f"✓ Valid PDF verified: {pf} ({pages} pages, {os.path.getsize(pf)} bytes)")
            except Exception as e:
                errors.append(f"Corrupted PDF file {pf}: {e}")

    # Optional study aid files (not required by PDF Section 14)
    if os.path.exists("hw06/docs/oral-defense-notes.md"):
        print("ℹ Optional study aid present: hw06/docs/oral-defense-notes.md (Optional / Study Aid Only)")

    # 10. Security & Repository Hygiene
    tracked_files = subprocess.check_output(["git", "ls-files"]).decode("utf-8").splitlines()
    for tf in tracked_files:
        if "2026.hw06" in tf.lower() or "api testing_en" in tf.lower():
            errors.append(f"SECURITY VIOLATION: Assignment prompt PDF tracked in git: {tf}")
        if "node_modules" in tf:
            errors.append(f"SECURITY VIOLATION: node_modules tracked in git: {tf}")
        if tf.endswith(".env") or tf.startswith(".env"):
            errors.append(f"SECURITY VIOLATION: .env file tracked in git: {tf}")
        if tf.endswith(".bak"):
            errors.append(f"SECURITY VIOLATION: .bak database backup tracked in git: {tf}")

    print("-" * 65)
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  [ERROR] {err}")
        sys.exit(1)
    else:
        print("ALL PROGRAMMATIC VERIFICATION CHECKS PASSED (0 ERRORS)!")
        print("-" * 65)

if __name__ == "__main__":
    run_checks()
