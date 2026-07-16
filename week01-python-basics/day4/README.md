# Week 1 · Day 4 — Files, venv & pip

Today = the real developer workflow. You'll read/write files, use built-in modules,
and set up virtual environments — the professional habit behind every AI project.

## Do these in order (about 4 hours)
- [ ] `01_write_files.py` — create and write to files.
- [ ] `02_read_files.py` — read files back (run 01 first!).
- [ ] `03_modules.py` — import built-in modules (incl. `json` — key for AI!). 📌
- [ ] `04_venv_and_pip.md` — **READ + do the terminal steps.** Most important today. 📌
- [ ] `05_use_package.py` — use the `requests` package you installed with pip.

## Order matters today
1. Run scripts 01–03 normally (`python3 01_write_files.py`, etc.).
2. Then open `04_venv_and_pip.md` and follow ALL 7 terminal steps.
3. With the venv active and `requests` installed, run `05_use_package.py`.

## 🎯 Day 4 challenge — a simple note saver
Create `note_saver.py` that:
1. Asks the user to type a note using `input()`.
2. Appends that note to a file `my_notes.txt` (with a newline).
3. Then reads the whole file and prints all saved notes back.

Run it a few times — each note should stick around. That's a real, persistent app!

## Key ideas to remember
> **Files** let your program remember things after it closes.
> **`json`** module = convert between Python dicts and text (how AI APIs talk).
> **`venv`** = a private package box per project. Activate before you work.
> **`pip install`** = download libraries. **`pip freeze > requirements.txt`** = save them.

Tomorrow (Day 5) you build your **first real project** to close out Week 1. 🎉
