import json

def generate_postman_collection():
    collection = {
        "info": {
            "_postman_id": "c1a2b3d4-e5f6-47a8-b9c0-112233445566",
            "name": "FR-01 — Account Registration Test Suite",
            "description": "Comprehensive automated API test suite for FR-01 Account Registration (HCMUS EShop SUT). Created for HW06 API Testing by student Pham Ngoc Gia Bao (23127027). Contains 42 automated API requests (37 reviewed AI tests + 5 student-selected extension tests).",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "event": [
            {
                "listen": "prerequest",
                "script": {
                    "type": "text/javascript",
                    "exec": [
                        "// Central X-Student-Id injection required by HW06",
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
                        "pm.test('Central Injection - Request header X-Student-Id is present and matches 23127027', function () {",
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

    # Helper function to create an item
    def create_request(test_id, title, method, url_path, body_obj, raw_body_str, headers_list, test_script_lines, prerequest_lines=None):
        req = {
            "name": f"{test_id} — {title}",
            "event": [],
            "request": {
                "method": method,
                "header": headers_list,
                "url": {
                    "raw": "{{baseUrl}}" + url_path,
                    "host": ["{{baseUrl}}"],
                    "path": [p for p in url_path.split("/") if p]
                }
            },
            "response": []
        }

        if prerequest_lines:
            req["event"].append({
                "listen": "prerequest",
                "script": {
                    "type": "text/javascript",
                    "exec": prerequest_lines
                }
            })

        if test_script_lines:
            req["event"].append({
                "listen": "test",
                "script": {
                    "type": "text/javascript",
                    "exec": test_script_lines
                }
            })

        if raw_body_str is not None:
            req["request"]["body"] = {
                "mode": "raw",
                "raw": raw_body_str
            }
        elif body_obj is not None:
            req["request"]["body"] = {
                "mode": "raw",
                "raw": json.dumps(body_obj, ensure_ascii=False, indent=2)
            }

        return req

    # Standard headers
    json_headers = [
        {"key": "Content-Type", "value": "application/json"}
    ]

    # Standard 200 OK test lines
    std_200_tests = [
        "pm.test('Status Code is 200 OK (SPECIFIED)', function () {",
        "    pm.response.to.have.status(200);",
        "});",
        "pm.test('Response contains success message and id (EXAMPLE-DERIVED)', function () {",
        "    var jsonData = pm.response.json();",
        "    pm.expect(jsonData).to.have.property('message');",
        "    pm.expect(jsonData).to.have.property('id');",
        "});",
        "pm.test('Security Hardening - Password is not leaked in response', function () {",
        "    var text = pm.response.text();",
        "    pm.expect(text).to.not.include('Password');",
        "});"
    ]

    # Standard Rejection test lines
    std_rejection_tests = [
        "pm.test('Semantic Rejection - Invalid request must NOT return 200 OK (SPECIFIED REJECTION)', function () {",
        "    pm.expect(pm.response.code).to.not.equal(200);",
        "});",
        "pm.test('Response is controlled and parseable', function () {",
        "    pm.expect(pm.response.code).to.be.oneOf([400, 422, 500]);",
        "});"
    ]

    # Standard Robustness test lines
    std_robustness_tests = [
        "pm.test('Robustness / Characterization - Server handles input safely without crashing', function () {",
        "    pm.expect(pm.response.code).to.be.oneOf([200, 201, 400, 409, 422, 500]);",
        "});",
        "pm.test('Response is parseable JSON', function () {",
        "    var jsonData = pm.response.json();",
        "    pm.expect(jsonData).to.be.an('object');",
        "});"
    ]

    # Folder 1: Positive Happy Path
    f1 = {"name": "01 - Positive Happy Path", "item": []}
    f1["item"].append(create_request(
        "FR01-AI-001", "Standard Valid ASCII Registration", "POST", "/api/register",
        {"name": "Nguyen Van A", "email": "fr01_ai_001_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_200_tests
    ))
    f1["item"].append(create_request(
        "FR01-AI-009", "Standard Valid RFC Email Registration", "POST", "/api/register",
        {"name": "Standard User", "email": "fr01_ai_009_{{$timestamp}}@domain.com", "password": "Password123!"},
        None, json_headers, std_200_tests
    ))
    f1["item"].append(create_request(
        "FR01-AI-020", "Standard Strong Password Meeting All 5 Criteria", "POST", "/api/register",
        {"name": "Strong Pass User", "email": "fr01_ai_020_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_200_tests
    ))
    f1["item"].append(create_request(
        "FR01-AI-027", "Password Length Boundary: 8 Chars (Exact Minimum)", "POST", "/api/register",
        {"name": "Len 8 User", "email": "fr01_ai_027_{{$timestamp}}@example.com", "password": "Pass12!a"},
        None, json_headers, std_200_tests
    ))
    f1["item"].append(create_request(
        "FR01-AI-028", "Password Length Boundary: 9 Chars (Minimum + 1)", "POST", "/api/register",
        {"name": "Len 9 User", "email": "fr01_ai_028_{{$timestamp}}@example.com", "password": "Passw12!a"},
        None, json_headers, std_200_tests
    ))
    collection["item"].append(f1)

    # Folder 2: Required Fields Validation
    f2 = {"name": "02 - Required Fields Validation", "item": []}
    f2["item"].append(create_request(
        "FR01-AI-003", "Omitted Mandatory Name Field Rejection", "POST", "/api/register",
        {"email": "fr01_ai_003_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_rejection_tests
    ))
    f2["item"].append(create_request(
        "FR01-AI-004", "Empty String Name Value Inferred Rejection", "POST", "/api/register",
        {"name": "", "email": "fr01_ai_004_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_rejection_tests
    ))
    f2["item"].append(create_request(
        "FR01-AI-011", "Omitted Mandatory Email Field Rejection", "POST", "/api/register",
        {"name": "No Email User", "password": "Password123!"},
        None, json_headers, std_rejection_tests
    ))
    f2["item"].append(create_request(
        "FR01-AI-012", "Empty String Email Value Rejection", "POST", "/api/register",
        {"name": "Empty Email User", "email": "", "password": "Password123!"},
        None, json_headers, std_rejection_tests
    ))
    f2["item"].append(create_request(
        "FR01-AI-032", "Empty String Password Value Rejection", "POST", "/api/register",
        {"name": "Empty Pass User", "email": "fr01_ai_032_{{$timestamp}}@example.com", "password": ""},
        None, json_headers, std_rejection_tests
    ))
    f2["item"].append(create_request(
        "FR01-AI-035", "Empty JSON Body Rejection", "POST", "/api/register",
        {},
        None, json_headers, std_rejection_tests
    ))
    collection["item"].append(f2)

    # Folder 3: Email Format & Validation
    f3 = {"name": "03 - Email Format & Validation", "item": []}
    f3["item"].append(create_request(
        "FR01-AI-010", "Advanced RFC Email Plus-Addressing Characterization", "POST", "/api/register",
        {"name": "Tagged User", "email": "fr01_ai_010+tag_{{$timestamp}}@domain.com", "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    f3["item"].append(create_request(
        "FR01-AI-013", "Malformed Email Missing At-Symbol (@) Rejection", "POST", "/api/register",
        {"name": "No At User", "email": "fr01_ai_013_userdomain.com", "password": "Password123!"},
        None, json_headers, std_rejection_tests
    ))
    f3["item"].append(create_request(
        "FR01-AI-014", "Malformed Email Missing Domain Part Rejection", "POST", "/api/register",
        {"name": "No Domain User", "email": "fr01_ai_014_user@", "password": "Password123!"},
        None, json_headers, std_rejection_tests
    ))
    collection["item"].append(f3)

    # Folder 4: Password Policy Verification
    f4 = {"name": "04 - Password Policy Verification", "item": []}
    f4["item"].append(create_request(
        "FR01-AI-021", "Documented Special Symbol: At-Sign (@)", "POST", "/api/register",
        {"name": "Symbol At User", "email": "fr01_ai_021_{{$timestamp}}@example.com", "password": "Passw0rd@"},
        None, json_headers, std_200_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-022", "Documented Special Symbol: Dollar-Sign ($)", "POST", "/api/register",
        {"name": "Symbol Dollar User", "email": "fr01_ai_022_{{$timestamp}}@example.com", "password": "Passw0rd$"},
        None, json_headers, std_200_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-023", "Documented Special Symbol: Ampersand (&)", "POST", "/api/register",
        {"name": "Symbol Amp User", "email": "fr01_ai_023_{{$timestamp}}@example.com", "password": "Passw0rd&"},
        None, json_headers, std_200_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-024", "Required Special Symbol Plus Extra Symbol (!#)", "POST", "/api/register",
        {"name": "Combo Symbol User", "email": "fr01_ai_024_{{$timestamp}}@example.com", "password": "Password123!#"},
        None, json_headers, std_200_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-025", "Missing Required Special Character from Set Rejection", "POST", "/api/register",
        {"name": "No Symbol User", "email": "fr01_ai_025_{{$timestamp}}@example.com", "password": "Password1234"},
        None, json_headers, std_rejection_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-026", "Password Length Boundary: 7 Chars (Minimum - 1) Rejection", "POST", "/api/register",
        {"name": "Len 7 User", "email": "fr01_ai_026_{{$timestamp}}@example.com", "password": "Pass1!a"},
        None, json_headers, std_rejection_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-029", "Missing Uppercase Letter in Password Rejection", "POST", "/api/register",
        {"name": "No Upper User", "email": "fr01_ai_029_{{$timestamp}}@example.com", "password": "password123!"},
        None, json_headers, std_rejection_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-030", "Missing Lowercase Letter in Password Rejection", "POST", "/api/register",
        {"name": "No Lower User", "email": "fr01_ai_030_{{$timestamp}}@example.com", "password": "PASSWORD123!"},
        None, json_headers, std_rejection_tests
    ))
    f4["item"].append(create_request(
        "FR01-AI-031", "Missing Numeric Digit in Password Rejection", "POST", "/api/register",
        {"name": "No Digit User", "email": "fr01_ai_031_{{$timestamp}}@example.com", "password": "Password!@#$"},
        None, json_headers, std_rejection_tests
    ))
    collection["item"].append(f4)

    # Folder 5: State & Duplicate Lifecycle
    f5 = {"name": "05 - State & Duplicate Lifecycle", "item": []}
    f5["item"].append(create_request(
        "FR01-AI-016", "Duplicate Registration of Pre-Seeded Email Rejection", "POST", "/api/register",
        {"name": "Duplicate SeedTest", "email": "test@eshop.com", "password": "Password123!"},
        None, json_headers, [
            "pm.test('Duplicate Email Rejection - Pre-seeded email must not be re-registered (SPECIFIED)', function () {",
            "    pm.expect(pm.response.code).to.not.equal(200);",
            "});"
        ]
    ))
    # Chained sequential duplicate test: Pre-request script registers the user, main request tests rejection
    seq_prereq = [
        "var uniqueEmail = 'fr01_seq_dup_' + Date.now() + '@example.com';",
        "pm.environment.set('seqDupEmail', uniqueEmail);",
        "// Send preliminary registration",
        "pm.sendRequest({",
        "    url: pm.environment.get('baseUrl') + '/api/register',",
        "    method: 'POST',",
        "    header: {",
        "        'Content-Type': 'application/json',",
        "        'X-Student-Id': '23127027'",
        "    },",
        "    body: {",
        "        mode: 'raw',",
        "        raw: JSON.stringify({",
        "            name: 'First Instance',",
        "            email: uniqueEmail,",
        "            password: 'Password123!'",
        "        })",
        "    }",
        "}, function (err, res) {",
        "    console.log('Step 1 pre-registration completed with status:', res ? res.code : err);",
        "});"
    ]
    f5["item"].append(create_request(
        "FR01-AI-017", "Duplicate Registration via Dynamic Sequential Call", "POST", "/api/register",
        {"name": "Second Instance", "email": "{{seqDupEmail}}", "password": "Password123!"},
        None, json_headers, [
            "pm.test('State-Dependent Duplicate Rejection - Repeated registration with same email must be rejected (SPECIFIED)', function () {",
            "    pm.expect(pm.response.code).to.not.equal(200);",
            "});"
        ],
        seq_prereq
    ))
    f5["item"].append(create_request(
        "FR01-AI-018", "Case-Insensitive Duplicate Email Characterization Probe", "POST", "/api/register",
        {"name": "Case User", "email": "TEST@eshop.com", "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    collection["item"].append(f5)

    # Folder 6: Security Assertions
    f6 = {"name": "06 - Security Assertions", "item": []}
    f6["item"].append(create_request(
        "FR01-AI-007", "Literal SQL Syntax Handling in Name (SEC-05)", "POST", "/api/register",
        {"name": "O'Connor", "email": "fr01_ai_007_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, [
            "pm.test('SEC-05 - Apostrophe in name handled safely as literal data without SQL crash', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400]);",
            "    var text = pm.response.text();",
            "    pm.expect(text).to.not.include('SQLITE_ERROR');",
            "    pm.expect(text).to.not.include('syntax error');",
            "});"
        ]
    ))
    f6["item"].append(create_request(
        "FR01-AI-019", "Parameterized Query Verification via SQL Injection String in Name (SEC-05 Redesign)", "POST", "/api/register",
        {"name": "Robert'); DROP TABLE users;--", "email": "fr01_ai_019_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, [
            "pm.test('SEC-05 - SQL injection syntax in name handled safely without SQL syntax error', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400]);",
            "    var text = pm.response.text();",
            "    pm.expect(text).to.not.include('SQLITE_ERROR');",
            "    pm.expect(text).to.not.include('syntax error');",
            "});"
        ]
    ))
    f6["item"].append(create_request(
        "FR01-AI-038", "Security Hardening: Credential Non-Leakage in Response", "POST", "/api/register",
        {"name": "Hardened User", "email": "fr01_ai_038_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, [
            "pm.test('Security Hardening - Response body does not leak password or sensitive credentials', function () {",
            "    var text = pm.response.text();",
            "    pm.expect(text).to.not.include('Password123!');",
            "    pm.expect(text).to.not.include('hash');",
            "    pm.expect(text).to.not.include('salt');",
            "    pm.expect(text).to.not.include('reset_token');",
            "});"
        ]
    ))
    collection["item"].append(f6)

    # Folder 7: Robustness & Characterization
    f7 = {"name": "07 - Robustness & Characterization", "item": []}
    f7["item"].append(create_request(
        "FR01-AI-002", "Vietnamese Unicode Name Characterization Probe", "POST", "/api/register",
        {"name": "Trần Thị Bích Hạnh", "email": "fr01_ai_002_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-005", "Non-String Integer Name Data Type Robustness Probe", "POST", "/api/register",
        {"name": 12345, "email": "fr01_ai_005_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-006", "Extreme Upper Length Name Robustness Probe (1000 Chars)", "POST", "/api/register",
        {"name": "A" * 1000, "email": "fr01_ai_006_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-008", "HTML Script Tag Robustness Probe in Name", "POST", "/api/register",
        {"name": "<script>alert(1)</script>", "email": "fr01_ai_008_{{$timestamp}}@example.com", "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-015", "Non-String Integer Email Data Type Robustness Probe", "POST", "/api/register",
        {"name": "Type User", "email": 99999, "password": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-033", "Non-String Integer Password Data Type Robustness Probe", "POST", "/api/register",
        {"name": "Type Pass User", "email": "fr01_ai_033_{{$timestamp}}@example.com", "password": 12345678},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-034", "Extreme Upper Length Password Robustness Probe (128 Chars)", "POST", "/api/register",
        {"name": "Long Pass User", "email": "fr01_ai_034_{{$timestamp}}@example.com", "password": "Password123!" + "A" * 116},
        None, json_headers, std_robustness_tests
    ))
    f7["item"].append(create_request(
        "FR01-AI-036", "Unexpected Extra Field (confirmPassword) Robustness Probe", "POST", "/api/register",
        {"name": "Extra Field User", "email": "fr01_ai_036_{{$timestamp}}@example.com", "password": "Password123!", "confirmPassword": "Password123!"},
        None, json_headers, std_robustness_tests
    ))
    collection["item"].append(f7)

    # Folder 8: Student-Selected Extensions
    f8 = {"name": "08 - Student-Selected Extensions", "item": []}
    # FR01-STU-001: Malformed raw JSON (missing closing brace)
    raw_malformed = '{"name": "Malformed User", "email": "stu001_malformed@example.com", "password": "Password123!"'
    f8["item"].append(create_request(
        "FR01-STU-001", "Syntactically Malformed JSON Body Robustness Probe", "POST", "/api/register",
        None, raw_malformed, json_headers, [
            "pm.test('Parser Robustness - Malformed JSON does not create user or crash server', function () {",
            "    pm.expect(pm.response.code).to.not.equal(200);",
            "    pm.expect(pm.response.code).to.be.oneOf([400, 500]);",
            "});"
        ]
    ))
    # FR01-STU-002: Wrong Content-Type (text/plain)
    f8["item"].append(create_request(
        "FR01-STU-002", "Unsupported Content-Type Header (text/plain) Robustness Probe", "POST", "/api/register",
        {"name": "PlainText ContentType", "email": "stu002_plaintext@example.com", "password": "Password123!"},
        None, [{"key": "Content-Type", "value": "text/plain"}], [
            "pm.test('MIME Handling - Non-JSON Content-Type handled safely', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 415, 500]);",
            "});"
        ]
    ))
    # FR01-STU-003: Duplicate JSON property key
    raw_dup = '{\n  "name": "Duplicate Key User",\n  "email": "first_stu003@example.com",\n  "email": "second_stu003@example.com",\n  "password": "Password123!"\n}'
    f8["item"].append(create_request(
        "FR01-STU-003", "Duplicate JSON Property Key Parser Characterization Probe", "POST", "/api/register",
        None, raw_dup, json_headers, [
            "pm.test('Duplicate Key Characterization - Server handles duplicate property safely', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400]);",
            "});"
        ]
    ))
    # FR01-STU-004: Unsupported HTTP Method PUT
    f8["item"].append(create_request(
        "FR01-STU-004", "Unsupported HTTP Method (PUT) Routing Verification Probe", "PUT", "/api/register",
        {"name": "Put Method User", "email": "stu004_put@example.com", "password": "Password123!"},
        None, json_headers, [
            "pm.test('Method Routing - Registration rejected for unsupported PUT verb', function () {",
            "    pm.expect(pm.response.code).to.not.equal(200);",
            "    pm.expect(pm.response.code).to.be.oneOf([404, 405, 500]);",
            "});"
        ]
    ))
    # FR01-STU-005: Email Domain as IP literal
    f8["item"].append(create_request(
        "FR01-STU-005", "Email Domain as IP Address Literal Characterization Probe", "POST", "/api/register",
        {"name": "IP Domain User", "email": "stu005_ip@[127.0.0.1]", "password": "Password123!"},
        None, json_headers, [
            "pm.test('Email Grammar Characterization - IP address literal domain handled safely', function () {",
            "    pm.expect(pm.response.code).to.be.oneOf([200, 400]);",
            "});"
        ]
    ))
    collection["item"].append(f8)

    # Output file
    out_path = "hw06/postman/collections/fr01-registration.postman_collection.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(collection, f, ensure_ascii=False, indent=2)
    print(f"Collection written to {out_path}")

if __name__ == "__main__":
    generate_postman_collection()
