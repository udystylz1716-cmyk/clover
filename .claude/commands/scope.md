---
description: Write a Clover scope document from a job post (e.g. /scope jobs/airtable-crm.md)
argument-hint: jobs/[job-name].md
---

Use the **scope-writer** skill (`.claude/skills/scope-writer/SKILL.md`) to write a scope document for this job post:

$ARGUMENTS

- If nothing was given after /scope, do not guess a job. List the job posts in `jobs/` and ask which one to use.
- Only read the job post (and `output/[job-name]/proposal.md` if it exists). Never edit anything in `jobs/`.
- Follow every step of the skill, including the self-check, and every house rule in `CLAUDE.md`.
- Save the result to `output/[job-name]/scope.md`, where job-name is the job file name without `.md`.
