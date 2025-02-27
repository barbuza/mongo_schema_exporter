default: black ruff mypy pytest

pytest:
    pytest --verbose --doctest-modules *.py

mypy:
    mypy *.py

ruff:
    ruff check *.py

black:
    black *.py
