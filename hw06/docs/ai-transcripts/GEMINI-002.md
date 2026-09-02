# Verbatim AI Transcript — Interaction GEMINI-002

- **Session / Interaction ID:** GEMINI-002
- **Date & Time:** 2026-09-02T10:57:18+07:00
- **AI Model:** Gemini 3.7 Flash (High) via Antigravity IDE
- **Phase:** Phase 0 — Feature Confirmation & Scope Definition

---

## 1. Verbatim Student Prompt

```text
# HW06 – API TESTING
# MASTER EXECUTION PROMPT FOR GEMINI / ANTIGRAVITY

You are my AI-first Software Testing Engineering Agent working directly inside
my local clone of the official HCMUS EShop SUT repository.

============================================================
STUDENT INFORMATION
============================================================

Student ID:
23127027

GitHub username:
giabaocode

Final selected features:

Pool A:
FR-01 — Account Registration

Pool B:
FR-07 — Shopping Cart

Pool C:
FR-12 — Access Control

I CONFIRM that this exact combination:

FR-01 + FR-07 + FR-12

does NOT duplicate another member's three-feature selection in my group.

Record this confirmation in the homework documentation.

============================================================
AUTHORITATIVE SOURCES
============================================================

This repository contains:

1. The official EShop SUT source code.
2. api_specification.md.
3. Functional requirements FR-01 through FR-19.
4. Security requirements SEC-01 through SEC-07.
5. The official HW06 – API Testing PDF that I placed in the repository.

Before doing substantial work, locate and read the COMPLETE HW06 PDF.

The assignment PDF is the HIGHEST-PRIORITY source for academic rules.

api_specification.md and the official requirements in the repository are the
HIGHEST-PRIORITY sources for expected API behavior.

The actual implementation may be inspected for execution/debugging, but:

DO NOT silently change expected results to match implementation behavior.

If the specification and implementation disagree, record:

POSSIBLE DEFECT / SPECIFICATION DISCREPANCY

and preserve the specification-derived expected behavior.

If this prompt conflicts with the official HW06 PDF:

THE PDF ALWAYS WINS.

Stop and tell me about the conflict.

============================================================
PRIMARY OBJECTIVE
============================================================

Help me complete as much of HW06 – API Testing as legitimately possible.

Automate everything that AI, terminal tools, Postman/Newman, Git, GitHub
Actions, scripts, and the local workspace can truthfully perform.

However, STOP whenever the assignment requires:

- student judgment,
- human review,
- student-authored test design,
- personal design decisions,
- real screenshots,
- real execution evidence,
- or evidence that you cannot genuinely produce.

Never fabricate evidence.

Never impersonate me.

Never turn the entire homework into one opaque "generate everything" action.

============================================================
RULE 1 — AI-FIRST DOES NOT MEAN BLACK BOX
============================================================

Work phase-by-phase.

Do not complete the entire homework in one uninterrupted execution.

After each major phase:

1. summarize what was done,
2. list files created/changed,
3. list assumptions,
4. list unresolved questions,
5. update the AI Audit,
6. show current Git status,
7. propose an appropriate Git commit,
8. stop whenever student review/action is required.

Use explicit checkpoints.

============================================================
RULE 2 — HUMAN AUDIT IS MANDATORY
============================================================

The HW06 assignment requires ME to review every AI-generated testcase.

For every AI-generated testcase, create empty fields:

- Student Verdict
- Student Reasoning
- Student Correction
- Student Reviewed At

Student Verdict must eventually be one of:

VALID
INVALID
INCOMPLETE

YOU MUST NOT fill these fields.

Also:

DO NOT provide an AI review hint before I perform my audit.

First show the testcase and let me judge it independently.

Only AFTER I submit my own verdict/reasoning may you provide an independent
AI retrospective review for comparison.

Preserve both:

- original AI testcase,
- human-reviewed/final testcase.

Never erase incorrect AI output because it is useful evidence for the AI Audit
and AI Critique.

============================================================
RULE 3 — THE >=5 STUDENT TESTS PER API ARE MANUAL
============================================================

For EACH selected feature:

FR-01
FR-07
FR-12

I must personally create at least five additional testcases that AI missed.

Therefore:

DO NOT write those five actual testcases for me.

You MAY:

- detect coverage gaps,
- identify broad missing areas,
- prepare blank worksheets,
- suggest category labels.

Examples of acceptable category labels:

- authorization edge
- authentication edge
- domain boundary
- state-dependent behavior
- security boundary
- schema edge
- cross-field interaction
- concurrency consideration

But DO NOT give a concrete:

input + steps + expected result

that I could simply copy as one of my required student-authored tests.

After I create the tests myself, you may:

- review them against the specification,
- point out inconsistencies,
- automate them,
- execute them,
- include them in Postman,
- calculate results,
- document them.

Do not materially rewrite my test idea without asking.

============================================================
RULE 4 — FINAL AGENT SKILL DIAGRAM MUST BE STUDENT-CREATED
============================================================

The HW06 assignment requires the AI-driven API test-generator diagram to be
self-drawn by the student.

Therefore DO NOT generate the final diagram.

Specifically, DO NOT:

- create the final Mermaid architecture diagram,
- create PlantUML,
- generate SVG,
- generate PNG,
- generate an AI image,
- create Draw.io content representing the final design,
- create a fake hand-drawn version.

You MAY:

- ask me to make architectural decisions,
- explain design tradeoffs,
- prepare a blank checklist,
- help write pseudocode after MY design decisions exist,
- implement the Agent Skill,
- review my diagram after I create it.

Any Mermaid diagram used to explain the homework workflow must be clearly
labelled:

"Execution workflow illustration only.
This is NOT the mandatory AI test-generator diagram."

============================================================
RULE 5 — REAL EVIDENCE ONLY
============================================================

NEVER fabricate:

- screenshots,
- Postman Console screenshots,
- X-Student-Id evidence,
- Newman CLI output,
- Newman HTML reports,
- HTTP request/response evidence,
- GitHub Actions runs,
- GitHub Actions screenshots,
- GitHub Issue screenshots,
- commit hashes,
- timestamps,
- URLs,
- test execution statistics,
- bugs,
- pass/fail counts.

If you genuinely execute something in the local workspace, preserve the real
output.

Clearly distinguish:

REAL EXECUTION

from:

EXAMPLE / TEMPLATE / NOT EXECUTED

Never place fake example evidence in the final submission directories.

============================================================
RULE 6 — X-STUDENT-ID
============================================================

Every executed API request must contain:

X-Student-Id: 23127027

Prefer a centralized Postman mechanism such as:

collection-level pre-request script

or another clearly traceable approach.

Do not invent screenshot evidence.

The required console screenshot must come from a REAL execution.

Create a manual checklist explaining exactly how I should capture it.

============================================================
RULE 7 — CONTINUOUS AI AUDIT
============================================================

Create and continuously maintain:

hw06/docs/ai-audit.md

The AI Audit must be updated throughout the project, NOT only at the end.

For every meaningful Gemini interaction, record:

- AI tool name
- date/time
- phase
- exact student prompt
- AI output/action
- files affected

Do not hide incorrect AI outputs.

Create a section:

## Previous / External AI Interactions — Student Must Add

because I may have used ChatGPT or other AI tools before/during this project.

Do not invent those interactions.

Also remind me that the ChatGPT interactions used to prepare this workflow
must be added manually to the AI Audit.

============================================================
RULE 8 — GIT SAFETY
============================================================

Before modifying substantial files, inspect:

git status
git branch --show-current
git remote -v
git log --oneline -10

If origin still points to:

https://github.com/ttbhanh/eshop-sut

DO NOT PUSH ANYTHING.

Stop and tell me that my personal repository must be configured.

The desired eventual remote structure is:

origin   -> my personal HW06 repository under giabaocode
upstream -> official ttbhanh/eshop-sut

Do not invent my personal repository URL if it has not actually been created.

Never force-push unless I explicitly approve it.

Never remove .git.

Never rewrite official history unnecessarily.

============================================================
RULE 9 — GIT COMMIT STRATEGY
============================================================

The homework requires separate commits for procedure steps.

Do not complete several major steps and commit everything in one large commit.

Use meaningful incremental commits.

For example:

FR-01:
- fr01/spec-analysis
- fr01/ai-generation
- fr01/human-audit
- fr01/student-extension
- fr01/postman
- fr01/execution

FR-07:
- fr07/spec-analysis
- fr07/ai-generation
- fr07/human-audit
- fr07/student-extension
- fr07/postman
- fr07/execution

FR-12:
- fr12/spec-analysis
- fr12/ai-generation
- fr12/human-audit
- fr12/student-extension
- fr12/postman
- fr12/execution

Later:
- bugs/reporting
- cicd/setup
- agent-skill/implementation
- report/finalization

These names are examples; adapt them naturally.

Before each commit:

1. show git status,
2. summarize changed files,
3. propose a commit message,
4. state which HW06 procedure step it represents.

Do not fabricate hashes.

Generate the final Git commit log only from actual Git history.

============================================================
RULE 10 — PROJECT STRUCTURE
============================================================

Do not unnecessarily reorganize the official SUT.

Inspect the current repository first.

If no suitable homework structure exists, prefer:

hw06/
├── README.md
├── MANUAL_TODO.md
├── submission-checklist.md
├── docs/
│   ├── main-report.md
│   ├── ai-audit.md
│   ├── ai-critique.md
│   ├── cicd-report.md
│   ├── postman-features.md
│   ├── oral-defense-notes.md
│   └── git-commit-log.txt
├── testcases/
│   ├── fr01/
│   ├── fr07/
│   └── fr12/
├── postman/
│   └── data/
├── newman/
├── bugs/
│   └── evidence/
├── screenshots/
└── agent-skill/
    ├── design-decisions.md
    ├── student-diagram-checklist.md
    └── pseudocode.md

CI/CD workflows should remain in the normal repository location:

.github/workflows/

Do not duplicate existing folders unnecessarily.

============================================================
RULE 11 — MANUAL TODO REGISTER
============================================================

Create and continuously maintain:

hw06/MANUAL_TODO.md

Track every task requiring student/manual action.

Initial items should include:

[x] Final feature selection confirmed:
    FR-01 + FR-07 + FR-12

[x] Student confirms the exact combination does not duplicate another group
    member's selection.

[ ] Human audit of every AI-generated FR-01 testcase.

[ ] >=5 student-authored additional FR-01 tests.

[ ] Human audit of every AI-generated FR-07 testcase.

[ ] >=5 student-authored additional FR-07 tests.

[ ] Human audit of every AI-generated FR-12 testcase.

[ ] >=5 student-authored additional FR-12 tests.

[ ] Student explanation of why AI missed the additional tests.

[ ] Real X-Student-Id console screenshot.

[ ] Real Newman execution evidence.

[ ] Real Newman HTML report.

[ ] Real bug screenshots where genuine defects exist.

[ ] Real GitHub Issue evidence.

[ ] Real passing GitHub Actions run.

[ ] Real intentional-failure GitHub Actions run.

[ ] CI/CD screenshots and links.

[ ] Student architectural decisions for Agent Skill.

[ ] Student-created Agent Skill/test-generator diagram.

[ ] AI Critique student review/personalization.

[ ] Previous/external AI interactions inserted into AI Audit.

[ ] Student self-assessed grade.

[ ] Final submission package verification.

Do not mark a manual task complete without actual evidence/input.

============================================================
PHASE 0 — REPOSITORY + ASSIGNMENT ANALYSIS
============================================================

BEFORE generating testcases:

1. Inspect the repository tree.

2. Locate the official HW06 PDF.

3. Read the COMPLETE PDF.

4. Locate and read:
   - api_specification.md
   - FR-01
   - FR-07
   - FR-12
   - SEC-01 through SEC-07
   - README/setup documentation
   - backend startup instructions
   - database/setup instructions

5. Inspect:
   - git status
   - current branch
   - git remotes
   - recent commits

6. Determine:
   - how the backend starts,
   - required services,
   - base URL,
   - authentication mechanism,
   - relevant test data/setup.

7. Inspect whether any hw06 artifacts already exist.

8. Create/update:
   - hw06/docs/ai-audit.md
   - hw06/MANUAL_TODO.md
   - hw06/submission-checklist.md

9. Update implementation_plan.md so the selected features are:

   FR-01
   FR-07
   FR-12

Remove FR-02 / FR-09 / FR-18 as selected APIs.

They may remain mentioned only as unselected alternatives if useful.

10. Clearly label any workflow Mermaid as NOT being the required Agent Skill
diagram.

DO NOT generate >=35 testcases yet.

============================================================
PHASE 1 — SPECIFICATION ANALYSIS
============================================================

Analyze ONE selected feature at a time.

Recommended order:

1. FR-01 Account Registration
2. FR-07 Shopping Cart
3. FR-12 Access Control

For each feature, extract ONLY what the official sources support:

- functional requirement
- endpoint(s)
- HTTP method(s)
- authentication
- authorization / roles
- path parameters
- query parameters
- headers
- request body
- field names
- field types
- required / optional fields
- constraints
- documented HTTP statuses
- response schema
- relevant business rules
- state-dependent behavior
- applicable SEC-01–SEC-07 requirements.

Every statement must be tagged:

SPECIFIED
INFERRED
UNKNOWN

Do not convert an inference into a requirement.

Do not invent missing endpoint behavior.

FR-12 is particularly sensitive:

DO NOT invent generic admin/access-control endpoints.

Use ONLY endpoints and role/authentication rules that actually exist in
api_specification.md and the official requirements.

============================================================
STATE-TRANSITION RULE
============================================================

I did NOT select FR-10.

Therefore DO NOT force:

pending -> confirmed -> shipping -> delivered

into my selected test suites unless a selected API legitimately interacts with
that behavior according to the official specification.

For each selected feature, identify only relevant state-dependent behavior.

Possible examples must be confirmed from the official source.

For FR-01, inspect whether meaningful state changes involve account existence,
duplicate registration, or another specified lifecycle.

For FR-07, inspect the actual cart lifecycle such as empty/non-empty cart,
item creation, quantity changes, deletion, etc., ONLY if specified.

For FR-12, inspect authentication/authorization state and role-dependent access
behavior ONLY where supported.

If there is no explicit state machine, state:

NO EXPLICIT STATE MACHINE SPECIFIED

and test legitimate state-dependent behavior instead.

============================================================
COVERAGE MODEL
============================================================

For each selected feature, create a coverage matrix containing:

1. Domain / equivalence partitions for EVERY parameter.

2. Valid partitions.

3. Invalid partitions.

4. Boundary values where meaningful.

5. Missing/null/empty/type-related cases where supported.

6. Authentication.

7. Authorization.

8. Relevant SEC-01–SEC-07.

9. Injection/security cases where applicable.

10. IDOR / role escalation where applicable.

11. State-dependent behavior.

12. Schema validation.

13. Error behavior.

14. Cross-field constraints.

15. Preconditions/setup/cleanup needs.

Do not generate testcases yet.

After analyzing the first API, STOP:

=== CHECKPOINT 1 — STUDENT REVIEW OF SPEC ANALYSIS ===

Show me:

- exact requirements found,
- exact endpoints,
- coverage matrix,
- ambiguities,
- SPECIFIED / INFERRED / UNKNOWN items.

Wait for my approval.

============================================================
PHASE 2 — AI TEST GENERATION
============================================================

Only after I approve specification analysis.

Generate tests for ONE API AT A TIME.

Target:

>= 35 meaningful AI-generated testcases PER selected API.

That means eventually:

FR-01 >= 35 AI-generated tests
FR-07 >= 35 AI-generated tests
FR-12 >= 35 AI-generated tests

Do not meet the target using meaningless duplicates.

Every AI-generated testcase should contain:

- Test ID
- Origin = AI
- FR
- SEC reference if relevant
- Category
- Objective
- Preconditions
- Initial state
- Authentication/role
- HTTP method
- Endpoint
- Input
- Partition/boundary represented
- Execution steps
- Expected HTTP status
- Expected response/body behavior
- Schema assertions
- Security assertions when applicable
- State assertions when applicable
- Cleanup
- Automation status

Use IDs such as:

FR01-AI-001
FR01-AI-002

FR07-AI-001

FR12-AI-001

After generating the first API:

1. save the generated tests,
2. update the coverage matrix,
3. create the human audit worksheet,
4. update the AI Audit,
5. show Git status,
6. propose the generation commit,
7. STOP.

Use:

=== CHECKPOINT 2 — HUMAN AUDIT REQUIRED ===

Do NOT audit the tests for me.

============================================================
HUMAN AUDIT WORKSHEET
============================================================

For each AI-generated testcase create:

| Test ID |
| Test Summary |
| Requirement Trace |
| Student Verdict |
| Student Reasoning |
| Student Correction |
| Student Reviewed At |

Leave all student fields EMPTY.

Do not provide AI verdict hints yet.

Once I fill my audit:

- preserve original AI test,
- preserve my verdict,
- preserve my reasoning,
- preserve my correction,
- create a finalized test version separately.

Do not overwrite the original AI output.

============================================================
PHASE 3 — STUDENT EXTENSION
============================================================

After human audit of an API, analyze remaining coverage gaps.

Create a blank worksheet:

| Student Test ID |
| Gap Category |
| Student Objective |
| Preconditions |
| Input |
| Steps |
| Expected Result |
| Requirement/SEC |
| Why AI Missed It |
| Student Authorship Confirmation |

Do not populate concrete testcase content.

Then STOP:

=== CHECKPOINT 3 — STUDENT MUST CREATE >=5 ORIGINAL TESTS ===

After I write them, you may:

- validate against specification,
- flag mistakes,
- automate them,
- execute them,
- integrate them into reports.

Do not replace my authorship.

============================================================
PHASE 4 — POSTMAN AUTOMATION
============================================================

After the reviewed AI tests and student-authored extension tests exist,
create/update the Postman suite.

Use Postman features where genuinely useful.

Consider:

- collections
- folders
- collection variables
- environment variables
- pre-request scripts
- test scripts
- authentication handling
- dynamic variable extraction
- chaining requests
- data-driven JSON/CSV
- Collection Runner
- schema validation
- cleanup scripts
- mocks only if genuinely useful
- monitors only if practical

Do NOT add pointless features just to inflate the list.

Maintain:

hw06/docs/postman-features.md

For every used feature record:

- feature name
- where used
- why it was useful
- associated testcase/API
- evidence still required.

============================================================
X-STUDENT-ID IMPLEMENTATION
============================================================

Every request must contain:

X-Student-Id: 23127027

Prefer centralized injection.

For example, if appropriate:

pm.request.headers.upsert({
    key: "X-Student-Id",
    value: "23127027"
});

Use the API supported by the Postman runtime available in this project.

Do not assume a specific script is correct without validation.

The final screenshot showing this header must be REAL and captured by me from
an actual execution.

============================================================
PHASE 5 — REAL EXECUTION WITH POSTMAN / NEWMAN
============================================================

Before execution:

1. identify the exact SUT startup steps from the repository,
2. start/configure required database/service,
3. start the real backend,
4. verify health/base URL,
5. confirm authentication/test accounts/data,
6. confirm X-Student-Id injection.

Then, if terminal execution is genuinely available:

run Newman for real.

Preserve:

- exact command,
- real base URL,
- real CLI output,
- start/end time,
- total requests,
- total assertions,
- pass count,
- fail count,
- failure details,
- generated HTML report.

Do not weaken a valid assertion just to make the suite green.

If the SUT violates the specification, preserve the failure.

If Newman execution cannot actually run:

STOP.

Create exact commands for me under:

MANUAL REAL EXECUTION REQUIRED

Do not create a fake HTML report.

============================================================
PHASE 6 — BUG REPORTING
============================================================

Only report a bug based on genuine reproducible behavior.

For every failure classify first as:

- likely SUT defect
- likely testcase defect
- environment/configuration issue
- specification ambiguity
- requires further investigation

Do not automatically treat every failed testcase as a bug.

For a likely genuine bug, draft:

- Bug ID
- Title
- Related FR
- Related SEC
- Environment
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity suggestion
- Evidence
- Related testcase

Expected behavior must be traceable to the official specification.

If a screenshot is required and you cannot capture genuine evidence, leave:

[STUDENT MUST ATTACH REAL SCREENSHOT]

GitHub Issues must only contain genuine observed defects.

============================================================
PHASE 7 — CI/CD
============================================================

Create a real GitHub Actions workflow when the repository is properly
configured.

Prefer:

.github/workflows/api-tests.yml

The workflow should:

- install required dependencies,
- configure/start the SUT if necessary,
- wait for backend readiness,
- execute Newman,
- fail when genuine assertions fail,
- preserve/report useful artifacts where practical.

Do not hardcode secrets.

The assignment requires TWO genuine CI/CD runs:

RUN A:
all intended tests pass.

RUN B:
one intentionally demonstrated test failure.

Do not fabricate RUN B.

For the failure demonstration:

- use an explicit temporary demonstration commit or controlled configuration,
- clearly document that it intentionally demonstrates pipeline failure,
- do not corrupt the final real test suite.

Record only actual:

- commit hashes
- GitHub Actions URLs
- statuses
- screenshots

after they exist.

============================================================
PHASE 8 — AI-DRIVEN API TEST GENERATOR / AGENT SKILL
============================================================

Do not design the final architecture without me.

First ask me to make decisions about:

- main components
- input
- specification parser
- intermediate representation
- partition-generation strategy
- security-mapping strategy
- state-model strategy
- schema validation
- quality/coverage checking
- human-review gate
- output formats.

Record MY decisions in:

hw06/agent-skill/design-decisions.md

After my decisions exist, you may:

- help refine them,
- write pseudocode,
- implement a reusable Agent Skill/script,
- test it,
- generate candidate tests from the official API spec,
- prepare demo commands.

But DO NOT create the final required diagram.

Maintain:

hw06/agent-skill/student-diagram-checklist.md

The checklist may mention conceptual elements, but the final diagram itself
must be drawn by me.

============================================================
PHASE 9 — AI CRITIQUE
============================================================

The final AI Critique must be 200–300 words.

Do not invent weaknesses before we have real evidence.

Collect factual examples from:

- INVALID AI-generated tests,
- INCOMPLETE AI-generated tests,
- specification assumptions AI got wrong,
- student-authored tests AI genuinely missed,
- security/state behavior AI missed,
- real bugs AI failed to predict.

Then prepare:

1. factual evidence list,
2. critique outline,
3. 200–300 word DRAFT.

Mark the draft:

STUDENT MUST REVIEW AND PERSONALIZE BEFORE SUBMISSION

Do not claim personal learning experiences I did not provide.

============================================================
PHASE 10 — REPORTING
============================================================

Continuously build the main report from real evidence.

Eventually cover:

1. Introduction
2. Selected APIs
3. Environment
4. AI-first methodology
5. FR-01 full pipeline
6. FR-07 full pipeline
7. FR-12 full pipeline
8. Cross-API coverage
9. Human audit summary
10. Student extension summary
11. Postman features
12. Postman/Newman execution
13. Bugs
14. CI/CD
15. Agent Skill
16. Test summary
17. AI Critique
18. AI Audit
19. Limitations/unresolved items
20. Evidence references

Never invent missing statistics.

Use:

[WAITING FOR REAL EXECUTION]

where necessary.

============================================================
EXCEL TEST CASES AND TEST SUMMARY
============================================================

Prepare structured testcase data suitable for Excel export.

Recommended columns:

- API / Feature
- Test ID
- Origin (AI / Student)
- Requirement
- SEC
- Category
- Objective
- Preconditions
- Input
- Steps
- Expected Status
- Expected Result
- Audit Verdict
- Actual Result
- Execution Status
- Bug ID
- Notes

Do not fill human audit fields yourself.

After real execution, calculate:

- APIs tested
- AI-generated testcase count
- student-added testcase count
- total final testcases
- executed
- passed
- failed
- blocked/skipped
- genuine bug count

Use actual data only.

============================================================
README AND SELF-ASSESSMENT
============================================================

Create/update the HW06 README with:

- assignment overview
- selected features
- repository structure
- setup instructions
- run instructions
- artifact locations
- test summary
- self-assessment table

Assessment structure:

FR-01 full pipeline: /30
FR-07 full pipeline: /30
FR-12 full pipeline: /30
Agent Skill: /10
Total: /100

Do NOT choose my final self-assessed grade.

You may suggest a score based on evidence, but I make the final decision.

============================================================
SUBMISSION CHECKLIST
============================================================

Maintain:

hw06/submission-checklist.md

Use an explicit checklist including at least:

[ ] Main report Markdown
[ ] Main report PDF
[ ] Public GitHub repository link
[ ] Postman collection JSON
[ ] Newman HTML report
[ ] Postman feature list
[ ] CI/CD report
[ ] Passing CI/CD run
[ ] Failing CI/CD run
[ ] CI/CD screenshots
[ ] CI/CD links
[ ] Excel testcases
[ ] Test summary
[ ] Student-created Agent Skill diagram
[ ] Agent Skill pseudocode
[ ] Agent Skill implementation/demo materials if used
[ ] Bug report
[ ] Genuine GitHub Issue screenshots where bugs exist
[ ] AI Critique 200–300 words
[ ] AI Audit Markdown
[ ] AI Audit PDF
[ ] Git commit log text file
[ ] README self-assessment
[ ] Supporting evidence/materials

Optional OpenAPI conversion may be produced only if useful.
If AI generates it, include it in the AI Audit and review it.

Do not claim the package is complete while required items are missing.

============================================================
ORAL DEFENSE SUPPORT
============================================================

Create:

hw06/docs/oral-defense-notes.md

Only use facts from the actual project.

Prepare concise prompts enabling ME to explain:

- why I selected FR-01 / FR-07 / FR-12,
- how partitions were derived,
- meaningful state-dependent behavior,
- authorization/security testing,
- one incorrect AI testcase,
- one incomplete AI testcase,
- one test I personally added,
- why AI missed it,
- one genuine bug if found,
- how Postman works,
- how X-Student-Id is injected,
- how Newman execution works,
- CI/CD design,
- Agent Skill design decisions,
- what I personally reviewed/did.

Do not create a deceptive memorized script.

============================================================
FINAL QUALITY GATE
============================================================

Before claiming readiness, verify:

SELECTION
[ ] exactly one Pool A feature: FR-01
[ ] exactly one Pool B feature: FR-07
[ ] exactly one Pool C feature: FR-12
[ ] non-duplication confirmation recorded

AI GENERATION
[ ] >=35 meaningful AI-generated tests for FR-01
[ ] >=35 meaningful AI-generated tests for FR-07
[ ] >=35 meaningful AI-generated tests for FR-12
[ ] every parameter appropriately partitioned
[ ] boundaries addressed
[ ] relevant security requirements addressed
[ ] relevant state-dependent behavior addressed
[ ] schema validation addressed

HUMAN OWNERSHIP
[ ] every AI testcase human-reviewed
[ ] verdict exists
[ ] reasoning exists
[ ] correction exists where needed
[ ] >=5 student-authored tests for FR-01
[ ] >=5 student-authored tests for FR-07
[ ] >=5 student-authored tests for FR-12
[ ] student explanation of why AI missed them exists
[ ] Agent Skill diagram is student-created

EXECUTION
[ ] every executed request carries X-Student-Id: 23127027
[ ] real Postman/Newman execution exists
[ ] real HTML report exists
[ ] hostname matches real deployment
[ ] statistics are based on execution
[ ] no fake evidence exists

BUGS
[ ] genuine bugs only
[ ] expected behavior traceable to spec
[ ] GitHub Issues consistent with report
[ ] screenshots are genuine

CI/CD
[ ] workflow exists
[ ] real passing run exists
[ ] real intentional failure run exists
[ ] real links exist
[ ] real screenshots exist

DOCUMENTATION
[ ] AI Audit complete
[ ] previous/external AI use included
[ ] AI Critique 200–300 words
[ ] student reviewed critique
[ ] Git commit log is real
[ ] Postman features documented
[ ] README complete
[ ] test summary complete
[ ] required files present

If any item fails, report:

NOT READY FOR SUBMISSION

and list exactly what remains.

============================================================
IMPORTANT ANTI-CHEAT RULE
============================================================

Do not search for, copy, or reuse another student's:

- HW06 report
- testcase set
- prompt
- GitHub repository
- AI Audit
- Agent Skill diagram
- bug report

Use only:

- this student's work,
- official assignment material,
- official SUT,
- official API specification,
- official course requirements,
- legitimate supporting documentation.

============================================================
START NOW
============================================================

For this execution, DO ONLY PHASE 0 FIRST.

Perform these actions:

1. Inspect the current repository.
2. Find and read the COMPLETE HW06 PDF.
3. Read api_specification.md.
4. Read FR-01, FR-07, FR-12.
5. Read SEC-01 through SEC-07.
6. Inspect backend/setup instructions.
7. Inspect git status, branch, remotes, and recent history.
8. Inspect existing homework files.
9. Update implementation_plan.md to use:
   FR-01 + FR-07 + FR-12.
10. Create/update:
    hw06/docs/ai-audit.md
    hw06/MANUAL_TODO.md
    hw06/submission-checklist.md
11. Extract the exact endpoint(s) and technical requirements for:
    FR-01
    FR-07
    FR-12
12. Do NOT generate >=35 testcases.
13. Do NOT create the Agent Skill diagram.
14. Do NOT run the full homework.
15. Do NOT push to GitHub yet unless the personal remote is confirmed.

At the end of Phase 0 show me exactly:

=== CURRENT STATE ===

=== OFFICIAL PDF REQUIREMENTS UNDERSTOOD ===

=== SELECTED FEATURES ===
FR-01
FR-07
FR-12

=== EXACT ENDPOINTS FOUND ===

=== SEC MAPPING ===

=== SPECIFIED / INFERRED / UNKNOWN ITEMS ===

=== GIT STATUS ===

=== GIT REMOTES ===

=== FILES CREATED / CHANGED ===

=== AI AUDIT STATUS ===

=== MANUAL ACTIONS REMAINING ===

=== PROPOSED GIT COMMIT ===

=== NEXT STEP ===

Then STOP.

Wait for my explicit approval before starting Phase 1 specification analysis
or generating any testcase.
```

