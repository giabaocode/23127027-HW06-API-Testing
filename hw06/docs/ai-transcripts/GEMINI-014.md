# Verbatim AI Transcript — Interaction GEMINI-014

- **Session / Interaction ID:** GEMINI-014
- **Date & Time:** 2026-09-02T13:54:44+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Phase 3A — Reviewed AI Final Set Creation & Student Extension Blank Template Setup

---

## 1. Verbatim Student Prompt

```text
Phase 2 FR-01 human audit is complete and committed.

Proceed with Phase 3A for FR-01.

IMPORTANT:
Do NOT start FR-07.
Do NOT start Postman/Newman yet.
Do NOT push yet.

============================================================
0. RETROSPECTIVE AI AUDIT
============================================================

Finalize the previous Gemini transcript using the established retrospective
logging rule.

Create the current interaction transcript.

Update hw06/docs/ai-audit.md truthfully.

============================================================
1. IMPORTANT STUDENT-EXTENSION INTEGRITY RULE
============================================================

The following gap ideas were already suggested by Gemini:

- whitespace trimming
- Unicode normalization
- concurrent duplicate registration
- email local-part length boundary
- SQL comment / inline injection strings
- password case-sensitivity/authentication interaction

Therefore these are now AI-PROPOSED ideas.

Do NOT count them as the student's >=5 original tests that AI missed.

Record them as:

AI-SUGGESTED GAP IDEAS — NOT ELIGIBLE AS STUDENT-ORIGINAL EXTENSIONS

unless there is documentary evidence that the student independently proposed
the same idea before seeing the AI suggestion.

Do not generate replacement ideas for the student.

============================================================
2. CREATE REVIEWED AI FINAL SET
============================================================

Create:

hw06/testcases/fr01/reviewed-ai-final.md

Use:

generated-ai-original.md
human-audit.md

as inputs.

Do NOT modify generated-ai-original.md.

Apply the completed audit decisions:

VALID cases:
- preserve the original core test design,
- only normalize formatting if necessary.

INCOMPLETE cases:
- apply exactly the correction recorded in human-audit.md,
- do not introduce new requirements beyond the student's accepted correction.

INVALID case:
FR01-AI-019

Preserve traceability to the original case but replace its unusable final
test design according to the recorded correction.

For every final case retain:

- Original Test ID
- Original Verdict
- Correction Applied
- Final Test Objective
- Preconditions
- Request
- Expected Semantic Behavior
- Expected HTTP Status classification
- Security assertion
- State assertion
- Setup/cleanup
- Automation status
- requirement traceability

Do not erase evidence of the original AI error.

============================================================
3. FINAL ORACLE RULES
============================================================

Preserve the reviewed distinctions:

SPECIFIED
INFERRED
UNKNOWN
ROBUSTNESS
EXAMPLE-DERIVED
SECURITY-HARDENING

Do not convert UNKNOWN behavior into deterministic pass/fail rules.

For robustness/characterization tests:

define a concrete safe oracle where possible, such as:

- no unhandled server crash
- no database corruption
- parseable controlled response
- no unintended SQL execution

but do not invent functional requirements.

For SEC-01:

official required oracle:

stored password != submitted plaintext password

Do not require bcrypt/argon2 specifically unless the specification requires it.

============================================================
4. VALIDATE THE FINAL REVIEWED SET
============================================================

Programmatically verify:

- exactly 38 traceable reviewed AI cases exist
- every final case maps back to FR01-AI-001 ... FR01-AI-038
- all 12 INCOMPLETE corrections were applied
- FR01-AI-019 was corrected
- generated-ai-original.md remains unchanged
- no student-extension test has been generated

Create a concise correction summary:

VALID unchanged:
25

INCOMPLETE corrected:
12

INVALID redesigned:
1

TOTAL:
38

============================================================
5. PREPARE EMPTY STUDENT EXTENSION WORKSHEET
============================================================

Create:

hw06/testcases/fr01/student-extensions.md

IMPORTANT:
DO NOT generate the required student tests.

Do not provide:
- concrete inputs
- concrete expected results
- concrete execution steps
- suggested edge cases
- suggested gap categories
- example student tests

because the underlying ideas must come from the student.

Create at least 5 empty slots:

## FR01-STU-001
Student Raw Idea:
[STUDENT MUST WRITE]

Why I Believe AI Missed It:
[STUDENT MUST WRITE]

Then empty fields for later AI formalization:

- Requirement / SEC
- Objective
- Preconditions
- Input
- Steps
- Expected Result
- Setup
- Cleanup
- Automation Status

Repeat through at least:

FR01-STU-005

You may create FR01-STU-006/007 blank slots as optional extras.

============================================================
6. MINIMUM STUDENT WORKFLOW
============================================================

The student should only need to supply TWO short pieces of text for each
student-owned test:

1. Student Raw Idea
2. Why I Believe AI Missed It

Once the student supplies those ideas, YOU may perform all mechanical work:

- check whether idea is genuinely different from AI-generated cases
- check whether it was already suggested by Gemini/ChatGPT
- formalize objective
- build exact input
- build steps
- map requirement
- define expected result
- automate in Postman
- execute
- document

Do not alter the underlying student idea.

============================================================
7. GIT
============================================================

After reviewed-ai-final.md is complete and validated, create a LOCAL commit
for applying the human audit corrections.

Suggested message:

test(fr01): apply human audit corrections to registration tests

Commit:
- reviewed-ai-final.md
- updated AI Audit
- relevant Gemini transcripts
- student-extensions.md blank template

Do NOT claim the student extension step is completed.

Do NOT push.

============================================================
8. OUTPUT REQUIRED
============================================================

Show:

=== FR-01 REVIEWED AI FINAL SET ===

=== CORRECTIONS APPLIED ===

=== FR01-AI-019 FINAL REDESIGN ===

=== ORIGINAL AI SET INTEGRITY ===

=== STUDENT EXTENSION TEMPLATE ===

=== AI-SUGGESTED GAPS MARKED INELIGIBLE ===

=== LOCAL COMMIT RESULT ===
- real hash
- files
- git status

Then STOP at:

=== HUMAN GATE — STUDENT MUST PROVIDE 5 ORIGINAL TEST IDEAS ===

Do not suggest any additional test ideas.

Do not begin Postman/Newman.
Do not begin FR-07.
```

---

## 2. Verbatim Conversational AI Response

[VERBATIM AI RESPONSE TO BE FINALIZED AT NEXT INTERACTION]
