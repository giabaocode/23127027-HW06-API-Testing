#!/usr/bin/env python3
"""
Generate and validate the 38 AI test cases for FR-07 Shopping Cart.
Adheres strictly to the reviewed spec-analysis.md and coverage-matrix.md.
"""
import os
import json
import re

TESTS = [
    # COV-FR07-01: Empty cart baseline (1 test)
    {
        "id": "FR07-AI-001",
        "cov_id": "COV-FR07-01",
        "endpoints": "GET /api/cart",
        "req_ref": "FR-07 / README.md L100",
        "sec_ref": "SEC-02 (Authenticated Session)",
        "source_ref": "README.md L100, api_specification.md L115",
        "oracle_class": "INFERRED / IMPLEMENTATION-OBSERVED",
        "category": "Positive Functional / State Baseline",
        "objective": "Verify newly registered user starts with an empty shopping cart",
        "condition": "Authenticated user with no prior cart additions sends GET /api/cart",
        "partition": "P_E1 (Initial Empty State)",
        "preconditions": "User account registered and authenticated with valid JWT token",
        "initial_state": "Cart is empty (0 items)",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Return empty collection representing absence of items in user cart",
        "expected_status": "200 OK (INFERRED)",
        "expected_contract": "JSON array with length 0: []",
        "state_assertion": "Cart remains empty (length 0)",
        "sec_assertion": "Access granted only with valid JWT",
        "setup": "Register and log in fresh test user",
        "cleanup": "None required (fresh user)"
    },

    # COV-FR07-02: Populated cart retrieval (2 tests)
    {
        "id": "FR07-AI-002",
        "cov_id": "COV-FR07-02",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / api_specification.md L115",
        "sec_ref": "SEC-02 (Authenticated Session)",
        "source_ref": "api_specification.md L115-127",
        "oracle_class": "INFERRED",
        "category": "Positive Functional / State Verification",
        "objective": "Verify GET /api/cart correctly reflects a single added product item",
        "condition": "Add 1 product (id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2) then retrieve cart",
        "partition": "P_E2 (Single Item Cart)",
        "preconditions": "Authenticated user with initially empty cart",
        "initial_state": "Cart is empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Cart returns an array containing exactly the single added item with matching properties",
        "expected_status": "POST: 200 OK (INFERRED); GET: 200 OK (INFERRED)",
        "expected_contract": "Array of objects: [{ id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2 }]",
        "state_assertion": "Cart array length === 1; item[0].id === 1; item[0].quantity === 2",
        "sec_assertion": "Session isolation maintained",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-003",
        "cov_id": "COV-FR07-02",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / api_specification.md L115",
        "sec_ref": "SEC-02 (Authenticated Session)",
        "source_ref": "api_specification.md L115-127, README.md L95",
        "oracle_class": "INFERRED",
        "category": "Positive Functional / Multi-Item State",
        "objective": "Verify GET /api/cart correctly reflects multiple distinct added products",
        "condition": "Add Product 1 (q=1) and Product 2 (q=3) then retrieve cart",
        "partition": "P_E4 (Multi-Item Heterogeneous Cart)",
        "preconditions": "Authenticated user with initially empty cart",
        "initial_state": "Cart is empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 2, "name": "Sản phẩm B", "price": 150000, "quantity": 3}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Cart returns an array containing both distinct product items with their respective quantities",
        "expected_status": "POST calls: 200 OK (INFERRED); GET: 200 OK (INFERRED)",
        "expected_contract": "Array of 2 objects containing distinct items with id 1 and id 2",
        "state_assertion": "Cart array length === 2; both product entries retained independently",
        "sec_assertion": "Session isolation maintained",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-03: GET Missing Auth Token (1 test)
    {
        "id": "FR07-AI-004",
        "cov_id": "COV-FR07-03",
        "endpoints": "GET /api/cart",
        "req_ref": "SEC-02 / api_specification.md L112",
        "sec_ref": "SEC-02 (Mandatory JWT for Secured APIs)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)",
        "category": "Security / Authentication Barrier",
        "objective": "Verify GET /api/cart rejects request when Authorization header is completely omitted",
        "condition": "Send GET /api/cart with no Authorization header",
        "partition": "P_A2 (Missing Token)",
        "preconditions": "Server running",
        "initial_state": "N/A",
        "auth_state": "Unauthenticated (No token)",
        "requests": [
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Access denied; cart information not exposed to unauthenticated callers",
        "expected_status": "401 Unauthorized (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)",
        "expected_contract": "JSON error payload indicating unauthenticated access",
        "state_assertion": "No user cart state inspected or leaked",
        "sec_assertion": "SEC-02 enforced: protected resource denies unauthenticated request",
        "setup": "None",
        "cleanup": "None"
    },

    # COV-FR07-04: GET Invalid Token (2 tests)
    {
        "id": "FR07-AI-005",
        "cov_id": "COV-FR07-04",
        "endpoints": "GET /api/cart",
        "req_ref": "SEC-02 / api_specification.md L112",
        "sec_ref": "SEC-02 (Mandatory JWT for Secured APIs)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)",
        "category": "Security / Token Verification",
        "objective": "Verify GET /api/cart rejects request with forged or tamper-corrupted JWT signature",
        "condition": "Send GET /api/cart with JWT token having an invalid HMAC signature",
        "partition": "P_A3 (Invalid Signature Token)",
        "preconditions": "Server running with SECRET_KEY",
        "initial_state": "N/A",
        "auth_state": "Invalid JWT token (corrupted signature)",
        "requests": [
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTE2MjM5MDIyfQ.InvalidSignatureStringForTesting", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Access denied; forged or invalid token rejected",
        "expected_status": "403 Forbidden (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)",
        "expected_contract": "JSON error payload: { error: 'Forbidden' }",
        "state_assertion": "No user cart state accessed",
        "sec_assertion": "SEC-02 cryptographic signature verification enforced",
        "setup": "None",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-006",
        "cov_id": "COV-FR07-04",
        "endpoints": "GET /api/cart",
        "req_ref": "SEC-02 / api_specification.md L112",
        "sec_ref": "SEC-02 (Mandatory JWT for Secured APIs)",
        "source_ref": "api_specification.md L112",
        "oracle_class": "ROBUSTNESS / SPECIFIED REJECTION",
        "category": "Security / Header Format Robustness",
        "objective": "Verify GET /api/cart rejects Authorization header lacking the 'Bearer ' scheme prefix",
        "condition": "Send GET /api/cart with raw token string without 'Bearer ' prefix",
        "partition": "P_A5 (Malformed Authorization Scheme)",
        "preconditions": "Server running",
        "initial_state": "N/A",
        "auth_state": "Malformed Authorization header scheme",
        "requests": [
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "RawTokenWithoutBearerPrefix12345", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Access denied; non-Bearer scheme rejected cleanly",
        "expected_status": "401 / 403 (INFERRED FROM MIDDLEWARE; official status UNKNOWN)",
        "expected_contract": "JSON error payload",
        "state_assertion": "No user cart state accessed",
        "sec_assertion": "SEC-02 scheme enforcement",
        "setup": "None",
        "cleanup": "None"
    },

    # COV-FR07-05: Standard valid item addition (2 tests)
    {
        "id": "FR07-AI-007",
        "cov_id": "COV-FR07-05",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L118",
        "sec_ref": "SEC-02 (Authenticated Session)",
        "source_ref": "api_specification.md L118-127",
        "oracle_class": "INFERRED",
        "category": "Positive Functional / Cart Mutation",
        "objective": "Verify POST /api/cart succeeds when adding a valid product item matching the specification example",
        "condition": "Send POST /api/cart with valid body { id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2 }",
        "partition": "P_B1, P_C1, P_D1 (Standard Valid Item Addition)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}
            }
        ],
        "expected_semantic": "Item accepted and added to user's shopping cart session",
        "expected_status": "200 OK (INFERRED)",
        "expected_contract": "JSON object with confirmation message: { message: 'Added to cart' } (IMPLEMENTATION-OBSERVED)",
        "state_assertion": "Subsequent GET /api/cart contains the item",
        "sec_assertion": "Mutation scoped strictly to authenticated user",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-008",
        "cov_id": "COV-FR07-05",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L118",
        "sec_ref": "SEC-02 (Authenticated Session)",
        "source_ref": "api_specification.md L118-127",
        "oracle_class": "INFERRED",
        "category": "Positive Functional / Sequential Additions",
        "objective": "Verify POST /api/cart succeeds when adding a second distinct product item",
        "condition": "Add product 1 then add product 2",
        "partition": "P_B1, P_C1, P_D1 (Second Distinct Product Addition)",
        "preconditions": "Authenticated user with 1 item already in cart",
        "initial_state": "Cart contains product 1",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 2, "name": "Sản phẩm B", "price": 250000, "quantity": 1}
            }
        ],
        "expected_semantic": "Second item accepted without removing or corrupting first item",
        "expected_status": "200 OK (INFERRED)",
        "expected_contract": "JSON object confirming addition",
        "state_assertion": "Cart contains 2 distinct product items",
        "sec_assertion": "Scoped to authenticated user",
        "setup": "Register user and add product 1",
        "cleanup": "None"
    },

    # COV-FR07-06: Duplicate Product Accumulation (SPECIFIED BUSINESS RULE) (3 tests)
    {
        "id": "FR07-AI-009",
        "cov_id": "COV-FR07-06",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / README.md L96",
        "sec_ref": "None",
        "source_ref": "README.md L96: 'Thêm cùng một sản phẩm vào giỏ sẽ tăng số lượng, không tạo dòng mới.'",
        "oracle_class": "SPECIFIED BUSINESS RULE",
        "category": "Business Rule / Cart Accumulation",
        "objective": "Verify adding the same product ID twice increments quantity and does not create duplicate rows",
        "condition": "POST product id: 1 with q=2, then POST product id: 1 with q=3, then GET cart",
        "partition": "P_E3 (Duplicate Product Accumulation)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Cart must contain exactly ONE entry for product id: 1 with accumulated quantity === 5 (2 + 3)",
        "expected_status": "POST calls: 200 OK (INFERRED); GET: 200 OK (INFERRED)",
        "expected_contract": "Array containing exactly 1 item: [{ id: 1, quantity: 5, ... }]",
        "state_assertion": "cart.length === 1 && cart[0].quantity === 5",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-010",
        "cov_id": "COV-FR07-06",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / README.md L96",
        "sec_ref": "None",
        "source_ref": "README.md L96",
        "oracle_class": "SPECIFIED BUSINESS RULE",
        "category": "Business Rule / Interleaved Accumulation",
        "objective": "Verify duplicate product accumulation succeeds when interleaved with a different product",
        "condition": "POST product 1 (q=1) -> POST product 2 (q=2) -> POST product 1 (q=4) -> GET cart",
        "partition": "P_E3 (Interleaved Duplicate Accumulation)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 2, "name": "Sản phẩm B", "price": 200000, "quantity": 2}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 4}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Cart has exactly 2 lines: product 1 with quantity === 5 (1 + 4), product 2 with quantity === 2",
        "expected_status": "All calls 200 OK (INFERRED)",
        "expected_contract": "Array of 2 objects",
        "state_assertion": "cart.length === 2 && cart.find(x => x.id === 1).quantity === 5",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-011",
        "cov_id": "COV-FR07-06",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / README.md L96",
        "sec_ref": "None",
        "source_ref": "README.md L96",
        "oracle_class": "SPECIFIED BUSINESS RULE",
        "category": "Business Rule / Minimum Increment Accumulation",
        "objective": "Verify duplicate accumulation when adding single-unit increments (q=1 then q=1)",
        "condition": "POST product id: 1 with q=1, then POST product id: 1 with q=1, then GET cart",
        "partition": "P_E3 (Minimum Increment Accumulation)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Cart has exactly 1 entry for product 1 with quantity === 2 (1 + 1)",
        "expected_status": "All calls 200 OK (INFERRED)",
        "expected_contract": "Array of 1 object with quantity: 2",
        "state_assertion": "cart.length === 1 && cart[0].quantity === 2",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-07: Quantity exact minimum boundary (q=1) (1 test)
    {
        "id": "FR07-AI-012",
        "cov_id": "COV-FR07-07",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86: 'chỉ nhận số nguyên dương, tối thiểu là 1.'",
        "oracle_class": "SPECIFIED",
        "category": "Boundary Value Analysis / Lower Valid Bound",
        "objective": "Verify POST /api/cart successfully accepts quantity at exact minimum valid boundary (quantity = 1)",
        "condition": "Send POST /api/cart with quantity: 1",
        "partition": "P_B1 (Exact Minimum Boundary: q=1)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            }
        ],
        "expected_semantic": "Item accepted with quantity 1",
        "expected_status": "200 OK (SPECIFIED / INFERRED)",
        "expected_contract": "JSON confirmation",
        "state_assertion": "Cart retains item with quantity 1",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-08: Quantity min + 1 (q=2) (1 test)
    {
        "id": "FR07-AI-013",
        "cov_id": "COV-FR07-08",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86, api_specification.md L125",
        "oracle_class": "SPECIFIED",
        "category": "Boundary Value Analysis / Valid Small Integer",
        "objective": "Verify POST /api/cart successfully accepts quantity at min + 1 boundary (quantity = 2)",
        "condition": "Send POST /api/cart with quantity: 2",
        "partition": "P_B1 (Min + 1 Boundary: q=2)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}
            }
        ],
        "expected_semantic": "Item accepted with quantity 2",
        "expected_status": "200 OK (SPECIFIED / INFERRED)",
        "expected_contract": "JSON confirmation",
        "state_assertion": "Cart retains item with quantity 2",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-09: Quantity zero boundary violation (q=0) (1 test)
    {
        "id": "FR07-AI-014",
        "cov_id": "COV-FR07-09",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86: 'chỉ nhận số nguyên dương, tối thiểu là 1.'",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)",
        "category": "Boundary Value Analysis / Lower Invalid Bound",
        "objective": "Verify POST /api/cart rejects request when quantity is 0 (min - 1 boundary violation)",
        "condition": "Send POST /api/cart with quantity: 0",
        "partition": "P_B2 (Min - 1 Invalid Boundary: q=0)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 0}
            }
        ],
        "expected_semantic": "Server must reject request; zero quantity violates minimum 1 rule",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty; no zero-quantity item added",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-10: Negative quantity (2 tests)
    {
        "id": "FR07-AI-015",
        "cov_id": "COV-FR07-10",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)",
        "category": "Input Validation / Negative Quantity Boundary",
        "objective": "Verify POST /api/cart rejects request when quantity is -1 (immediate negative boundary)",
        "condition": "Send POST /api/cart with quantity: -1",
        "partition": "P_B3 (Immediate Negative Boundary: q=-1)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -1}
            }
        ],
        "expected_semantic": "Server must reject request; negative quantity violates positive integer requirement",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty; no negative quantity item added",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-016",
        "cov_id": "COV-FR07-10",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)",
        "category": "Input Validation / Large Negative Quantity",
        "objective": "Verify POST /api/cart rejects request when quantity is a large negative integer (-100)",
        "condition": "Send POST /api/cart with quantity: -100",
        "partition": "P_B3 (Large Negative Integer: q=-100)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": -100}
            }
        ],
        "expected_semantic": "Server must reject request; negative integer is forbidden",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-11: Fractional / Decimal quantity (2 tests)
    {
        "id": "FR07-AI-017",
        "cov_id": "COV-FR07-11",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86: 'chỉ nhận số nguyên dương'",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)",
        "category": "Type Validation / Fractional Quantity",
        "objective": "Verify POST /api/cart rejects fractional/decimal quantity (quantity = 1.5)",
        "condition": "Send POST /api/cart with quantity: 1.5",
        "partition": "P_B4 (Fractional Decimal > 1: q=1.5)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1.5}
            }
        ],
        "expected_semantic": "Server must reject request; fractional values violate integer requirement",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty; no fractional item added",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-018",
        "cov_id": "COV-FR07-11",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: UNKNOWN / INFERRED REJECTION)",
        "category": "Type Validation / Sub-Unit Decimal Quantity",
        "objective": "Verify POST /api/cart rejects decimal quantity between 0 and 1 (quantity = 0.5)",
        "condition": "Send POST /api/cart with quantity: 0.5",
        "partition": "P_B4 (Sub-Unit Fractional: q=0.5)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 0.5}
            }
        ],
        "expected_semantic": "Server must reject request; sub-unit decimal violates both integer and minimum 1 constraints",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-12: String numeric quantity (1 test)
    {
        "id": "FR07-AI-019",
        "cov_id": "COV-FR07-12",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "TYPE ROBUSTNESS / CHARACTERIZATION",
        "category": "Type Robustness / JSON Type Coercion Probe",
        "objective": "Characterize SUT behavior when quantity is supplied as a string-encoded integer ('2')",
        "condition": "Send POST /api/cart with quantity: '2'",
        "partition": "P_B5 (String Integer Value: q='2')",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": "2"}
            }
        ],
        "expected_semantic": "Characterize whether server strictly rejects non-number type or coerces string integer safely without crash",
        "expected_status": "UNKNOWN by specification (Controlled HTTP response, no 500 error)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server remains operational; if stored, cart structure is internally consistent",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-13: Non-numeric string quantity (2 tests)
    {
        "id": "FR07-AI-020",
        "cov_id": "COV-FR07-13",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "INFERRED REJECTION",
        "category": "Type Validation / Alphabetic String",
        "objective": "Verify POST /api/cart rejects request when quantity is an alphabetic string ('abc')",
        "condition": "Send POST /api/cart with quantity: 'abc'",
        "partition": "P_B6 (Non-Numeric Alphabetic String)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": "abc"}
            }
        ],
        "expected_semantic": "Server must reject request; non-numeric string violates integer constraint",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty; NaN/string not added to cart calculations",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-021",
        "cov_id": "COV-FR07-13",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "INFERRED REJECTION",
        "category": "Type Validation / Special Character String",
        "objective": "Verify POST /api/cart rejects request when quantity is special symbols ('@#$')",
        "condition": "Send POST /api/cart with quantity: '@#$'",
        "partition": "P_B6 (Special Symbol String)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": "@#$"}
            }
        ],
        "expected_semantic": "Server must reject request; special character string cannot represent integer quantity",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-14: Large quantity (1 test)
    {
        "id": "FR07-AI-022",
        "cov_id": "COV-FR07-14",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "ROBUSTNESS / UNKNOWN UPPER BOUND",
        "category": "Robustness / Extreme Large Integer",
        "objective": "Characterize server handling of extreme large quantity (10^9) without crash or corrupted memory",
        "condition": "Send POST /api/cart with quantity: 1000000000",
        "partition": "P_B7 (Extreme Large Integer: q=10^9)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1000000000}
            }
        ],
        "expected_semantic": "Server handles large integer safely with controlled response and no process crash",
        "expected_status": "UNKNOWN by specification (Controlled response, no crash)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server process remains alive and responsive",
        "sec_assertion": "No unhandled numeric exception or memory failure",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-15: Omitted quantity field (2 tests)
    {
        "id": "FR07-AI-023",
        "cov_id": "COV-FR07-15",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86: 'Có ô nhập Số lượng'",
        "oracle_class": "INFERRED REJECTION",
        "category": "Input Validation / Omitted Mandatory Property",
        "objective": "Verify POST /api/cart rejects request when the mandatory quantity property is completely omitted",
        "condition": "Send POST /api/cart with body omitting 'quantity': { id: 1, name: 'Sản phẩm A', price: 100000 }",
        "partition": "P_B8 (Omitted Quantity Property)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000}
            }
        ],
        "expected_semantic": "Server must reject request; quantity is a required input for cart additions",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty; undefined quantity item not added",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-024",
        "cov_id": "COV-FR07-15",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / README.md L86",
        "sec_ref": "None",
        "source_ref": "README.md L86",
        "oracle_class": "INFERRED REJECTION",
        "category": "Input Validation / Explicit Null Quantity",
        "objective": "Verify POST /api/cart rejects request when quantity is explicitly passed as null",
        "condition": "Send POST /api/cart with quantity: null",
        "partition": "P_B8 (Null Quantity Property)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": None}
            }
        ],
        "expected_semantic": "Server must reject request; null quantity cannot satisfy positive integer requirement",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-16: Non-existent product ID (1 test)
    {
        "id": "FR07-AI-025",
        "cov_id": "COV-FR07-16",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L122",
        "sec_ref": "None",
        "source_ref": "api_specification.md L122",
        "oracle_class": "ROBUSTNESS / BUSINESS PROBE",
        "category": "Business Rule / Catalog Existence Probe",
        "objective": "Probe SUT behavior when adding a product ID that does not exist in database catalog (id = 999999)",
        "condition": "Send POST /api/cart with non-existent id: 999999",
        "partition": "P_C2 (Non-Existent Product ID)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 999999, "name": "Phantom Item", "price": 50000, "quantity": 1}
            }
        ],
        "expected_semantic": "Characterize whether cart checks database catalog or blindly pushes unverified product IDs",
        "expected_status": "UNKNOWN by specification (Controlled response, no crash)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server remains responsive",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-17: Negative product ID (1 test)
    {
        "id": "FR07-AI-026",
        "cov_id": "COV-FR07-17",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L122",
        "sec_ref": "None",
        "source_ref": "api_specification.md L122",
        "oracle_class": "ROBUSTNESS PROBE",
        "category": "Input Robustness / Negative Product ID",
        "objective": "Probe SUT handling of a negative integer product identifier (id = -1)",
        "condition": "Send POST /api/cart with id: -1",
        "partition": "P_C3 (Negative Product ID: id=-1)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": -1, "name": "Negative ID Item", "price": 50000, "quantity": 1}
            }
        ],
        "expected_semantic": "Probe whether server handles negative ID safely without unexpected state corruption",
        "expected_status": "UNKNOWN by specification (Controlled response, no crash)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server process remains alive",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-18: Omitted / Non-Integer product ID (2 tests)
    {
        "id": "FR07-AI-027",
        "cov_id": "COV-FR07-18",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L122",
        "sec_ref": "None",
        "source_ref": "api_specification.md L122",
        "oracle_class": "ROBUSTNESS PROBE",
        "category": "Schema Robustness / Omitted Product ID",
        "objective": "Probe SUT handling when the product ID property is completely omitted from body",
        "condition": "Send POST /api/cart with body lacking 'id': { name: 'No ID Item', price: 50000, quantity: 1 }",
        "partition": "P_C5 (Omitted Product ID)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"name": "No ID Item", "price": 50000, "quantity": 1}
            }
        ],
        "expected_semantic": "Probe whether server requires an item ID or blindly stores ID-less cart entries",
        "expected_status": "UNKNOWN by specification (Controlled response, no crash)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server process remains operational",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-028",
        "cov_id": "COV-FR07-18",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L122",
        "sec_ref": "None",
        "source_ref": "api_specification.md L122",
        "oracle_class": "ROBUSTNESS PROBE",
        "category": "Type Robustness / Non-Integer Product ID",
        "objective": "Probe SUT handling when product ID is passed as a string ('one')",
        "condition": "Send POST /api/cart with id: 'one'",
        "partition": "P_C4 (String Product ID)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": "one", "name": "String ID Item", "price": 50000, "quantity": 1}
            }
        ],
        "expected_semantic": "Probe whether server coerces string ID, rejects it, or allows string key",
        "expected_status": "UNKNOWN by specification (Controlled response, no crash)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server process remains operational",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-19: Client price tampering (1 test)
    {
        "id": "FR07-AI-029",
        "cov_id": "COV-FR07-19",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / api_specification.md L124",
        "sec_ref": "None",
        "source_ref": "api_specification.md L124, README.md L107",
        "oracle_class": "SECURITY / INTEGRITY PROBE",
        "category": "Security / Client Price Tampering Probe",
        "objective": "Probe whether POST /api/cart trusts client-submitted price (e.g. price: 1) or looks up catalog price",
        "condition": "Send POST /api/cart for known 100000 VND product with tampered price: 1, then GET cart",
        "partition": "P_D2 (Client Price Tampering)",
        "preconditions": "Authenticated user with empty cart",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 1, "quantity": 1}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "Characterize whether cart stores arbitrary client price or overrides it with official catalog price",
        "expected_status": "UNKNOWN by specification (POST returns controlled response; GET reflects state)",
        "expected_contract": "Array of cart items",
        "state_assertion": "Inspect stored price property in retrieved cart item",
        "sec_assertion": "Integrity probe: identifies if client can manipulate unit price in cart layer",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-20: Negative price (1 test)
    {
        "id": "FR07-AI-030",
        "cov_id": "COV-FR07-20",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L124",
        "sec_ref": "None",
        "source_ref": "api_specification.md L124",
        "oracle_class": "ROBUSTNESS PROBE",
        "category": "Input Robustness / Negative Price",
        "objective": "Probe SUT handling when price is supplied as a negative number (-50000)",
        "condition": "Send POST /api/cart with price: -50000",
        "partition": "P_D3 (Negative Price)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": -50000, "quantity": 1}
            }
        ],
        "expected_semantic": "Characterize handling of negative price without server crash",
        "expected_status": "UNKNOWN by specification (Controlled response, no crash)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server process remains alive",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },

    # COV-FR07-21: POST Missing Auth Token (1 test)
    {
        "id": "FR07-AI-031",
        "cov_id": "COV-FR07-21",
        "endpoints": "POST /api/cart",
        "req_ref": "SEC-02 / api_specification.md L112",
        "sec_ref": "SEC-02 (Mandatory JWT for Secured APIs)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)",
        "category": "Security / Authentication Barrier",
        "objective": "Verify POST /api/cart rejects addition when Authorization header is completely omitted",
        "condition": "Send POST /api/cart with valid body but without Authorization header",
        "partition": "P_A2 (Missing Token on Mutation)",
        "preconditions": "Server running",
        "initial_state": "N/A",
        "auth_state": "Unauthenticated (No token)",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            }
        ],
        "expected_semantic": "Cart mutation denied; unauthenticated user cannot mutate any cart",
        "expected_status": "401 Unauthorized (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)",
        "expected_contract": "JSON error payload",
        "state_assertion": "No user cart state mutated",
        "sec_assertion": "SEC-02 enforced on write endpoint",
        "setup": "None",
        "cleanup": "None"
    },

    # COV-FR07-22: POST Invalid / Forged JWT Token (2 tests)
    {
        "id": "FR07-AI-032",
        "cov_id": "COV-FR07-22",
        "endpoints": "POST /api/cart",
        "req_ref": "SEC-02 / api_specification.md L112",
        "sec_ref": "SEC-02 (Mandatory JWT for Secured APIs)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "SPECIFIED REJECTION (Oracle status: INFERRED FROM MIDDLEWARE)",
        "category": "Security / Token Verification",
        "objective": "Verify POST /api/cart rejects request carrying forged JWT signature",
        "condition": "Send POST /api/cart with valid body and forged HMAC signature",
        "partition": "P_A3 (Invalid Signature on Mutation)",
        "preconditions": "Server running",
        "initial_state": "N/A",
        "auth_state": "Forged JWT signature",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTE2MjM5MDIyfQ.ForgedSignatureBytes12345", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            }
        ],
        "expected_semantic": "Cart mutation denied; token signature verification fails",
        "expected_status": "403 Forbidden (INFERRED FROM MIDDLEWARE; official spec status is UNKNOWN)",
        "expected_contract": "JSON error payload: { error: 'Forbidden' }",
        "state_assertion": "No cart mutation executed",
        "sec_assertion": "SEC-02 cryptographic barrier prevents unauthorized mutation",
        "setup": "None",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-033",
        "cov_id": "COV-FR07-22",
        "endpoints": "POST /api/cart",
        "req_ref": "SEC-02 / api_specification.md L112",
        "sec_ref": "SEC-02 (Mandatory JWT for Secured APIs)",
        "source_ref": "api_specification.md L112",
        "oracle_class": "ROBUSTNESS / SPECIFIED REJECTION",
        "category": "Security / Header Format Robustness",
        "objective": "Verify POST /api/cart rejects Authorization header using Basic scheme instead of Bearer",
        "condition": "Send POST /api/cart with Authorization: Basic dXNlcjpwYXNz",
        "partition": "P_A5 (Wrong Authentication Scheme)",
        "preconditions": "Server running",
        "initial_state": "N/A",
        "auth_state": "Basic auth scheme instead of Bearer",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Basic dXNlcjpwYXNz", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 1}
            }
        ],
        "expected_semantic": "Access denied; non-Bearer scheme rejected",
        "expected_status": "401 / 403 (INFERRED FROM MIDDLEWARE; official status UNKNOWN)",
        "expected_contract": "JSON error payload",
        "state_assertion": "No cart mutation",
        "sec_assertion": "SEC-02 scheme enforcement",
        "setup": "None",
        "cleanup": "None"
    },

    # COV-FR07-23: User Cart Isolation (3 tests)
    {
        "id": "FR07-AI-034",
        "cov_id": "COV-FR07-23",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / SEC-02",
        "sec_ref": "SEC-02 (Authenticated Session Isolation)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02",
        "category": "Security / Multi-Tenant Cart Isolation",
        "objective": "Verify User A adding items to their cart leaves User B's cart completely empty",
        "condition": "User A adds product 1 -> User B (fresh login) retrieves GET /api/cart",
        "partition": "P_E5 (Cross-User Isolation: Empty Cart Independence)",
        "preconditions": "Two distinct registered users (User A, User B)",
        "initial_state": "Both carts empty",
        "auth_state": "Separate JWT tokens for User A and User B",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_A_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_B_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "User B's cart remains completely empty ([]); User A's items are strictly isolated",
        "expected_status": "POST: 200 OK (INFERRED); GET: 200 OK (INFERRED)",
        "expected_contract": "User B GET returns empty array: []",
        "state_assertion": "user_b_cart.length === 0",
        "sec_assertion": "Multi-tenant data isolation: no cross-user cart leakage (BOLA prevention)",
        "setup": "Register User A and User B",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-035",
        "cov_id": "COV-FR07-23",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / SEC-02",
        "sec_ref": "SEC-02 (Authenticated Session Isolation)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02",
        "category": "Security / Multi-Tenant Non-Interference",
        "objective": "Verify User A's additions do not mutate or overwrite User B's existing populated cart",
        "condition": "User B adds product 2 -> User A adds product 1 -> User B retrieves cart",
        "partition": "P_E5 (Cross-User Isolation: Populated Non-Interference)",
        "preconditions": "User A and User B registered",
        "initial_state": "Both carts empty",
        "auth_state": "Separate JWT tokens for User A and User B",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_B_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 2, "name": "Sản phẩm B", "price": 200000, "quantity": 1}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_A_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_B_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "User B's cart still contains only product 2 with quantity 1; completely unaffected by User A",
        "expected_status": "All calls 200 OK (INFERRED)",
        "expected_contract": "User B GET returns [{ id: 2, quantity: 1 }]",
        "state_assertion": "user_b_cart.length === 1 && user_b_cart[0].id === 2",
        "sec_assertion": "State segregation maintained across concurrent customer sessions",
        "setup": "Register User A and User B",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-036",
        "cov_id": "COV-FR07-23",
        "endpoints": "POST /api/cart, GET /api/cart",
        "req_ref": "FR-07 / SEC-02",
        "sec_ref": "SEC-02 (Authenticated Session Isolation)",
        "source_ref": "api_specification.md L112, README.md L279",
        "oracle_class": "INFERRED FROM AUTHENTICATED CART SEMANTICS & SEC-02",
        "category": "Security / Independent Accumulation Isolation",
        "objective": "Verify accumulation of the same product ID operates independently across distinct users",
        "condition": "User A adds product 1 (q=2) -> User B adds product 1 (q=3) -> User A GET cart",
        "partition": "P_E5 (Independent Cross-User Accumulation)",
        "preconditions": "User A and User B registered",
        "initial_state": "Both carts empty",
        "auth_state": "Separate JWT tokens for User A and User B",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_A_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2}
            },
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_B_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 3}
            },
            {
                "method": "GET",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <USER_A_TOKEN>", "X-Student-Id": "23127027"},
                "body": None
            }
        ],
        "expected_semantic": "User A's cart quantity for product 1 is strictly 2; not contaminated by User B's addition of product 1",
        "expected_status": "All calls 200 OK (INFERRED)",
        "expected_contract": "User A cart returns [{ id: 1, quantity: 2 }]",
        "state_assertion": "user_a_cart[0].quantity === 2",
        "sec_assertion": "Item-level aggregation is strictly per-tenant",
        "setup": "Register User A and User B",
        "cleanup": "None"
    },

    # COV-FR07-24: Empty JSON body & Extra payload properties (2 tests)
    {
        "id": "FR07-AI-037",
        "cov_id": "COV-FR07-24",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L119",
        "sec_ref": "None",
        "source_ref": "api_specification.md L119",
        "oracle_class": "ROBUSTNESS PROBE",
        "category": "Payload Robustness / Empty JSON Object",
        "objective": "Verify POST /api/cart handles empty JSON body ({}) safely without server crash",
        "condition": "Send POST /api/cart with empty body {}",
        "partition": "P_Payload (Empty Object)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {}
            }
        ],
        "expected_semantic": "Server safely handles empty object with controlled response; does not crash process",
        "expected_status": "Rejection status != 200 (UNKNOWN by spec; 400 Bad Request expected)",
        "expected_contract": "JSON error payload",
        "state_assertion": "Cart remains empty",
        "sec_assertion": "None",
        "setup": "Register fresh user",
        "cleanup": "None"
    },
    {
        "id": "FR07-AI-038",
        "cov_id": "COV-FR07-24",
        "endpoints": "POST /api/cart",
        "req_ref": "FR-07 / api_specification.md L119",
        "sec_ref": "None",
        "source_ref": "api_specification.md L119",
        "oracle_class": "ROBUSTNESS PROBE",
        "category": "Schema Robustness / Extra Unexpected Properties",
        "objective": "Verify POST /api/cart safely handles extra unexpected properties in request payload",
        "condition": "Send POST /api/cart with valid item plus extra fields: { id: 1, name: 'Sản phẩm A', price: 100000, quantity: 2, adminNote: 'hack', discountBypass: true }",
        "partition": "P_Payload (Extra Properties)",
        "preconditions": "Authenticated user",
        "initial_state": "Cart empty",
        "auth_state": "Valid customer JWT Bearer token",
        "requests": [
            {
                "method": "POST",
                "endpoint": "/api/cart",
                "headers": {"Authorization": "Bearer <VALID_USER_TOKEN>", "Content-Type": "application/json", "X-Student-Id": "23127027"},
                "body": {"id": 1, "name": "Sản phẩm A", "price": 100000, "quantity": 2, "adminNote": "hack", "discountBypass": True}
            }
        ],
        "expected_semantic": "Server handles extra properties safely without crashing or corrupting cart state",
        "expected_status": "200 OK / 400 (UNKNOWN by spec; controlled response)",
        "expected_contract": "Controlled response payload",
        "state_assertion": "Server remains operational",
        "sec_assertion": "No parameter tampering or privilege escalation",
        "setup": "Register fresh user",
        "cleanup": "None"
    }
]

