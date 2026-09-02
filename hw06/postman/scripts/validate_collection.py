import json, re

def validate():
    col_path = "hw06/postman/collections/fr01-registration.postman_collection.json"
    env_path = "hw06/postman/environments/eshop-local.postman_environment.json"

    with open(col_path, "r", encoding="utf-8") as f:
        col = json.load(f)

    with open(env_path, "r", encoding="utf-8") as f:
        env = json.load(f)

    # 1. Check environment
    env_keys = {v["key"]: v["value"] for v in env["values"]}
    assert env_keys.get("baseUrl") == "http://localhost:3000", f"Invalid baseUrl: {env_keys.get('baseUrl')}"
    assert env_keys.get("studentId") == "23127027", f"Invalid studentId: {env_keys.get('studentId')}"
    print("✓ Environment variables valid (baseUrl=http://localhost:3000, studentId=23127027).")

    # 2. Check central injection in collection
    col_prereq = ""
    for ev in col.get("event", []):
        if ev.get("listen") == "prerequest":
            col_prereq = "\n".join(ev["script"]["exec"])
    assert "X-Student-Id" in col_prereq and "23127027" in col_prereq, "Missing central X-Student-Id injection!"
    print("✓ Central X-Student-Id injection configured in collection pre-request script.")

    # 3. Collect all requests
    requests = []
    for folder in col["item"]:
        folder_name = folder["name"]
        for item in folder["item"]:
            requests.append((folder_name, item))

    print(f"Total requests in collection: {len(requests)}")
    assert len(requests) == 42, f"Expected exactly 42 API requests, found {len(requests)}"

    # Check IDs
    all_ids = []
    traceability = []
    for folder_name, item in requests:
        name = item["name"]
        m = re.match(r"(FR01-(?:AI|STU)-\d{3})", name)
        assert m, f"Request name missing standard test ID prefix: {name}"
        t_id = m.group(1)
        all_ids.append(t_id)
        traceability.append((t_id, name, folder_name))

    # Check for duplicates or missing
    assert len(all_ids) == len(set(all_ids)), f"Duplicate test IDs found in collection: {[x for x in all_ids if all_ids.count(x) > 1]}"

    # Expected AI tests: 1..38 except 037 (37 tests)
    expected_ai = [f"FR01-AI-{i:03d}" for i in range(1, 39) if i != 37]
    expected_stu = [f"FR01-STU-{i:03d}" for i in range(1, 6)]
    expected_all = expected_ai + expected_stu

    assert set(all_ids) == set(expected_all), f"ID mismatch! Missing: {set(expected_all) - set(all_ids)}, Extra: {set(all_ids) - set(expected_all)}"
    print("✓ Exactly 42 expected test IDs (37 reviewed AI + 5 student-selected extensions) present with 0 missing and 0 duplicates.")

    # 4. Check special tests
    # FR01-STU-001: Malformed JSON
    stu001 = [item for f, item in requests if "FR01-STU-001" in item["name"]][0]
    raw1 = stu001["request"]["body"]["raw"]
    assert raw1.endswith('Password123!"') and not raw1.endswith('}'), f"FR01-STU-001 malformed body error: {raw1}"
    print("✓ FR01-STU-001 raw malformed JSON verified (missing closing brace preserved).")

    # FR01-STU-002: Wrong Content-Type
    stu002 = [item for f, item in requests if "FR01-STU-002" in item["name"]][0]
    ct = [h["value"] for h in stu002["request"]["header"] if h["key"].lower() == "content-type"][0]
    assert ct == "text/plain", f"FR01-STU-002 Content-Type is {ct}, expected text/plain"
    print("✓ FR01-STU-002 Content-Type header verified (text/plain preserved).")

    # FR01-STU-003: Duplicate JSON property key
    stu003 = [item for f, item in requests if "FR01-STU-003" in item["name"]][0]
    raw3 = stu003["request"]["body"]["raw"]
    assert raw3.count('"email"') == 2, f"FR01-STU-003 duplicate key missing: {raw3}"
    print("✓ FR01-STU-003 duplicate JSON property keys verified (both email keys preserved).")

    # FR01-STU-004: PUT method
    stu004 = [item for f, item in requests if "FR01-STU-004" in item["name"]][0]
    assert stu004["request"]["method"] == "PUT", f"FR01-STU-004 method is {stu004['request']['method']}, expected PUT"
    print("✓ FR01-STU-004 method verified (PUT preserved).")

    # FR01-AI-019: SQL injection name
    ai019 = [item for f, item in requests if "FR01-AI-019" in item["name"]][0]
    assert "DROP TABLE users" in ai019["request"]["body"]["raw"], "FR01-AI-019 redesigned SQL payload missing!"
    print("✓ FR01-AI-019 redesigned SQL injection payload verified.")

    print("\nALL PRE-EXECUTION COLLECTION CHECKS PASSED.")

if __name__ == "__main__":
    validate()
