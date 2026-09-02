#!/usr/bin/env python3
"""
Generate Postman Collection v2.1.0 for FR-12 Access Control Test Suite.
Automates 38 Reviewed AI Test Cases + 5 Student Extension Test Cases.
Author: Pham Ngoc Gia Bao (23127027)
"""

import json
import os

def create_request(name, method, url_path, headers, body_obj=None, tests=None, description=""):
    header_list = []
    for k, v in headers.items():
        header_list.append({"key": k, "value": v, "type": "text"})
        
    req = {
        "name": name,
        "request": {
            "method": method,
            "header": header_list,
            "url": {
                "raw": "{{baseUrl}}" + url_path,
                "host": ["{{baseUrl}}"],
                "path": [p for p in url_path.split("/") if p]
            },
            "description": description
        }
    }
    
    if body_obj is not None:
        req["request"]["body"] = {
            "mode": "raw",
            "raw": json.dumps(body_obj, indent=2),
            "options": {"raw": {"language": "json"}}
        }
        
    if tests:
        req["event"] = [{
            "listen": "test",
            "script": {
                "type": "text/javascript",
                "exec": tests
            }
        }]
        
    return req

def build_collection():
    collection = {
        "info": {
            "_postman_id": "fr12-access-control-23127027",
            "name": "FR-12 — Access Control Test Suite",
            "description": "Automated test suite for FR-12 Access Control (HCMUS EShop SUT). Created for HW06 API Testing by student Pham Ngoc Gia Bao (23127027). Automates 38 reviewed AI test cases + 5 student extension test cases (43 testcase designs across 59 HTTP requests).",
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

    # =========================================================================
    # Folder 1: Standard-User Role Denial (SEC-03) — FR12-AI-001 to FR12-AI-014
    # =========================================================================
    f1_items = []
    
    # 001: GET /api/admin/users
    f1_items.append(create_request(
        "FR12-AI-001 — Standard User GET /api/admin/users",
        "GET", "/api/admin/users",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-001 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});",
            "pm.test('FR12-AI-001 - User management records not exposed', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))
    
    # 002: DELETE /api/admin/users/:id
    f1_items.append(create_request(
        "FR12-AI-002 — Standard User DELETE /api/admin/users/:id",
        "DELETE", "/api/admin/users/50",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-002 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-002 (Verify) — Verify Target User Persists & Can Login",
        "POST", "/api/login",
        {"Content-Type": "application/json"},
        {"email": "disp002@example.com", "password": "dispPassword1!"},
        [
            "pm.test('FR12-AI-002 (Verify) - Side-effect check: target user still exists and can login', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 003: GET /api/admin/orders
    f1_items.append(create_request(
        "FR12-AI-003 — Standard User GET /api/admin/orders",
        "GET", "/api/admin/orders",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-003 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});",
            "pm.test('FR12-AI-003 - System-wide order records not exposed', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))

    # 004: PUT /api/admin/orders/:id/status
    f1_items.append(create_request(
        "FR12-AI-004 — Standard User PUT /api/admin/orders/:id/status",
        "PUT", "/api/admin/orders/101/status",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"status": "confirmed"},
        [
            "pm.test('FR12-AI-004 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-004 (Verify) — Verify Order Status Remains Unchanged",
        "GET", "/api/orders/101",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-004 (Verify) - Side-effect check: order status remains pending', function () {",
            "    var data = pm.response.json();",
            "    pm.expect(data.status).to.eql('pending');",
            "});"
        ]
    ))

    # 005: POST /api/admin/import-products
    f1_items.append(create_request(
        "FR12-AI-005 — Standard User POST /api/admin/import-products",
        "POST", "/api/admin/import-products",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"products": [{"name": "ImportProbe_23127027", "price": 100000, "category_id": 1}]},
        [
            "pm.test('FR12-AI-005 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-005 (Verify) — Verify ImportProbe_23127027 Not Added",
        "GET", "/api/products",
        {},
        None,
        [
            "pm.test('FR12-AI-005 (Verify) - Side-effect check: ImportProbe_23127027 absent from catalog', function () {",
            "    var products = pm.response.json();",
            "    var found = products.some(p => p.name === 'ImportProbe_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # 006: POST /api/admin/coupons
    f1_items.append(create_request(
        "FR12-AI-006 — Standard User POST /api/admin/coupons",
        "POST", "/api/admin/coupons",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"code": "HACK23127027", "discountPercent": 50, "validUntil": "2026-12-31T23:59:59Z"},
        [
            "pm.test('FR12-AI-006 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-006 (Verify) — Verify Coupon HACK23127027 Not Created",
        "GET", "/api/coupons",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-006 (Verify) - Side-effect check: HACK23127027 absent from coupon list', function () {",
            "    var coupons = pm.response.json();",
            "    var found = Array.isArray(coupons) && coupons.some(c => c.code === 'HACK23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # 007: DELETE /api/admin/coupons/:id
    f1_items.append(create_request(
        "FR12-AI-007 — Standard User DELETE /api/admin/coupons/:id",
        "DELETE", "/api/admin/coupons/50",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-007 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-007 (Verify) — Verify Disposable Coupon 50 Remains Intact",
        "GET", "/api/coupons",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-007 (Verify) - Side-effect check: coupon 50 remains present in database', function () {",
            "    var coupons = pm.response.json();",
            "    var found = Array.isArray(coupons) && coupons.some(c => c.id === 50);",
            "    pm.expect(found).to.be.true;",
            "});"
        ]
    ))

    # 008: POST /api/products
    f1_items.append(create_request(
        "FR12-AI-008 — Standard User POST /api/products",
        "POST", "/api/products",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"name": "UnauthorizedProduct_23127027", "price": 50000, "category_id": 1},
        [
            "pm.test('FR12-AI-008 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-008 (Verify) — Verify UnauthorizedProduct_23127027 Absent",
        "GET", "/api/products",
        {},
        None,
        [
            "pm.test('FR12-AI-008 (Verify) - Side-effect check: UnauthorizedProduct_23127027 absent from catalog', function () {",
            "    var products = pm.response.json();",
            "    var found = Array.isArray(products) && products.some(p => p.name === 'UnauthorizedProduct_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # 009: PUT /api/products/:id
    f1_items.append(create_request(
        "FR12-AI-009 — Standard User PUT /api/products/:id",
        "PUT", "/api/products/50",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"name": "DispProduct_009_MOD", "price": 999999, "category_id": 1},
        [
            "pm.test('FR12-AI-009 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-009 (Verify) — Verify Product 50 Price Unchanged",
        "GET", "/api/products/50",
        {},
        None,
        [
            "pm.test('FR12-AI-009 (Verify) - Side-effect check: product 50 price unchanged (remains 100000)', function () {",
            "    var p = pm.response.json();",
            "    pm.expect(Number(p.price)).to.eql(100000);",
            "});"
        ]
    ))

    # 010: DELETE /api/products/:id
    f1_items.append(create_request(
        "FR12-AI-010 — Standard User DELETE /api/products/:id",
        "DELETE", "/api/products/51",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-010 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-010 (Verify) — Verify Product 51 Still Exists",
        "GET", "/api/products/51",
        {},
        None,
        [
            "pm.test('FR12-AI-010 (Verify) - Side-effect check: product 51 still exists in database', function () {",
            "    var p = pm.response.json();",
            "    pm.expect(p.id).to.eql(51);",
            "});"
        ]
    ))

    # 011: POST /api/categories
    f1_items.append(create_request(
        "FR12-AI-011 — Standard User POST /api/categories",
        "POST", "/api/categories",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"name": "UserCategory_23127027"},
        [
            "pm.test('FR12-AI-011 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-011 (Verify) — Verify UserCategory_23127027 Absent",
        "GET", "/api/categories",
        {},
        None,
        [
            "pm.test('FR12-AI-011 (Verify) - Side-effect check: UserCategory_23127027 absent from categories', function () {",
            "    var categories = pm.response.json();",
            "    var found = Array.isArray(categories) && categories.some(c => c.name === 'UserCategory_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # 012: PUT /api/categories/:id
    f1_items.append(create_request(
        "FR12-AI-012 — Standard User PUT /api/categories/:id",
        "PUT", "/api/categories/50",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"name": "DispCategory_012_MOD"},
        [
            "pm.test('FR12-AI-012 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-012 (Verify) — Verify Category 50 Name Unchanged",
        "GET", "/api/categories",
        {},
        None,
        [
            "pm.test('FR12-AI-012 (Verify) - Side-effect check: category 50 name unchanged', function () {",
            "    var categories = pm.response.json();",
            "    var cat = Array.isArray(categories) && categories.find(c => c.id === 50);",
            "    pm.expect(cat && cat.name).to.eql('DispCategory_012');",
            "});"
        ]
    ))

    # 013: DELETE /api/categories/:id
    f1_items.append(create_request(
        "FR12-AI-013 — Standard User DELETE /api/categories/:id",
        "DELETE", "/api/categories/51",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-013 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f1_items.append(create_request(
        "FR12-AI-013 (Verify) — Verify Category 51 Still Exists",
        "GET", "/api/categories",
        {},
        None,
        [
            "pm.test('FR12-AI-013 (Verify) - Side-effect check: category 51 still exists', function () {",
            "    var categories = pm.response.json();",
            "    var found = Array.isArray(categories) && categories.some(c => c.id === 51);",
            "    pm.expect(found).to.be.true;",
            "});"
        ]
    ))

    # 014: GET /api/coupons
    f1_items.append(create_request(
        "FR12-AI-014 — Standard User GET /api/coupons",
        "GET", "/api/coupons",
        {"Authorization": "Bearer {{userToken}}"},
        None,
        [
            "pm.test('FR12-AI-014 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});",
            "pm.test('FR12-AI-014 - Administrative coupon listing not disclosed to standard user', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))
    
    collection["item"].append({
        "name": "Folder 1 — Standard-User Role Denial (SEC-03)",
        "item": f1_items
    })

    # =========================================================================
    # Folder 2: Valid Administrator Access Clearance (FR-12) — FR12-AI-015 to FR12-AI-028
    # =========================================================================
    f2_items = []
    
    # 015: Admin GET /api/admin/users
    f2_items.append(create_request(
        "FR12-AI-015 — Admin GET /api/admin/users",
        "GET", "/api/admin/users",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-015 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});",
            "pm.test('FR12-AI-015 - Response contains user records array', function () {",
            "    var users = pm.response.json();",
            "    pm.expect(users).to.be.an('array');",
            "    pm.expect(users.length).to.be.at.least(1);",
            "});"
        ]
    ))

    # 016: Admin DELETE /api/admin/users/:id
    f2_items.append(create_request(
        "FR12-AI-016 — Admin DELETE /api/admin/users/:id",
        "DELETE", "/api/admin/users/51",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-016 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))
    f2_items.append(create_request(
        "FR12-AI-016 (Verify) — Verify Deleted User Cannot Authenticate",
        "POST", "/api/login",
        {"Content-Type": "application/json"},
        {"email": "disp016@example.com", "password": "dispPassword2!"},
        [
            "pm.test('FR12-AI-016 (Verify) - Side-effect check: deleted user can no longer authenticate', function () {",
            "    pm.response.to.not.have.status(200);",
            "});"
        ]
    ))

    # 017: Admin GET /api/admin/orders
    f2_items.append(create_request(
        "FR12-AI-017 — Admin GET /api/admin/orders",
        "GET", "/api/admin/orders",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-017 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});",
            "pm.test('FR12-AI-017 - Response contains system order records array', function () {",
            "    var orders = pm.response.json();",
            "    pm.expect(orders).to.be.an('array');",
            "});"
        ]
    ))

    # 018: Admin PUT /api/admin/orders/:id/status
    f2_items.append(create_request(
        "FR12-AI-018 — Admin PUT /api/admin/orders/:id/status",
        "PUT", "/api/admin/orders/102/status",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"status": "confirmed"},
        [
            "pm.test('FR12-AI-018 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 019: Admin POST /api/admin/import-products
    f2_items.append(create_request(
        "FR12-AI-019 — Admin POST /api/admin/import-products",
        "POST", "/api/admin/import-products",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"products": [{"name": "AdminImport_23127027", "price": 150000, "category_id": 1}]},
        [
            "pm.test('FR12-AI-019 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 020: Admin POST /api/admin/coupons
    f2_items.append(create_request(
        "FR12-AI-020 — Admin POST /api/admin/coupons",
        "POST", "/api/admin/coupons",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"code": "ADMINCPN_23127027", "discountPercent": 15, "validUntil": "2026-12-31T23:59:59Z"},
        [
            "pm.test('FR12-AI-020 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 021: Admin DELETE /api/admin/coupons/:id
    f2_items.append(create_request(
        "FR12-AI-021 — Admin DELETE /api/admin/coupons/:id",
        "DELETE", "/api/admin/coupons/51",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-021 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 022: Admin POST /api/products
    f2_items.append(create_request(
        "FR12-AI-022 — Admin POST /api/products",
        "POST", "/api/products",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"name": "AdminProduct_23127027", "price": 250000, "category_id": 1},
        [
            "pm.test('FR12-AI-022 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 023: Admin PUT /api/products/:id
    f2_items.append(create_request(
        "FR12-AI-023 — Admin PUT /api/products/:id",
        "PUT", "/api/products/52",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"name": "DispProduct_023_MOD", "price": 222222, "category_id": 1},
        [
            "pm.test('FR12-AI-023 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 024: Admin DELETE /api/products/:id
    f2_items.append(create_request(
        "FR12-AI-024 — Admin DELETE /api/products/:id",
        "DELETE", "/api/products/53",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-024 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 025: Admin POST /api/categories
    f2_items.append(create_request(
        "FR12-AI-025 — Admin POST /api/categories",
        "POST", "/api/categories",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"name": "AdminCategory_23127027"},
        [
            "pm.test('FR12-AI-025 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 026: Admin PUT /api/categories/:id
    f2_items.append(create_request(
        "FR12-AI-026 — Admin PUT /api/categories/:id",
        "PUT", "/api/categories/52",
        {"Authorization": "Bearer {{adminToken}}", "Content-Type": "application/json"},
        {"name": "DispCategory_026_MOD"},
        [
            "pm.test('FR12-AI-026 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 027: Admin DELETE /api/categories/:id
    f2_items.append(create_request(
        "FR12-AI-027 — Admin DELETE /api/categories/:id",
        "DELETE", "/api/categories/53",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-027 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});"
        ]
    ))

    # 028: Admin GET /api/coupons
    f2_items.append(create_request(
        "FR12-AI-028 — Admin GET /api/coupons",
        "GET", "/api/coupons",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-AI-028 - Admin clearance permitted (Status 200 OK)', function () {",
            "    pm.response.to.have.status(200);",
            "});",
            "pm.test('FR12-AI-028 - Master coupons array returned', function () {",
            "    var coupons = pm.response.json();",
            "    pm.expect(coupons).to.be.an('array');",
            "});"
        ]
    ))
    
    collection["item"].append({
        "name": "Folder 2 — Valid Administrator Access Clearance (FR-12)",
        "item": f2_items
    })

    # =========================================================================
    # Folder 3: Anonymous / Missing JWT Denial (SEC-02) — FR12-AI-029 to FR12-AI-034
    # =========================================================================
    f3_items = []
    
    # 029: Anonymous POST /api/products
    f3_items.append(create_request(
        "FR12-AI-029 — Anonymous POST /api/products",
        "POST", "/api/products",
        {"Content-Type": "application/json"},
        {"name": "AnonProduct_23127027", "price": 70000, "category_id": 1},
        [
            "pm.test('FR12-AI-029 - Semantic Access Denied (SEC-02 / 401 Unauthorized)', function () {",
            "    pm.response.to.have.status(401);",
            "});"
        ]
    ))
    f3_items.append(create_request(
        "FR12-AI-029 (Verify) — Verify AnonProduct_23127027 Absent",
        "GET", "/api/products",
        {},
        None,
        [
            "pm.test('FR12-AI-029 (Verify) - Side-effect check: AnonProduct_23127027 absent from catalog', function () {",
            "    var products = pm.response.json();",
            "    var found = Array.isArray(products) && products.some(p => p.name === 'AnonProduct_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # 030: Anonymous PUT /api/products/:id
    f3_items.append(create_request(
        "FR12-AI-030 — Anonymous PUT /api/products/:id",
        "PUT", "/api/products/54",
        {"Content-Type": "application/json"},
        {"name": "AnonProduct_030_MOD", "price": 99999, "category_id": 1},
        [
            "pm.test('FR12-AI-030 - Semantic Access Denied (SEC-02 / 401 Unauthorized)', function () {",
            "    pm.response.to.have.status(401);",
            "});"
        ]
    ))

    # 031: Anonymous DELETE /api/products/:id
    f3_items.append(create_request(
        "FR12-AI-031 — Anonymous DELETE /api/products/:id",
        "DELETE", "/api/products/55",
        {},
        None,
        [
            "pm.test('FR12-AI-031 - Semantic Access Denied (SEC-02 / 401 Unauthorized)', function () {",
            "    pm.response.to.have.status(401);",
            "});"
        ]
    ))

    # 032: Anonymous GET /api/admin/users
    f3_items.append(create_request(
        "FR12-AI-032 — Anonymous GET /api/admin/users",
        "GET", "/api/admin/users",
        {},
        None,
        [
            "pm.test('FR12-AI-032 - Semantic Access Denied (SEC-02 / 401 Unauthorized)', function () {",
            "    pm.response.to.have.status(401);",
            "});",
            "pm.test('FR12-AI-032 - User records not exposed to unauthenticated caller', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))

    # 033: Anonymous POST /api/categories
    f3_items.append(create_request(
        "FR12-AI-033 — Anonymous POST /api/categories",
        "POST", "/api/categories",
        {"Content-Type": "application/json"},
        {"name": "AnonCategory_23127027"},
        [
            "pm.test('FR12-AI-033 - Semantic Access Denied (SEC-02 / 401 Unauthorized)', function () {",
            "    pm.response.to.have.status(401);",
            "});"
        ]
    ))
    f3_items.append(create_request(
        "FR12-AI-033 (Verify) — Verify AnonCategory_23127027 Absent",
        "GET", "/api/categories",
        {},
        None,
        [
            "pm.test('FR12-AI-033 (Verify) - Side-effect check: AnonCategory_23127027 absent from categories', function () {",
            "    var categories = pm.response.json();",
            "    var found = Array.isArray(categories) && categories.some(c => c.name === 'AnonCategory_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # 034: Anonymous GET /api/coupons
    f3_items.append(create_request(
        "FR12-AI-034 — Anonymous GET /api/coupons",
        "GET", "/api/coupons",
        {},
        None,
        [
            "pm.test('FR12-AI-034 - Semantic Access Denied (SEC-02 / 401 Unauthorized)', function () {",
            "    pm.response.to.have.status(401);",
            "});",
            "pm.test('FR12-AI-034 - Coupon records not exposed to unauthenticated caller', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))
    
    collection["item"].append({
        "name": "Folder 3 — Anonymous / Missing JWT Denial (SEC-02)",
        "item": f3_items
    })

    # =========================================================================
    # Folder 4: Token Boundary & Cryptographic Robustness — FR12-AI-035 to FR12-AI-038
    # =========================================================================
    f4_items = []
    
    # 035: Expired Token GET /api/admin/users
    f4_items.append(create_request(
        "FR12-AI-035 — Expired Token GET /api/admin/users",
        "GET", "/api/admin/users",
        {"Authorization": "Bearer {{expiredAdminToken}}"},
        None,
        [
            "pm.test('FR12-AI-035 - Semantic Access Denied (SEC-02 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});",
            "pm.test('FR12-AI-035 - Expired token rejected by JWT verification', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))

    # 036: Forged Signature GET /api/admin/orders
    f4_items.append(create_request(
        "FR12-AI-036 — Forged Signature GET /api/admin/orders",
        "GET", "/api/admin/orders",
        {"Authorization": "Bearer {{forgedToken}}"},
        None,
        [
            "pm.test('FR12-AI-036 - Semantic Access Denied (SEC-02 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});",
            "pm.test('FR12-AI-036 - Invalid HMAC signature rejected', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))

    # 037: Missing Role Claim POST /api/admin/coupons
    f4_items.append(create_request(
        "FR12-AI-037 — Missing Role Claim POST /api/admin/coupons",
        "POST", "/api/admin/coupons",
        {"Authorization": "Bearer {{missingRoleToken}}", "Content-Type": "application/json"},
        {"code": "NOROLE_CPN_23127027", "discountPercent": 10, "validUntil": "2026-12-31T23:59:59Z"},
        [
            "pm.test('FR12-AI-037 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))

    # 038: Uppercase Role 'ADMIN' DELETE /api/admin/users/:id
    f4_items.append(create_request(
        "FR12-AI-038 — Uppercase Role 'ADMIN' DELETE /api/admin/users/:id",
        "DELETE", "/api/admin/users/52",
        {"Authorization": "Bearer {{uppercaseRoleToken}}"},
        None,
        [
            "pm.test('FR12-AI-038 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    
    collection["item"].append({
        "name": "Folder 4 — Token Boundary & Role Inspection",
        "item": f4_items
    })

    # =========================================================================
    # Folder 5: Student Extension Security Probes — FR12-STU-001 to FR12-STU-005
    # =========================================================================
    f5_items = []
    
    # STU-001: Unsigned alg=none
    f5_items.append(create_request(
        "FR12-STU-001 — Unsigned JWT alg=none GET /api/admin/users",
        "GET", "/api/admin/users",
        {"Authorization": "Bearer {{unsignedAlgNoneToken}}"},
        None,
        [
            "pm.test('FR12-STU-001 - Semantic Access Denied (SEC-02 / 401 or 403)', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))

    # STU-002: Future nbf claim
    f5_items.append(create_request(
        "FR12-STU-002 — Future nbf Claim GET /api/admin/orders",
        "GET", "/api/admin/orders",
        {"Authorization": "Bearer {{futureNbfToken}}"},
        None,
        [
            "pm.test('FR12-STU-002 - Semantic Access Denied (SEC-02 / 401 or 403)', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([401, 403]);",
            "});"
        ]
    ))

    # STU-003: Whitespace role ' admin '
    f5_items.append(create_request(
        "FR12-STU-003 — Whitespace Role ' admin ' POST /api/admin/coupons",
        "POST", "/api/admin/coupons",
        {"Authorization": "Bearer {{whitespaceRoleToken}}", "Content-Type": "application/json"},
        {"code": "WSROLE_23127027", "discountPercent": 15, "validUntil": "2026-12-31T23:59:59Z"},
        [
            "pm.test('FR12-STU-003 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f5_items.append(create_request(
        "FR12-STU-003 (Verify) — Verify WSROLE_23127027 Absent",
        "GET", "/api/coupons",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-STU-003 (Verify) - Side-effect check: WSROLE_23127027 not in coupon list', function () {",
            "    var coupons = pm.response.json();",
            "    var found = Array.isArray(coupons) && coupons.some(c => c.code === 'WSROLE_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))

    # STU-004: Array role ['admin']
    f5_items.append(create_request(
        "FR12-STU-004 — Array Role ['admin'] GET /api/admin/users",
        "GET", "/api/admin/users",
        {"Authorization": "Bearer {{arrayRoleToken}}"},
        None,
        [
            "pm.test('FR12-STU-004 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))

    # STU-005: Request body role='admin' override
    f5_items.append(create_request(
        "FR12-STU-005 — Body Role Override POST /api/admin/coupons",
        "POST", "/api/admin/coupons",
        {"Authorization": "Bearer {{userToken}}", "Content-Type": "application/json"},
        {"code": "BODYOVERRIDE_23127027", "discountPercent": 25, "validUntil": "2026-12-31T23:59:59Z", "role": "admin"},
        [
            "pm.test('FR12-STU-005 - Semantic Access Denied (SEC-03 / 403 Forbidden)', function () {",
            "    pm.response.to.have.status(403);",
            "});"
        ]
    ))
    f5_items.append(create_request(
        "FR12-STU-005 (Verify) — Verify BODYOVERRIDE_23127027 Absent",
        "GET", "/api/coupons",
        {"Authorization": "Bearer {{adminToken}}"},
        None,
        [
            "pm.test('FR12-STU-005 (Verify) - Side-effect check: BODYOVERRIDE_23127027 not in coupon list', function () {",
            "    var coupons = pm.response.json();",
            "    var found = Array.isArray(coupons) && coupons.some(c => c.code === 'BODYOVERRIDE_23127027');",
            "    pm.expect(found).to.be.false;",
            "});"
        ]
    ))
    
    collection["item"].append({
        "name": "Folder 5 — Student Extension Security Probes",
        "item": f5_items
    })

    # Count total requests
    total_reqs = sum(len(f["item"]) for f in collection["item"])
    print(f"Total Folders: {len(collection['item'])}, Total HTTP Requests: {total_reqs}")

    output_path = "hw06/postman/collections/fr12-access-control.postman_collection.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(collection, f, indent=2)
    print(f"Saved collection to {output_path}")

if __name__ == "__main__":
    build_collection()
