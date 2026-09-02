# Agent Skill: Test Generator — Algorithmic Pseudocode

> **Student Information:**
> - **Student Name:** Phạm Ngọc Gia Bảo
> - **Student ID:** `23127027`
> - **Artifact:** Architectural Pseudocode for Automated API Test Case Generation

---

```text
ALGORITHM GenerateAPITestSuite(endpointSpec):
    INPUT: endpointSpec = {
        route: String,
        method: Enum[GET, POST, PUT, DELETE],
        authLevel: Enum[PUBLIC, USER_PROTECTED, ADMIN_PROTECTED],
        parameters: List of FieldSpec {
            name: String,
            type: Enum[STRING, INTEGER, NUMBER, BOOLEAN, OBJECT],
            required: Boolean,
            minVal: Optional[Number],
            maxVal: Optional[Number],
            format: Optional[String]
        }
    }
    OUTPUT: testCases = List of TestCase

    INITIALIZE testCases = EmptyList()
    counter = 1

    // =========================================================================
    // 1. HAPPY PATH & NOMINAL VALID EQUIVALENCE PARTITIONS
    // =========================================================================
    nominalPayload = GenerateNominalPayload(endpointSpec.parameters)
    validAuth = GetAppropriateToken(endpointSpec.authLevel)

    testCases.Append(CreateTestCase(
        id = FormatID("GEN-NOM", counter++),
        category = "Positive Nominal Equivalence",
        route = endpointSpec.route,
        method = endpointSpec.method,
        auth = validAuth,
        payload = nominalPayload,
        semanticOracle = "MUTATION_ACCEPTED_OR_DATA_RETURNED",
        statusOracle = (endpointSpec.authLevel == ADMIN_PROTECTED) ? "200/201 (INFERRED)" : "200/201 (SPECIFIED)",
        classification = "SPECIFIED"
    ))

    // =========================================================================
    // 2. FIELD-LEVEL EQUIVALENCE & BOUNDARY VALUE ANALYSIS (BVA)
    // =========================================================================
    FOR EACH field IN endpointSpec.parameters:
        // A. Omission of Mandatory Field
        IF field.required IS True:
            omittedPayload = Clone(nominalPayload)
            RemoveKey(omittedPayload, field.name)
            testCases.Append(CreateTestCase(
                id = FormatID("GEN-REQ", counter++),
                category = "Negative Equivalence - Missing Field",
                auth = validAuth,
                payload = omittedPayload,
                semanticOracle = "REJECTED_WITH_NO_STATE_MUTATION",
                statusOracle = "400 Bad Request / 422 Unprocessable (INFERRED)",
                classification = "INFERRED"
            ))

        // B. Empty String / Zero Value Probe
        IF field.type == STRING:
            emptyPayload = Clone(nominalPayload)
            emptyPayload[field.name] = ""
            testCases.Append(CreateTestCase(
                id = FormatID("GEN-BVA", counter++),
                category = "Boundary Value Analysis - Empty String",
                auth = validAuth,
                payload = emptyPayload,
                semanticOracle = "REJECTED_OR_TRIMMED_CLEANLY",
                statusOracle = "UNKNOWN / SPEC-SILENT",
                classification = "ROBUSTNESS"
            ))

        // C. Numeric Bounds (Min, Below-Min, Max, Above-Max)
        IF field.type IN [INTEGER, NUMBER]:
            IF field.minVal IS NOT None:
                // Exact Minimum (Valid BVA)
                bvaMinPayload = Clone(nominalPayload)
                bvaMinPayload[field.name] = field.minVal
                testCases.Append(CreateTestCase(
                    id = FormatID("GEN-BVA", counter++),
                    category = "Boundary Value Analysis - Exact Minimum",
                    auth = validAuth,
                    payload = bvaMinPayload,
                    semanticOracle = "MUTATION_ACCEPTED",
                    statusOracle = "200 OK (INFERRED)",
                    classification = "INFERRED"
                ))

                // Just Below Minimum (Invalid BVA)
                bvaSubMinPayload = Clone(nominalPayload)
                bvaSubMinPayload[field.name] = field.minVal - 1
                testCases.Append(CreateTestCase(
                    id = FormatID("GEN-BVA", counter++),
                    category = "Boundary Value Analysis - Out-of-Bounds Low",
                    auth = validAuth,
                    payload = bvaSubMinPayload,
                    semanticOracle = "REJECTED_WITH_NO_STATE_MUTATION",
                    statusOracle = "400 Bad Request (INFERRED)",
                    classification = "INFERRED"
                ))

        // D. Type Confusion Probe
        wrongTypePayload = Clone(nominalPayload)
        wrongTypePayload[field.name] = (field.type == STRING) ? 12345 : "non_numeric_string"
        testCases.Append(CreateTestCase(
            id = FormatID("GEN-TYP", counter++),
            category = "Type Confusion & Robustness",
            auth = validAuth,
            payload = wrongTypePayload,
            semanticOracle = "REJECTED_CLEANLY_NO_SERVER_CRASH",
            statusOracle = "400 Bad Request (INFERRED)",
            classification = "ROBUSTNESS"
        ))

    // =========================================================================
    // 3. SECURITY & ACCESS CONTROL PROBES (SEC-02 & SEC-03)
    // =========================================================================
    IF endpointSpec.authLevel != PUBLIC:
        // A. Missing Authorization Header
        testCases.Append(CreateTestCase(
            id = FormatID("GEN-SEC", counter++),
            category = "Security - Unauthenticated Access (SEC-02)",
            auth = NONE,
            payload = nominalPayload,
            semanticOracle = "ACCESS_DENIED_NO_SIDE_EFFECTS",
            statusOracle = "401 Unauthorized (SPECIFIED)",
            classification = "SPECIFIED"
        ))

        // B. Cryptographically Forged Token
        testCases.Append(CreateTestCase(
            id = FormatID("GEN-SEC", counter++),
            category = "Security - Signature Tampering (SEC-02)",
            auth = TOKEN_WITH_INVALID_SIGNATURE,
            payload = nominalPayload,
            semanticOracle = "ACCESS_DENIED_NO_SIDE_EFFECTS",
            statusOracle = "403 Forbidden (SPECIFIED)",
            classification = "SPECIFIED"
        ))

        // C. Expired Token
        testCases.Append(CreateTestCase(
            id = FormatID("GEN-SEC", counter++),
            category = "Security - Expired Token Lifecycle (SEC-02)",
            auth = EXPIRED_TOKEN,
            payload = nominalPayload,
            semanticOracle = "ACCESS_DENIED_NO_SIDE_EFFECTS",
            statusOracle = "401 / 403 (SPECIFIED)",
            classification = "SPECIFIED"
        ))

    IF endpointSpec.authLevel == ADMIN_PROTECTED:
        // D. Unprivileged Normal User Token
        testCases.Append(CreateTestCase(
            id = FormatID("GEN-SEC", counter++),
            category = "Security - Broken Function Level Auth (SEC-03)",
            auth = STANDARD_USER_TOKEN,
            payload = nominalPayload,
            semanticOracle = "ACCESS_DENIED_MUTATION_PREVENTED",
            statusOracle = "403 Forbidden (INFERRED)",
            classification = "SPECIFIED_SEMANTIC",
            sideEffectCheck = (endpointSpec.method IN [POST, PUT, DELETE]) ? "QUERY_STORAGE_VERIFY_UNCHANGED" : NULL
        ))

        // E. Role Tampering & Case Spoofing
        testCases.Append(CreateTestCase(
            id = FormatID("GEN-SEC", counter++),
            category = "Security - Role Spoofing Probe (SEC-03)",
            auth = TOKEN_WITH_ROLE("ADMIN"), // Uppercase
            payload = nominalPayload,
            semanticOracle = "ACCESS_DENIED_MUTATION_PREVENTED",
            statusOracle = "403 Forbidden (INFERRED)",
            classification = "SECURITY-HARDENING"
        ))

    RETURN testCases
```
