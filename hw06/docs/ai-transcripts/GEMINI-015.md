# Verbatim AI Transcript — Interaction GEMINI-015

- **Session / Interaction ID:** GEMINI-015
- **Date & Time:** 2026-09-02T14:08:03+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Phase 3B — Student-Selected Registration Extension Tests Formalization

---

## 1. Verbatim Student Prompt

```text
I selected the following 5 FR-01 extension ideas for formalization:

STU-001 — Malformed JSON body
STU-002 — Wrong Content-Type
STU-003 — Duplicate JSON property
STU-004 — Wrong HTTP method
STU-005 — Email domain expressed as IP address

IMPORTANT PROVENANCE RULE:

These ideas were originally surfaced during AI brainstorming and then selected
by the student.

Therefore do NOT falsely label them as:

"student-original from scratch"

Use truthful provenance such as:

Origin:
Student-selected from AI brainstorming

Student Selection:
CONFIRMED

Do not misrepresent authorship in the AI Audit.

============================================================
1. FORMALIZE THE 5 SELECTED IDEAS
============================================================

Update:

hw06/testcases/fr01/student-extensions.md

Formalize the following five selected ideas into executable test designs.

------------------------------------------------------------
FR01-STU-001 — Malformed JSON Body
------------------------------------------------------------

Student-selected idea:
Send syntactically invalid JSON to POST /api/register.

Purpose:
Test parser/protocol robustness when the request body is not valid JSON.

Design one concrete malformed JSON payload only.

For example, choose ONE malformed structure such as:
- missing closing brace
OR
- trailing comma

Do not combine several malformed variants into one testcase.

Expected oracle must be derived carefully:

- request must not create a user,
- backend must not crash,
- response must be controlled,
- exact HTTP error status is UNKNOWN unless officially specified.

Do not invent a specific status as SPECIFIED.

------------------------------------------------------------
FR01-STU-002 — Wrong Content-Type
------------------------------------------------------------

Student-selected idea:
Send a syntactically valid registration JSON payload but declare an incorrect
Content-Type such as:

Content-Type: text/plain

Purpose:
Test HTTP protocol/body-parser behavior.

Keep:
- name valid
- email valid and unique
- password valid

so Content-Type is the only intended changed condition.

Expected behavior must distinguish:

SPECIFIED
INFERRED
UNKNOWN

If the official API specification does not define behavior for wrong
Content-Type, treat this primarily as robustness/characterization.

Primary safe assertions:
- no server crash,
- no unintended user creation if request cannot be parsed,
- controlled response.

------------------------------------------------------------
FR01-STU-003 — Duplicate JSON Property
------------------------------------------------------------

Student-selected idea:
Send a JSON object containing the same property name twice.

Use the `email` property for the duplicate-key condition.

Example structural concept:

{
  "name": "...",
  "email": "first@example.com",
  "email": "second@example.com",
  "password": "..."
}

IMPORTANT:

JSON duplicate-key semantics are not consistently defined across parsers.

Therefore classify this as:

ROBUSTNESS / PARSER CHARACTERIZATION

Do NOT invent a requirement saying the first or last key must win unless the
official specification explicitly defines it.

Design verification to determine:

- how the parser resolves the duplicate property,
- whether exactly one intended account is created,
- no server crash,
- no unexpected multiple DB rows,
- database integrity remains intact.

Record actual parser behavior only during real execution.

------------------------------------------------------------
FR01-STU-004 — Wrong HTTP Method
------------------------------------------------------------

Student-selected idea:
Call the registration route using an unsupported HTTP method.

Use ONE concrete method, preferably:

PUT /api/register

instead of POST /api/register.

Keep body otherwise valid.

Purpose:
Verify method-routing behavior.

Expected semantic behavior:

registration must NOT execute through an unsupported method if the API only
documents POST /api/register.

Do not automatically claim HTTP 405 is SPECIFIED.

If exact status is undocumented:

Expected HTTP status:
UNKNOWN

Potential framework outcomes such as 404 or 405 must be treated as observed
implementation behavior, not official specification requirements.

Assertions:
- no account created,
- no registration side effect,
- controlled response,
- no server crash.

------------------------------------------------------------
FR01-STU-005 — Email Domain as IP Address
------------------------------------------------------------

Student-selected idea:
Test an email whose domain is represented as an IP address rather than a normal
DNS hostname.

Choose one concrete candidate.

Example concept:

user@[127.0.0.1]

IMPORTANT:

Do not automatically call this valid or invalid under FR-01 unless the course
specification defines the accepted email grammar precisely enough.

Classify as:

EMAIL FORMAT CHARACTERIZATION / ROBUSTNESS

Determine whether the documented `user@domain.com` requirement implies normal
hostname-only syntax or whether broader email formats remain unspecified.

Expected functional acceptance may therefore remain UNKNOWN.

Primary assertions:
- deterministic handling,
- no crash,
- no unintended DB corruption,
- if accepted, normal documented success behavior applies,
- if rejected, do not automatically classify rejection as a SUT defect unless
  it violates the official course specification.

============================================================
2. SOURCE / TRACEABILITY
============================================================

For every selected test include:

- Test ID
- Origin
- Student Selection confirmation
- Feature = FR-01
- Requirement trace
- Category
- Objective
- Preconditions
- Initial State
- Method
- Endpoint
- Headers
- Concrete request/body
- Expected Semantic Behavior
- Expected HTTP Status classification
- Response assertion
- State assertion
- Setup
- Cleanup
- Automation Status

Use:

FR01-STU-001
FR01-STU-002
FR01-STU-003
FR01-STU-004
FR01-STU-005

============================================================
3. DO NOT OVERSTATE AUTHORSHIP
============================================================

Record accurately:

Idea Source:
AI brainstorming

Student Action:
Student selected these five ideas for extension

Do NOT record:
"student independently invented these five ideas"

unless that statement is genuinely true.

============================================================
4. DUPLICATION CHECK
============================================================

Compare these five tests against:

hw06/testcases/fr01/generated-ai-original.md
hw06/testcases/fr01/reviewed-ai-final.md

Verify they are not duplicates of the existing 38 cases.

If one overlaps materially with an existing case:

STOP for that case and report the overlap.

Do not silently count a duplicate as an extension.

============================================================
5. AUTOMATION PREPARATION
============================================================

After formalization, mark each testcase:

READY FOR POSTMAN AUTOMATION

if technically automatable.

Do NOT execute yet.

For malformed JSON and duplicate-key JSON:

make sure the eventual Postman/Newman implementation preserves the RAW request
body exactly as required.

Do not allow serializers to silently normalize the malformed/duplicate
structure before sending.

============================================================
6. AI AUDIT
============================================================

Finalize the previous Gemini transcript first.

Update:

hw06/docs/ai-audit.md

Record:
- these ideas were AI-brainstormed,
- the student selected IDs 1, 4, 8, 11, and 14,
- Gemini performed mechanical formalization.

Do not misstate provenance.

============================================================
7. VALIDATION
============================================================

After formalization verify:

- exactly 5 extension tests exist,
- all are distinct from the original 38,
- each has one concrete test condition,
- every expected result respects SPECIFIED / INFERRED / UNKNOWN,
- no exact HTTP code has been invented,
- no real execution result has been fabricated.

============================================================
8. GIT
============================================================

After validation, make a LOCAL commit for the extension formalization.

Suggested commit:

test(fr01): formalize selected registration extension tests

Do NOT push yet.

============================================================
9. OUTPUT
============================================================

Show:

=== FR-01 EXTENSION TESTS FORMALIZED ===

=== DUPLICATION CHECK ===

=== PROVENANCE ===

=== FIVE TEST SUMMARY ===

=== AUTOMATION READINESS ===

=== LOCAL COMMIT RESULT ===

Then proceed directly to preparing FR-01 Postman automation unless the official
HW06 PDF requires another human checkpoint first.

Do not start FR-07 yet.
```

---

## 2. Verbatim Conversational AI Response

[VERBATIM AI RESPONSE TO BE FINALIZED AT NEXT INTERACTION]
