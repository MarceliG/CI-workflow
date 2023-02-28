# CI-workflow

If you want have only CI-workflow without pre-commit copy only directory `.github/workflows`

## How to setup projekt
Create virtualenv 
```sh python3.11 -m venv .venv```
```sh source .venv/bin/activate```
Check version of python 
```sh python --version```

## Installation package

```sh
pip install black
pip install flake8
pip install tox 
pip install pre-commit
```

# Setup
```sh
pip install -r requirements.txt
```

Add file `.pre-commit-config.yaml` to the main directory and write in terminal:

### Additional informations
First commit will spend long time (about 1min). If you don't have failed tests you can push your commit, if not changes your files and try again.

## Use `tox` to create same virtual environments that are used by CI.

## Instructions from video 
1. prepare all file 
2. ```pip install -e .```
3. ```pip install -r requirements_dev.txt ```
4. ```mypy src```
5. ```black src```
6. ```flake8 src```
7. ```pytest```
8. ```tox```
