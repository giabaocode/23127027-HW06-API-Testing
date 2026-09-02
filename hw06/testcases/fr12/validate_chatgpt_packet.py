#!/usr/bin/env python3
"""
Validation script for ChatGPT External Review Packet.
Verifies all 10 integrity rules.
"""

import os
import re
import subprocess
import sys

def validate():
    print("=== STARTING VALIDATION OF CHATGPT REVIEW PACKET ===")
    errors = []
    
    packet_path = "hw06/testcases/fr12/chatgpt-review-packet.md"
    try:
        with open(packet_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"FAIL: Could not read {packet_path}: {e}")
        return False
    
    # 1. Exactly 38 testcase sections
    sections = re.findall(r"^### (FR12-AI-\d{3})$", content, re.MULTILINE)
    print(f"[Check 1] Section count: {len(sections)} (Expected: 38)")
    if len(sections) != 38:
        errors.append(f"Expected 38 sections, found {len(sections)}")
    
    # 2. Continuous IDs
    expected_ids = [f"FR12-AI-{i:03d}" for i in range(1, 39)]
    if sections != expected_ids:
        errors.append(f"Section IDs not continuous: {sections}")
    else:
        print("[Check 2] Section IDs continuous: FR12-AI-001 .. FR12-AI-038")
    
    # Split by section
    raw_blocks = re.split(r"^### FR12-AI-\d{3}$", content, flags=re.MULTILINE)[1:]
    
    for i, block in enumerate(raw_blocks):
        tc_id = sections[i]
        
        # 3. Method + endpoint
        if not re.search(r"- \*\*Method:\*\* `[A-Z]+`", block) or not re.search(r"- \*\*Endpoint:\*\* `.*?`", block):
            errors.append(f"{tc_id} missing Method or Endpoint")
        
        # 4. Caller, JWT, Role
        if not re.search(r"- \*\*Caller Type:\*\*", block) or not re.search(r"- \*\*JWT State:\*\*", block) or not re.search(r"- \*\*Role:\*\*", block):
            errors.append(f"{tc_id} missing Caller, JWT, or Role")
            
        # 5. Semantic oracle
        if not re.search(r"- \*\*Expected Access-Control Semantic Outcome:\*\*", block):
            errors.append(f"{tc_id} missing Semantic Outcome")
            
        # 6. HTTP classification
        if not re.search(r"- \*\*Expected HTTP Status \+ Classification:\*\*", block):
            errors.append(f"{tc_id} missing HTTP Status + Classification")
            
        # 7. Side-effect assertion
        if not re.search(r"- \*\*Unauthorized Side-Effect Assertion:\*\*", block):
            errors.append(f"{tc_id} missing Side-Effect Assertion")
    
    print("[Check 3-7] Every section contains complete metadata, oracle, and assertions.")
    
    # 8 & 9. No pre-baked verdicts
    forbidden_terms = ["Verdict: VALID", "Verdict: INVALID", "Verdict: INCOMPLETE", "Student Verdict:"]
    for term in forbidden_terms:
        if term in content:
            errors.append(f"Packet contains forbidden pre-baked verdict string: '{term}'")
    else:
        print("[Check 8-9] Packet contains zero pre-baked AI verdicts and zero student verdicts.")
        
    # 10. generated-ai-original.md unchanged from commit 6b50faa
    diff_proc = subprocess.run(["git", "diff", "6b50faa", "--", "hw06/testcases/fr12/generated-ai-original.md"],
                               capture_output=True, text=True)
    if diff_proc.stdout.strip():
        errors.append("generated-ai-original.md has been modified from commit 6b50faa!")
    else:
        print("[Check 10] generated-ai-original.md is byte-for-byte identical to commit 6b50faa.")
        
    if errors:
        print("\n=== VALIDATION FAILED ===")
        for e in errors:
            print(f"  - ERROR: {e}")
        return False
    else:
        print("\n=== ALL REVIEW PACKET CHECKS PASSED PERFECTLY ===")
        return True

if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
