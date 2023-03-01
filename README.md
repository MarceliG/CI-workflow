# Starter testing can implement in any project

<p>
  <a href="https://github.com/MarceliG/CI-workflow/actions"><img alt="Actions Status" src="https://github.com/psf/black/workflows/Test/badge.svg"></a>
  <a href="https://github.com/MarceliG/CI-workflow/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
</p>

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

Tools that can be used:
- [conda](https://docs.conda.io/en/latest/)
- [virtualenv](https://github.com/pyenv/pyenv)
- [venv](https://docs.python.org/3/library/venv.html)

Create virtual enviroment [Recommended latest version Python]:
```
python3.11 -m venv .venv
```
Activate enviroment:
```
source .venv/bin/activate
```

## Installation packages
When you have virtual enviroment and all files from this repositories in your work directory you can install recommended libraries:
```
pip install -r requirements.txt
```
And check that everything is in order. Do this steps:
1. ```pip install -e .``` - Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path
2. ```black src tests```
3. ```isort src tests```
4. ```flake8 src tests```
5. ```mypy src tests```
6. ```pytest```
7. ```tox``` - to create same virtual environments that are used by CI.






### Additional informations
First commit will spend long time (about 1min). If you don't have failed tests you can push your commit, if not changes your files and try again.

## Use `tox` to create same virtual environments that are used by CI.

