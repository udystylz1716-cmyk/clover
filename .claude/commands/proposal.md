---
description: Write a Clover proposal from a job post (e.g. /proposal jobs/airtable-crm.md)
argument-hint: jobs/[job-name].md
---

Use the **proposal-writer** skill (`.claude/skills/proposal-writer/SKILL.md`) to write a client proposal for this job post:

$ARGUMENTS

- If nothing was given after /proposal, do not guess a job. List the job posts in `jobs/` and ask which one to use.
- Only read the job post. Never edit anything in `jobs/`.
- Follow every step of the skill, including the self-check, and every house rule in `CLAUDE.md`.
- Save the result to `output/[job-name]/proposal.md`, where job-name is the job file name without `.md`.
