# Lesson 2 — Creating, moving, copying & deleting

Now you can move around. Let's make and manage things. Type every command.

## Make folders & files

### `mkdir` — "make directory" (new folder)
```
mkdir myfolder
mkdir -p a/b/c       # -p makes the whole nested chain at once (a, then b, then c)
```

### `touch` — create an empty file (or update its timestamp)
```
touch notes.txt
touch a.txt b.txt c.txt     # create several at once
```

## Move, rename & copy

### `mv` — "move" (also how you RENAME)
```
mv notes.txt docs/           # move notes.txt INTO the docs folder
mv old.txt new.txt           # rename (there's no separate "rename" command!)
mv file.txt ../              # move it up one level
```
👉 Key insight: **renaming and moving are the same command.** `mv A B` means
"A is now at B" — whether B is a new name or a new folder.

### `cp` — "copy"
```
cp file.txt backup.txt       # copy a file
cp file.txt archive/         # copy INTO a folder
cp -r folder1 folder2        # -r = recursive, needed to copy a whole FOLDER
```

## Delete (⚠️ careful — no Recycle Bin!)

### `rm` — "remove" (files)
```
rm file.txt
rm a.txt b.txt               # remove several
```

### `rm -r` — remove a folder and everything in it
```
rm -r oldfolder
```

## ⚠️ THE GOLDEN SAFETY RULES
- `rm` is **permanent** — there is NO undo, NO trash can. Deleted = gone.
- **NEVER** run `rm -rf /` or `rm -rf ~` or `rm -rf *` unless you are 100% sure.
  The `-f` (force) flag deletes without asking. This can wipe your whole disk.
- Before `rm`, run `ls` first to SEE exactly what you're about to delete.
- When unsure, move to a `trash` folder instead of deleting: `mkdir ~/trash; mv x ~/trash`.

## TRY IT (in a safe throwaway spot)
```
cd ~/Documents/AI/python/week02-git-and-web/day1
mkdir practice
cd practice
touch one.txt two.txt
mkdir backup
cp one.txt backup/
mv two.txt renamed.txt
ls -R                        # look at the tree you built
cd ..
rm -r practice               # clean up (you SAW what's inside, so it's safe)
```