---

## 2. Verbatim Conversational AI Response

=== CURRENT STATE ===

Phase 0 is complete.
- The official assignment PDF (`2026.HW06.API Testing_En.pdf`), SUT source code (`backend/server.js`, `backend/database.js`), and specification files (`api_specification.md`, `README.md`) have been thoroughly analyzed.
- Your feature selection (**FR-01**, **FR-07**, **FR-12**) and non-duplication confirmation have been authoritatively recorded across all tracking registers.
- The homework workspace layout has been initialized under `hw06/`.
- No test cases or diagrams have been generated. Zero code has been executed. No commits or pushes have been made.
- Execution is strictly halted at **Checkpoint 1**.

---

=== OFFICIAL PDF REQUIREMENTS UNDERSTOOD ===

1. **Course & Deliverable Requirements (`HW06-AI`)**:
   - Individual assignment; strict anti-plagiarism policy.
   - Requires selecting 3 APIs (1 from Pool A, 1 from Pool B, 1 from Pool C; Pool D mobile is excluded).
   - Target: $\ge 35$ AI-generated test cases per API + $\ge 5$ student-authored extension tests per API (total $\ge 40$ tests per feature, $\ge 120$ tests overall).
   - Packaging format: `23127027_HW06_AI_API_<SelfAssessedGrade>.zip` containing all 14 mandatory artifacts (main report, Postman collection, Newman HTML report, CI/CD report with 2 runs, Excel sheets, student-drawn diagram, pseudocode, bug reports with GitHub issues, AI Critique, AI Audit, Git commit log, and README).
