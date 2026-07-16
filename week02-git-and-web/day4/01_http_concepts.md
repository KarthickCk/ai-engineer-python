# Lesson 1 — HTTP concepts (the precise mental model)

## The conversation
```
YOUR PROGRAM  ---- request  --->  SERVER
              <--- response ----
```
One request, one response. Stateless — each request stands alone (that's why
APIs make you send your auth key every time).

## A REQUEST has 4 parts
1. **Method** — the verb (what you want to do)
2. **URL** — the address (which resource)
3. **Headers** — metadata (`Authorization`, `Content-Type`, ...)
4. **Body** — the data you send (usually JSON; only for POST/PUT/PATCH)

## HTTP methods (verbs)
| Method | Means | Example |
|--------|-------|---------|
| GET    | read / fetch | get a user's profile |
| POST   | create | create a new message |
| PUT    | replace | overwrite a whole record |
| PATCH  | update part | change just the email |
| DELETE | remove | delete a post |

You'll mostly use **GET** (read data) and **POST** (send data — e.g. a prompt to Claude).

## A RESPONSE has 3 parts
1. **Status code** — a number: did it work? (see below)
2. **Headers** — metadata (`Content-Type: application/json`, rate-limit info, ...)
3. **Body** — the actual data, usually JSON

## Status codes — memorize the RANGES, not every number
| Range | Meaning | Common ones |
|-------|---------|-------------|
| `1xx` | informational | (rare) |
| `2xx` | ✅ success | **200** OK · **201** Created · 204 No Content |
| `3xx` | redirect | 301 Moved · 304 Not Modified |
| `4xx` | ❌ **YOU** made a mistake | **400** Bad Request · **401** Unauthorized · **403** Forbidden · **404** Not Found · **429** Too Many Requests |
| `5xx` | 💥 **SERVER** made a mistake | **500** Internal Error · 502 Bad Gateway · 503 Unavailable |

Rule of thumb: **4xx = fix your request. 5xx = not your fault, maybe retry.**

## Query strings vs body
- **Query string** = data in the URL after `?`: `https://api.site.com/search?q=cats&limit=5`
  (used with GET — filters, params). In `requests`: `params={"q": "cats", "limit": 5}`
- **Body** = data sent separately (used with POST): `json={"prompt": "hello"}`

## Why this matters for AI
A Claude API call is: **POST** to a URL, with an **Authorization** header (your key),
a JSON **body** (your messages), and you check the **status code** and parse the
JSON **body** of the response. Everything today is that call in miniature.
