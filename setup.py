from setuptools import find_packages, setup

requirements = {
    "install": [
        "pre-commit >=2.21.0",
        "isort >= 5.12.0",
        "flake8 >= 4.0.1",
        "tox >= 4.4.6",
    ],
    "ut": [
        "pytest >= 6.2.5, < 7.0.0",
    ],
    "style": [
        "black >= 22.12.0",
    ],
}

setup(
    name="YourNameOfProject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements["install"],
    extras_require={
        "ut": requirements["ut"],
        "style": requirements["style"],
    },
)