2. **AI-First / Academic Integrity Rules**:
   - Disciplined AI collaboration, NOT a black-box prompt.
   - **Human Audit Gate:** Every AI-generated test case must have `Student Verdict` (`VALID` / `INVALID` / `INCOMPLETE`), `Student Reasoning`, and `Student Correction` filled manually by the student. AI must NOT pre-fill these fields or provide hints prior to student review.
   - **Student Extension Gate:** The $\ge 5$ tests per API must be originally authored by the student. AI provides only coverage gap categories and blank templates.
   - **Anti-AI-Cheat Constraints:**
     - Real `X-Student-Id: 23127027` header evidenced in an authentic Postman Console screenshot.
     - Real Newman HTML report matching local deployment (`localhost` / `127.0.0.1`).
     - AI test-generator diagram must be **self-drawn by the student** (zero AI-generated diagrams or AI images).
3. **CI/CD Requirements**:
   - GitHub Actions workflow running Newman against the SUT.
   - Exactly two sample runs: Run A (all tests pass) and Run B (intentional 1-test failure demonstration commit).

---

=== SELECTED FEATURES ===

- **Pool A:** **FR-01 — Account Registration** (`POST /api/register`)
- **Pool B:** **FR-07 — Shopping Cart** (`GET /api/cart`, `POST /api/cart`)
- **Pool C:** **FR-12 — Access Control** (Admin endpoints & protected data mutation endpoints)

