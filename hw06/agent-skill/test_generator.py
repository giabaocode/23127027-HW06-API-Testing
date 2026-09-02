#!/usr/bin/env python3
"""
test_generator.py
Agent Skill: Deterministic API Test Case Generator for REST Endpoints.
Implements Equivalence Partitioning (EP), Boundary Value Analysis (BVA),
and Course Security Rules (SEC-02/03) with Oracle Status Decoupling.

Author: Pham Ngoc Gia Bao (ID: 23127027)
Course: Software Testing (HW06 - API Testing)
"""

import sys
import json
import argparse
from typing import Dict, List, Any

class APITestGenerator:
    def __init__(self, endpoint_spec: Dict[str, Any]):
        self.spec = endpoint_spec
        self.route = endpoint_spec.get("route", "/api/resource")
        self.method = endpoint_spec.get("method", "POST").upper()
        self.auth_level = endpoint_spec.get("auth_level", "public").lower()
        self.parameters = endpoint_spec.get("parameters", [])
        self.test_cases = []
        self._counter = 1

    def _format_id(self, prefix: str) -> str:
        tid = f"{prefix}-{self._counter:03d}"
        self._counter += 1
        return tid

    def _get_nominal_payload(self) -> Dict[str, Any]:
        payload = {}
        for param in self.parameters:
            p_name = param["name"]
            p_type = param.get("type", "string").lower()
            if p_type == "string":
                payload[p_name] = param.get("nominal", f"Valid_{p_name}")
            elif p_type in ["integer", "number"]:
                payload[p_name] = param.get("nominal", 10)
            elif p_type == "boolean":
                payload[p_name] = True
            elif p_type == "array":
                payload[p_name] = [1, 2]
        return payload

    def generate(self) -> List[Dict[str, Any]]:
        self.test_cases = []
        self._counter = 1
        nominal = self._get_nominal_payload()

        # 1. Nominal Happy Path
        auth_tag = "ANONYMOUS" if self.auth_level == "public" else f"BEARER_{self.auth_level.upper()}"
        self.test_cases.append({
            "id": self._format_id("GEN-NOM"),
            "category": "Positive Equivalence Partitioning",
            "method": self.method,
            "route": self.route,
            "auth": auth_tag,
            "payload": nominal,
            "semantic_oracle": "Operation succeeds; entity returned or persisted cleanly in storage",
            "expected_status": "200 OK / 201 Created",
            "oracle_classification": "SPECIFIED" if self.auth_level != "admin" else "INFERRED (Admin Functional Status)",
            "side_effect_check": "Query entity state to assert storage update" if self.method in ["POST", "PUT", "DELETE"] else None
        })

        # 2. Field-Level Validation (EP & BVA)
        for param in self.parameters:
            p_name = param["name"]
            p_type = param.get("type", "string").lower()
            is_req = param.get("required", False)

            # A. Omission of required field
            if is_req:
                omitted = {k: v for k, v in nominal.items() if k != p_name}
                self.test_cases.append({
                    "id": self._format_id("GEN-REQ"),
                    "category": "Negative Equivalence (Missing Mandatory Field)",
                    "method": self.method,
                    "route": self.route,
                    "auth": auth_tag,
                    "payload": omitted,
                    "semantic_oracle": f"Request rejected; missing mandatory field '{p_name}' prevents state mutation",
                    "expected_status": "400 Bad Request / 422 Unprocessable (INFERRED)",
                    "oracle_classification": "INFERRED",
                    "side_effect_check": "Query entity state to confirm no mutation occurred"
                })

            # B. Empty string check
            if p_type == "string":
                empty_payload = {**nominal, p_name: ""}
                self.test_cases.append({
                    "id": self._format_id("GEN-BVA"),
                    "category": "Boundary Value Analysis (Empty String Value)",
                    "method": self.method,
                    "route": self.route,
                    "auth": auth_tag,
                    "payload": empty_payload,
                    "semantic_oracle": f"Field '{p_name}' empty string rejected or sanitized without crashing server",
                    "expected_status": "UNKNOWN (Spec silent on empty string rejection)",
                    "oracle_classification": "ROBUSTNESS / CHARACTERIZATION",
                    "side_effect_check": None
                })

            # C. Numeric Boundaries (Min, Sub-Min)
            if p_type in ["integer", "number"] and "min" in param:
                p_min = param["min"]
                # Exact Minimum (Valid boundary)
                bva_min = {**nominal, p_name: p_min}
                self.test_cases.append({
                    "id": self._format_id("GEN-BVA"),
                    "category": "Boundary Value Analysis (Exact Lower Boundary)",
                    "method": self.method,
                    "route": self.route,
                    "auth": auth_tag,
                    "payload": bva_min,
                    "semantic_oracle": f"Boundary value {p_name}={p_min} accepted as valid lower threshold",
                    "expected_status": "200 OK (INFERRED)",
                    "oracle_classification": "INFERRED",
                    "side_effect_check": "Assert state records exact boundary value"
                })

                # Sub-minimum (Invalid boundary)
                sub_min = p_min - 1
                bva_sub = {**nominal, p_name: sub_min}
                self.test_cases.append({
                    "id": self._format_id("GEN-BVA"),
                    "category": "Boundary Value Analysis (Below Lower Bound Violation)",
                    "method": self.method,
                    "route": self.route,
                    "auth": auth_tag,
                    "payload": bva_sub,
                    "semantic_oracle": f"Sub-minimum value {p_name}={sub_min} rejected; no storage update",
                    "expected_status": "400 Bad Request / UNKNOWN",
                    "oracle_classification": "INFERRED",
                    "side_effect_check": "Query storage to confirm no invalid entry created"
                })

            # D. Type Confusion
            wrong_val = 99999 if p_type == "string" else "not_a_number"
            typ_payload = {**nominal, p_name: wrong_val}
            self.test_cases.append({
                "id": self._format_id("GEN-TYP"),
                "category": "Type Confusion & Robustness Probe",
                "method": self.method,
                "route": self.route,
                "auth": auth_tag,
                "payload": typ_payload,
                "semantic_oracle": f"Invalid type for '{p_name}' handled gracefully without unhandled server exception",
                "expected_status": "400 Bad Request (INFERRED)",
                "oracle_classification": "ROBUSTNESS",
                "side_effect_check": None
            })

        # 3. Security & Access Control Probes
        if self.auth_level in ["user", "admin"]:
            # A. Anonymous Request
            self.test_cases.append({
                "id": self._format_id("GEN-SEC"),
                "category": "Security: Unauthenticated Caller (SEC-02)",
                "method": self.method,
                "route": self.route,
                "auth": "NONE (Missing Authorization Header)",
                "payload": nominal,
                "semantic_oracle": "Access denied; anonymous caller cannot view or mutate resource",
                "expected_status": "401 Unauthorized (SPECIFIED)",
                "oracle_classification": "SPECIFIED",
                "side_effect_check": "Verify resource state unmodified"
            })

            # B. Forged Cryptographic Signature
            self.test_cases.append({
                "id": self._format_id("GEN-SEC"),
                "category": "Security: Forged Signature Tampering (SEC-02)",
                "method": self.method,
                "route": self.route,
                "auth": "BEARER_FORGED_SIGNATURE",
                "payload": nominal,
                "semantic_oracle": "Access denied; token with unverified cryptographic signature rejected",
                "expected_status": "403 Forbidden (SPECIFIED)",
                "oracle_classification": "SPECIFIED",
                "side_effect_check": "Verify resource state unmodified"
            })

            # C. Expired Token
            self.test_cases.append({
                "id": self._format_id("GEN-SEC"),
                "category": "Security: Expired Token Lifecycle (SEC-02)",
                "method": self.method,
                "route": self.route,
                "auth": "BEARER_EXPIRED_TOKEN",
                "payload": nominal,
                "semantic_oracle": "Access denied; expired token rejected at authentication boundary",
                "expected_status": "401 / 403 (SPECIFIED)",
                "oracle_classification": "SPECIFIED",
                "side_effect_check": "Verify resource state unmodified"
            })

        if self.auth_level == "admin":
            # D. Broken Function Level Authorization (BFLA)
            self.test_cases.append({
                "id": self._format_id("GEN-SEC"),
                "category": "Security: Privilege Escalation / Non-Admin Access (SEC-03)",
                "method": self.method,
                "route": self.route,
                "auth": "BEARER_STANDARD_USER (role='user')",
                "payload": nominal,
                "semantic_oracle": "Access denied; standard user possesses insufficient privilege to execute admin route",
                "expected_status": "403 Forbidden (INFERRED)",
                "oracle_classification": "SPECIFIED_SEMANTIC (Denied)",
                "side_effect_check": "Dual-assertion: query storage to confirm mutation did NOT execute"
            })

            # E. Case Spoofing & Role Tampering
            self.test_cases.append({
                "id": self._format_id("GEN-SEC"),
                "category": "Security: Role Attribute Confusion (SEC-03)",
                "method": self.method,
                "route": self.route,
                "auth": "BEARER_TOKEN (role='ADMIN')",
                "payload": nominal,
                "semantic_oracle": "Access denied; uppercase role must not bypass strict 'admin' match",
                "expected_status": "403 Forbidden (INFERRED)",
                "oracle_classification": "SECURITY-HARDENING",
                "side_effect_check": "Verify resource state unmodified"
            })

        return self.test_cases

