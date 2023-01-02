# CI-workflow

If you want have only CI-workflow without pre-commit copy only directory `.github/workflows`

# Setup

pip install -r requirements.txt

Add file `.pre-commit-config.yaml` to the main directory and write in terminal:

pre-commit install

# Additional informations

First commit will spend long time (about 1min). If you don't have failed tests you can push your commit, if not changes your files and try again.