*Non-duplication statement:* The student has confirmed that this exact combination (`FR-01 + FR-07 + FR-12`) does not duplicate any other group member's selection.

---

=== EXACT ENDPOINTS FOUND ===

### 1. FR-01: Account Registration
- **Endpoint:** `POST /api/register`
- **Method:** `POST`
- **Auth:** None (Public)
- **Request Body (JSON):**
  ```json
  {
    "name": "Nguyen Van A",
    "email": "test@domain.com",
    "password": "Password123!"
  }
  ```
- **Documented Success (200 OK):** `{"message": "User registered successfully", "id": 1}`
- **Source Inspection Note:** In `backend/server.js`, passwords are saved in plaintext without format checks, and duplicate emails throw unhandled SQLite unique constraint errors returning `500 Internal Server Error`.

### 2. FR-07: Shopping Cart
- **Endpoints:**
  - `GET /api/cart`: Retrieve current user's cart items.
  - `POST /api/cart`: Add product item to cart.
- **Method:** `GET`, `POST`
- **Auth:** `Authorization: Bearer <token>` (Required)
- **Request Body for `POST /api/cart` (JSON):**
  ```json
  {
    "id": 1,
    "name": "Sản phẩm A",
    "price": 100000,
    "quantity": 2
  }
  ```
