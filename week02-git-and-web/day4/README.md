# Week 2 · Day 4 — How the Web Works 📌

Every AI app you build talks to servers over **HTTP**. When you call the Claude
API (Week 5), you're doing exactly what this day covers. You've used APIs in
React Native — today we make the mental model precise and see it live in Python.

## The one-sentence model
> HTTP is a **request → response** conversation: your program asks a server for
> something (a request), the server answers (a response). Both carry headers,
> maybe a body, and the response carries a **status code**.

## Do these in order (about 3 hours)
- [ ] `01_http_concepts.md` — methods, status codes, headers, request/response anatomy. 📌
- [ ] `02_inspect_requests.py` — RUN this: make real calls and inspect every part. 📌
- [ ] `03_status_codes.py` — RUN this: trigger 200/404/500 and handle them.
- [ ] Then do the 🎯 challenge below.

Run the Python files with:
```
cd ~/Documents/AI/python/week02-git-and-web/day4
python3 02_inspect_requests.py
```
(If `requests` isn't found, make a venv: `python3 -m venv .venv && source .venv/bin/activate && pip install requests`.)

## 🎯 Day 4 challenge — a resilient API caller
Write `weather.py` (or use any public API) that:
1. Calls a public API with `requests.get(...)`.
2. Checks `response.status_code` — only parse JSON if it's `200`.
3. On success, digs out and prints 2-3 useful fields.
4. On failure (non-200 or network error), prints a friendly message instead of crashing.
5. Uses a `try/except` around the network call.

If it prints clean output on success AND doesn't crash on failure → Day 4 done. ✅

## Key idea to remember
> A response has a **status code** (did it work?), **headers** (metadata), and a
> **body** (the data, usually JSON). Always check the status BEFORE trusting the body.
> This is the exact shape of every Claude API call you'll make later.
