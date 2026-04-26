# OpportuAI — Backend

> AI-powered opportunity matching for students.
> This README is for developers only. Follow every step in order.

---

## What Was Built in Week 1

- FastAPI project structure initialized
- PostgreSQL schema designed (6 tables)
- SQLAlchemy models written
- Alembic migration ran — all 6 tables live in Supabase
- RLS enabled on all 6 tables
- `GET /health` endpoint working
- Swagger docs at `/docs` working
- Supabase PostgreSQL connected

---

## Prerequisites

Make sure you have these installed on your machine before starting:

- Python 3.12+
- Git
- VS Code (recommended)

Check your Python version:

```bash
python --version
```

---

## Step 1 — Clone the Repo

```bash
git clone https://github.com/YOUR_ORG/opportuai.git
cd opportuai
```

---

## Step 2 — Go Into Backend Folder

```bash
cd backend
```

---

## Step 3 — Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

You should see `(.venv)` at the start of your terminal line.

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Set Up Environment Variables

Copy the example file:

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Open `.env` and fill in your real values:

```env
# LLM
GEMINI_API_KEY=get from aistudio.google.com
GROQ_API_KEY=get from console.groq.com

# Scraping
FIRECRAWL_API_KEY=get from firecrawl.dev
SERP_API_KEY=get from serpapi.com

# Supabase
SUPABASE_URL=get from supabase.com project settings
SUPABASE_ANON_KEY=get from supabase.com project API keys
SUPABASE_SERVICE_ROLE_KEY=get from supabase.com project API keys

# Database
DATABASE_URL=get from supabase.com connect page (Session Pooler URI)

# Redis
REDIS_URL=redis://localhost:6379
```

> Ask the backend lead for the real values over WhatsApp/Telegram.
> Never commit `.env` to GitHub. Ever.

---

## Step 6 — Run Database Migrations

This creates all 6 tables in Supabase:

```bash
alembic upgrade head
```

You should see:

```
INFO  [alembic.runtime.migration] Running upgrade -> xxxxxxx, initial tables
```

If tables already exist you will see:

```
INFO  [alembic.runtime.migration] No new upgrade operations to perform.
```

Both are fine. Move on.

---

## Step 7 — Run the Server

```bash
uvicorn main:app --reload
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process using StatReload
```

---

## Step 8 — Confirm Everything Works

Open these two URLs in your browser:

| URL | What you should see |
|-----|-------------------|
| `http://localhost:8000/health` | `{"status":"ok","version":"1.0.0","project":"OpportuAI"}` |
| `http://localhost:8000/docs` | Swagger UI with all API endpoints |

If both work you are fully set up. ✅

---

## Project Structure

```
backend/
├── main.py                  ← FastAPI app entry point
├── requirements.txt         ← All Python dependencies
├── .env                     ← Your local secrets (never commit)
├── .env.example             ← Template for env variables
│
├── agents/                  ← AI pipeline agents
│   ├── agent01_scraper.py   ← Firecrawl URL scraper
│   ├── agent02_matcher.py   ← Gemini opportunity matcher
│   ├── agent03_drafter.py   ← Groq cover letter writer
│   └── agent04_upskiller.py ← Learning path generator
│
├── services/                ← Business logic
│   ├── profile_builder.py   ← Resume → student profile
│   ├── profile_updater.py   ← Skill update handler
│   └── rescan_engine.py     ← Rescan opportunities on update
│
├── utils/                   ← Shared utilities
│   ├── llm_client.py        ← Gemini + Groq client
│   ├── pdf_reader.py        ← PDF text extractor
│   └── link_extractor.py    ← URL extractor from text
│
├── models/
│   ├── schemas.py           ← Pydantic request/response models
│   └── database.py          ← SQLAlchemy table models
│
├── routers/                 ← API route handlers
│   ├── auth.py              ← /auth/* endpoints
│   ├── profile.py           ← /profile/* endpoints
│   ├── opportunities.py     ← /opportunities endpoint
│   └── analyze.py           ← /analyze endpoint
│
├── migrations/              ← Alembic migration files
│   └── versions/
│       └── xxxx_initial_tables.py
│
└── data/                    ← Static JSON data files
    ├── certificates.json    ← 50+ free cert links
    ├── hackathons.json      ← 20+ hackathon listings
    └── fallbacks.json       ← Pre-scraped demo data
```

---

## Database Tables

All 6 tables live in Supabase PostgreSQL:

| Table | Purpose |
|-------|---------|
| `students` | Student accounts and profiles |
| `skills` | Individual skills per student |
| `opportunities` | Jobs, hackathons, internships |
| `matches` | Match results per student per opportunity |
| `skill_updates` | History of what student learned |
| `learning_paths` | 3-step cert plans per match |

---

## API Endpoints

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| GET | `/health` | Health check | ✅ Done |
| GET | `/docs` | Swagger UI | ✅ Done |
| POST | `/auth/signup` | Student signup | 🔨 Week 2 |
| POST | `/auth/login` | Student login | 🔨 Week 2 |
| GET | `/auth/me` | Get current student | 🔨 Week 2 |
| POST | `/profile/build` | Build profile from resume | 🔨 Week 2 |
| POST | `/profile/update` | Update skill | 🔨 Week 3 |
| POST | `/analyze` | Run full AI pipeline | 🔨 Week 3 |
| GET | `/opportunities` | Get matched opportunities | 🔨 Week 3 |

---

## Branch Strategy

```
main          → production only. Never push directly.
dev           → active development. Merge PRs here.
feature/*     → your individual work branch.
```

Always create your own branch:

```bash
git checkout dev
git pull origin dev
git checkout -b feature/your-task-name
```

Never push directly to `main` or `dev`.

---

## Common Errors and Fixes

**`Error loading ASGI app. Attribute "app" not found`**
→ `main.py` is empty. Paste the FastAPI app code into it.

**`invalid literal for int() with base 10: 'port'`**
→ `DATABASE_URL` in `.env` still has placeholder text. Replace with real Supabase URL.

**`Import pydantic could not be resolved`**
→ VS Code is using wrong Python. Press `Ctrl+Shift+P` → `Python: Select Interpreter` → choose `.venv`.

**`ResolutionImpossible` during pip install**
→ Delete pinned versions from `requirements.txt`. Keep only package names. Run `pip install -r requirements.txt` again.

**`venv\Scripts\activate` not recognized**
→ Run this instead: `.venv\Scripts\activate`

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| Language | Python 3.12 |
| Database | PostgreSQL via Supabase |
| ORM | SQLAlchemy + Alembic |
| Auth | Supabase Auth + JWT |
| File Storage | Supabase Storage |
| LLM Primary | Gemini 2.0 Flash |
| LLM Fallback | Groq Llama 3.3 70b |
| Scraping | Firecrawl + SERP API |
| Cache/Queue | Redis + Celery |
| Deploy | Railway |

---

## Questions

Reach out to the backend lead on the team group chat.
Do not open GitHub issues for setup problems — just message directly.