- **Documented Success:**
  - `GET`: Array of cart item objects `[...]`.
  - `POST`: `{"message": "Added to cart"}`.
- **Source Inspection Note:** Cart items are kept in an in-memory object `userCarts`. In `server.js`, `POST /api/cart` executes `userCarts[userId].push(req.body)`, which violates the SRS rule requiring quantity accumulation on existing products rather than creating duplicate lines.

### 3. FR-12: Access Control
- **Scope & Endpoints (Explicitly defined in `api_specification.md` and `README.md`):**
  - **Admin-dedicated APIs (`/api/admin/*`):**
    - `GET /api/admin/users`: List all users.
    - `DELETE /api/admin/users/:id`: Delete a user.
    - `GET /api/admin/orders`: List system-wide orders.
    - `PUT /api/admin/orders/:id/status`: Update order status.
    - `POST /api/admin/import-products`: Bulk product import.
    - `POST /api/admin/coupons`: Create coupon.
    - `DELETE /api/admin/coupons/:id`: Delete coupon.
  - **Data Mutation Management APIs (Explicitly restricted to Admin by SRS FR-12):**
    - `POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id`
    - `POST /api/categories`, `PUT /api/categories/:id`, `DELETE /api/categories/:id`
    - `GET /api/coupons`
- **Auth & Authorization:** Must require a valid JWT token (`SEC-02`) AND require `role === 'admin'` (`SEC-03`).
- **Source Inspection Note:** In `backend/server.js`, `/api/products` (POST/PUT/DELETE) lacks any authentication middleware; `/api/categories` and `/api/admin/*` have `authenticateToken` but never check `req.user.role === 'admin'`, allowing standard user tokens to perform administrative actions.

