<p align="left">
<a href="https://github.com/MarceliG/CI-workflow/actions"><img alt="Actions Status" src="https://github.com/psf/black/workflows/Test/badge.svg"></a>
<a href="https://github.com/MarceliG/CI-workflow/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
</p>

# Introduction to the project

A project to show how to set up and use automated testing in Python. 

In this project the code is verified by:
- [Black](https://black.readthedocs.io/en/stable/) - The uncompromising code formatter.
- [Isort](https://pycqa.github.io/isort/) - Sorting the imports alphabetically.
- [Flake8](https://flake8.pycqa.org/en/latest/) - Tool For Style Guide Enforcement.
- [Mypy](https://mypy.readthedocs.io/en/stable/) - A static type checker for Python.
- [Pytest](https://docs.pytest.org/en/7.1.x/contents.html) - Is a Python testing framework

# Installation and usage

## Create virtual environment [optional but recommended].

When you start a new project and want to use a different version eg. Python or any libraries you can create a virtual environment. 

1. Chose your favorite virtual enviroment. 
    
    You can use:
    - [conda](https://docs.conda.io/en/latest/)
    - [pyenv](https://github.com/pyenv/pyenv)
    - [venv](https://docs.python.org/3/library/venv.html)

2. Create virtualenv.
    
    Example with `venv`:
    
    ```python3.11 -m venv .venv```
    
    Activate enviroment:
    
    ```source .venv/bin/activate```


## Installation packages

When you have virtual enviroment and all files from this repositories in your work directory you can install recommended libraries:
```
pip install -r requirements.txt
```

## Initial launch

1. Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path

```
pip install -e .
``` 

2. Run libraries

```
black src tests
isort src tests
flake8 src tests
mypy src tests
```

3. Run python tests

```
pytest
```

4. Run tox

```
tox
```


## What is tox

Tox is a generic virtual environment management and test command line tool you can use for:
 - checking your package builds and installs correctly under different environments (such as different Python implementations, versions or installation dependencies),
 - running your tests in each of the environments with the test tool of choice,
 - acting as a frontend to continuous integration servers, greatly reducing boilerplate and merging CI and shell-based testing.
 
 ### Proposal to use tox
 
If you make changes to your code and want to push it out to a remote repository use tox and make sure you've written your code great.
 

