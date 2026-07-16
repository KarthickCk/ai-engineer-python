# Week 2 · Day 1 — The Command Line 📌

You've been *using* the terminal to run `python3 ...`. Today you **learn it properly**.
The command line is a developer's home base — Git, servers, deploys all live here.
Once it clicks, you'll feel 10× faster.

## Why this matters
Every real dev job expects you to move around, create, and manage files from the
terminal without a mouse. It's also the foundation for Git (tomorrow) and deploys.

## Do these in order (about 3-4 hours)
- [ ] `01_navigation.md` — where am I? move around: `pwd`, `ls`, `cd`. 📌
- [ ] `02_files_and_folders.md` — create/move/copy/delete: `mkdir`, `touch`, `mv`, `cp`, `rm`.
- [ ] `03_handy_extras.md` — view files, search, history, tab-completion tricks.
- [ ] Then do the 🎯 challenge below.

These are **markdown lessons** (not `.py` files) — read each one and **type every command
yourself** in your terminal. Muscle memory only comes from typing.

## 🎯 Day 1 challenge — organize a project from the terminal ONLY
No mouse, no VS Code file explorer. Using only the terminal:
1. Make a folder `~/Documents/AI/python/week02-git-and-web/day1/sandbox`.
2. `cd` into it.
3. Create 3 files: `notes.txt`, `todo.txt`, `readme.txt`.
4. Make two folders inside: `docs` and `archive`.
5. Move `notes.txt` and `readme.txt` into `docs`.
6. Copy `todo.txt` into `archive`.
7. Delete the original `todo.txt` (the one left in `sandbox`).
8. Run `ls -R` to show the final tree and check it matches.

If the final structure is right, Day 1 is done. ✅ (Solution steps are in `03_handy_extras.md`.)

## Key idea to remember
> The terminal is just a **text way to do what you'd do with a mouse** — but faster,
> scriptable, and available on every server (where there IS no mouse).
> `pwd` = where am I, `ls` = what's here, `cd` = go there. That's 80% of it.
