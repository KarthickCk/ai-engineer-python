# Lesson 3 — Status codes in action + handling failures gracefully.
# Run:  python3 03_status_codes.py
#
# httpbin.org/status/CODE returns whatever status code you ask for,
# so we can trigger 200, 404, 500 on demand and practice handling them.

import requests

def call_and_report(code):
    url = f"https://httpbin.org/status/{code}"
    response = requests.get(url)
    sc = response.status_code

    # Classify by RANGE (the important skill):
    if 200 <= sc < 300:
        category = "✅ success"
    elif 300 <= sc < 400:
        category = "↪️  redirect"
    elif 400 <= sc < 500:
        category = "❌ client error (fix YOUR request)"
    else:
        category = "💥 server error (not your fault)"

    print(f"Asked for {code} -> got {sc}  {category}")

print("=== Triggering different status codes ===")
for code in [200, 301, 404, 429, 500, 503]:
    call_and_report(code)

print("\n=== The RIGHT way to call an API (check status BEFORE parsing) ===")
def safe_get_json(url):
    try:
        response = requests.get(url, timeout=10)      # timeout so we don't hang forever
        if response.status_code == 200:
            return response.json()                    # only trust the body on 200
        else:
            print(f"  Request failed with status {response.status_code} — not parsing body.")
            return None
    except requests.exceptions.RequestException as e:
        # Network down, DNS fail, timeout — catch it so we don't crash.
        print(f"  Network error: {e}")
        return None

print("Good URL:")
data = safe_get_json("https://api.adviceslip.com/advice")
if data:
    print("  Advice:", data["slip"]["advice"])

print("Bad URL (404):")
safe_get_json("https://httpbin.org/status/404")

print("Nonexistent host (network error):")
safe_get_json("https://this-domain-does-not-exist-xyz123.com")

print("\nThat's the pattern: try -> check status -> parse only on success.")
