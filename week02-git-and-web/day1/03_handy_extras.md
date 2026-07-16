# Lesson 3 — Handy extras + the challenge solution

A few more commands you'll use daily, then the challenge answer.

## Viewing files without opening an editor
```
cat notes.txt        # dump the whole file to the screen
head notes.txt       # first 10 lines
tail notes.txt       # last 10 lines
tail -f app.log      # FOLLOW a file live (great for watching logs) — Ctrl+C to stop
```

## Finding things
```
grep "hello" notes.txt        # find lines containing "hello" in a file
grep -r "TODO" .              # search ALL files under here (recursive) for "TODO"
find . -name "*.py"          # find all .py files under the current folder
```

## Clearing & history
```
clear                # wipe the screen (or Cmd+K on Mac). Ctrl+L also works.
history              # show past commands
```
Press **Up arrow** to recall previous commands. Press **Tab** to auto-complete paths.

## Chaining commands
```
mkdir logs && cd logs        # && = "do the second ONLY if the first succeeded"
```

## Opening things
```
open .               # (macOS) open the current folder in Finder
code .               # open the current folder in VS Code (if 'code' is installed)
```

---

## 🎯 Challenge solution (try it yourself FIRST, then check)
```
cd ~/Documents/AI/python/week02-git-and-web/day1
mkdir sandbox
cd sandbox
touch notes.txt todo.txt readme.txt
mkdir docs archive
mv notes.txt readme.txt docs/      # move two files at once into docs/
cp todo.txt archive/               # copy todo.txt into archive/
rm todo.txt                        # delete the original in sandbox/
ls -R                              # verify the tree
```

Expected `ls -R` output:
```
archive  docs

./archive:
todo.txt

./docs:
notes.txt  readme.txt
```
(`sandbox/` itself now holds only the two folders — no loose files.)

Clean up when done:
```
cd ..
rm -r sandbox
```

If your tree matched — **Day 1 done.** ✅ Tomorrow: Git.
