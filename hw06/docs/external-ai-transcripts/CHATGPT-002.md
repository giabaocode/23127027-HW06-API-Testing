# External AI Transcript — Interaction CHATGPT-002

- **Session / Interaction ID:** CHATGPT-002
- **Date & Time:** 2026-09-02 (During Phase 2 Human Audit)
- **AI Tool / Model:** ChatGPT (OpenAI)
- **Phase:** Phase 2 — Secondary External Reference Review of 38 FR-01 AI Test Cases
- **Context:** Provided by student as external reference material to assist in reviewing AI-generated test cases.

---

## 1. Verbatim Student Prompt

```text
Review all 38 AI-generated FR-01 test cases (FR01-AI-001 to FR01-AI-038) for HCMUS EShop SUT. Classify each as VALID, INVALID, or INCOMPLETE, providing reasons and suggested corrections.
```

---

## 2. Verbatim Conversational AI Response

```text
FR01-AI-001
Reference Verdict: VALID
Reason:
Happy-path registration is well defined. The input satisfies FR-01 and the
documented successful response status is 200.
Suggested Correction:
None required.

FR01-AI-002
Reference Verdict: INCOMPLETE
Reason:
Vietnamese Unicode name support is reasonable robustness coverage, but the
official specification does not explicitly guarantee acceptance of Vietnamese
diacritics.
Suggested Correction:
Treat it as a robustness/characterization test. Do not classify rejection as a
defect solely because Unicode acceptance is not formally specified. If
accepted, verify UTF-8 preservation.

FR01-AI-003
Reference Verdict: VALID
Reason:
The requirement explicitly states that name is mandatory. Omitting the field
should therefore be semantically rejected.
Suggested Correction:
Keep the exact error HTTP status UNKNOWN/INFERRED unless officially specified.

FR01-AI-004
Reference Verdict: INCOMPLETE
Reason:
The requirement says the user must provide a full name, but does not explicitly
define empty-string or trimming behavior.
Suggested Correction:
Keep rejection as INFERRED or classify this as robustness rather than a fully
specified contract test.

FR01-AI-005
Reference Verdict: INCOMPLETE
Reason:
The string type of name is inferred from the JSON example rather than formally
defined by a schema.
Suggested Correction:
Treat integer-name handling as a type robustness test. Do not claim official
semantic rejection unless supported by the specification.

FR01-AI-006
Reference Verdict: INCOMPLETE
Reason:
The specification defines no maximum name length, therefore 1000 characters is
not an official boundary and has no deterministic functional oracle.
Suggested Correction:
Treat as robustness. Acceptance or clean rejection may both be legitimate.
Primary assertions should focus on no crash and preserved database integrity.

FR01-AI-007
Reference Verdict: VALID
Reason:
This is meaningful SEC-05 coverage because an apostrophe reaches the
parameterized database insert and tests whether input remains data instead of
altering SQL structure.
Suggested Correction:
Do not require name acceptance as an official FR-01 rule. Successful literal
storage or legitimate independent validation rejection can both remain secure.

FR01-AI-008
Reference Verdict: INCOMPLETE
Reason:
SEC-04 applies to UI rendering rather than the JSON API. The current test also
asserts literal stored data without defining how persistence will actually be
verified.
Suggested Correction:
Keep it as a generic robustness test or add an explicit DB verification step
if literal persistence is intended to be checked.

FR01-AI-009
Reference Verdict: VALID
Reason:
A normal user@domain.com email directly follows the documented FR-01 email
format and forms a valid happy-path test.
Suggested Correction:
None required.

FR01-AI-010
Reference Verdict: INCOMPLETE
Reason:
Plus-addressing is valid under broader email standards, but the course
specification does not explicitly require full RFC email syntax support.
Suggested Correction:
Treat acceptance as INFERRED/characterization. If accepted, verify the
documented 200 success behavior and faithful persistence.

FR01-AI-011
Reference Verdict: VALID
Reason:
Email is explicitly mandatory, therefore omitting it directly violates FR-01.
Suggested Correction:
Keep exact error status UNKNOWN unless specified.

FR01-AI-012
Reference Verdict: VALID
Reason:
An empty email cannot satisfy the explicitly required valid-email format.
Suggested Correction:
Semantic rejection can be tied to the format rule; exact HTTP status remains
UNKNOWN/INFERRED.

FR01-AI-013
Reference Verdict: VALID
Reason:
Email without @ clearly violates the documented email-format requirement.
Suggested Correction:
None required.

FR01-AI-014
Reference Verdict: VALID
Reason:
Email with no domain after @ clearly violates the documented format rule.
Suggested Correction:
None required.

FR01-AI-015
Reference Verdict: INCOMPLETE
Reason:
Numeric email rejection depends on a type contract that is only inferred from
the JSON example.
Suggested Correction:
Treat as type robustness/characterization rather than a formally specified
rejection.

FR01-AI-016
Reference Verdict: VALID
Reason:
FR-01 explicitly requires email uniqueness. Attempting to register the
pre-seeded email must be semantically rejected.
Suggested Correction:
Exact failure HTTP status remains UNKNOWN. Verify that duplicate-row count does
not increase.

FR01-AI-017
Reference Verdict: VALID
Reason:
This is a strong state-dependent test: unregistered email -> successful
registration -> repeated same email -> duplicate rejection.
Suggested Correction:
None required.

FR01-AI-018
Reference Verdict: INCOMPLETE
Reason:
The specification says email must be unique but does not define whether
uniqueness is case-insensitive.
Suggested Correction:
Treat this as characterization of email canonicalization. Do not claim
case-insensitive rejection is an explicit requirement.

FR01-AI-019
Reference Verdict: INVALID
Reason:
The selected SQL-looking email is itself malformed. A correct implementation
could reject it during email validation before reaching the database, meaning
the test cannot reliably demonstrate SEC-05 parameterized-query behavior.
Suggested Correction:
Use SEC-05 coverage through an input that actually reaches persistence, such as
the name field with SQL-looking characters, or redesign the email payload so it
remains syntactically valid while still meaningfully exercising persistence.

FR01-AI-020
Reference Verdict: VALID
Reason:
The password satisfies all five explicitly documented password-policy
requirements.
Suggested Correction:
None required.

FR01-AI-021
Reference Verdict: VALID
Reason:
@ belongs to the documented special-character set and the remaining password
rules are satisfied.
Suggested Correction:
None required.

FR01-AI-022
Reference Verdict: VALID
Reason:
$ belongs to the documented special-character set and the remaining password
rules are satisfied.
Suggested Correction:
None required.

FR01-AI-023
Reference Verdict: VALID
Reason:
& belongs to the documented special-character set and the remaining password
rules are satisfied.
Suggested Correction:
None required.

FR01-AI-024
Reference Verdict: VALID
Reason:
The password contains !, which satisfies the explicit requirement to contain
at least one character from the documented special-character set. The
specification does not explicitly prohibit an additional # character.
Suggested Correction:
If rejected solely because of #, record that behavior separately rather than
claiming the specification requires rejection.

FR01-AI-025
Reference Verdict: VALID
Reason:
The password contains no special character from the documented required set,
so it clearly violates the password policy.
Suggested Correction:
None required.

FR01-AI-026
Reference Verdict: VALID
Reason:
The input isolates the minimum-length boundary correctly: seven characters,
while still satisfying the other required character classes.
Suggested Correction:
None required.

FR01-AI-027
Reference Verdict: VALID
Reason:
Exactly eight characters satisfies the documented minimum and all other
password criteria are present.
Suggested Correction:
None required.

FR01-AI-028
Reference Verdict: VALID
Reason:
Nine characters is immediately above the documented minimum and the password
satisfies all other required classes.
Suggested Correction:
None required.

FR01-AI-029
Reference Verdict: VALID
Reason:
The test cleanly isolates violation of the required uppercase-letter rule.
Suggested Correction:
None required.

FR01-AI-030
Reference Verdict: VALID
Reason:
The test cleanly isolates violation of the required lowercase-letter rule.
Suggested Correction:
None required.

FR01-AI-031
Reference Verdict: VALID
Reason:
The test cleanly isolates violation of the required numeric-digit rule while
the other policy categories remain satisfied.
Suggested Correction:
None required.

FR01-AI-032
Reference Verdict: VALID
Reason:
An empty password clearly violates the explicit minimum length and required
character-class rules.
Suggested Correction:
Semantic rejection should be classified from the explicit password policy;
exact failure HTTP status remains UNKNOWN.

FR01-AI-033
Reference Verdict: INCOMPLETE
Reason:
Rejecting an integer password assumes a formal API type rule that is currently
only inferred from the JSON example.
Suggested Correction:
Treat it as a type-safety robustness test with unspecified exact semantic
behavior. A crash/unhandled 5xx should still be considered undesirable.

FR01-AI-034
Reference Verdict: INCOMPLETE
Reason:
The official specification defines no maximum password length. The test also
references bcrypt/argon2 and CPU exhaustion although no specific hashing
algorithm is required by FR-01.
Suggested Correction:
Keep this as robustness. Do not require a particular hashing algorithm.
Acceptance is UNKNOWN; verify safe handling and database integrity.

FR01-AI-035
Reference Verdict: VALID
Reason:
An empty JSON body omits all three explicitly mandatory FR-01 fields.
Suggested Correction:
None required beyond leaving exact failure status UNKNOWN/INFERRED.

FR01-AI-036
Reference Verdict: INCOMPLETE
Reason:
The API contract does not specify how unknown additional properties such as
confirmPassword must be handled.
Suggested Correction:
Treat this as characterization/robustness. Acceptance and clean rejection may
both be valid; fail only on unsafe behavior such as crash or unintended
side effects.

FR01-AI-037
Reference Verdict: INCOMPLETE
Reason:
SEC-01 explicitly requires that passwords not be stored in plaintext. The test
goes further by saying the value must use a secured hashed representation such
as bcrypt/argon2, which is stronger than the documented oracle.
Suggested Correction:
The required oracle should be:
stored password value MUST NOT equal submitted plaintext password.
Do not require bcrypt, argon2, or a particular algorithm unless the official
specification states it.

FR01-AI-038
Reference Verdict: VALID
Reason:
Credential non-leakage is a reasonable security-hardening test and the original
testcase correctly labels it as SECURITY-HARDENING rather than pretending it is
an explicit FR-01 requirement.
Suggested Correction:
Keep it separate from mandatory SEC requirement coverage.
```
