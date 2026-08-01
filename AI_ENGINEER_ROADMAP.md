# AI App Developer — 12-Week Day-by-Day Roadmap

**Goal:** Become a junior AI application developer who builds and deploys full-stack AI web apps.
**Schedule:** 5 study days/week × 4 hrs = 20 hrs/week. 12 weeks total.
**How to use:** Do days in order. Check `[x]` when done. Don't skip the "Deliverable" — building is the point.

Legend: 🎯 = deliverable/project checkpoint · 📌 = don't-skip fundamental

---

## PHASE 1 — Programming Foundations

### Week 1 — Python basics
- [x] Day 1: Install Python + VS Code. Learn variables, numbers, strings, `print`. Write 5 tiny scripts.
- [x] Day 2: Lists, dictionaries, loops (`for`/`while`). 📌
- [x] Day 3: Functions, arguments, return values. `if`/`else` logic.
- [x] Day 4: `venv`, `pip install`, importing modules. Read/write files.
- [x] Day 5: Practice — build a CLI to-do list (add/list/remove tasks). 🎯

### Week 2 — Git + web fundamentals
- [x] Day 1: Command line basics (cd, ls, mkdir, mv). 📌
- [x] Day 2: Git: init, add, commit, log. Make a local repo.
- [x] Day 3: GitHub: push a repo, understand branches + PRs.
- [x] Day 4: How the web works: HTTP requests, JSON, status codes, APIs.
- [x] Day 5: Python `requests` — call a public API (weather/jokes), print results. Push to GitHub. 🎯

---

## PHASE 2 — JavaScript + Web Basics

### Week 3 — HTML, CSS, JS
- [ ] Day 1: HTML structure — tags, forms, inputs, buttons.
- [ ] Day 2: CSS basics — selectors, flexbox, layout.
- [ ] Day 3: JavaScript fundamentals — variables, functions, arrays, objects. 📌
- [ ] Day 4: DOM manipulation — select elements, handle clicks.
- [ ] Day 5: Build a static webpage with a button that changes the page. 🎯

### Week 4 — Async JS + APIs
- [ ] Day 1: `fetch`, promises, `async/await`. 📌
- [ ] Day 2: Call a public API from JavaScript, show data on the page.
- [ ] Day 3: TypeScript basics — types, interfaces (light intro).
- [ ] Day 4: Practice — weather app webpage (input city → show weather).
- [ ] Day 5: Polish it, deploy to Vercel (free). Public URL! 🎯 (first deploy)

---

## PHASE 3 — First AI App (Backend)

### Week 5 — Claude API
- [ ] Day 1: Get an Anthropic API key. Read Claude API docs (messages, models). 📌
- [ ] Day 2: First API call in Python — send a message, print response.
- [ ] Day 3: System prompts + conversation history (multi-turn).
- [ ] Day 4: Streaming responses (token-by-token).
- [ ] Day 5: Build a CLI AI chatbot with memory of the conversation. 🎯

### Week 6 — Prompt engineering + tools
- [ ] Day 1: Prompt techniques — clear instructions, few-shot examples.
- [ ] Day 2: Structured output (ask for JSON, parse it).
- [ ] Day 3: Tool use / function calling — let Claude call a function.
- [ ] Day 4: Build a small agent: Claude + a calculator/search tool.
- [ ] Day 5: Wrap your chatbot logic in a simple API (FastAPI intro). 🎯

---

## PHASE 4 — React Frontend

### Week 7 — React fundamentals
- [ ] Day 1: Next.js setup, project structure, pages. 📌
- [ ] Day 2: Components, props, JSX.
- [ ] Day 3: State (`useState`), events, forms.
- [ ] Day 4: `useEffect`, fetching data in React.
- [ ] Day 5: Tailwind CSS — style a clean component. 🎯

### Week 8 — AI Chat App (Project #1)
- [ ] Day 1: Design the chat UI (message list, input box).
- [ ] Day 2: Connect React frontend to your FastAPI + Claude backend.
- [ ] Day 3: Stream AI responses into the UI live. 📌
- [ ] Day 4: Handle loading states, errors, empty states.
- [ ] Day 5: Polish + deploy. **🎯 PROJECT #1: Deployed AI Chat App**

---

## PHASE 5 — RAG (the standout skill)

### Week 9 — Embeddings + retrieval
- [ ] Day 1: What embeddings are; generate embeddings for text. 📌
- [ ] Day 2: Vector DB intro — set up Chroma (local).
- [ ] Day 3: Chunking documents; store chunks + embeddings.
- [ ] Day 4: Similarity search — retrieve relevant chunks for a query.
- [ ] Day 5: Combine retrieval + Claude to answer from your docs. 🎯

### Week 10 — Chat with your PDF (Project #2)
- [ ] Day 1: PDF upload + text extraction.
- [ ] Day 2: Full pipeline: upload → chunk → embed → store.
- [ ] Day 3: Query → retrieve → answer **with citations**. 📌
- [ ] Day 4: Build the frontend (upload UI + chat).
- [ ] Day 5: Deploy. **🎯 PROJECT #2: Chat with your PDF**

---

## PHASE 6 — Deployment Engineering + Polish

### Week 11 — Real production skills
- [ ] Day 1: Environment variables + secrets management (never commit keys!). 📌
- [ ] Day 2: Docker basics — containerize your backend.
- [ ] Day 3: Add a database (Postgres via Supabase/Neon) — save chat history.
- [ ] Day 4: Add auth (Clerk or NextAuth) — user login.
- [ ] Day 5: CI/CD — GitHub Actions to auto-deploy on push. 🎯

### Week 12 — Portfolio + launch
- [ ] Day 1: Error tracking (Sentry) + basic logging.
- [ ] Day 2: Write great READMEs (screenshots, live demo links, setup steps). 📌
- [ ] Day 3: Build a personal portfolio site linking all projects.
- [ ] Day 4: Clean up GitHub, pin best repos, write a short "what I built" post.
- [ ] Day 5: Review everything. Plan next 3 months (deepen cloud + apply to jobs). 🎯

---

## After 12 weeks
- [ ] Pick one cloud (AWS or GCP) and go deep.
- [ ] Learn evals & observability for AI apps.
- [ ] Build a 3rd bigger project (an AI agent that does real work).
- [ ] Start applying to jobs while you keep building.

---

## Progress tracker
| Phase | Weeks | Status |
|-------|-------|--------|
| 1. Programming foundations | 1–2 | ☐ |
| 2. JavaScript + web | 3–4 | ☐ |
| 3. First AI app (backend) | 5–6 | ☐ |
| 4. React frontend | 7–8 | ☐ |
| 5. RAG | 9–10 | ☐ |
| 6. Deployment + polish | 11–12 | ☐ |

**Rule:** deploy early, deploy often. A deployed messy project beats a perfect local one.
