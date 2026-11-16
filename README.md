# Clover

> From brief to delivery.

Clover is a Claude Code toolkit that helps a small freelance automation team handle every client job the same way, from the first job post to the weekly progress updates.

## What Clover is

Clover was made for a five-person freelance agency (made-up, for this project) that builds things like n8n workflows, AI voice agents and Airtable systems for clients.

Without a shared process, every freelancer writes proposals, scopes and updates in their own style, and it is easy to slip up: promising a deadline, quoting a price too early or guessing which tools a client uses. Clover gives the whole team one process and one voice:

1. Read the client's job post.
2. Write a **proposal** that answers it.
3. Write a **scope document** once the client is interested.
4. Send short **weekly updates** while the work is happening.

There is no website and no app. Clover is just a `.claude` folder (skills, slash commands, a hook and settings) plus a `CLAUDE.md` rulebook. You open the folder in Claude Code and type a command.

## Folder structure

```
Freelancer-toolkits/
├── README.md                     This guide.
├── CLAUDE.md                     Clover's rulebook: voice, house rules, folder layout.
├── .gitignore                    Keeps .env (secrets) and Mac system files out of git.
├── jobs/                         Source files (protected).
│   ├── airtable-crm.md           Sample job post: Airtable CRM for a design studio.
│   ├── n8n-lead-automation.md    Sample job post: n8n lead capture for a renovation company.
│   ├── voice-agent-receptionist.md  Sample job post: AI phone receptionist for a salon.
│   └── notes/
│       └── weekly-notes.md       Sample rough notes for a weekly update.
├── output/                       Everything Clover writes. One folder per job.
│   ├── airtable-crm/
│   │   ├── proposal.md
│   │   └── scope.md
│   ├── n8n-lead-automation/
│   │   ├── proposal.md
│   │   ├── scope.md
│   │   └── weekly-update.md
│   └── voice-agent-receptionist/
│       ├── proposal.md
│       └── scope.md
└── .claude/
    ├── skills/
    │   ├── proposal-writer/SKILL.md
    │   └── scope-writer/SKILL.md
    ├── commands/
    │   ├── proposal.md
    │   ├── scope.md
    │   └── weekly-update.md
    ├── hooks/
    │   └── check-output.py
    └── settings.json
```

All client names and details in `jobs/` and `output/` are made up. The files in `output/` are sample results you can compare your own runs against.

## What each part does

### CLAUDE.md (the rulebook)

Claude Code reads this file automatically. It sets Clover's voice (friendly, intelligent, organised, dependable) and seven house rules that apply to everything Clover writes:

1. Never use em dashes (the long dash).
2. Never use the word "guarantee" in any form.
3. Never promise dates, deadlines or timelines.
4. Never invent prices, rates or budgets. Pricing is confirmed after a discovery call.
5. Always ask before guessing a tool the client uses (CRM, email platform, booking system and so on).
6. `jobs/` holds protected source files. Claude must not change them unless you explicitly ask for that specific change.
7. Only use made-up data. No real client names, emails, phone numbers, links or API keys.

### Skills

Skills are step-by-step instructions Claude follows for a task.

