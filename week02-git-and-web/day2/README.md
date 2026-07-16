# Week 2 · Day 2 — Git: your project's time machine 📌

Remember deleting those Day 1 files with no way back? **Git fixes that forever.**
Git records snapshots of your project over time, so you can see history, undo
mistakes, and (tomorrow) share your code on GitHub.

## The one-sentence mental model
> Git is a **save-game system for code**: you take "snapshots" (commits) of your
> project, and you can always go back to any snapshot.

## Do these in order (about 3-4 hours)
- [ ] `01_setup.md` — one-time Git config (your name & email). 📌
- [ ] `02_first_repo.md` — `init`, `status`, `add`, `commit` — make your first repo. 📌
- [ ] `03_history_and_changes.md` — `log`, `diff`, changing files, `.gitignore`.
- [ ] Then do the 🎯 challenge below.

Type every command yourself in your terminal.

## The core loop (memorize this rhythm)
```
edit files  →  git add <files>  →  git commit -m "message"  →  repeat
```
- **add** = "stage" the changes you want in the next snapshot
- **commit** = actually take the snapshot (with a message describing it)

## 🎯 Day 2 challenge — put your Week 1 to-do app under Git
1. `cd` into your Day 5 to-do project folder.
2. `git init` to start tracking it.
3. Create a `.gitignore` that ignores `tasks.txt` and `__pycache__/`.
4. `git add` your code and commit it: "Initial commit: CLI to-do app".
5. Make a small change to `todo.py` (e.g. improve a print message).
6. Use `git diff` to see the change, then `add` + `commit` it: "Improve messages".
7. Run `git log --oneline` — you should see your TWO commits.

Two commits in your log = Day 2 done. ✅ Tomorrow you push this to GitHub.

## Key idea to remember
> `git init` once per project. Then the loop forever: **add → commit**.
> Commit small and often, with clear messages. Your future self will thank you.
