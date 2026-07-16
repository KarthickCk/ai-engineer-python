# Lesson 2 — Your first repository

Let's make a throwaway practice repo first, then you'll do the real one in the challenge.

## Step 1 — make a folder and go in
```
cd ~/Documents/AI/python/week02-git-and-web/day2
mkdir practice-repo
cd practice-repo
```

## Step 2 — `git init` (start tracking this folder)
```
git init
```
This creates a hidden `.git` folder — that's where Git stores all history.
Run `ls -a` and you'll see `.git`. **Never edit inside it manually.**
One `git init` per project, ever.

## Step 3 — `git status` (your most-used command)
```
git status
```
Git says "No commits yet" and lists files it isn't tracking. Run `git status`
CONSTANTLY — before and after every action — to see where things stand.

## Step 4 — make a file, then check status
```
echo "# My Practice Repo" > README.md
git status
```
Now `README.md` shows in red under "Untracked files" — Git sees it but isn't
tracking it yet.

## Step 5 — `git add` (stage the file for the next snapshot)
```
git add README.md
git status
```
`README.md` is now green under "Changes to be committed". It's **staged** —
loaded into the chamber, ready to be committed.
(Shortcut: `git add .` stages EVERYTHING changed in the folder.)

## Step 6 — `git commit` (take the snapshot)
```
git commit -m "Initial commit: add README"
```
`-m` = the message describing this snapshot. Now it's permanently recorded. 🎉

## Step 7 — see it in the log
```
git log
```
Shows your commit: a unique id (hash), author, date, and message.
Press `q` to quit the log view.

## The two-stage idea (why add AND commit?)
```
Working directory  --git add-->  Staging area  --git commit-->  History
   (your edits)                  (chosen changes)              (permanent snapshot)
```
Staging lets you commit SOME changes now and others later — you pick exactly
what goes into each snapshot. Small, focused commits are the goal.
```
