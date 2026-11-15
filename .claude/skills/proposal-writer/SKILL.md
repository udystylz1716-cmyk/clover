---
name: proposal-writer
description: Writes a client proposal in Clover's voice from a job post in jobs/, following every house rule in CLAUDE.md, and saves it to output/[job-name]/proposal.md. Use when the user runs /proposal or asks for a proposal for a job post.
---

# Proposal writer

You are writing a proposal for one of Clover's five freelancers to send to a client. The goal: the client reads it and thinks "they really understood our problem". Follow these steps in order.

## Step 1: Load the rules

Read `CLAUDE.md` in the project root. Every house rule and the voice section apply to this proposal. If you cannot find CLAUDE.md, stop and tell the user.

## Step 2: Read the job post

- The job file path is given to you (for example `jobs/airtable-crm.md`).
- If no path was given, or the file does not exist, stop. Tell the user, and list the `.md` files in `jobs/` (not `jobs/notes/`) so they can choose one.
- Read the file. **Never edit, move or delete anything in `jobs/`.**
- Work out the job name: the file name without `.md`. Example: `jobs/airtable-crm.md` gives `airtable-crm`.

## Step 3: Understand the client (think before writing)

Before writing anything, note for yourself:

1. **Who they are:** business name, industry, size, who will read this.
2. **Their tone:** formal, chatty, brisk, non-technical? Match it. A brisk client who asks for a short proposal gets a short one. A non-technical client gets zero jargon.
3. **The real problem:** what is going wrong today, and what it costs them (lost leads, missed calls, forgotten follow-ups). Use their own details.
4. **What they asked for:** list each thing they want, including "nice to haves".
5. **Tools they named:** only tools the post actually names.
6. **Tools they did NOT name:** anything we would need to know about (CRM, email platform, chat tool, booking system, phone setup, hosting, plan type). These become questions. Never pick one for them.
7. **Vague or missing details:** volumes, who the users are, data quality, edge cases. Pick the ones that would most change how we build it.
8. **Anything they asked us to send:** for example examples of past work.

## Step 4: Write the proposal

Use this structure. Headings may be reworded to suit the client, but keep the order.

```
# Proposal: [short project name] for [client business name]

Hi [first name if given, otherwise "there" or the team name],

## [A heading about their problem, in their words]
2 short paragraphs. Open with THEIR situation and what it is costing them,
using specific details from the post. Do not open with "I" or "We are".

## How we would solve it
Plain-English explanation of the solution. Short paragraphs or a short
numbered list, one item per part of what they asked for. Explain any
technical term in a few words. Mention how it handles the messy details
from their post (duplicates, missing info, patch tests, migration, etc.).

## How we would work together
2 to 4 bullets: discovery call first, build in clear stages, check-ins,
handover/walkthrough. No dates or durations.

## A few questions before we start
3 to 5 numbered questions, each specific to this job.
Any tool they did not name MUST appear here as a question.

## Pricing and next steps
Pricing will be confirmed after a short discovery call, once we have the
answers above. Invite them to a call. Friendly sign-off.

[Your name]
Clover
```

### Writing rules for this step

- **Specific, not generic.** Every paragraph must mention something from this job post. If a sentence could be pasted into a proposal for a different job, rewrite it. Do not reuse stock phrases like "I am excited to help" or "I have read your job post carefully".
- **Plain English, short paragraphs** (2 to 3 sentences).
- **Honest.** Say what we would do. Where something depends on an answer (for example whether their booking system allows connections), say so plainly instead of promising.
- **Past work requests:** never invent past clients or projects. Add a placeholder line: `[Add 1 or 2 relevant examples from your portfolio here.]`
- **Their budget:** do not repeat, judge or suggest any number. Pricing is confirmed after the discovery call.
- **Length:** usually 250 to 450 words. Shorter if the client asked for short.

## Step 5: Self-check before saving

Go through the draft line by line and fix anything that fails:

- [ ] No em dash character (—) anywhere. Use a comma, full stop or brackets.
- [ ] No "guarantee" in any form or capitalisation.
- [ ] No dates, deadlines, durations or timelines (no "in 2 weeks", "by Friday", "within days", "quick turnaround").
- [ ] No prices, rates, budgets or hours. Only "confirmed after a discovery call".
- [ ] No tool named unless the job post named it. Every unknown tool is a question.
- [ ] 3 to 5 questions, all specific to this job.
- [ ] Opens with the client's problem in their context.
- [ ] Sounds friendly, intelligent, organised and dependable.
- [ ] Only made-up data. No real emails, phone numbers, links or API keys.

## Step 6: Save

- Save to `output/[job-name]/proposal.md` (create the folder if needed).
- If that file already exists, replace it and mention that you did.
- Do not save anything anywhere else.

## Step 7: Report back

Tell the user, in 3 or 4 short lines: where the file was saved, the client's main problem in one sentence, and the questions you asked. Do not paste the whole proposal into the chat.
