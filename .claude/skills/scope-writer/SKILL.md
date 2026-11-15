---
name: scope-writer
description: Writes a scope document in Clover's voice from a job post in jobs/ (what is and is not included), following every house rule in CLAUDE.md, and saves it to output/[job-name]/scope.md. Use when the user runs /scope or asks for a scope document for a job post.
---

# Scope writer

You are writing a scope document for one of Clover's five freelancers to send to a client who is interested. The goal: client and freelancer agree, in writing, on exactly what will be built and what will not, so there are no surprises later. Follow these steps in order.

## Step 1: Load the rules

Read `CLAUDE.md` in the project root. Every house rule and the voice section apply to this document. If you cannot find CLAUDE.md, stop and tell the user.

## Step 2: Read the job post (and the proposal, if there is one)

- The job file path is given to you (for example `jobs/airtable-crm.md`).
- If no path was given, or the file does not exist, stop. Tell the user, and list the `.md` files in `jobs/` (not `jobs/notes/`) so they can choose one.
- Read the file. **Never edit, move or delete anything in `jobs/`.**
- Work out the job name: the file name without `.md`. Example: `jobs/airtable-crm.md` gives `airtable-crm`.
- If `output/[job-name]/proposal.md` exists, read it too. The scope must match what the proposal offered. Do not add features the proposal did not mention, and keep its open questions.

## Step 3: Work out the boundaries (think before writing)

Before writing anything, note for yourself:

1. **Every deliverable:** each thing the client asked for, broken into concrete parts they can check off.
2. **What depends on an answer:** anything that only works with a certain tool, plan or access (for example "last contact date depends on the email platform"). These are included only as "to be confirmed", never as a firm promise.
3. **Sensible exclusions:** things a client could reasonably assume are included but are not. Think about: ongoing support after hand-over, extra features, training beyond the walkthrough, fixing data we cannot verify, paid tool subscriptions, work in tools not named in the post.
4. **What the client must provide:** access, logins (shared safely, never in the document), sample data, decisions, a named person to answer questions.
5. **Tools they did NOT name:** these become open questions. Never pick one for them.

## Step 4: Write the scope document

Use exactly these sections, in this order:

```
# Scope: [short project name] for [client business name]

One or two sentences saying what this document is for.

## Project summary
2 to 3 short sentences: the client's problem and what we will build to fix it.

## What is included
Bulleted list. One deliverable per bullet, specific enough to check off.
Mark anything that depends on an open question as "(to be confirmed, see Open questions)".

## What is not included
Bulleted list of clear exclusions. Friendly, not defensive.
End with: anything not listed above can be discussed and added separately.

## What the client must provide
Bulleted list of access, data, decisions and people we need from them.

## Build steps
Numbered list of stages in order. Each step says what happens and what the
client gets to check. No dates, durations or deadlines.

## Open questions
Numbered list. Every unknown tool, plan or detail that affects the build.
Pricing will be confirmed after the discovery call, once these are answered.
```

### Writing rules for this step

- **Specific, not generic.** Every bullet must relate to this job. If a line could be pasted into a scope for a different job, rewrite it.
- **Plain English.** Short bullets. Explain any technical term in a few words.
- **Honest.** Include only what we can actually deliver. Anything uncertain is flagged, not promised.
- **No pricing.** Do not repeat, judge or suggest the client's budget.
- **Logins and keys:** never write real or example passwords, API keys, emails or links. Say how access will be shared, not what it is.
- **Length:** usually 300 to 550 words.

## Step 5: Self-check before saving

Go through the draft line by line and fix anything that fails:

- [ ] No em dash character (—) anywhere. Use a comma, full stop or brackets.
- [ ] No "guarantee" in any form or capitalisation.
- [ ] No dates, deadlines, durations or timelines (no "in 2 weeks", "by Friday", "within days").
- [ ] No prices, rates, budgets or hours. Only "confirmed after the discovery call".
- [ ] No tool named unless the job post named it. Every unknown tool is an open question.
- [ ] All six sections present, in order, with `##` headings (not bold, not escaped).
- [ ] Every "to be confirmed" item in What is included has a matching open question.
- [ ] Matches the proposal, if one exists. No new features.
- [ ] Only made-up data. No real emails, phone numbers, links or API keys.

## Step 6: Save

- Save to `output/[job-name]/scope.md` (create the folder if needed).
- If that file already exists, replace it and mention that you did.
- Do not save anything anywhere else.

## Step 7: Report back

Tell the user, in 3 or 4 short lines: where the file was saved, the number of included and excluded items, and the open questions. Do not paste the whole document into the chat.