---

=== SEC MAPPING ===

| Security Requirement | Description | Applicable Selected Feature | Testing Dimension |
| :--- | :--- | :--- | :--- |
| **SEC-01** | Passwords must not be stored in plaintext. | **FR-01** | Verify if registration hashes passwords (e.g., bcrypt/argon2) vs. saving raw strings in SQLite. |
| **SEC-02** | Secured APIs must require valid JWT token. | **FR-07**, **FR-12** | Test unauthenticated requests (`401`), malformed tokens (`403`), and expired/forged signatures. |
| **SEC-03** | Admin APIs must check `role = 'admin'` in token. | **FR-12** | Test privilege escalation: regular user token (`role='user'`) calling admin endpoints (`403 Forbidden` expected). |
| **SEC-04** | User input displayed on UI must be escaped (XSS prevention). | **FR-01**, **FR-07** | Store XSS payloads in `name` during registration and cart additions; verify response escaping. |
| **SEC-05** | Database queries must use parameterized queries (SQLi). | **FR-01**, **FR-07**, **FR-12** | Test SQL injection payloads in registration fields, cart payloads, and path parameter `:id`. |
| **SEC-06** | Profile update cannot change `role`. | Cross-cutting Auth | Contextual baseline for role tampering across tokens. |
| **SEC-07** | Reset OTP entropy / expiration / single-use. | Cross-cutting Auth | Not directly exercised by FR-01/07/12 (belongs to FR-03). |

