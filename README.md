# Game Deals Data Pipeline

A Python data pipeline that pulls live video game deals from the CheapShark API , validates the data, stored in SQLite and reports on data quality.
(https://apidocs.cheapshark.com/)

Built as a personal portfolio project while completing B.Sc. in Computing For Business at DCU.

## What it Does

The pipeline runs in 5 stages:
1. **Extract** - fetches up to 60 discounted game deals from the CheapShark '/deals' endpoint.
2. **Clean** - converts raw string fields to proper types (price to 'float', scores to 'int', or 'None') and normalises missing values.
3. **Load** - stores each deal in a SQLite database, replacing existing rows by primary key ('dealID).
4. **Validate** - runs data quality checks against the cleaned deals: duplicate IDs, missing titles, suspicious prices. Returns a list of issue dictionaries. 
5. **Report** - prints a human-readable summary and exits non-zero if any issues were found.

## How to Run it
Requires Python 3.10+

'''bash
git clone https://github.com/marcomarsella2/Game-deals-pipeline-with-a-quality-report.git
cd Game-deals-pipeline-with-a-quality-report
python -m venv .venv

# Windows (Powershell)
.venv/Scripts/Activate.ps1
# MacoOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

python store.py             # fetch, clean, and store deals
python report.py            # run quality checks and print a report
pytest                      # run the test sute


```

`data/deals.db` is generated on first run and is git-ignored.

## Example output

Clean run (real CheapShark data):

```
Data quality: PASS (0 issues)
```

Run with a bad record injected (used to test the checks fire):

```
Data quality: FAIL (2 issues)
  missing_title: 1
  suspicious_price: 1
```

## Design decisions

- **Checks return issue dictionaries, not printed strings.** The
  `main` entry point decides the exit code based on the count, so the
  checks can be tested in isolation, reused by `report.py`, and wired
  to any future output format without changing.
- **A test surfaced a real bug.** `deal.get("title", "")` returns
  `""` only when the *key* is missing — if the key exists but the
  value is `None`, it returns `None`, and `None.strip()` crashes.
  A pytest case for `title: None` caught this, and the fix is
  `(deal.get("title") or "").strip()`.
- **`clean_deal` returns `None` for a missing Metacritic score**, and
  `tests/test_clean.py` documents that choice. Real CheapShark data
  had no missing scores in the sample, but the test protects the
  behaviour if the source changes.
- **Tests use fake dictionaries, not the live API.** They run fast,
  produce deterministic results, and don't break when the network is
  down or the API changes.

## Project structure

```
Game-deals-pipeline-with-a-quality-report/
├── conftest.py          # pytest root marker
├── requirements.txt
├── fetch_deals.py       # extract stage
├── clean.py             # clean stage
├── store.py             # load stage
├── checks.py            # validate stage
├── report.py            # report stage
├── tests/
│   ├── test_checks.py
│   └── test_clean.py
├── docs/
│   └── ai_log.md
└── data/
    └── deals.db         # generated, git-ignored
```

## What I'd do next

- Add a GitHub Actions workflow to run `pytest` on every push.
- Add a second data source (e.g. a public car API) to show the
  pipeline handles more than one source.
- Build a small dashboard that reads from `data/deals.db`.

## AI usage

I used Claude as a coding coach throughout this project. It explained
concepts before I wrote code, gave hints before solutions, and reviewed
drafts. A log of my prompts and what I learned is in
[docs/ai_log.md](docs/ai_log.md).