| Skill | What it does |
|---|---|
| `proposal-writer` | Reads a job post, works out the client's real problem, tone and the tools they did not name, then writes a proposal. Runs a self-check against the house rules before saving. |
| `scope-writer` | Reads a job post (and the job's proposal, if one exists, so the scope matches it), then writes a scope document that says clearly what is and is not included. Runs the same kind of self-check. |

### Slash commands

| Command | Uses | Saves to |
|---|---|---|
| `/proposal` | `proposal-writer` skill | `output/[job-name]/proposal.md` |
| `/scope` | `scope-writer` skill | `output/[job-name]/scope.md` |
| `/weekly-update` | Its own instructions (no separate skill) | `output/[job-name]/weekly-update.md` |

`[job-name]` is the job file name without `.md`. For example, `jobs/airtable-crm.md` gives `output/airtable-crm/`.

### The hook (`.claude/hooks/check-output.py`)

An automatic quality gate. Every time Claude tries to save a file in `output/` with its Write or Edit tool, the hook checks the **whole file as it would look after the save**. If it contains an em dash or any form of the word "guarantee" (any capitalisation), the save is blocked and Claude is told which lines to fix.

### Settings (`.claude/settings.json`)

Registers the hook and sets what Claude may and may not touch. See [Safety rules and permissions](#safety-rules-and-permissions) below.

## Prerequisites

- **Claude Code**, either the VS Code extension or the command line version.
- **Python 3**, available as `python3`. The hook is a Python script and will not run without it.
- **Git** (recommended), to keep track of versions and to restore a file if a command replaces it.
- **macOS.** Clover has been set up and tested on macOS only.

### Platform limitations

- The settings **require** Claude Code's sandbox (`failIfUnavailable: true`). If the sandbox cannot run on your machine, Claude Code will not start in this folder.
- Native Windows has no sandbox, so Clover will not start there as configured.
- The first time you open the folder, Claude Code asks whether you trust it. Say yes, or the project's permission rules will not apply.

## How to use each command

Open the project folder in VS Code (or run `claude` from inside the folder), then type the command in the Claude Code chat.

### /proposal

Turns a job post into a client proposal.

```
/proposal jobs/airtable-crm.md
```

- Saves to `output/airtable-crm/proposal.md`.
- If you type `/proposal` with no file, Claude lists the job posts in `jobs/` and asks which one to use.

What you get: a proposal that opens with the client's problem, explains the solution in plain English, describes how you would work together, asks 3 to 5 questions specific to the job (including any tool the post did not name) and says pricing will be confirmed after a discovery call. It ends with:

```
Best,

[Your name]
```

Before sending, replace `[Your name]` and the line `[Add 1 or 2 relevant examples from your portfolio here.]`. Clover never invents past projects.

### /scope

Turns a job post into a scope document.

```
/scope jobs/airtable-crm.md
```

- Saves to `output/airtable-crm/scope.md`.
- If you type `/scope` with no file, Claude lists the job posts and asks which one to use.
- Run `/proposal` first if you can. The scope reads the proposal so the two match.

What you get, in this order: Project summary, What is included, What is not included, What the client must provide, Build steps and Open questions. Anything that depends on an answer from the client is marked "to be confirmed" and linked to an open question.

### /weekly-update

Turns rough progress notes into a short client update.

```
/weekly-update
/weekly-update jobs/notes/weekly-notes.md
```

- With no file, it uses `jobs/notes/weekly-notes.md`.
- Claude works out which job the notes are about by matching the client's name and details against the job posts. If it cannot tell, it stops and asks.
- Saves to `output/[job-name]/weekly-update.md`. For the sample notes, that is `output/n8n-lead-automation/weekly-update.md`.
- If a scope exists for that job, the update uses the same names for each part of the work.

What you get: a short greeting, then **Done**, **Next**, **Blockers** and **One decision needed**, and a sign-off. Test results are reported as tests, private notes to yourself are left out, and Claude tells you what it left out.

## Where results are saved

| Document | Location |
|---|---|
| Proposal | `output/[job-name]/proposal.md` |
| Scope | `output/[job-name]/scope.md` |
| Weekly update | `output/[job-name]/weekly-update.md` |

Each command creates the job folder if it does not exist.

> **Important:** if the file already exists, the command **replaces it** (Claude will mention this). Commit your approved documents to git first, or copy them somewhere safe, before running a command again for the same job.

## How to provide weekly notes

1. Write your notes as a plain `.md` file. Rough shorthand is fine. Use `jobs/notes/weekly-notes.md` as a model:

   ```
   # notes - brightstone n8n leads job

   done
   - ...

   next
   - ...

   blocker
   - ...

   decision needed
   - ...

   misc
   - ...
   ```

2. Mention the client's name so Clover can match the notes to the right job post.
3. Either overwrite `jobs/notes/weekly-notes.md` with your new notes, or save a new file in `jobs/notes/` and pass its path, for example `/weekly-update jobs/notes/my-notes.md`.
4. Create and edit notes files **yourself** in your editor. Claude asks for approval before writing anything in `jobs/`, and the house rules tell it not to change source files there unless you explicitly ask.

Never put passwords or API keys in notes. Clover will not write them into an update, and will ask the client to share access securely instead.

## Safety rules and permissions

### What Claude can and cannot do in this folder

| Area | Claude can... |
|---|---|
| `jobs/` | Read freely. Writing asks for your approval every time, and the house rules say not to change source files unless you ask. |
| `output/` | Read and write freely (every save is checked by the hook). |
| `CLAUDE.md`, `.gitignore`, everything in `.claude/` | Read only. Editing is denied. |
| `.env` and `.env.*` | Nothing. Reading is denied, both for Claude's file tools and for terminal commands. |
| Other new files in the project (such as this README) | Write only after asking you. |
| Anything outside the project folder | Nothing. Reads and writes outside the project are blocked. |

### The sandbox

Terminal (Bash) commands Claude runs are sandboxed, and Claude cannot switch the sandbox off. In tests:

- Bash could read project files but could **not write anywhere in the project**, including `jobs/` and `output/`, and could not read `.env`.
- This means Claude **cannot run `git commit`, delete or move files** for you. Run those yourself in your own terminal.

### What the hook does and does not cover

The hook covers:

- Saves made by Claude's **Write** and **Edit** tools to files inside `output/`.
- Two rules only: no em dash, and no form of "guarantee".
- The whole resulting file, not just the changed lines.

The hook does **not** cover:

- The other house rules (dates, prices, unnamed tools, made-up data). These rely on the skills' self-checks and **your review before sending**.
- Files outside `output/`.
- Edits you make yourself in your editor or terminal.
- Other ways of writing files (for example notebook edits or external tools). Bash writes to `output/` are blocked by the sandbox, so they cannot get around the hook.

### Changing Clover itself

Because `CLAUDE.md`, `.gitignore` and `.claude/` are locked against Claude's edits, any change to the rules, skills, commands, hook or settings has to be made **by you**, in your editor or terminal. This is on purpose: it stops Claude from rewriting its own rules.

### Secrets

Keep API keys and passwords in a `.env` file if you need them at all. `.gitignore` keeps `.env` out of git, and the settings stop Claude from reading it.

## First-time walkthrough

1. **Get the folder.** Copy or clone `Freelancer-toolkits` to your computer. Keep the folder names (`jobs/`, `output/`, `.claude/`) as they are, because the settings and commands rely on them.
2. **Check Python.** In a terminal, run `python3 --version`. You should see a version number.
3. **Open it in VS Code** and start Claude Code. When asked whether you trust the folder, say yes.
4. **Try a sample proposal.** In the chat, type:
   ```
   /proposal jobs/voice-agent-receptionist.md
   ```
   This replaces the sample in `output/voice-agent-receptionist/proposal.md`. If you want to keep the sample, commit or copy it first.
5. **Read the result.** Check it against the job post, then fill in `[Your name]` and the portfolio placeholder.
6. **Write the scope:**
   ```
   /scope jobs/voice-agent-receptionist.md
   ```
7. **Try a weekly update** with the sample notes:
   ```
   /weekly-update
   ```
   This writes to `output/n8n-lead-automation/weekly-update.md`.
8. **Save your work** with git, in your own terminal:
   ```
   git add output/
   git commit -m "Add proposal and scope for voice agent job"
   ```

### Adding your own job

1. In your editor, save the client's job post as a new `.md` file in `jobs/`, for example `jobs/my-new-job.md`. Use made-up data only while testing.
2. Run `/proposal jobs/my-new-job.md`.
3. When the client is interested, run `/scope jobs/my-new-job.md`.
4. Each week, write your notes and run `/weekly-update` with the notes file path.

## Known limitations

- Clover writes documents only. It does not send emails, connect to job boards, or talk to n8n, Airtable, CRMs or any other client tool.
- Running a command again for the same job replaces the previous file.
- The hook only checks for em dashes and "guarantee". Always read a document before sending it.
- Claude cannot commit, delete or move files in this project, and cannot edit `CLAUDE.md`, `.gitignore` or `.claude/`.
- Set up and tested on macOS only. It will not start where Claude Code's sandbox is unavailable, including native Windows.
- Documents have placeholders (`[Your name]`, portfolio examples) that you must fill in yourself.
