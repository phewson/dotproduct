# NumPy Dot Product Example
 
https://github.com/phewson/dotproduct/actions/workflows/ci.yml/badge.svg
 
A simple example project demonstrating:
 
- Conda environments
- pytest
- flake8
- GitHub Actions
 
## Installation
 
```bash
conda env create -f environment.yml
conda activate dotproduct
``` 

You will then need to "solve" the problem in file src/dotproduct.py. 

As you work on the problem, you can use the `run` script to check your progress.  

```bash
./run test
./run lint
./run check
```

Will run your unit tests, your linter, or both.

At intervals, you should save your changes to GitHub. You can do this with 

```bash
git add src/dotproduct.py
git commit -m 'An informative message'
git push
```

If you make a small change to the top of this file, you will get a badge if all your tests pass.