def main():
    parser = argparse.ArgumentParser(description="Deterministic API Test Case Generator (Agent Skill)")
    parser.add_argument("--spec", help="Path to JSON file containing endpoint specification")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown", help="Output format")
    parser.add_argument("--sample", action="store_true", help="Generate test suite for built-in sample endpoint (/api/cart)")
    args = parser.parse_args()

    sample_spec = {
        "route": "/api/cart",
        "method": "POST",
        "auth_level": "user",
        "parameters": [
            {
                "name": "productId",
                "type": "integer",
                "required": True,
                "min": 1,
                "nominal": 1
            },
            {
                "name": "quantity",
                "type": "integer",
                "required": True,
                "min": 1,
                "nominal": 2
            }
        ]
    }

    if args.spec:
        with open(args.spec, "r", encoding="utf-8") as f:
            spec = json.load(f)
    elif args.sample or len(sys.argv) == 1:
        spec = sample_spec
    else:
        parser.print_help()
        sys.exit(1)

    generator = APITestGenerator(spec)
    cases = generator.generate()

    if args.format == "json":
        print(json.dumps(cases, indent=2))
    else:
        print(f"# Generated Test Suite: {spec.get('method', 'POST')} {spec.get('route', '')}")
        print(f"Total Test Cases Generated: {len(cases)}\n")
        print("| Test ID | Category | Auth Context | Input Payload | Semantic Expected Oracle | Expected Status | Status Classification |")
        print("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        for tc in cases:
            payload_str = json.dumps(tc["payload"])
            print(f"| `{tc['id']}` | {tc['category']} | `{tc['auth']}` | `{payload_str}` | {tc['semantic_oracle']} | `{tc['expected_status']}` | {tc['oracle_classification']} |")

if __name__ == "__main__":
    main()
