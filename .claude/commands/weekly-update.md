---
description: Turn rough progress notes into a short Clover client update (e.g. /weekly-update or /weekly-update jobs/notes/weekly-notes.md)
argument-hint: "[notes file, default jobs/notes/weekly-notes.md]"
---

Turn rough progress notes into a short weekly update for the client.

Notes file: $ARGUMENTS

## Step 1: Load the rules

Read `CLAUDE.md`. Every house rule and the voice section apply. If you cannot find it, stop and tell the user.

## Step 2: Read the notes

- If no notes file was given above, use `jobs/notes/weekly-notes.md`.
- If the file does not exist, stop, tell the user and list the files in `jobs/notes/`.
- Only read it. **Never edit, move or delete anything in `jobs/`.**

## Step 3: Find the job

- Work out which job the notes are about by matching client names and details against the job posts in `jobs/`.
- The job name is that job file's name without `.md` (for example `n8n-lead-automation`).
- Read that job post for context: client name, who the main contact is and how technical they are.
- If `output/[job-name]/scope.md` exists, read it too, so the update uses the same names for each part of the work.
- If you cannot tell which job the notes belong to, stop and ask. Do not guess.

## Step 4: Write the update

Use exactly this structure:

```
# Weekly update: [short project name]

Hi [main contact's first name if known, otherwise the team name],

One or two friendly sentences with the overall picture.

## Done
Bullets. What works now, in plain English, and what it means for them.

## Next
Bullets. What we will work on next. No dates or durations.

## Blockers
Bullets. What is stopping progress and exactly what we need from them.
If nothing is blocked, say so in one line.

## One decision needed
One decision only, with the options laid out simply and what each means
for them. If the notes have no decision, say none is needed this week.

Short friendly sign-off.

Best,

[Your name]
```

### Writing rules

- **Write for the client, not the freelancer.** Turn shorthand ("dupe check", "webhook", "mapped dropdown to tags") into plain English. Explain any technical term in a few words.
- **Short.** Usually 150 to 300 words. Bullets of one or two lines.
- **Honest.** Report test results as tests ("worked in testing"), not as live results.
- **Blockers are polite and specific.** Say what is needed and why. Never sound annoyed (for example, do not say how many times we have asked).
- **Logins and API keys:** never write any. Ask the client to share access securely, not by email or chat.
- **Leave out private notes.** Things the freelancer wrote to themselves (for example "might mention later") stay out unless they clearly need the client's attention. Mention what you left out in your report.
- **Tools:** only name a tool if the notes or job post name it. Unknown tools are asked about, never guessed.
- **One decision only.** Other small questions can go in Next or Blockers.

## Step 5: Self-check before saving

- [ ] No em dash character anywhere.
- [ ] No "guarantee" in any form or capitalisation.
- [ ] No dates, deadlines, durations or timelines.
- [ ] No prices, rates, budgets or per-lead costs. Paid options say the cost will be confirmed.
- [ ] No tool named unless the notes or job post name it.
- [ ] Sections Done, Next, Blockers, One decision needed, in that order, as `##` headings.
- [ ] Only made-up data. No real emails, phone numbers, links or API keys.

## Step 6: Save and report

- Save to `output/[job-name]/weekly-update.md` (create the folder if needed). If it exists, replace it and say so.
- Tell the user in 3 or 4 short lines: where it was saved, which job it matched, the blocker and decision, and anything from the notes you left out.
