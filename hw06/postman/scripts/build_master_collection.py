#!/usr/bin/env python3
"""
build_master_collection.py
Constructs the unified master Postman collection hw06/postman/eshop-hw06-collection.json
containing FR-01, FR-07, and FR-12 as top-level folders while preserving central
X-Student-Id: 23127027 injection and all feature-specific test semantics.
"""

import json
import os

def build_master_collection():
    fr01_path = "hw06/postman/collections/fr01-registration.postman_collection.json"
    fr07_path = "hw06/postman/collections/fr07-shopping-cart.postman_collection.json"
    fr12_path = "hw06/postman/collections/fr12-access-control.postman_collection.json"
    output_path = "hw06/postman/eshop-hw06-collection.json"

    with open(fr01_path, 'r', encoding='utf-8') as f:
        fr01 = json.load(f)
    with open(fr07_path, 'r', encoding='utf-8') as f:
        fr07 = json.load(f)
    with open(fr12_path, 'r', encoding='utf-8') as f:
        fr12 = json.load(f)

    # Master Collection Info
    master_collection = {
        "info": {
            "_postman_id": "95308b01-1bfe-414d-8483-hw06-master-suite",
            "name": "E-Shop API Testing Master Suite — HW06-AI (FR-01, FR-07, FR-12)",
            "description": "Unified Master Postman Collection for HW06 API Testing.\nStudent: Phạm Ngọc Gia Bảo (ID: 23127027)\nFeatures: FR-01 (Account Registration), FR-07 (Shopping Cart), FR-12 (Access Control)\n129 Logical Test Cases (43 per feature: 38 AI + 5 Student Extensions).",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "event": [
            {
                "listen": "prerequest",
                "script": {
                    "type": "text/javascript",
                    "exec": [
                        "// Central Injection of Student Identifier",
                        "pm.request.headers.upsert({",
                        "    key: 'X-Student-Id',",
                        "    value: '23127027'",
                        "});",
                        "console.log('[Central Pre-Request Hook] Injected X-Student-Id: 23127027 into request to ' + pm.request.url.toString());"
                    ]
                }
            },
            {
                "listen": "test",
                "script": {
                    "type": "text/javascript",
                    "exec": [
                        "// Central Pre-flight & Resilience Assertions",
                        "pm.test('Central Injection - Request header X-Student-Id matches 23127027', function () {",
                        "    pm.expect(pm.request.headers.get('X-Student-Id')).to.eql('23127027');",
                        "});",
                        "",
                        "pm.test('Server Resilience - Server responded with valid HTTP status', function () {",
                        "    pm.expect(pm.response.code).to.be.oneOf([200, 201, 400, 401, 403, 404, 409, 422, 500]);",
                        "});"
                    ]
                }
            }
        ],
        "item": [
            {
                "name": "Feature 1 — FR-01: Account Registration (POST /api/register)",
                "description": "Comprehensive test suite for FR-01: 38 reviewed AI test cases + 5 student-authored extension probes.",
                "item": fr01.get("item", [])
            },
            {
                "name": "Feature 2 — FR-07: Shopping Cart Management (GET /api/cart, POST /api/cart)",
                "description": "Comprehensive test suite for FR-07: 38 reviewed AI test cases + 5 student-authored extension probes.",
                "item": fr07.get("item", [])
            },
            {
                "name": "Feature 3 — FR-12: Access Control & Authorization (Admin Subsystems & Catalog Mutations)",
                "description": "Comprehensive test suite for FR-12: 38 reviewed AI test cases + 5 student-authored extension probes across 14 exposed operations.",
                "item": fr12.get("item", [])
            }
        ]
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_collection, f, indent=2, ensure_ascii=False)

    print(f"Unified master collection saved to {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    build_master_collection()
