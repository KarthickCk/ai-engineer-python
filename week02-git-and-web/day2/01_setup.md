# Lesson 1 — One-time Git setup

Before your first commit, Git needs to know WHO is making commits. You do this
**once per computer** — every future commit gets stamped with this name/email.

## Set your identity
```
git config --global user.name "Karthick"
git config --global user.email "karthick@envisioning.group"
```
(`--global` = applies to all your projects on this machine.)

## Set a sensible default branch name
Modern convention is `main` (not the old `master`):
```
git config --global init.defaultBranch main
```

## Check it worked
```
git config --global --list
```
You should see your `user.name`, `user.email`, and `init.defaultBranch=main`.

## Why the email matters
When you push to GitHub tomorrow, GitHub matches this email to your account to
credit your commits (the green contribution squares). Use the same email you'll
sign up to GitHub with.

## That's it
This is a once-and-done step. Now to the real work → `02_first_repo.md`.
