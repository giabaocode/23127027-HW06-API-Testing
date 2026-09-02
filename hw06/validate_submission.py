#!/usr/bin/env python3
"""
validate_submission.py
Programmatic verification script for all HW06 requirements and quality gates.
"""

import os
import sys
import json
import subprocess

def run_checks():
    print("=" * 60)
    print("HW06 FINAL SUBMISSION PROGRAMMATIC VERIFICATION")
    print("=" * 60)
    
    errors = []
    warnings = []

    # 1. Verify Excel file and 129 testcases
    excel_path = "hw06/testcases/testcases-master.xlsx"
    if not os.path.exists(excel_path):
        errors.append(f"Missing master Excel workbook: {excel_path}")
    else:
        try:
            import openpyxl
            wb = openpyxl.load_workbook(excel_path, read_only=True)
            all_cases_sheet = wb["All Test Cases"]
            # Count rows minus header
            rows = sum(1 for row in all_cases_sheet.iter_rows()) - 1
            print(f"✓ Excel Master Workbook present ({os.path.getsize(excel_path)} bytes)")
            print(f"  Total logical test case rows in 'All Test Cases': {rows}")
            if rows != 129:
                errors.append(f"Excel row count is {rows}, expected exactly 129.")
            wb.close()
        except Exception as e:
            errors.append(f"Failed to parse Excel workbook: {e}")

    # 2. Verify Postman collections
    master_col = "hw06/postman/eshop-hw06-collection.json"
    if not os.path.exists(master_col):
        errors.append(f"Missing master Postman collection: {master_col}")
    else:
        with open(master_col) as f:
            d = json.load(f)
        folders = [item["name"] for item in d.get("item", [])]
        print(f"✓ Master Postman Collection present with {len(folders)} top-level folders: {folders}")

    # 3. Verify GitHub Actions workflow
    wf_path = ".github/workflows/api-tests.yml"
    if not os.path.exists(wf_path):
        errors.append(f"Missing GitHub Actions workflow: {wf_path}")
    else:
        print(f"✓ GitHub Actions workflow present at {wf_path}")

    # 4. Verify Screenshots
    screenshots = [
        "hw06/screenshots/fr01-x-student-id.png",
        "hw06/screenshots/fr07-x-student-id.png",
        "hw06/screenshots/fr12-x-student-id.png",
        "hw06/screenshots/fr07-bug-issue-001.png",
        "hw06/screenshots/fr12-bug-issue-001.png"
    ]
    for sc in screenshots:
        if os.path.exists(sc):
            print(f"✓ Screenshot present: {sc} ({os.path.getsize(sc)} bytes)")
        else:
            errors.append(f"Missing mandatory screenshot: {sc}")

    # 5. Verify Newman reports
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
            print(f"✓ Newman artifact present: {nr} ({os.path.getsize(nr)} bytes)")
        else:
            errors.append(f"Missing Newman artifact: {nr}")

    # 6. Verify 11 Bug Reports
    for feat, num in [("FR01", 5), ("FR07", 2), ("FR12", 4)]:
        for i in range(1, num + 1):
            bf = f"hw06/bugs/DEF-{feat}-{i:02d}.md"
            if os.path.exists(bf):
                print(f"✓ Bug report present: {bf}")
            else:
                errors.append(f"Missing defect report: {bf}")

    # 7. Verify Agent Skill
    agent_skill_files = [
        "hw06/agent-skill/design-decisions.md",
        "hw06/agent-skill/pseudocode.md",
        "hw06/agent-skill/test_generator.py",
        "hw06/agent-skill/student-diagram-checklist.md"
    ]
    for asf in agent_skill_files:
        if os.path.exists(asf):
            print(f"✓ Agent Skill file present: {asf}")
        else:
            errors.append(f"Missing Agent Skill file: {asf}")

    # 8. Verify Documentation Deliverables
    docs_files = [
        "hw06/docs/ai-audit.md",
        "hw06/docs/ai-critique.md",
        "hw06/docs/cicd-report.md",
        "hw06/docs/main-report.md",
        "hw06/docs/oral-defense-notes.md",
        "hw06/docs/git-commit-log.txt",
        "hw06/docs/postman-features.md",
        "hw06/README.md"
    ]
    for df in docs_files:
        if os.path.exists(df):
            print(f"✓ Documentation file present: {df}")
        else:
            errors.append(f"Missing documentation file: {df}")

    # 9. Verify Safety: No assignment PDF, no node_modules, no .env tracked in git
    tracked_files = subprocess.check_output(["git", "ls-files"]).decode("utf-8").splitlines()
    for tf in tracked_files:
        if tf.lower().endswith(".pdf"):
            errors.append(f"SECURITY VIOLATION: PDF file tracked in git: {tf}")
        if "node_modules" in tf:
            errors.append(f"SECURITY VIOLATION: node_modules tracked in git: {tf}")
        if tf.endswith(".env") or tf.startswith(".env"):
            errors.append(f"SECURITY VIOLATION: .env file tracked in git: {tf}")
        if tf.endswith(".bak"):
            errors.append(f"SECURITY VIOLATION: .bak database backup tracked in git: {tf}")

    print("-" * 60)
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  [ERROR] {err}")
        sys.exit(1)
    else:
        print("ALL PROGRAMMATIC VERIFICATION CHECKS PASSED (0 ERRORS)!")
        print("-" * 60)

if __name__ == "__main__":
    run_checks()
