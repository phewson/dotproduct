# Your Coding Workflow

If in doubt, this is what a typical coding session looks like.

## Start Your Session

Get the latest version of the repository:

```bash
git pull
```

This downloads any changes from GitHub.


## Do Some Coding

Implement one function.

Run the tests.

Fix any errors.

Run the tests again.

A good workflow is:

```bash
./run_tests
```

Make a small change.

```bash
./run_tests
```

Make another small change.

```bash
./run_tests
```

Try to keep the tests passing as often as possible.


## Check What Changed

Before committing, ask Git what has changed.

```bash
git status
```

Read the output carefully.

You should understand what files you are about to commit.


## Stage Your Changes

### Option 1: Add Everything

If you trust the repository's `.gitignore` file:

```bash
git add .
```

This stages all changed files.

### Option 2: Add Specific Files

If you want more control:

```bash
git add functions.py
```

or

```bash
git add test_functions.py
```

Many experienced developers prefer this approach.


## Commit Your Work

Create a commit:

```bash
git commit -m "Implement total_score"
```

Good commit messages describe what changed.

### Good Examples

```bash
git commit -m "Implement try_points function"
```

```bash
git commit -m "Fix bug in conversion validation"
```

```bash
git commit -m "Add tests for result_message"
```

### Less Helpful Examples

```bash
git commit -m "stuff"
```

```bash
git commit -m "changes"
```

```bash
git commit -m "fixed bugs"
```

Imagine that six months from now you are trying to understand what you did. Write the message for your future self.


## Push Your Work

Send your commits to GitHub:

```bash
git push
```

This creates a backup of your work and allows others to see your changes.


# The Full Cycle

A typical session might look like:

```bash
git pull

./run_tests

# Do some coding

./run_tests

git status

git add functions.py

git commit -m "Implement try_points function"

git push
```

Or, if several files were changed:

```bash
git pull

./run_tests

# Do some coding

./run_tests

git status

git add .

git commit -m "Implement rugby scoring functions"

git push
```


# Work Little and Often

The best habit you can develop is:

```text
Code
→ Test
→ Commit
→ Push
```

Repeat as often as you like.

Small commits are better than large commits.

Frequent pushes are better than infrequent pushes.

A repository with 20 small commits is usually easier to understand than a repository with one huge commit at the end.