def main():
    print(f"Total test cases defined: {len(TESTS)}")
    assert len(TESTS) == 38, f"Expected 38 tests, got {len(TESTS)}"

    # Check continuous IDs
    for idx, t in enumerate(TESTS):
        expected_id = f"FR07-AI-{idx+1:03d}"
        assert t["id"] == expected_id, f"ID mismatch: expected {expected_id}, got {t['id']}"

    # Check coverage allocation
    cov_counts = {}
    for t in TESTS:
        c = t["cov_id"]
        cov_counts[c] = cov_counts.get(c, 0) + 1

    print("\nCoverage Allocation Summary:")
    for c in sorted(cov_counts.keys()):
        print(f"  {c}: {cov_counts[c]} test(s)")
    print(f"Total across all Coverage IDs: {sum(cov_counts.values())}")
    assert sum(cov_counts.values()) == 38

    # Ensure all 24 Coverage IDs are represented
    assert len(cov_counts) == 24, f"Expected 24 coverage IDs, got {len(cov_counts)}"

    # Write generated-ai-original.md
    out_dir = "/Users/phamngocgiabao/eshop-sut/hw06/testcases/fr07"
    gen_file = os.path.join(out_dir, "generated-ai-original.md")
    with open(gen_file, "w", encoding="utf-8") as f:
        f.write("# FR-07: Shopping Cart — AI-Generated Original Test Cases (38 Cases)\n\n")
        f.write("> **Document Status:** Immutable Original AI Generation Record\n")
        f.write("> **Feature ID:** Pool B — `FR-07` (Shopping Cart)\n")
        f.write("> **Endpoints:** `GET /api/cart`, `POST /api/cart`\n")
        f.write("> **Total Generated Tests:** 38 (`FR07-AI-001` through `FR07-AI-038`)\n")
        f.write("> **Author:** AI (Gemini 3.7 Flash via Antigravity IDE)\n")
        f.write("> **Student / Reviewer:** Phạm Ngọc Gia Bảo (`23127027`)\n")
        f.write("> **Created Date:** 2026-09-02\n\n")
        f.write("---\n\n")
        f.write("## 1. Test Suite Overview & Coverage Allocation\n\n")
        f.write("| Coverage ID | Endpoint | Target Condition | Generated Test Cases | Count |\n")
        f.write("| :--- | :--- | :--- | :--- | :---: |\n")

        for c in sorted(cov_counts.keys()):
            c_tests = [t["id"] for t in TESTS if t["cov_id"] == c]
            first_t = next(t for t in TESTS if t["cov_id"] == c)
            f.write(f"| **`{c}`** | `{first_t['endpoints']}` | {first_t['objective']} | {', '.join(f'`{tid}`' for tid in c_tests)} | {len(c_tests)} |\n")
        f.write(f"| **TOTAL** | — | — | **38 Unique Tests** | **38** |\n\n")
        f.write("---\n\n")
        f.write("## 2. Detailed Test Specifications\n\n")

        for t in TESTS:
            f.write(f"### `{t['id']}` — {t['objective']}\n\n")
            f.write("#### Identity\n")
            f.write(f"- **Test ID:** `{t['id']}`\n")
            f.write("- **Origin:** AI\n")
            f.write("- **Feature:** FR-07 (Shopping Cart)\n")
            f.write(f"- **Coverage ID:** `{t['cov_id']}`\n")
            f.write(f"- **Endpoint(s):** `{t['endpoints']}`\n\n")

            f.write("#### Traceability\n")
            f.write(f"- **Requirement Reference:** `{t['req_ref']}`\n")
            f.write(f"- **SEC Reference:** `{t['sec_ref']}`\n")
            f.write(f"- **Source Reference:** {t['source_ref']}\n")
            f.write(f"- **Oracle Classification:** **`{t['oracle_class']}`**\n\n")

            f.write("#### Test Design\n")
            f.write(f"- **Category:** {t['category']}\n")
            f.write(f"- **Test Objective:** {t['objective']}\n")
            f.write(f"- **Test Condition:** {t['condition']}\n")
            f.write(f"- **Partition / Boundary:** {t['partition']}\n")
            f.write(f"- **Preconditions:** {t['preconditions']}\n")
            f.write(f"- **Initial Cart State:** {t['initial_state']}\n")
            f.write(f"- **Authentication State:** {t['auth_state']}\n\n")

            f.write("#### HTTP Request(s)\n")
            for req_idx, req in enumerate(t["requests"]):
                if len(t["requests"]) > 1:
                    f.write(f"*Step {req_idx + 1}:* `{req['method']} {req['endpoint']}`\n")
                else:
                    f.write(f"- **Method & Endpoint:** `{req['method']} {req['endpoint']}`\n")
                f.write(f"- **Headers:**\n")
                for hk, hv in req["headers"].items():
                    f.write(f"  - `{hk}`: `{hv}`\n")
                if req["body"] is not None:
                    f.write(f"- **Request Body (JSON):**\n```json\n{json.dumps(req['body'], indent=2, ensure_ascii=False)}\n```\n")
                else:
                    f.write(f"- **Request Body:** None\n")
                f.write("\n")

            f.write("#### Expected Result\n")
            f.write(f"- **Expected Semantic Behavior:** {t['expected_semantic']}\n")
            f.write(f"- **Expected HTTP Status:** `{t['expected_status']}`\n")
            f.write(f"- **Expected Response Contract:** {t['expected_contract']}\n")
            f.write(f"- **State Assertion:** `{t['state_assertion']}`\n")
            f.write(f"- **Security Assertion:** {t['sec_assertion']}\n\n")

            f.write("#### Lifecycle\n")
            f.write(f"- **Setup Required:** {t['setup']}\n")
            f.write(f"- **Cleanup Required:** {t['cleanup']}\n")
            f.write(f"- **Automation Status:** NOT AUTOMATED YET\n\n")
            f.write("---\n\n")

    print(f"Wrote {gen_file}")

    # Write blank human-audit.md
    audit_file = os.path.join(out_dir, "human-audit.md")
    with open(audit_file, "w", encoding="utf-8") as f:
        f.write("# FR-07: Shopping Cart — Student Human Audit Worksheet\n\n")
        f.write("> **Instructions for Student Reviewer:**\n")
        f.write("> - Review each of the 38 AI-generated test cases independently against the reviewed specification.\n")
        f.write("> - Assign `Student Verdict` as one of: **`VALID`**, **`INVALID`**, or **`INCOMPLETE`**.\n")
        f.write("> - Provide your personal `Student Reasoning` and required `Student Correction` where applicable.\n")
        f.write("> - **Academic Integrity Rule:** All student fields start strictly BLANK. Do NOT accept pre-filled verdicts.\n\n")
        f.write("---\n\n")
        f.write("## Human Audit Table\n\n")
        f.write("| Test ID | Coverage ID | Short Test Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |\n")
        f.write("| :---: | :---: | :--- | :---: | :--- | :--- | :---: |\n")
        for t in TESTS:
            f.write(f"| **`{t['id']}`** | `{t['cov_id']}` | {t['objective']} | | | | |\n")

    print(f"Wrote {audit_file}")

    # Write blank human-review-compact.md
    compact_file = os.path.join(out_dir, "human-review-compact.md")
    with open(compact_file, "w", encoding="utf-8") as f:
        f.write("# FR-07: Shopping Cart — Compact Review Sheet\n\n")
        f.write("> **Instructions:** Fast-review tracking table for student human audit.\n\n")
        f.write("| Test ID | Coverage ID | One-Sentence Condition | Expected Oracle | Student Final Verdict | Student Note |\n")
        f.write("| :---: | :---: | :--- | :--- | :---: | :--- |\n")
        for t in TESTS:
            f.write(f"| **`{t['id']}`** | `{t['cov_id']}` | {t['condition']} | {t['expected_semantic']} | | |\n")

    print(f"Wrote {compact_file}")

if __name__ == "__main__":
    main()