---

=== SPECIFIED / INFERRED / UNKNOWN ITEMS ===

### FR-01: Account Registration
- **SPECIFIED:**
  - Endpoint: `POST /api/register`
  - Fields: `name`, `email`, `password`
  - Email format: valid RFC/standard pattern (`user@domain.com`), must be unique.
  - Password policy: $\ge 8$ chars, $\ge 1$ uppercase, $\ge 1$ lowercase, $\ge 1$ digit, $\ge 1$ special char (`@$!%*?&`).
  - Passwords must not be plaintext (`SEC-01`).
- **INFERRED:**
  - Confirm password field (`confirmPassword`): Specified for Web UI form in SRS; for API payload, `api_specification.md` defines only `{name, email, password}`. API should either validate password directly or reject mismatched inputs if passed.
  - HTTP Status: `200 OK` (specified in spec) or `201 Created` (REST standard). Error status for duplicate email is inferred as `409 Conflict` or `400 Bad Request` (SUT currently throws SQLite error 500).
- **UNKNOWN:**
  - Maximum allowed string length for `name` and `password` on backend (SRS mentions 255 for product names; user fields unspecified).

### FR-07: Shopping Cart
- **SPECIFIED:**
  - Endpoints: `GET /api/cart`, `POST /api/cart`
  - Header: `Authorization: Bearer <token>`
  - Request body for POST: `id`, `name`, `price`, `quantity`
  - Quantity constraint: Positive integer ($\ge 1$).
  - Price constraint: Positive number ($> 0$).
  - Adding an existing product must increase quantity, not add a duplicate item.
  - Cart isolation: Users only view and modify their own carts.
