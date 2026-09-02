#!/usr/bin/env python3
"""
Generate FR-12 AI Test Cases (Exactly 38), Blank Human Audit Worksheet, and Compact Review Sheet.
Author: Antigravity AI Pair Programmer
Student: Pham Ngoc Gia Bao (23127027)
"""

import os
import json

TEST_CASES = [
    # -------------------------------------------------------------
    # SECTION A: STANDARD-USER ROLE DENIAL (14 Tests)
    # Caller: Valid JWT, role = 'user'
    # Oracle: Semantic Denial via SEC-03; 403 Forbidden (Inferred) / UNKNOWN
    # -------------------------------------------------------------
    {
        "id": "FR12-AI-001",
        "coverage_id": "COV-FR12-02",
        "method": "GET",
        "endpoint": "/api/admin/users",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that an authenticated standard user (role: 'user') is denied access to the administrative user accounts directory.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Backend running on http://localhost:3000; valid standard user account registered and logged in.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Non-admin subject attempting administrative user listing)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response payload must not expose user account directory rows (passwords, emails, roles).",
        "side_effect_assertion": "Read-only operation; zero mutation expected.",
        "sec_assertion": "SEC-03: System verifies role === 'admin' and strictly rejects role: 'user'.",
        "setup": "Authenticate standard user to obtain valid JWT.",
        "cleanup": "None.",
        "short_objective": "Standard user denied access to GET /api/admin/users",
        "condition_summary": "Standard user (role: 'user') calls GET /api/admin/users",
        "oracle_summary": "Semantic access denied (SEC-03); 403 (Inferred)"
    },
    {
        "id": "FR12-AI-002",
        "coverage_id": "COV-FR12-04",
        "method": "DELETE",
        "endpoint": "/api/admin/users/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that an authenticated standard user cannot delete an arbitrary user account, and that the target account is not deleted.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable target user account created with ID <TARGET_USER_ID>.",
        "disposable_resource": "Disposable test user (e.g. test_victim_23127027@eshop.com)",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Standard user cannot execute administrative user deletion)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must indicate authorization rejection and not confirm deletion.",
        "side_effect_assertion": "Target user account remains active in database; follow-up login probe with target user credentials must succeed.",
        "sec_assertion": "SEC-03: Deletion requires role === 'admin'; unauthorized deletion side-effect is prevented.",
        "setup": "Create disposable test user account via /api/register to act as deletion target.",
        "cleanup": "Clean up disposable test user via admin credentials after test completion.",
        "short_objective": "Standard user denied DELETE /api/admin/users/:id + user not deleted",
        "condition_summary": "Standard user calls DELETE /api/admin/users/:id on disposable user",
        "oracle_summary": "Semantic access denied (SEC-03); target user not deleted"
    },
    {
        "id": "FR12-AI-003",
        "coverage_id": "COV-FR12-07",
        "method": "GET",
        "endpoint": "/api/admin/orders",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that an authenticated standard user is denied access to view system-wide orders across all customers.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "System contains orders from multiple users in database.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Non-admin cannot view system-wide customer order history)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response payload must not expose order records belonging to other system users.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "SEC-03: System-wide order viewing is restricted strictly to role: 'admin'.",
        "setup": "Obtain standard user JWT token.",
        "cleanup": "None.",
        "short_objective": "Standard user denied access to GET /api/admin/orders",
        "condition_summary": "Standard user calls GET /api/admin/orders",
        "oracle_summary": "Semantic access denied (SEC-03); zero foreign order data exposed"
    },
    {
        "id": "FR12-AI-004",
        "coverage_id": "COV-FR12-09",
        "method": "PUT",
        "endpoint": "/api/admin/orders/:id/status",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot update the fulfillment status of an order, and that the order status remains unchanged.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable order exists with status: 'pending'.",
        "disposable_resource": "Order ID <TARGET_ORDER_ID> with initial status 'pending'",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "status": "delivered"
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Non-admin prohibited from modifying administrative order status)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject status mutation request.",
        "side_effect_assertion": "Order status in database remains 'pending' (verified via admin order query); no state transition occurred.",
        "sec_assertion": "SEC-03: Order status mutation requires role === 'admin'.",
        "setup": "Identify or create a test order with status 'pending'.",
        "cleanup": "None.",
        "short_objective": "Standard user denied PUT /api/admin/orders/:id/status + status unchanged",
        "condition_summary": "Standard user calls PUT /api/admin/orders/:id/status with body status: 'delivered'",
        "oracle_summary": "Semantic access denied (SEC-03); order status remains 'pending'"
    },
    {
        "id": "FR12-AI-005",
        "coverage_id": "COV-FR12-12",
        "method": "POST",
        "endpoint": "/api/admin/import-products",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot invoke bulk product catalog import, and that no new products are added to catalog.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Standard user token available; unique product payload prepared.",
        "disposable_resource": "Product import payload with unique marker 'ImportProbe_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "products": [
                {
                    "name": "ImportProbe_23127027",
                    "price": 99000,
                    "description": "Unauthorized import probe",
                    "imageUrl": "",
                    "category_id": 1
                }
            ]
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Bulk catalog import restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject import execution.",
        "side_effect_assertion": "Product 'ImportProbe_23127027' is NOT added to database (follow-up GET /api/products?search=ImportProbe_23127027 returns empty list).",
        "sec_assertion": "SEC-03: Catalog import strictly enforces role === 'admin'.",
        "setup": "Prepare unique import JSON payload.",
        "cleanup": "If defect occurs and product is created, delete created product via admin credentials.",
        "short_objective": "Standard user denied POST /api/admin/import-products + catalog unmutated",
        "condition_summary": "Standard user calls POST /api/admin/import-products with product array",
        "oracle_summary": "Semantic access denied (SEC-03); product not inserted into catalog"
    },
    {
        "id": "FR12-AI-006",
        "coverage_id": "COV-FR12-18",
        "method": "POST",
        "endpoint": "/api/admin/coupons",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot create a new promotional coupon, and that the coupon code is not stored in database.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Standard user token available; unique coupon code 'HACK23127027' prepared.",
        "disposable_resource": "Coupon code 'HACK23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "code": "HACK23127027",
            "type": "percent",
            "discount_value": 50,
            "min_order_amount": 100000,
            "expired_at": "2099-12-31",
            "max_uses_per_user": 1
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Promotional coupon creation restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must indicate rejection of coupon creation.",
        "side_effect_assertion": "Coupon 'HACK23127027' is NOT created in database; checkout probe with code returns invalid coupon error.",
        "sec_assertion": "SEC-03: Coupon creation strictly requires role === 'admin'.",
        "setup": "Prepare coupon creation request body.",
        "cleanup": "If defect occurs and coupon is created, delete coupon via admin credentials.",
        "short_objective": "Standard user denied POST /api/admin/coupons + coupon not created",
        "condition_summary": "Standard user calls POST /api/admin/coupons with coupon payload",
        "oracle_summary": "Semantic access denied (SEC-03); coupon code not stored"
    },
    {
        "id": "FR12-AI-007",
        "coverage_id": "COV-FR12-20",
        "method": "DELETE",
        "endpoint": "/api/admin/coupons/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot delete a promotional coupon, and that the coupon remains valid in the database.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable test coupon exists with ID <TARGET_COUPON_ID>.",
        "disposable_resource": "Disposable test coupon (code: 'DISP_COUPON_23127027')",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Coupon deletion restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject coupon deletion.",
        "side_effect_assertion": "Coupon record remains in database; query or application of coupon still succeeds.",
        "sec_assertion": "SEC-03: Coupon deletion requires role === 'admin'.",
        "setup": "Create disposable test coupon using admin credentials prior to probe.",
        "cleanup": "Delete disposable test coupon using admin credentials after test.",
        "short_objective": "Standard user denied DELETE /api/admin/coupons/:id + coupon not deleted",
        "condition_summary": "Standard user calls DELETE /api/admin/coupons/:id on disposable coupon",
        "oracle_summary": "Semantic access denied (SEC-03); coupon remains intact in database"
    },
    {
        "id": "FR12-AI-008",
        "coverage_id": "COV-FR12-22",
        "method": "POST",
        "endpoint": "/api/products",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot insert a new product into the master catalog, and that the product is not created.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Standard user token available; unique product payload prepared.",
        "disposable_resource": "Product name 'UnauthorizedProduct_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "UnauthorizedProduct_23127027",
            "price": 500000,
            "description": "Unauthorized creation probe",
            "imageUrl": "https://placehold.co/300x300/png?text=Probe",
            "category_id": 1
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Master catalog product creation restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must indicate access denial and not return created product ID.",
        "side_effect_assertion": "Product is NOT created in catalog (GET /api/products?search=UnauthorizedProduct_23127027 returns empty list).",
        "sec_assertion": "SEC-03: Catalog data-affecting APIs require role === 'admin' (README Line 177).",
        "setup": "Prepare unique product payload.",
        "cleanup": "If defect occurs and product is created, delete created product via admin credentials.",
        "short_objective": "Standard user denied POST /api/products + product not created",
        "condition_summary": "Standard user calls POST /api/products with product payload",
        "oracle_summary": "Semantic access denied (SEC-03); product not added to catalog"
    },
    {
        "id": "FR12-AI-009",
        "coverage_id": "COV-FR12-25",
        "method": "PUT",
        "endpoint": "/api/products/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot modify an existing product in the catalog, and that the product attributes remain unchanged.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable test product exists with known original attributes.",
        "disposable_resource": "Disposable product ID <DISP_PRODUCT_ID> (Original Price: 100,000)",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "Tampered Product Name",
            "price": 1,
            "description": "Tampered description",
            "imageUrl": "",
            "category_id": 1
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Master catalog product modification restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject product modification request.",
        "side_effect_assertion": "Product attributes in database remain unchanged (GET /api/products/:id verifies original price 100,000).",
        "sec_assertion": "SEC-03: Catalog modification requires role === 'admin'.",
        "setup": "Create disposable test product using admin credentials.",
        "cleanup": "Delete disposable test product using admin credentials after test.",
        "short_objective": "Standard user denied PUT /api/products/:id + product unchanged",
        "condition_summary": "Standard user calls PUT /api/products/:id with altered price",
        "oracle_summary": "Semantic access denied (SEC-03); product attributes unchanged"
    },
    {
        "id": "FR12-AI-010",
        "coverage_id": "COV-FR12-28",
        "method": "DELETE",
        "endpoint": "/api/products/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot delete a product from the catalog, and that the product continues to exist.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable test product exists in catalog.",
        "disposable_resource": "Disposable product ID <DISP_PRODUCT_ID>",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Master catalog product deletion restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject product deletion request.",
        "side_effect_assertion": "Product continues to exist in catalog (GET /api/products/:id returns 200 with product data).",
        "sec_assertion": "SEC-03: Catalog product deletion strictly requires role === 'admin'.",
        "setup": "Create disposable test product using admin credentials.",
        "cleanup": "Delete disposable test product using admin credentials after test.",
        "short_objective": "Standard user denied DELETE /api/products/:id + product not deleted",
        "condition_summary": "Standard user calls DELETE /api/products/:id on disposable product",
        "oracle_summary": "Semantic access denied (SEC-03); product still exists in catalog"
    },
    {
        "id": "FR12-AI-011",
        "coverage_id": "COV-FR12-30",
        "method": "POST",
        "endpoint": "/api/categories",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot create a product category, and that the category is not inserted into database.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Standard user token available; unique category name prepared.",
        "disposable_resource": "Category name 'UnauthorizedCategory_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "UnauthorizedCategory_23127027"
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Category creation restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject category creation.",
        "side_effect_assertion": "Category is NOT inserted into database (GET /api/categories does not contain probe category name).",
        "sec_assertion": "SEC-03: Category mutation requires role === 'admin' (README Line 177).",
        "setup": "Prepare unique category name.",
        "cleanup": "If defect occurs and category is created, delete category via admin credentials.",
        "short_objective": "Standard user denied POST /api/categories + category not created",
        "condition_summary": "Standard user calls POST /api/categories with category name",
        "oracle_summary": "Semantic access denied (SEC-03); category not created in database"
    },
    {
        "id": "FR12-AI-012",
        "coverage_id": "COV-FR12-32",
        "method": "PUT",
        "endpoint": "/api/categories/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot modify an existing category, and that the category name remains unchanged.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable test category exists with known initial name.",
        "disposable_resource": "Disposable category ID <DISP_CAT_ID> (Original Name: 'OriginalCat_23127027')",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "TamperedCategoryName"
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Category modification restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject category modification.",
        "side_effect_assertion": "Category name in database remains 'OriginalCat_23127027' (verified via GET /api/categories).",
        "sec_assertion": "SEC-03: Category modification requires role === 'admin'.",
        "setup": "Create disposable category using admin credentials.",
        "cleanup": "Delete disposable category using admin credentials after test.",
        "short_objective": "Standard user denied PUT /api/categories/:id + category unchanged",
        "condition_summary": "Standard user calls PUT /api/categories/:id with new name",
        "oracle_summary": "Semantic access denied (SEC-03); category name remains unchanged"
    },
    {
        "id": "FR12-AI-013",
        "coverage_id": "COV-FR12-33",
        "method": "DELETE",
        "endpoint": "/api/categories/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user cannot delete a category, and that the category continues to exist in database.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "Disposable test category exists in database.",
        "disposable_resource": "Disposable category ID <DISP_CAT_ID>",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Category deletion restricted to admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject category deletion.",
        "side_effect_assertion": "Category continues to exist in database (verified via GET /api/categories).",
        "sec_assertion": "SEC-03: Category deletion requires role === 'admin'.",
        "setup": "Create disposable category using admin credentials.",
        "cleanup": "Delete disposable category using admin credentials after test.",
        "short_objective": "Standard user denied DELETE /api/categories/:id + category not deleted",
        "condition_summary": "Standard user calls DELETE /api/categories/:id on disposable category",
        "oracle_summary": "Semantic access denied (SEC-03); category still exists in database"
    },
    {
        "id": "FR12-AI-014",
        "coverage_id": "COV-FR12-15",
        "method": "GET",
        "endpoint": "/api/coupons",
        "sec_mapping": "SEC-03",
        "caller_type": "Authenticated Standard User",
        "jwt_state": "Valid cryptographically signed token",
        "role": "user",
        "objective": "Verify that a standard user is denied access to view the administrative coupon master list.",
        "access_condition": "Valid JWT token containing role: 'user'",
        "preconditions": "System contains active and inactive discount coupons in database.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <VALID_USER_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Coupon master list reserved for admin)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must not expose master coupon records, discount values, or usage thresholds.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "SEC-03: Administrative coupon listing requires role === 'admin' (api_spec Section 5.2).",
        "setup": "Obtain standard user JWT token.",
        "cleanup": "None.",
        "short_objective": "Standard user denied access to GET /api/coupons",
        "condition_summary": "Standard user calls GET /api/coupons",
        "oracle_summary": "Semantic access denied (SEC-03); coupon master list not exposed"
    },

    # -------------------------------------------------------------
    # SECTION B: VALID ADMIN AUTHORIZATION (14 Tests)
    # Caller: Valid JWT, role = 'admin'
    # Oracle: AUTHORIZED (Not Blocked by SEC-02/03); 200 OK (Inferred)
    # -------------------------------------------------------------
    {
        "id": "FR12-AI-015",
        "coverage_id": "COV-FR12-03",
        "method": "GET",
        "endpoint": "/api/admin/users",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator (role: 'admin') is authorized to retrieve the system user accounts directory.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin user authenticated with valid JWT token.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response returns JSON array containing user accounts as authorized.",
        "side_effect_assertion": "Read operation; state remains consistent.",
        "sec_assertion": "FR-12 / SEC-03: Valid admin token successfully satisfies authorization check.",
        "setup": "Login as administrator (admin@eshop.com) to obtain admin JWT token.",
        "cleanup": "None.",
        "short_objective": "Admin authorized for GET /api/admin/users",
        "condition_summary": "Admin user (role: 'admin') calls GET /api/admin/users",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); 200 OK (Inferred)"
    },
    {
        "id": "FR12-AI-016",
        "coverage_id": "COV-FR12-05",
        "method": "DELETE",
        "endpoint": "/api/admin/users/:id",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to delete a disposable user account from the system.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Disposable test user account registered specifically for this deletion test.",
        "disposable_resource": "Disposable user ID <DISP_USER_ID> (Never delete seeded lecturer users ID 1 or 2)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms successful execution of user deletion.",
        "side_effect_assertion": "Target disposable user is removed from database (subsequent login probe fails with 401).",
        "sec_assertion": "FR-12 / SEC-03: Admin clearance allows execution of user deletion handler.",
        "setup": "Register a new disposable user account via /api/register to serve as target.",
        "cleanup": "None (disposable user was deleted by the test).",
        "short_objective": "Admin authorized for DELETE /api/admin/users/:id on disposable user",
        "condition_summary": "Admin calls DELETE /api/admin/users/:id on disposable user",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); disposable user deleted"
    },
    {
        "id": "FR12-AI-017",
        "coverage_id": "COV-FR12-08",
        "method": "GET",
        "endpoint": "/api/admin/orders",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to view system-wide customer orders.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin authenticated with valid JWT token.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response returns JSON array containing system order records.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "FR-12 / SEC-03: Admin token passes authorization layer unhindered.",
        "setup": "Obtain admin JWT token.",
        "cleanup": "None.",
        "short_objective": "Admin authorized for GET /api/admin/orders",
        "condition_summary": "Admin calls GET /api/admin/orders",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); 200 OK (Inferred)"
    },
    {
        "id": "FR12-AI-018",
        "coverage_id": "COV-FR12-10",
        "method": "PUT",
        "endpoint": "/api/admin/orders/:id/status",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to update order fulfillment status on an existing order.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Existing test order available in database with initial status.",
        "disposable_resource": "Target order ID <TARGET_ORDER_ID>",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "status": "confirmed"
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response indicates order status update was accepted.",
        "side_effect_assertion": "Order status updated to 'confirmed' in database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token passes authorization to reach order management handler.",
        "setup": "Locate valid order ID.",
        "cleanup": "Reset status if needed.",
        "short_objective": "Admin authorized for PUT /api/admin/orders/:id/status",
        "condition_summary": "Admin calls PUT /api/admin/orders/:id/status with valid status",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); order status updated"
    },
    {
        "id": "FR12-AI-019",
        "coverage_id": "COV-FR12-13",
        "method": "POST",
        "endpoint": "/api/admin/import-products",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to execute bulk product catalog import.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin authenticated; valid product import payload provided.",
        "disposable_resource": "Disposable product name 'AdminImport_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "products": [
                {
                    "name": "AdminImport_23127027",
                    "price": 120000,
                    "description": "Authorized admin import test item",
                    "imageUrl": "",
                    "category_id": 1
                }
            ]
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms completion of bulk product import.",
        "side_effect_assertion": "Product 'AdminImport_23127027' is successfully added into catalog.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears authorization layer.",
        "setup": "Prepare valid import payload with unique marker.",
        "cleanup": "Delete imported test product using admin credentials after test.",
        "short_objective": "Admin authorized for POST /api/admin/import-products",
        "condition_summary": "Admin calls POST /api/admin/import-products with valid payload",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); products imported"
    },
    {
        "id": "FR12-AI-020",
        "coverage_id": "COV-FR12-19",
        "method": "POST",
        "endpoint": "/api/admin/coupons",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to create a new promotional coupon.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin authenticated; unique coupon code 'ADMIN_CPN_23127027' prepared.",
        "disposable_resource": "Disposable coupon code 'ADMIN_CPN_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "code": "ADMIN_CPN_23127027",
            "type": "fixed",
            "discount_value": 20000,
            "min_order_amount": 150000,
            "expired_at": "2099-12-31",
            "max_uses_per_user": 1
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms coupon creation with new ID.",
        "side_effect_assertion": "Coupon 'ADMIN_CPN_23127027' is created in database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token satisfies coupon creation authorization.",
        "setup": "Prepare valid coupon creation payload.",
        "cleanup": "Delete created test coupon via DELETE /api/admin/coupons/:id after test.",
        "short_objective": "Admin authorized for POST /api/admin/coupons",
        "condition_summary": "Admin calls POST /api/admin/coupons with valid coupon payload",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); coupon created"
    },
    {
        "id": "FR12-AI-021",
        "coverage_id": "COV-FR12-21",
        "method": "DELETE",
        "endpoint": "/api/admin/coupons/:id",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to delete a disposable promotional coupon.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Disposable test coupon created prior to execution.",
        "disposable_resource": "Disposable coupon ID <DISP_COUPON_ID> (Never delete seeded coupons SAVE10, BIGBUY)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms successful deletion of coupon.",
        "side_effect_assertion": "Disposable coupon is removed from database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears coupon deletion authorization.",
        "setup": "Create disposable test coupon via POST /api/admin/coupons.",
        "cleanup": "None (coupon deleted by test).",
        "short_objective": "Admin authorized for DELETE /api/admin/coupons/:id on disposable coupon",
        "condition_summary": "Admin calls DELETE /api/admin/coupons/:id on disposable coupon",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); disposable coupon deleted"
    },
    {
        "id": "FR12-AI-022",
        "coverage_id": "COV-FR12-23",
        "method": "POST",
        "endpoint": "/api/products",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to add a new product to the catalog.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin authenticated; valid product payload prepared.",
        "disposable_resource": "Disposable product 'AdminProduct_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "AdminProduct_23127027",
            "price": 250000,
            "description": "Authorized admin product creation",
            "imageUrl": "https://placehold.co/300x300/png?text=AdminProd",
            "category_id": 1
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms product creation with new product ID.",
        "side_effect_assertion": "Product 'AdminProduct_23127027' is stored in catalog database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears catalog creation authorization.",
        "setup": "Prepare valid product payload.",
        "cleanup": "Delete created product using admin credentials after test.",
        "short_objective": "Admin authorized for POST /api/products",
        "condition_summary": "Admin calls POST /api/products with valid product body",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); product created"
    },
    {
        "id": "FR12-AI-023",
        "coverage_id": "COV-FR12-26",
        "method": "PUT",
        "endpoint": "/api/products/:id",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to modify an existing disposable product in the catalog.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Disposable test product created prior to execution.",
        "disposable_resource": "Disposable product ID <DISP_PRODUCT_ID> (Never modify seeded products 1–5)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "Updated AdminProduct_23127027",
            "price": 300000,
            "description": "Updated description",
            "imageUrl": "https://placehold.co/300x300/png?text=Updated",
            "category_id": 1
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms product update.",
        "side_effect_assertion": "Product attributes updated to new values in catalog database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears product modification authorization.",
        "setup": "Create disposable product via POST /api/products.",
        "cleanup": "Delete disposable product after test.",
        "short_objective": "Admin authorized for PUT /api/products/:id on disposable product",
        "condition_summary": "Admin calls PUT /api/products/:id on disposable product",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); product updated"
    },
    {
        "id": "FR12-AI-024",
        "coverage_id": "COV-FR12-27",
        "method": "DELETE",
        "endpoint": "/api/products/:id",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to delete a disposable product from the catalog.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Disposable test product created prior to execution.",
        "disposable_resource": "Disposable product ID <DISP_PRODUCT_ID> (Never delete seeded products 1–5)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms product deletion.",
        "side_effect_assertion": "Disposable product is removed from catalog database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears catalog deletion authorization.",
        "setup": "Create disposable product via POST /api/products.",
        "cleanup": "None (product deleted by test).",
        "short_objective": "Admin authorized for DELETE /api/products/:id on disposable product",
        "condition_summary": "Admin calls DELETE /api/products/:id on disposable product",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); disposable product deleted"
    },
    {
        "id": "FR12-AI-025",
        "coverage_id": "COV-FR12-31",
        "method": "POST",
        "endpoint": "/api/categories",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to add a new category to the system.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin authenticated; unique category name prepared.",
        "disposable_resource": "Disposable category 'AdminCategory_23127027'",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "AdminCategory_23127027"
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms category creation with new category ID.",
        "side_effect_assertion": "Category 'AdminCategory_23127027' is stored in database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears category creation authorization.",
        "setup": "Prepare valid category creation payload.",
        "cleanup": "Delete created category using admin credentials after test.",
        "short_objective": "Admin authorized for POST /api/categories",
        "condition_summary": "Admin calls POST /api/categories with valid category body",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); category created"
    },
    {
        "id": "FR12-AI-026",
        "coverage_id": "COV-FR12-32",
        "method": "PUT",
        "endpoint": "/api/categories/:id",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to modify a disposable category.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Disposable test category created prior to execution.",
        "disposable_resource": "Disposable category ID <DISP_CAT_ID> (Never modify seeded categories 1–3)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "Updated AdminCategory_23127027"
        },
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms category update.",
        "side_effect_assertion": "Category name in database is updated to 'Updated AdminCategory_23127027'.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears category modification authorization.",
        "setup": "Create disposable category via POST /api/categories.",
        "cleanup": "Delete disposable category after test.",
        "short_objective": "Admin authorized for PUT /api/categories/:id on disposable category",
        "condition_summary": "Admin calls PUT /api/categories/:id on disposable category",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); category updated"
    },
    {
        "id": "FR12-AI-027",
        "coverage_id": "COV-FR12-34",
        "method": "DELETE",
        "endpoint": "/api/categories/:id",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to delete a disposable category.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Disposable test category created prior to execution.",
        "disposable_resource": "Disposable category ID <DISP_CAT_ID> (Never delete seeded categories 1–3)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response confirms category deletion.",
        "side_effect_assertion": "Disposable category is removed from database.",
        "sec_assertion": "FR-12 / SEC-03: Admin token clears category deletion authorization.",
        "setup": "Create disposable category via POST /api/categories.",
        "cleanup": "None (category deleted by test).",
        "short_objective": "Admin authorized for DELETE /api/categories/:id on disposable category",
        "condition_summary": "Admin calls DELETE /api/categories/:id on disposable category",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); disposable category deleted"
    },
    {
        "id": "FR12-AI-028",
        "coverage_id": "COV-FR12-16",
        "method": "GET",
        "endpoint": "/api/coupons",
        "sec_mapping": "FR-12",
        "caller_type": "Authenticated Administrator",
        "jwt_state": "Valid cryptographically signed token",
        "role": "admin",
        "objective": "Verify that an authenticated administrator is authorized to view the administrative coupon overview list.",
        "access_condition": "Valid JWT token containing role: 'admin'",
        "preconditions": "Admin authenticated with valid JWT token.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <VALID_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "AUTHORIZED (Not Blocked by SEC-02 or SEC-03: Administrative clearance granted)",
        "http_status": "200 OK (Inferred from SUT / Unspecified in spec)",
        "exposure_assertion": "Response returns JSON array containing all coupon records as authorized for admin.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "FR-12 / SEC-03: Admin token satisfies coupon overview authorization (api_spec Section 5.2).",
        "setup": "Obtain admin JWT token.",
        "cleanup": "None.",
        "short_objective": "Admin authorized for GET /api/coupons",
        "condition_summary": "Admin calls GET /api/coupons",
        "oracle_summary": "AUTHORIZED (Not blocked by SEC-02/03); 200 OK (Inferred)"
    },

    # -------------------------------------------------------------
    # SECTION C: ANONYMOUS / MISSING JWT (6 Tests)
    # Caller: Anonymous (No Authorization header)
    # Oracle: Semantic Denial via SEC-02; 401 Unauthorized (Inferred)
    # Must include all 3 product mutations (CAND-FR12-02 probe)
    # -------------------------------------------------------------
    {
        "id": "FR12-AI-029",
        "coverage_id": "COV-FR12-21",
        "method": "POST",
        "endpoint": "/api/products",
        "sec_mapping": "SEC-02",
        "caller_type": "Anonymous Caller",
        "jwt_state": "No Authorization header present",
        "role": "None",
        "objective": "Verify that an unauthenticated caller is denied permission to create a product, and that no product is inserted into database.",
        "access_condition": "Authorization header omitted",
        "preconditions": "Backend running; unique product payload prepared.",
        "disposable_resource": "Product name 'AnonProduct_23127027'",
        "headers": {
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "AnonProduct_23127027",
            "price": 150000,
            "description": "Anonymous creation probe",
            "imageUrl": "",
            "category_id": 1
        },
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Catalog mutation requires valid JWT authentication)",
        "http_status": "401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response must reject creation and not return created ID.",
        "side_effect_assertion": "Product 'AnonProduct_23127027' is NOT added to database (probed via GET /api/products).",
        "sec_assertion": "SEC-02: Protected catalog mutation APIs require valid JWT token (README Line 177).",
        "setup": "Prepare creation payload without Authorization header.",
        "cleanup": "If defect CAND-FR12-02 allows insertion, delete created product via admin credentials.",
        "short_objective": "Anonymous denied POST /api/products + product not created",
        "condition_summary": "Anonymous caller calls POST /api/products with product payload",
        "oracle_summary": "Semantic access denied (SEC-02); 401 (Inferred); product not created"
    },
    {
        "id": "FR12-AI-030",
        "coverage_id": "COV-FR12-24",
        "method": "PUT",
        "endpoint": "/api/products/:id",
        "sec_mapping": "SEC-02",
        "caller_type": "Anonymous Caller",
        "jwt_state": "No Authorization header present",
        "role": "None",
        "objective": "Verify that an unauthenticated caller is denied permission to update a product, and that product attributes remain unchanged.",
        "access_condition": "Authorization header omitted",
        "preconditions": "Disposable test product exists with original price 200,000.",
        "disposable_resource": "Disposable product ID <DISP_PRODUCT_ID> (Original Price: 200,000)",
        "headers": {
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "AnonTamperedName",
            "price": 10,
            "description": "Anon update probe",
            "imageUrl": "",
            "category_id": 1
        },
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Product update requires valid JWT authentication)",
        "http_status": "401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response must reject update request.",
        "side_effect_assertion": "Product attributes in database remain unchanged (GET /api/products/:id verifies original price 200,000).",
        "sec_assertion": "SEC-02: Product modification requires valid JWT authentication.",
        "setup": "Create disposable product via admin credentials.",
        "cleanup": "Delete disposable product after test.",
        "short_objective": "Anonymous denied PUT /api/products/:id + product unchanged",
        "condition_summary": "Anonymous caller calls PUT /api/products/:id on disposable product",
        "oracle_summary": "Semantic access denied (SEC-02); 401 (Inferred); product unchanged"
    },
    {
        "id": "FR12-AI-031",
        "coverage_id": "COV-FR12-27",
        "method": "DELETE",
        "endpoint": "/api/products/:id",
        "sec_mapping": "SEC-02",
        "caller_type": "Anonymous Caller",
        "jwt_state": "No Authorization header present",
        "role": "None",
        "objective": "Verify that an unauthenticated caller is denied permission to delete a product, and that the product is not deleted.",
        "access_condition": "Authorization header omitted",
        "preconditions": "Disposable test product exists in catalog.",
        "disposable_resource": "Disposable product ID <DISP_PRODUCT_ID>",
        "headers": {
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Product deletion requires valid JWT authentication)",
        "http_status": "401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response must reject deletion request.",
        "side_effect_assertion": "Product continues to exist in database (GET /api/products/:id returns product details).",
        "sec_assertion": "SEC-02: Product deletion requires valid JWT authentication.",
        "setup": "Create disposable product via admin credentials.",
        "cleanup": "Delete disposable product via admin credentials after test.",
        "short_objective": "Anonymous denied DELETE /api/products/:id + product not deleted",
        "condition_summary": "Anonymous caller calls DELETE /api/products/:id on disposable product",
        "oracle_summary": "Semantic access denied (SEC-02); 401 (Inferred); product not deleted"
    },
    {
        "id": "FR12-AI-032",
        "coverage_id": "COV-FR12-01",
        "method": "GET",
        "endpoint": "/api/admin/users",
        "sec_mapping": "SEC-02",
        "caller_type": "Anonymous Caller",
        "jwt_state": "No Authorization header present",
        "role": "None",
        "objective": "Verify that an unauthenticated caller is denied access to the administrative user accounts list.",
        "access_condition": "Authorization header omitted",
        "preconditions": "Backend running.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Admin API requires valid JWT authentication)",
        "http_status": "401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response payload must not expose user account directory records.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "SEC-02: /api/admin/* endpoints strictly require valid JWT authentication.",
        "setup": "None.",
        "cleanup": "None.",
        "short_objective": "Anonymous denied access to GET /api/admin/users",
        "condition_summary": "Anonymous caller calls GET /api/admin/users",
        "oracle_summary": "Semantic access denied (SEC-02); 401 (Inferred); zero user data exposed"
    },
    {
        "id": "FR12-AI-033",
        "coverage_id": "COV-FR12-29",
        "method": "POST",
        "endpoint": "/api/categories",
        "sec_mapping": "SEC-02",
        "caller_type": "Anonymous Caller",
        "jwt_state": "No Authorization header present",
        "role": "None",
        "objective": "Verify that an unauthenticated caller is denied permission to create a product category, and that category is not inserted.",
        "access_condition": "Authorization header omitted",
        "preconditions": "Backend running; unique category name prepared.",
        "disposable_resource": "Category name 'AnonCategory_23127027'",
        "headers": {
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "name": "AnonCategory_23127027"
        },
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Category creation requires valid JWT authentication)",
        "http_status": "401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response must reject category creation.",
        "side_effect_assertion": "Category is NOT added to database (probed via GET /api/categories).",
        "sec_assertion": "SEC-02: Category mutation requires valid JWT authentication.",
        "setup": "Prepare creation payload without Authorization header.",
        "cleanup": "None.",
        "short_objective": "Anonymous denied POST /api/categories + category not created",
        "condition_summary": "Anonymous caller calls POST /api/categories without token",
        "oracle_summary": "Semantic access denied (SEC-02); 401 (Inferred); category not inserted"
    },
    {
        "id": "FR12-AI-034",
        "coverage_id": "COV-FR12-14",
        "method": "GET",
        "endpoint": "/api/coupons",
        "sec_mapping": "SEC-02",
        "caller_type": "Anonymous Caller",
        "jwt_state": "No Authorization header present",
        "role": "None",
        "objective": "Verify that an unauthenticated caller is denied access to view the administrative coupon master list.",
        "access_condition": "Authorization header omitted",
        "preconditions": "Coupons present in database.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Coupon overview requires valid JWT authentication)",
        "http_status": "401 Unauthorized (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response must not return list of discount coupons.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "SEC-02: GET /api/coupons requires Authorization: Bearer <token> (api_spec Section 5.2).",
        "setup": "None.",
        "cleanup": "None.",
        "short_objective": "Anonymous denied access to GET /api/coupons",
        "condition_summary": "Anonymous caller calls GET /api/coupons without token",
        "oracle_summary": "Semantic access denied (SEC-02); 401 (Inferred); zero coupon data exposed"
    },

    # -------------------------------------------------------------
    # SECTION D: TOKEN VALIDITY & CRYPTOGRAPHIC BOUNDARIES (4 Tests)
    # Caller: Forged / Expired / Malformed / Tampered tokens on Admin endpoints
    # Oracle: Semantic Denial via SEC-02 / SEC-03; 403 Forbidden (Inferred)
    # -------------------------------------------------------------
    {
        "id": "FR12-AI-035",
        "coverage_id": "COV-FR12-35",
        "method": "GET",
        "endpoint": "/api/admin/users",
        "sec_mapping": "SEC-02",
        "caller_type": "Expired Admin Token Caller",
        "jwt_state": "Expired JWT (exp claim in the past)",
        "role": "admin",
        "objective": "Verify that an administrator request bearing an expired JWT token is rejected, preventing unauthorized access past session expiration.",
        "access_condition": "Token signed with correct secret but exp < currentTime",
        "preconditions": "Legitimately signed admin JWT generated with exp timestamp set 1 hour in the past.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <EXPIRED_ADMIN_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Expired token fails cryptographic verification)",
        "http_status": "403 Forbidden (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response payload must not expose user directory records.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "SEC-02: Expired tokens must be invalidated by jwt.verify.",
        "setup": "Generate expired admin token using test signing script.",
        "cleanup": "None.",
        "short_objective": "Expired admin token denied GET /api/admin/users",
        "condition_summary": "Expired admin token (exp < now) sent to GET /api/admin/users",
        "oracle_summary": "Semantic access denied (SEC-02); 403 (Inferred); expired token rejected"
    },
    {
        "id": "FR12-AI-036",
        "coverage_id": "COV-FR12-36",
        "method": "GET",
        "endpoint": "/api/admin/orders",
        "sec_mapping": "SEC-02",
        "caller_type": "Forged Signature Token Caller",
        "jwt_state": "Signature chunk altered / invalid cryptographic HMAC",
        "role": "admin (claimed in payload)",
        "objective": "Verify that a request bearing a JWT with a forged/manipulated cryptographic signature is rejected by the access-control layer.",
        "access_condition": "Header and payload claim admin role, but signature chunk is tampered",
        "preconditions": "Admin JWT with modified signature bytes.",
        "disposable_resource": "N/A (Read operation)",
        "headers": {
            "Authorization": "Bearer <FORGED_SIGNATURE_TOKEN>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-02 Violation: Forged signature fails cryptographic integrity check)",
        "http_status": "403 Forbidden (Inferred from SUT middleware / Unspecified in spec)",
        "exposure_assertion": "Response payload must not expose order records.",
        "side_effect_assertion": "Zero state modification.",
        "sec_assertion": "SEC-02: Invalid cryptographic signature rejected by jwt.verify.",
        "setup": "Construct token with altered signature chunk.",
        "cleanup": "None.",
        "short_objective": "Forged signature token denied GET /api/admin/orders",
        "condition_summary": "Forged signature token sent to GET /api/admin/orders",
        "oracle_summary": "Semantic access denied (SEC-02); 403 (Inferred); forged signature rejected"
    },
    {
        "id": "FR12-AI-037",
        "coverage_id": "COV-FR12-37",
        "method": "POST",
        "endpoint": "/api/admin/coupons",
        "sec_mapping": "SEC-03",
        "caller_type": "Missing Role Claim Token Caller",
        "jwt_state": "Valid signature, but payload contains no role field ({ id: 10 })",
        "role": "None (Omitted claim)",
        "objective": "Verify that a request bearing a valid JWT token that omits the 'role' claim entirely is denied access to admin coupon creation.",
        "access_condition": "Valid signature from SUT SECRET_KEY, payload has id but no role claim",
        "preconditions": "Custom token signed without role claim.",
        "disposable_resource": "Coupon code 'NOROLE_CPN_23127027'",
        "headers": {
            "Authorization": "Bearer <TOKEN_WITHOUT_ROLE_CLAIM>",
            "Content-Type": "application/json",
            "X-Student-Id": "23127027"
        },
        "body": {
            "code": "NOROLE_CPN_23127027",
            "type": "fixed",
            "discount_value": 10000,
            "min_order_amount": 50000,
            "expired_at": "2099-12-31",
            "max_uses_per_user": 1
        },
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Missing role claim does not satisfy role === 'admin')",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject coupon creation.",
        "side_effect_assertion": "Coupon 'NOROLE_CPN_23127027' is NOT created in database.",
        "sec_assertion": "SEC-03: System requires explicit role === 'admin'; missing claim must not grant elevated privileges.",
        "setup": "Generate custom signed token omitting role claim.",
        "cleanup": "None.",
        "short_objective": "Missing role claim token denied POST /api/admin/coupons",
        "condition_summary": "Valid JWT omitting 'role' claim sent to POST /api/admin/coupons",
        "oracle_summary": "Semantic access denied (SEC-03); coupon not created"
    },
    {
        "id": "FR12-AI-038",
        "coverage_id": "COV-FR12-38",
        "method": "DELETE",
        "endpoint": "/api/admin/users/:id",
        "sec_mapping": "SEC-03",
        "caller_type": "Tampered / Spoofed Role Caller",
        "jwt_state": "Valid signature, but payload contains spoofed role ('ADMIN' uppercase or 'manager')",
        "role": "ADMIN (Uppercase)",
        "objective": "Verify that case sensitivity is strictly enforced and that uppercase role 'ADMIN' or spoofed roles are denied administrative deletion.",
        "access_condition": "Valid signature from SUT SECRET_KEY, payload has role: 'ADMIN'",
        "preconditions": "Disposable test user exists; custom token signed with role: 'ADMIN'.",
        "disposable_resource": "Disposable test user ID <TARGET_USER_ID>",
        "headers": {
            "Authorization": "Bearer <TOKEN_UPPERCASE_ROLE>",
            "X-Student-Id": "23127027"
        },
        "body": None,
        "semantic_outcome": "ACCESS DENIED (SEC-03 Violation: Strict exact-match role === 'admin' required; uppercase or spoofed role rejected)",
        "http_status": "403 Forbidden (Inferred) / UNKNOWN by official specification",
        "exposure_assertion": "Response must reject user deletion.",
        "side_effect_assertion": "Target disposable user is NOT deleted from database (verified via login probe).",
        "sec_assertion": "SEC-03: Role verification must strictly match 'admin' in exact lowercase.",
        "setup": "Create disposable test user; sign custom token with role: 'ADMIN'.",
        "cleanup": "Clean up disposable test user via official admin credentials after test.",
        "short_objective": "Uppercase role 'ADMIN' denied DELETE /api/admin/users/:id",
        "condition_summary": "Token with uppercase role: 'ADMIN' sent to DELETE /api/admin/users/:id",
        "oracle_summary": "Semantic access denied (SEC-03); user not deleted"
    }
]

def generate_original_testcases():
    filepath = "hw06/testcases/fr12/generated-ai-original.md"
    content = """# FR-12: Access Control — AI-Generated Test Suite (Original / Immutable)

> **Provenance & Integrity Notice:**
> - **Origin:** AI (Gemini 3.7 Flash via Antigravity IDE)
> - **Generation Timestamp:** 2026-09-02T22:38:41+07:00
> - **Feature Pool:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Governing Contract Specifications:**
>   - `README.md`: Section 6 (Phân hệ Web Admin, FR-12 Lines 174–180), Section 9 (Yêu cầu Bảo mật, SEC-02 Line 279, SEC-03 Line 280)
>   - `api_specification.md`: Section 5.2 (Lines 165–168), Section 6 (Lines 171–215), Section 3.3–3.4 (Lines 87–107)
> - **Total Test Count:** Exactly **38 Test Cases** (`FR12-AI-001` through `FR12-AI-038`)
> - **Document Status:** **IMMUTABLE ORIGINAL AI GENERATION**. This artifact must be preserved exactly as generated by AI to maintain academic audit integrity. Subsequent human review verdicts and corrections are maintained in `human-audit.md` and `reviewed-ai-final.md`.

---

## Suite Summary & Strategy Breakdown

- **Section A: Standard-User Role Denial (`role = 'user'`):** 14 Test Cases (`FR12-AI-001` .. `FR12-AI-014`). Probes all 14 exposed operations to confirm standard users are denied administrative and catalog-mutation access (`SEC-03`).
- **Section B: Valid Admin Authorization (`role = 'admin'`):** 14 Test Cases (`FR12-AI-015` .. `FR12-AI-028`). Probes all 14 exposed operations to confirm administrators are authorized and not blocked by the access-control layer (`FR-12`).
- **Section C: Anonymous / Missing Authentication:** 6 Test Cases (`FR12-AI-029` .. `FR12-AI-034`). Probes unauthenticated requests across product mutations (`POST/PUT/DELETE /api/products`), user admin, category mutation, and coupon overview (`SEC-02`).
- **Section D: Token Cryptographic & Boundary Robustness:** 4 Test Cases (`FR12-AI-035` .. `FR12-AI-038`). Evaluates expired tokens, forged signatures, omitted role claims, and uppercase/spoofed role values (`SEC-02` & `SEC-03`).
- **Dual-Assertion Policy:** All 17 data-mutating negative test cases enforce response denial assertion AND a follow-up read (`GET`) verification proving no unauthorized side-effect occurred.
- **Disposable Data Policy:** All mutating admin operations run on disposable entities; zero lecturer baseline seeded data is modified or deleted.

---

"""

    for tc in TEST_CASES:
        body_json = json.dumps(tc["body"], indent=2) if tc["body"] is not None else "None (Empty Body)"
        headers_str = "\n".join([f"  - `{k}: {v}`" for k, v in tc["headers"].items()])

        content += f"""## {tc["id"]} — {tc["short_objective"]}

### Identity
- **Test ID:** `{tc["id"]}`
- **Origin:** AI
- **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
- **Coverage ID:** `{tc["coverage_id"]}`
- **HTTP Method:** `{tc["method"]}`
- **Target Endpoint:** `{tc["endpoint"]}`

### Traceability
- **FR-12 Contract Reference:** `README.md` Section 6 (Lines 174–180)
- **Security Requirement Mapping:** `{tc["sec_mapping"]}` (`README.md` Section 9 Line {"279 (SEC-02: Valid JWT required)" if "SEC-02" in tc["sec_mapping"] else "280 (SEC-03: Admin role enforced)" if "SEC-03" in tc["sec_mapping"] else "176-180 (FR-12 Admin Subsystem)"})
- **Official Specification Source:** `api_specification.md` / `README.md`
- **Oracle Classification:** Semantic Denial / Clearance = SPECIFIED; Exact HTTP code = INFERRED / UNKNOWN by spec

### Subject Identity
- **Caller Type:** {tc["caller_type"]}
- **JWT Token State:** {tc["jwt_state"]}
- **Embedded Role Claim:** `{tc["role"]}`
- **Authentication Condition:** {tc["access_condition"]}

### Test Design
- **Objective:** {tc["objective"]}
- **Access-Control Condition:** {tc["access_condition"]}
- **Preconditions:** {tc["preconditions"]}
- **Disposable Resource State:** {tc["disposable_resource"]}

### HTTP Request Specification
- **Method:** `{tc["method"]}`
- **Endpoint:** `{tc["endpoint"]}`
- **Request Headers:**
{headers_str}
- **Request Body:**
```json
{body_json}
```

### Expected Access-Control Result
- **Semantic Authorization Outcome:** {tc["semantic_outcome"]}
- **Expected HTTP Status:** `{tc["http_status"]}`
- **Response Exposure Assertion:** {tc["exposure_assertion"]}
- **Unauthorized Side-Effect Assertion:** {tc["side_effect_assertion"]}
- **Security Invariant Assertion:** {tc["sec_assertion"]}

### Lifecycle & Automation
- **Setup Required:** {tc["setup"]}
- **Cleanup Required:** {tc["cleanup"]}
- **Automation Status:** NOT AUTOMATED YET (Planned for Phase 4)

---

"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filepath} successfully with {len(TEST_CASES)} test cases.")

def generate_human_audit_worksheet():
    filepath = "hw06/testcases/fr12/human-audit.md"
    content = """# FR-12: Access Control — Human Audit Worksheet

> **Academic Integrity Notice & Student Ownership:**
> - **Auditor:** Phạm Ngọc Gia Bảo (Student ID: `23127027`)
> - **Feature:** Pool C — FR-12: Access Control (Kiểm soát truy cập)
> - **Source Test Suite:** `hw06/testcases/fr12/generated-ai-original.md` (38 AI-generated cases)
> - **Evaluation Rule:** Every AI-generated testcase must be independently evaluated by the student into one of three distinct verdicts:
>   - **VALID:** The testcase is logically sound, correctly mapped to FR-12/SEC-02/SEC-03, has realistic oracles, and is ready for execution.
>   - **INCOMPLETE:** The testcase has technical merit but requires calibrated headers, side-effect checks, or oracle corrections.
>   - **INVALID:** The testcase violates specification boundaries, tests out-of-scope functional logic, or targets nonexistent routes.
> - **Student Ownership Policy:** All student verdict, reasoning, and correction columns are initially completely **BLANK** to ensure honest human review without AI bias.

---

| Test ID | Coverage ID | Short Objective | Student Verdict | Student Reasoning | Student Correction | Student Reviewed At |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
"""
    for tc in TEST_CASES:
        content += f"| `{tc['id']}` | `{tc['coverage_id']}` | {tc['short_objective']} | | | | |\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filepath} successfully with {len(TEST_CASES)} blank rows.")

def generate_compact_review_sheet():
    filepath = "hw06/testcases/fr12/human-review-compact.md"
    content = """# FR-12: Access Control — Compact Human Review Sheet

> **Auditor:** Phạm Ngọc Gia Bảo (`23127027`) | **Total Cases:** 38 | **Student Verdicts:** PENDING REVIEW

| Test ID | Endpoint | Caller Identity | One-Sentence Condition | Requirement / Oracle | Student Final Verdict | Student Note |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
"""
    for tc in TEST_CASES:
        content += f"| `{tc['id']}` | `{tc['method']} {tc['endpoint']}` | {tc['role']} | {tc['condition_summary']} | {tc['oracle_summary']} | | |\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filepath} successfully with {len(TEST_CASES)} compact rows.")

if __name__ == "__main__":
    generate_original_testcases()
    generate_human_audit_worksheet()
    generate_compact_review_sheet()
