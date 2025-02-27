set export
PATH := ".venv/bin:" + env_var("PATH")

default: black ruff mypy pytest

pytest:
    pytest --verbose --doctest-modules *.py

mypy:
    mypy *.py

ruff:
    ruff check *.py

black:
    black *.py
