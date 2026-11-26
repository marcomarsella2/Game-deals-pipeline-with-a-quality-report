# AI Usage Log

I used Claude as a coding coach on this project. It did not write code
I couldn't explain; every change below was understood, typed, and
committed by me. The log is here so anyone reading the project can see
how the coaching was used.

## Format

Each entry: **Question** → **What I learned** → **What I changed**.

## Entries

### 1. Choosing a project
**Asked:** Which of three project ideas best fits my background and CV goals?
**Learned:** The API + data-quality pipeline covered APIs, pytest, and a
pipeline stage — three things I'd never done — with a small enough scope
to finish. The TechTube upgrade was lower risk but harder to show as my
own work (pair project).
**Changed:** Chose the game deals pipeline.

### 2. Virtual environment on Windows
**Asked:** Why does `.venv\Scripts\Activate.ps1` fail with an
execution-policy error?
**Learned:** PowerShell blocks unsigned scripts by default;
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` allows local
scripts for my user only. The `ad.venv\...` error was a typo, not a
policy issue.
**Changed:** Fixed the policy, activated the venv, selected the
interpreter in VS Code.

### 3. Database schema and types
**Asked:** Why are all my columns `TEXT` after I edited `CREATE TABLE`?
**Learned:** `CREATE TABLE IF NOT EXISTS` doesn't alter an existing
table. The `.db` file had to be deleted for the new types to take
effect. Also learned that SQLite treats column names case-insensitively,
unlike Python dict keys.
**Changed:** Deleted `data/deals.db`, re-ran, verified with `typeof()`.

### 4. A test found a real bug
**Asked:** Why does `deal.get("title", "").strip()` crash on
`{"title": None}`?
**Learned:** `.get(key, default)` only returns the default when the
**key is absent**. If the key exists with a `None` value, it returns
`None`, and `.strip()` on `None` raises `AttributeError`. The fix
`(deal.get("title") or "").strip()` uses `or` — which short-circuits
on any falsy value (including `None`) — so `.strip()` is always
called on a string.
**Changed:** Fixed `check_missing_titles`, added
`test_missing_titles_handles_none` which reproduces the bug before the
fix and confirms it after.

### 5. Fixing the pytest import path
**Asked:** Why does `from checks import ...` fail when tests are in
`tests/`?
**Learned:** Pytest starts import lookup from the test file's folder.
`conftest.py` at the project root tells pytest where the root is and
adds it to `sys.path`.
**Changed:** Added an empty `conftest.py` at the project root.

### 6. Git branch clean-up
**Asked:** I created `Dev` and `Test` branches I don't need. How do
I consolidate to `main` and avoid losing work?
**Learned:** For a solo project with serial work, `main` alone is
enough. `git branch -d` is the safe delete; `--force` should not be
used casually. Generated files (`__pycache__`, `data/*.db`,
`scratch.py`) should be in `.gitignore` from day one.
**Changed:** Consolidated to `main`, added `.gitignore`, deleted
`Dev`, `Test`, and `master` (local and remote).

### 7. README structure
**Asked:** What goes in a portfolio README?
**Learned:** The README is the project for most reviewers. Sections
that matter most: what it does, architecture, how to run it (tested
on a fresh clone), example output (PASS *and* FAIL), design decisions
with *why*, testing, and next steps.
**Changed:** Wrote the README with all sections, including the
`None`-title bug as a design decision.

(Add more entries as you continue — even rough notes are fine.)