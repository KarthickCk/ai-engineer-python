# Lesson 1 — Navigation: where am I & how do I move around?

Type EVERY command below in your terminal. Reading isn't enough — type it.

## The 3 commands that do 80% of the work

### `pwd` — "print working directory" (where am I right now?)
```
pwd
```
Prints the full path of the folder you're currently "standing in", e.g.
`/Users/karthick/Documents/AI/python`. When lost, `pwd` first.

### `ls` — "list" (what's in here?)
```
ls
```
Shows files & folders in the current directory. Useful variants:
```
ls -l      # long format: permissions, size, date
ls -a      # ALSO show hidden files (names starting with a dot, like .venv)
ls -la     # both combined (most common)
ls -R      # recursive: show everything in subfolders too
```

### `cd` — "change directory" (go somewhere)
```
cd Documents        # go INTO the Documents folder (relative to where you are)
cd ..               # go UP one level (to the parent folder)
cd ~                # go to your HOME folder (/Users/karthick)
cd /                # go to the root of the whole disk
cd -                # go BACK to the previous folder you were in
cd                  # (with nothing) also goes home
```

## Paths: relative vs absolute
- **Absolute path** starts with `/` (or `~`) — the full address from the top:
  `/Users/karthick/Documents/AI/python`
- **Relative path** is from wherever you are now: `day1`, `../day2`, `./notes.txt`
- `.` = "here (current folder)"  ·  `..` = "one level up"  ·  `~` = "my home folder"

## TRY IT
1. `pwd` — note where you are.
2. `cd ~/Documents/AI/python` then `ls` — you should see `week01-...` and `week02-...`.
3. `cd week02-git-and-web/day1` then `pwd` — confirm you moved.
4. `cd ..` then `pwd` — you went up one level.
5. `cd -` — jumps you back into `day1`. Handy!

## Pro tips (use these constantly)
- **Tab completion:** type `cd week0` then press **Tab** — the shell finishes the name.
  Saves typos and time. Press Tab often!
- **Up arrow:** recalls your previous commands. Stop retyping.
- If a folder name has spaces, wrap it in quotes: `cd "My Folder"` (or Tab-complete it).