- **INFERRED:**
  - Cart item removal: UI mentions delete dialog, but `api_specification.md` has no `DELETE /api/cart/:id` endpoint.
  - Empty cart payload: `GET /api/cart` returns empty array `[]` when no items added.
- **UNKNOWN:**
  - Behavior when `POST /api/cart` references an `id` that does not exist in the `products` table (foreign key validation).

### FR-12: Access Control
- **SPECIFIED:**
  - All `/api/admin/*` APIs require valid JWT AND `role === 'admin'`.
  - Mutation endpoints (`POST/PUT/DELETE /api/products`, `/api/categories`, `/api/admin/coupons`) require Admin privileges.
  - Missing token must return `401 Unauthorized`.
  - Standard user token accessing admin endpoints must return `403 Forbidden`.
- **INFERRED:**
  - If a user sends a token with invalid signature, response is `403 Forbidden`.
- **UNKNOWN:**
  - Exact JSON error envelope structure for authorization failures (e.g., `{ "error": "Forbidden" }` vs. `{ "message": "Access denied" }`).

---

=== GIT STATUS ===

```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	2026.HW06.API Testing_En.pdf
	hw06/

nothing added to commit but untracked files present (use "git add" to track)
```

---

=== GIT REMOTES ===

- **origin**: `https://github.com/giabaocode/23127027-HW06-API-Testing.git` (Student personal homework repository — configured!)
- **upstream**: `https://github.com/ttbhanh/eshop-sut.git` (Official course upstream repository)

---

=== FILES CREATED / CHANGED ===

1. **[hw06/docs/ai-audit.md](file:///Users/phamngocgiabao/eshop-sut/hw06/docs/ai-audit.md)**: AI Audit log updated with Session 2, feature selections, responsibility matrix, and prompt engineering declaration reminder.
2. **[hw06/MANUAL_TODO.md](file:///Users/phamngocgiabao/eshop-sut/hw06/MANUAL_TODO.md)**: Updated with completed feature selections and human gate checklists.
3. **[hw06/submission-checklist.md](file:///Users/phamngocgiabao/eshop-sut/hw06/submission-checklist.md)**: Created tracking all 14 required submission items from PDF Section 14.
4. **[implementation_plan.md](file:///Users/phamngocgiabao/.gemini/antigravity-ide/brain/95308b01-1bfe-414d-8483-877d83a584e0/implementation_plan.md)**: Synchronized with confirmed features FR-01, FR-07, and FR-12, explicitly noting state-dependent behavior and labeling workflow diagrams.

---

=== AI AUDIT STATUS ===

- Sessions 1 and 2 recorded with timestamps, tool declarations, exact objectives, and file changes.
- Student reminder added for manual inclusion of the preparatory ChatGPT conversation.
- Clear separation maintained between AI duties and human audit requirements.

---

=== MANUAL ACTIONS REMAINING ===

- [ ] Provide explicit approval to proceed from Phase 0 to Phase 1.
- [ ] Record preparatory ChatGPT prompt in Section 3 of `hw06/docs/ai-audit.md`.
- [ ] Review proposed Phase 0 Git commit.

---

=== PROPOSED GIT COMMIT ===

- **Branch:** `main`
- **Files to stage:**
  - `hw06/docs/ai-audit.md`
  - `hw06/MANUAL_TODO.md`
  - `hw06/submission-checklist.md`
  - `2026.HW06.API Testing_En.pdf`
- **Proposed Commit Message:**
  ```text
  feat(hw06): initialize Phase 0 setup, feature selection, and audit registers

  - Confirm selected features: FR-01 (Registration), FR-07 (Cart), FR-12 (Access Control)
  - Verify non-duplication across study group
  - Initialize hw06 layout, AI audit log, manual TODO register, and submission checklist
  - Map technical endpoints, security rules (SEC-01 to SEC-07), and spec discrepancies
  ```
- **Phase Represented:** Phase 0 — Environment & Assignment Setup

---

=== NEXT STEP ===

Upon your explicit approval:
1. Execute the Phase 0 Git commit (local commit only; no remote pushes until instructed).
2. Begin **Phase 1: Specification Analysis for FR-01 (Account Registration)**:
   - Construct parameter domain equivalence partitions (valid and invalid).
   - Define boundary value analysis.
   - Map security cases (SEC-01 plaintext password storage, SEC-05 SQL injection).
   - Formulate the initial FR-01 coverage matrix.
   - Halt at **Checkpoint 1** for your review before generating any test cases.

**Awaiting your approval to execute the commit and proceed to Phase 1.**
