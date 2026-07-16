# Lesson 2 — Inspect a real HTTP request/response, part by part.
# Run:  python3 02_inspect_requests.py
#
# We'll call httpbin.org — a free service that echoes back what you sent,
# so you can SEE every part of the request/response.

import requests

print("=== 1) A simple GET ===")
response = requests.get("https://httpbin.org/get")

# --- The RESPONSE has 3 parts ---
print("Status code:", response.status_code)          # 200 = OK
print("Content-Type header:", response.headers["Content-Type"])
print("Body (first 200 chars):", response.text[:200])

print("\n=== 2) GET with a query string (params) ===")
# params={...} becomes  ?city=Chennai&units=metric  in the URL
response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=10)
print("Final URL requests built:", response.url)      # see the ?city=... it made
data = response.json()
setup = data.get("setup", {})
punchline = data.get("punchline", {})                            # parse JSON body -> dict
print(f"Server saw these args: {setup} {punchline}")         # httpbin echoes them back

print("\n=== 3) POST with a JSON body ===")
# This is the shape of a Claude API call: POST + JSON body.
response = requests.post("https://httpbin.org/post", json={"prompt": "Hello, world"})
data = response.json()
print("Status code:", response.status_code)
print("Server received this JSON body:", data["json"])   # echoes your body back

print("\n=== 4) Sending a header (like an API key) ===")
response = requests.get("https://httpbin.org/get", headers={"Authorization": "Bearer FAKE_KEY_123"})
data = response.json()
print("Server saw Authorization header:", data["headers"].get("Authorization"))

print("\nDONE. You just sent methods, params, a body, and headers — the whole toolkit.")

# TRY IT: change the params in step 2 to your own key/values and re-run.
#         Notice how response.url shows exactly what got sent.
