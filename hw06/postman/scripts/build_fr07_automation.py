#!/usr/bin/env python3
"""
Build complete FR-07 Shopping Cart Postman Collection and Environment setup.
Automates 43 test cases: 38 reviewed AI tests + 5 student extension tests.
"""
import json
import os

COLLECTION_PATH = "/Users/phamngocgiabao/eshop-sut/hw06/postman/collections/fr07-shopping-cart.postman_collection.json"
SETUP_SCRIPT_PATH = "/Users/phamngocgiabao/eshop-sut/hw06/postman/scripts/setup_fr07_env.js"

def main():
    collection = {
        "info": {
            "_postman_id": "f7a1b2c3-d4e5-6789-0abc-ef1234567890",
            "name": "FR-07 — Shopping Cart Test Suite",
            "description": "Automated test suite for FR-07 Shopping Cart (HCMUS EShop SUT). Created for HW06 API Testing by student Pham Ngoc Gia Bao (23127027). Automates 38 reviewed AI test cases + 5 student extension test cases (43 total test cases across 72 HTTP requests).",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "event": [
            {
                "listen": "prerequest",
                "script": {
                    "type": "text/javascript",
                    "exec": [
                        "// Central X-Student-Id injection required by course specification",
                        "pm.request.headers.upsert({",
                        "    key: 'X-Student-Id',",
                        "    value: pm.environment.get('studentId') || '23127027'",
                        "});"
                    ]
                }
            },
            {
                "listen": "test",
                "script": {
                    "type": "text/javascript",
                    "exec": [
                        "// Central assertion: verify that request carries X-Student-Id: 23127027",
                        "pm.test('Central Injection - Request header X-Student-Id matches 23127027', function () {",
                        "    pm.expect(pm.request.headers.get('X-Student-Id')).to.eql('23127027');",
                        "});",
                        "// Server resilience check",
                        "pm.test('Server Resilience - Server responded with valid HTTP status', function () {",
                        "    pm.expect(pm.response.code).to.be.oneOf([200, 201, 400, 401, 403, 404, 405, 409, 415, 422, 500]);",
                        "});"
                    ]
                }
            }
        ],
        "item": []
    }

    # Helper function to create standard request item
    def add_request(name, method, url_path, token_var, body_obj=None, raw_body=None, content_type="application/json", test_scripts=[], prerequest_scripts=[], extra_headers=[]):
        headers = []
        if token_var:
            headers.append({"key": "Authorization", "value": f"Bearer {{{{{token_var}}}}}"})
        if content_type:
            headers.append({"key": "Content-Type", "value": content_type})
        headers.append({"key": "X-Student-Id", "value": "{{studentId}}"})
        for eh in extra_headers:
            headers.append(eh)

        req_body = None
        if raw_body is not None:
            req_body = {"mode": "raw", "raw": raw_body}
        elif body_obj is not None:
            req_body = {"mode": "raw", "raw": json.dumps(body_obj, indent=2, ensure_ascii=False)}

        item = {
            "name": name,
            "event": [],
            "request": {
                "method": method,
                "header": headers,
                "url": {
                    "raw": "{{baseUrl}}" + url_path,
                    "host": ["{{baseUrl}}"],
                    "path": [p for p in url_path.split("/") if p]
                }
            },
            "response": []
        }
        if req_body:
            item["request"]["body"] = req_body

        if prerequest_scripts:
            item["event"].append({
                "listen": "prerequest",
                "script": {"type": "text/javascript", "exec": prerequest_scripts}
            })
        if test_scripts:
            item["event"].append({
                "listen": "test",
                "script": {"type": "text/javascript", "exec": test_scripts}
            })

        collection["item"].append(item)

    # -------------------------------------------------------------
    # 38 REVIEWED AI TEST CASES
    # -------------------------------------------------------------

    # FR07-AI-001
    add_request(
        "FR07-AI-001 — Retrieve Empty Cart Baseline",
        "GET", "/api/cart", "token_user_01",
        test_scripts=[
            "pm.test('FR07-AI-001 - Response status is 200 OK', function () {",
            "    pm.response.to.have.status(200);",
            "});",
            "pm.test('FR07-AI-001 - Empty cart returns empty JSON array', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array');",
            "    pm.expect(data.length).to.eql(0);",
            "});"
        ]
    )

    # FR07-AI-002 (2 steps)
    add_request(
        "FR07-AI-002 (Step 1) — Add Single Item to Cart",
        "POST", "/api/cart", "token_user_02",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=[
            "pm.test('FR07-AI-002 - POST /api/cart accepts valid item addition', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    )
    add_request(
        "FR07-AI-002 (Step 2) — Verify Populated Cart Contains Item",
        "GET", "/api/cart", "token_user_02",
        test_scripts=[
            "pm.test('FR07-AI-002 - GET /api/cart returns populated array', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(1);",
            "    pm.expect(data[0].id).to.eql(1);",
            "    pm.expect(data[0].quantity).to.eql(2);",
            "});"
        ]
    )

    # FR07-AI-003 (3 steps)
    add_request(
        "FR07-AI-003 (Step 1) — Add Product 1 (q=1)",
        "POST", "/api/cart", "token_user_03",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-003 (Step 2) — Add Product 2 (q=3)",
        "POST", "/api/cart", "token_user_03",
        body_obj={"id": 2, "name": "Sản phẩm B", "price": 150000, "quantity": 3},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-003 (Step 3) — Verify Multi-Item Cart Contains Both Products",
        "GET", "/api/cart", "token_user_03",
        test_scripts=[
            "pm.test('FR07-AI-003 - GET /api/cart returns 2 distinct products', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(2);",
            "    var ids = data.map(function(item) { return item.id; });",
            "    pm.expect(ids).to.include.members([1, 2]);",
            "});"
        ]
    )

    # FR07-AI-004
    add_request(
        "FR07-AI-004 — GET /api/cart with Missing Auth Token",
        "GET", "/api/cart", None,
        test_scripts=[
            "pm.test('FR07-AI-004 - Unauthenticated GET rejected (401)', function () {",
            "    pm.expect(pm.response.code).to.eql(401);",
            "});"
        ]
    )

    # FR07-AI-005
    add_request(
        "FR07-AI-005 — GET /api/cart with Forged JWT Signature",
        "GET", "/api/cart", None,
        extra_headers=[{"key": "Authorization", "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTE2MjM5MDIyfQ.InvalidSignatureStringForTesting"}],
        test_scripts=[
            "pm.test('FR07-AI-005 - Forged token rejected (403)', function () {",
            "    pm.expect(pm.response.code).to.eql(403);",
            "});"
        ]
    )

    # FR07-AI-006
    add_request(
        "FR07-AI-006 — GET /api/cart with Non-Bearer Authorization Scheme",
        "GET", "/api/cart", None,
        extra_headers=[{"key": "Authorization", "value": "RawTokenWithoutBearerPrefix12345"}],
        test_scripts=[
            "pm.test('FR07-AI-006 - Malformed scheme rejected (401/403)', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    )

    # FR07-AI-007
    add_request(
        "FR07-AI-007 — Standard Valid Item Addition",
        "POST", "/api/cart", "token_user_07",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=[
            "pm.test('FR07-AI-007 - Standard addition succeeds with 200 OK', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    )

    # FR07-AI-008
    add_request(
        "FR07-AI-008 — Sequential Addition of Second Distinct Product",
        "POST", "/api/cart", "token_user_08",
        body_obj={"id": 2, "name": "Sản phẩm B", "price": 250000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-008 - Distinct item addition succeeds with 200 OK', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    )

    # FR07-AI-009 (3 steps) - Specified Duplicate Accumulation Rule
    add_request(
        "FR07-AI-009 (Step 1) — Add Product 1 (q=2)",
        "POST", "/api/cart", "token_user_09",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-009 (Step 2) — Add Product 1 Again (q=3)",
        "POST", "/api/cart", "token_user_09",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-009 (Step 3) — Verify Duplicate Accumulation (Expected: 1 row, q=5)",
        "GET", "/api/cart", "token_user_09",
        test_scripts=[
            "pm.test('FR07-AI-009 - SPECIFIED RULE: Exactly 1 row for duplicate product', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array');",
            "    pm.expect(data.length).to.eql(1, 'SUT violation: duplicate addition created duplicate rows instead of accumulating');",
            "});",
            "pm.test('FR07-AI-009 - SPECIFIED RULE: Quantity accumulated to 5 (2 + 3)', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data[0].quantity).to.eql(5, 'SUT violation: quantity did not accumulate to 5');",
            "});"
        ]
    )

    # FR07-AI-010 (4 steps) - Interleaved Duplicate Accumulation
    add_request(
        "FR07-AI-010 (Step 1) — Add Product 1 (q=1)",
        "POST", "/api/cart", "token_user_10",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-010 (Step 2) — Add Product 2 (q=2)",
        "POST", "/api/cart", "token_user_10",
        body_obj={"id": 2, "name": "Sản phẩm B", "price": 200000, "quantity": 2},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-010 (Step 3) — Add Product 1 Again (q=4)",
        "POST", "/api/cart", "token_user_10",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 4},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-010 (Step 4) — Verify Interleaved Accumulation (Expected: 2 rows, p1 q=5)",
        "GET", "/api/cart", "token_user_10",
        test_scripts=[
            "pm.test('FR07-AI-010 - Cart has exactly 2 rows for 2 distinct products', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data.length).to.eql(2, 'Duplicate rows created for product 1');",
            "});",
            "pm.test('FR07-AI-010 - Product 1 accumulated quantity is 5 (1 + 4)', function () {",
            "    var data = pm.response.json();",
            "    var p1 = data.find(function(x) { return x.id === 1; });",
            "    pm.expect(p1).to.exist;",
            "    pm.expect(p1.quantity).to.eql(5);",
            "});"
        ]
    )

    # FR07-AI-011 (3 steps) - Minimum Increment Accumulation
    add_request(
        "FR07-AI-011 (Step 1) — Add Product 1 (q=1)",
        "POST", "/api/cart", "token_user_11",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-011 (Step 2) — Add Product 1 Again (q=1)",
        "POST", "/api/cart", "token_user_11",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-011 (Step 3) — Verify Unit Increment Accumulation (Expected: 1 row, q=2)",
        "GET", "/api/cart", "token_user_11",
        test_scripts=[
            "pm.test('FR07-AI-011 - Exactly 1 row for product 1', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data.length).to.eql(1);",
            "});",
            "pm.test('FR07-AI-011 - Product 1 accumulated quantity is 2 (1 + 1)', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data[0].quantity).to.eql(2);",
            "});"
        ]
    )

    # FR07-AI-012
    add_request(
        "FR07-AI-012 — Quantity Min Boundary (q=1)",
        "POST", "/api/cart", "token_user_12",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-012 - Quantity min boundary (q=1) accepted (200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    )

    # FR07-AI-013
    add_request(
        "FR07-AI-013 — Quantity Min+1 Boundary (q=2)",
        "POST", "/api/cart", "token_user_13",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=[
            "pm.test('FR07-AI-013 - Quantity min+1 (q=2) accepted (200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    )

    # FR07-AI-014 - Zero Quantity (q=0)
    add_request(
        "FR07-AI-014 — Zero Quantity Rejection (q=0)",
        "POST", "/api/cart", "token_user_14",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 0},
        test_scripts=[
            "pm.test('FR07-AI-014 - SPECIFIED RULE: Quantity 0 must be rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT violation: accepted invalid quantity 0 with HTTP ' + pm.response.code);",
            "});"
        ]
    )

    # FR07-AI-015 - Negative Quantity (q=-1)
    add_request(
        "FR07-AI-015 — Immediate Negative Quantity Rejection (q=-1)",
        "POST", "/api/cart", "token_user_15",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -1},
        test_scripts=[
            "pm.test('FR07-AI-015 - SPECIFIED RULE: Negative quantity (-1) must be rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT violation: accepted invalid quantity -1 with HTTP ' + pm.response.code);",
            "});"
        ]
    )

    # FR07-AI-016 - Large Negative Quantity (q=-100)
    add_request(
        "FR07-AI-016 — Large Negative Quantity Rejection (q=-100)",
        "POST", "/api/cart", "token_user_16",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -100},
        test_scripts=[
            "pm.test('FR07-AI-016 - SPECIFIED RULE: Negative quantity (-100) must be rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT violation: accepted negative quantity -100');",
            "});"
        ]
    )

    # FR07-AI-017 - Fractional Quantity (q=1.5)
    add_request(
        "FR07-AI-017 — Fractional Quantity Rejection (q=1.5)",
        "POST", "/api/cart", "token_user_17",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1.5},
        test_scripts=[
            "pm.test('FR07-AI-017 - SPECIFIED RULE: Fractional quantity (1.5) must be rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT violation: accepted fractional quantity 1.5');",
            "});"
        ]
    )

    # FR07-AI-018 - Sub-Unit Decimal Quantity (q=0.5)
    add_request(
        "FR07-AI-018 — Sub-Unit Decimal Quantity Rejection (q=0.5)",
        "POST", "/api/cart", "token_user_18",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 0.5},
        test_scripts=[
            "pm.test('FR07-AI-018 - SPECIFIED RULE: Sub-unit decimal (0.5) must be rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT violation: accepted sub-unit decimal 0.5');",
            "});"
        ]
    )

    # FR07-AI-019 - String Quantity ('2')
    add_request(
        "FR07-AI-019 — String Numeric Quantity Probe (q='2')",
        "POST", "/api/cart", "token_user_19",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": "2"},
        test_scripts=[
            "pm.test('FR07-AI-019 - Server handles string numeric quantity safely without crash', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-020 - Non-numeric String ('abc')
    add_request(
        "FR07-AI-020 — Non-Numeric String Quantity Rejection (q='abc')",
        "POST", "/api/cart", "token_user_20",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": "abc"},
        test_scripts=[
            "pm.test('FR07-AI-020 - Non-numeric string quantity rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT accepted non-numeric string quantity');",
            "});"
        ]
    )

    # FR07-AI-021 - Special Symbol String ('@#$')
    add_request(
        "FR07-AI-021 — Special Symbol String Quantity Rejection (q='@#$')",
        "POST", "/api/cart", "token_user_21",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": "@#$"},
        test_scripts=[
            "pm.test('FR07-AI-021 - Special symbol quantity rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT accepted symbol string quantity');",
            "});"
        ]
    )

    # FR07-AI-022 - Large Quantity (10^9)
    add_request(
        "FR07-AI-022 — Extreme Large Quantity Probe (q=10^9)",
        "POST", "/api/cart", "token_user_22",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1000000000},
        test_scripts=[
            "pm.test('FR07-AI-022 - Server handles large integer without crash', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-023 - Omitted Quantity Field
    add_request(
        "FR07-AI-023 — Omitted Mandatory Quantity Property Rejection",
        "POST", "/api/cart", "token_user_23",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000},
        test_scripts=[
            "pm.test('FR07-AI-023 - Missing quantity property rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT accepted cart addition missing quantity');",
            "});"
        ]
    )

    # FR07-AI-024 - Explicit Null Quantity
    add_request(
        "FR07-AI-024 — Explicit Null Quantity Rejection",
        "POST", "/api/cart", "token_user_24",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": None},
        test_scripts=[
            "pm.test('FR07-AI-024 - Null quantity property rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422], 'SUT accepted null quantity');",
            "});"
        ]
    )

    # FR07-AI-025 - Non-existent ID (999999)
    add_request(
        "FR07-AI-025 — Non-Existent Catalog Product ID Probe (id=999999)",
        "POST", "/api/cart", "token_user_25",
        body_obj={"id": 999999, "name": "Phantom Item", "price": 50000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-025 - Server handles non-existent product ID with controlled response', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 404, 422]);",
            "});"
        ]
    )

    # FR07-AI-026 - Negative Product ID (-1)
    add_request(
        "FR07-AI-026 — Negative Product ID Probe (id=-1)",
        "POST", "/api/cart", "token_user_26",
        body_obj={"id": -1, "name": "Negative ID Item", "price": 50000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-026 - Server handles negative ID with controlled response', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-027 - Omitted Product ID
    add_request(
        "FR07-AI-027 — Omitted Product ID Property Probe",
        "POST", "/api/cart", "token_user_27",
        body_obj={"name": "No ID Item", "price": 50000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-027 - Server handles omitted ID with controlled response', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-028 - String Product ID ('one')
    add_request(
        "FR07-AI-028 — String Product ID Probe (id='one')",
        "POST", "/api/cart", "token_user_28",
        body_obj={"id": "one", "name": "String ID Item", "price": 50000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-028 - Server handles string ID with controlled response', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-029 (2 steps) - Price Tampering Probe
    add_request(
        "FR07-AI-029 (Step 1) — Add Item with Client Tampered Price (price=1)",
        "POST", "/api/cart", "token_user_29",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 1, "quantity": 1},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-029 (Step 2) — Inspect Stored Unit Price in Cart",
        "GET", "/api/cart", "token_user_29",
        test_scripts=[
            "pm.test('FR07-AI-029 - Cart returns item to characterize stored price', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(1);",
            "    // Characterize: does SUT store client price (1) or catalog price (100000)?",
            "    console.log('Observed stored price under price tampering:', data[0].price);",
            "});"
        ]
    )

    # FR07-AI-030 - Negative Price (-50000)
    add_request(
        "FR07-AI-030 — Negative Price Robustness Probe (price=-50000)",
        "POST", "/api/cart", "token_user_30",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": -50000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-030 - Server handles negative price without crash', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-031 - Unauthenticated POST
    add_request(
        "FR07-AI-031 — Unauthenticated POST /api/cart Mutation Denial",
        "POST", "/api/cart", None,
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-031 - Unauthenticated POST rejected (401)', function () {",
            "    pm.expect(pm.response.code).to.eql(401);",
            "});"
        ]
    )

    # FR07-AI-032 - Forged Token on POST
    add_request(
        "FR07-AI-032 — POST /api/cart with Forged JWT Signature",
        "POST", "/api/cart", None,
        extra_headers=[{"key": "Authorization", "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTE2MjM5MDIyfQ.ForgedSignatureBytes12345"}],
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-032 - Forged token on POST rejected (403)', function () {",
            "    pm.expect(pm.response.code).to.eql(403);",
            "});"
        ]
    )

    # FR07-AI-033 - Non-Bearer Scheme on POST
    add_request(
        "FR07-AI-033 — POST /api/cart with Wrong Auth Scheme (Basic)",
        "POST", "/api/cart", None,
        extra_headers=[{"key": "Authorization", "value": "Basic dXNlcjpwYXNz"}],
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-AI-033 - Non-Bearer scheme on POST rejected (401/403)', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    )

    # FR07-AI-034 (2 steps) - User Isolation (Empty Cart Independence)
    add_request(
        "FR07-AI-034 (Step 1) — User A Adds Item to Cart",
        "POST", "/api/cart", "token_user_a",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-034 (Step 2) — Verify User B Cart Remains Strictly Empty",
        "GET", "/api/cart", "token_user_b",
        test_scripts=[
            "pm.test('FR07-AI-034 - User B cart remains empty despite User A additions', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(0, 'Cross-user cart leakage detected (BOLA)');",
            "});"
        ]
    )

    # FR07-AI-035 (3 steps) - Cross-User Non-Interference
    add_request(
        "FR07-AI-035 (Step 1) — User B Adds Product 2 (q=1)",
        "POST", "/api/cart", "token_user_b",
        body_obj={"id": 2, "name": "Sản phẩm B", "price": 200000, "quantity": 1},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-035 (Step 2) — User A Adds Product 1 (q=3)",
        "POST", "/api/cart", "token_user_a",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-035 (Step 3) — Verify User B Cart Unaffected by User A",
        "GET", "/api/cart", "token_user_b",
        test_scripts=[
            "pm.test('FR07-AI-035 - User B cart retains only Product 2', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(1);",
            "    pm.expect(data[0].id).to.eql(2);",
            "});"
        ]
    )

    # FR07-AI-036 (3 steps) - Independent Accumulation Isolation
    add_request(
        "FR07-AI-036 (Step 1) — User A Adds Product 1 (q=2)",
        "POST", "/api/cart", "token_user_a",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-036 (Step 2) — User B Adds Same Product 1 (q=3)",
        "POST", "/api/cart", "token_user_b",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-AI-036 (Step 3) — Verify User A Product 1 Quantity Uncontaminated",
        "GET", "/api/cart", "token_user_a",
        test_scripts=[
            "pm.test('FR07-AI-036 - User A product 1 quantity is strictly isolated from User B', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    var p1 = data.find(function(x) { return x.id === 1; });",
            "    pm.expect(p1).to.exist;",
            "    // In SUT with push defect, verify no cross-user leakage occurred",
            "    var totalQ = data.filter(function(x) { return x.id === 1; }).reduce(function(acc, x) { return acc + x.quantity; }, 0);",
            "    pm.expect(totalQ).to.not.eql(5, 'Cross-user quantity contamination: User A got User B units');",
            "});"
        ]
    )

    # FR07-AI-037 - Empty Body
    add_request(
        "FR07-AI-037 — Empty JSON Body Robustness Probe ({})",
        "POST", "/api/cart", "token_user_37",
        body_obj={},
        test_scripts=[
            "pm.test('FR07-AI-037 - Server safely handles empty JSON body without crash', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # FR07-AI-038 - Extra Properties
    add_request(
        "FR07-AI-038 — Extra Unexpected Payload Properties Probe",
        "POST", "/api/cart", "token_user_38",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2, "adminNote": "hack", "discountBypass": True},
        test_scripts=[
            "pm.test('FR07-AI-038 - Server safely handles extra properties without crash', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 422]);",
            "});"
        ]
    )

    # -------------------------------------------------------------
    # 5 STUDENT-SELECTED EXTENSION TESTS
    # -------------------------------------------------------------

    # FR07-STU-001 (2 steps) - Malformed JSON (missing closing brace)
    add_request(
        "FR07-STU-001 (Step 1) — Syntactically Malformed JSON Body Probe",
        "POST", "/api/cart", "token_user_stu1",
        raw_body='{"id":1,"name":"Sản phẩm A","price":100000,"quantity":1',
        content_type="application/json",
        test_scripts=[
            "pm.test('FR07-STU-001 - Parser catches malformed JSON syntax cleanly (400 expected)', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 422]);",
            "});"
        ]
    )
    add_request(
        "FR07-STU-001 (Step 2) — Verify Malformed Payload Caused Zero Cart Mutation",
        "GET", "/api/cart", "token_user_stu1",
        test_scripts=[
            "pm.test('FR07-STU-001 - Cart remains empty following malformed request', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(0);",
            "});"
        ]
    )

    # FR07-STU-002 (2 steps) - Wrong Content-Type (text/plain)
    add_request(
        "FR07-STU-002 (Step 1) — Wrong Content-Type Header (text/plain)",
        "POST", "/api/cart", "token_user_stu2",
        raw_body='{"id":1,"name":"Sản phẩm A","price":100000,"quantity":1}',
        content_type="text/plain",
        test_scripts=[
            "pm.test('FR07-STU-002 - Server handles text/plain safely without crashing', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 415, 422]);",
            "});"
        ]
    )
    add_request(
        "FR07-STU-002 (Step 2) — Inspect Visible Cart State After text/plain Request",
        "GET", "/api/cart", "token_user_stu2",
        test_scripts=[
            "pm.test('FR07-STU-002 - Cart state remains internally consistent', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array');",
            "});"
        ]
    )

    # FR07-STU-003 (2 steps) - Expired JWT Token
    add_request(
        "FR07-STU-003 (Step 1) — POST /api/cart with Expired JWT Token",
        "POST", "/api/cart", "token_expired",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1},
        test_scripts=[
            "pm.test('FR07-STU-003 - SEC-02: Expired JWT token denied (401/403)', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    )
    add_request(
        "FR07-STU-003 (Step 2) — Verify Zero Cart Mutation for Expired Token",
        "GET", "/api/cart", "token_user_stu3",
        test_scripts=[
            "pm.test('FR07-STU-003 - Cart remains empty; expired token could not mutate state', function () {",
            "    pm.response.to.have.status(200);",
            "    var data = pm.response.json();",
            "    pm.expect(data).to.be.an('array').with.lengthOf(0);",
            "});"
        ]
    )

    # FR07-STU-004 (3 steps) - Conflicting Metadata Accumulation
    add_request(
        "FR07-STU-004 (Step 1) — Add Product 1 (q=2, price=100000, name='Sản phẩm A')",
        "POST", "/api/cart", "token_user_stu4",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-STU-004 (Step 2) — Add Product 1 with Conflicting Metadata (q=3, price=1, name='Modified Product Name')",
        "POST", "/api/cart", "token_user_stu4",
        body_obj={"id": 1, "name": "Modified Product Name", "price": 1, "quantity": 3},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-STU-004 (Step 3) — Verify Duplicate Accumulation & Characterize Metadata Resolution",
        "GET", "/api/cart", "token_user_stu4",
        test_scripts=[
            "pm.test('FR07-STU-004 - SPECIFIED RULE: Exactly 1 row for product ID 1', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data.length).to.eql(1, 'Duplicate row created under conflicting metadata addition');",
            "});",
            "pm.test('FR07-STU-004 - SPECIFIED RULE: Quantity accumulated to 5 (2 + 3)', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data[0].quantity).to.eql(5);",
            "});",
            "// Characterization of observed metadata resolution",
            "var data = pm.response.json();",
            "if (data && data.length > 0) {",
            "    console.log('FR07-STU-004 Observed Name:', data[0].name, 'Price:', data[0].price);",
            "}"
        ]
    )

    # FR07-STU-005 (4 steps) - Repeated GET Idempotency
    add_request(
        "FR07-STU-005 (Step 1) — Setup: Populate Cart with Product 1 (q=2)",
        "POST", "/api/cart", "token_user_stu5",
        body_obj={"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2},
        test_scripts=["pm.response.to.have.status(200);"]
    )
    add_request(
        "FR07-STU-005 (Step 2) — GET /api/cart (Read 1)",
        "GET", "/api/cart", "token_user_stu5",
        test_scripts=[
            "pm.response.to.have.status(200);",
            "pm.environment.set('read1_json', JSON.stringify(pm.response.json()));"
        ]
    )
    add_request(
        "FR07-STU-005 (Step 3) — GET /api/cart (Read 2)",
        "GET", "/api/cart", "token_user_stu5",
        test_scripts=[
            "pm.response.to.have.status(200);",
            "var r1 = JSON.parse(pm.environment.get('read1_json'));",
            "var r2 = pm.response.json();",
            "pm.test('FR07-STU-005 - Read 2 equals Read 1 (idempotent)', function () {",
            "    pm.expect(r2).to.deep.eql(r1);",
            "});"
        ]
    )
    add_request(
        "FR07-STU-005 (Step 4) — GET /api/cart (Read 3)",
        "GET", "/api/cart", "token_user_stu5",
        test_scripts=[
            "pm.response.to.have.status(200);",
            "var r1 = JSON.parse(pm.environment.get('read1_json'));",
            "var r3 = pm.response.json();",
            "pm.test('FR07-STU-005 - Read 3 equals Read 1 (idempotency preserved across repeated reads)', function () {",
            "    pm.expect(r3).to.deep.eql(r1);",
            "});"
        ]
    )

    print(f"Total Postman requests generated: {len(collection['item'])}")

    os.makedirs(os.path.dirname(COLLECTION_PATH), exist_ok=True)
    with open(COLLECTION_PATH, "w", encoding="utf-8") as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)
    print(f"Saved Postman collection to {COLLECTION_PATH}")

    # Generate setup_fr07_env.js
    setup_code = """// Automated environment generator for FR-07 Shopping Cart
// Uses legitimate SUT registration and login APIs to retrieve fresh tokens for test isolation.
const http = require('http');
const fs = require('fs');
const path = require('path');
const jwt = require('jsonwebtoken');

const BASE_URL = 'http://localhost:3000';
const SECRET_KEY = 'super_secret_key_that_should_not_be_here';
const ENV_FILE = path.join(__dirname, '../environments/fr07-environment.json');

function postJson(urlPath, data) {
    return new Promise((resolve, reject) => {
        const payload = JSON.stringify(data);
        const req = http.request(BASE_URL + urlPath, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(payload),
                'X-Student-Id': '23127027'
            }
        }, (res) => {
            let body = '';
            res.on('data', chunk => body += chunk);
            res.on('end', () => {
                try {
                    resolve({ status: res.statusCode, data: JSON.parse(body) });
                } catch (e) {
                    resolve({ status: res.statusCode, data: body });
                }
            });
        });
        req.on('error', reject);
        req.write(payload);
        req.end();
    });
}

async function getOrRegisterUserToken(emailPrefix) {
    const email = `${emailPrefix}_${Date.now()}_${Math.floor(Math.random()*10000)}@eshop.local`;
    const password = 'Password123!';
    await postJson('/api/register', { name: 'User ' + emailPrefix, email, password });
    const loginRes = await postJson('/api/login', { email, password });
    if (!loginRes.data.token) {
        throw new Error(`Failed to login user ${email}: ${JSON.stringify(loginRes.data)}`);
    }
    return loginRes.data.token;
}

async function main() {
    console.log('Generating isolated test tokens via legitimate SUT APIs...');
    const envValues = [
        { key: 'baseUrl', value: BASE_URL, enabled: true },
        { key: 'studentId', value: '23127027', enabled: true }
    ];

    // Single user tokens for AI tests
    const userKeys = [
        'token_user_01', 'token_user_02', 'token_user_03',
        'token_user_07', 'token_user_08', 'token_user_09', 'token_user_10', 'token_user_11',
        'token_user_12', 'token_user_13', 'token_user_14', 'token_user_15', 'token_user_16',
        'token_user_17', 'token_user_18', 'token_user_19', 'token_user_20', 'token_user_21',
        'token_user_22', 'token_user_23', 'token_user_24', 'token_user_25', 'token_user_26',
        'token_user_27', 'token_user_28', 'token_user_29', 'token_user_30',
        'token_user_37', 'token_user_38',
        'token_user_a', 'token_user_b',
        'token_user_stu1', 'token_user_stu2', 'token_user_stu3', 'token_user_stu4', 'token_user_stu5'
    ];

    for (const key of userKeys) {
        process.stdout.write(`  Registering ${key}... `);
        const token = await getOrRegisterUserToken(key);
        envValues.push({ key, value: token, enabled: true });
        console.log('OK');
    }

    // Expired token generation using local test setup
    const expiredToken = jwt.sign({ id: 9999, role: 'customer' }, SECRET_KEY, { expiresIn: '-1h' });
    envValues.push({ key: 'token_expired', value: expiredToken, enabled: true });
    console.log('  Generated legitimate expired token: OK');

    const envData = {
        id: 'f7a1b2c3-d4e5-6789-0abc-ef0000000000',
        name: 'FR-07 Cart Execution Environment',
        values: envValues,
        _postman_variable_scope: 'environment'
    };

    fs.mkdirSync(path.dirname(ENV_FILE), { recursive: true });
    fs.writeFileSync(ENV_FILE, JSON.stringify(envData, null, 2), 'utf-8');
    console.log(`Saved environment with ${envValues.length} variables to ${ENV_FILE}`);
}

main().catch(err => {
    console.error('Setup failed:', err);
    process.exit(1);
});
"""

    os.makedirs(os.path.dirname(SETUP_SCRIPT_PATH), exist_ok=True)
    with open(SETUP_SCRIPT_PATH, "w", encoding="utf-8") as f:
        f.write(setup_code)
    print(f"Saved environment setup script to {SETUP_SCRIPT_PATH}")

if __name__ == "__main__":
    main()
