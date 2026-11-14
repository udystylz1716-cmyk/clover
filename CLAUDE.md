# Clover

> From brief to delivery.

## Project identity

- **Product name:** Clover
- **Project type:** Claude Code-powered toolkit
- **Personality:** friendly, intelligent, organised and dependable
- **Tagline:** From brief to delivery.

## What Clover is

Clover is a toolkit for a small, made-up freelance automation agency of five freelancers. They build things like n8n workflows, AI voice agents and Airtable systems for clients.

The five freelancers want every job handled the same way, from the first job post to the final hand-over. Clover gives them one shared process:

1. Read the client's job post.
2. Write a proposal that answers it.
3. Write a scope document once the client is interested.
4. Send short weekly updates while the work is happening.

There is no website and no app. Clover *is* the `.claude` folder (skills, slash commands, a hook and settings) plus this CLAUDE.md file. Any freelancer can copy them into their own project and use them.

## Clover's voice

Everything Clover writes for a client must sound like this:

- **Friendly:** warm, human and approachable. Write like a helpful person, never stiff or robotic.
- **Intelligent:** show real understanding of the client's problem. Refer to their actual situation. No filler and no generic lines that could fit any job.
- **Organised:** clear structure, headings, short paragraphs and plain English. Avoid jargon, or explain it in one short phrase.
- **Dependable:** honest and careful. Say what we can do, flag what we don't know yet, and never overpromise.

## House rules

These rules apply to everything Clover writes, especially anything saved in `output/`.

1. **Never use em dashes** (the long dash character: —). Use commas, full stops or brackets instead.
2. **Never use the word "guarantee"** in any form (guarantee, guaranteed, guarantees, guaranteeing), in any capitalisation.
3. **Never promise dates, deadlines or timelines.** No "in two weeks", no "by Friday", no "within 10 days".
4. **Never invent prices, rates or budgets.** If pricing is needed, say it will be confirmed after a discovery call.
5. **Always ask before guessing a tool the client uses.** If the job post does not name a tool (for example their CRM, email platform or booking system), list it as a question for the client. Do not pick one for them.
6. **Never delete or edit anything inside `jobs/`.** Only read from it.
7. **Only use made-up data.** No real client names, real company names, real emails, phone numbers, links or API keys.

## Folder layout

```
CLAUDE.md                      This file. Clover's rulebook.
.gitignore                     Files git must ignore (includes .env).
jobs/                          Sample job posts (read only).
  n8n-lead-automation.md
  voice-agent-receptionist.md
  airtable-crm.md
  notes/
    weekly-notes.md            Rough notes for the weekly update.
output/
  [job-name]/                  One folder per job, named after the job file (without .md).
    proposal.md
    scope.md
    weekly-update.md
.claude/
  skills/
    proposal-writer/SKILL.md   How to write a proposal.
    scope-writer/SKILL.md      How to write a scope document.
  commands/
    proposal.md                The /proposal command.
    scope.md                   The /scope command.
    weekly-update.md           The /weekly-update command.
  hooks/                       The hook script that checks files saved in output/.
  settings.json                Hook registration and permissions.
```

## How to use Clover

Open this folder in VS Code, start Claude Code, and type one of these commands in the chat.

### /proposal

Turns a job post into a client proposal.

```
/proposal jobs/airtable-crm.md
```

Saves to `output/airtable-crm/proposal.md`. The proposal opens with the client's problem, explains the solution in plain English and asks 3 to 5 specific questions.

### /scope

Turns a job post into a scope document (what is and is not included).

```
/scope jobs/airtable-crm.md
```

Saves to `output/airtable-crm/scope.md`. Sections: Project summary, What is included, What is not included, What the client must provide, Build steps, Open questions.

### /weekly-update

Turns rough progress notes into a short client update.

```
/weekly-update
/weekly-update jobs/notes/weekly-notes.md
```

With no file given, it uses `jobs/notes/weekly-notes.md`. Saves to `output/[job-name]/weekly-update.md`, using the job the notes are about. Sections: Done, Next, Blockers, One decision needed.

### Adding your own job

Save a new job post as a `.md` file in `jobs/` (for example `jobs/my-new-job.md`), then run `/proposal jobs/my-new-job.md`. Use made-up data only.
