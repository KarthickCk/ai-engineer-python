# Virtual Environments (venv) & pip — READ THIS, then do the steps in Terminal

This is the **most important professional habit** in Python. Every real project
(and every AI project you'll build) uses a virtual environment. Do this once and
it'll click forever.

## What is a virtual environment?
A `venv` is a private, isolated Python box **just for one project**. Packages you
install go inside that box — not messing up your computer or other projects.

Think of it like a separate toolbox for each project, so their tools never clash.

## What is pip?
`pip` is Python's package installer. It downloads code libraries other people wrote
(like the Anthropic SDK you'll use for Claude) from the internet.

---

## Do these steps in your Terminal (in the day4 folder)

**1. Go to the day4 folder:**
```
cd /Users/karthick/Documents/AI/python/week01-python-basics/day4
```

**2. Create a virtual environment named `.venv`:**
```
python3 -m venv .venv
```
(A new hidden `.venv` folder appears — that's your project's private Python box.)

**3. Activate it:**
```
source .venv/bin/activate
```
Your terminal prompt now shows `(.venv)` at the start. That means it's ON. ✅

**4. Install a package (a friendly HTTP library called `requests`):**
```
pip install requests
```

**5. See what's installed:**
```
pip list
```

**6. Save your project's dependencies to a file (standard practice):**
```
pip freeze > requirements.txt
```
Open `requirements.txt` — it lists exactly what your project needs. Anyone can
recreate your setup later with `pip install -r requirements.txt`.

**7. When you're done working, turn it off:**
```
deactivate
```
The `(.venv)` disappears.

---

## The golden rules
- ✅ **One venv per project.** Create it right after making a project folder.
- ✅ **Activate it** (`source .venv/bin/activate`) every time you work on the project.
- ✅ **Never commit `.venv` to Git** — commit `requirements.txt` instead.
- ✅ If you see `(.venv)` in your prompt, you're in the right place.

## 🎯 Task for today
Complete steps 1–7 above. Then run:
```
python3 05_use_package.py
```
(That script uses the `requests` package you just installed.)
