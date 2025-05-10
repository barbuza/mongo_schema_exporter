set export
PATH := ".venv/bin:" + env_var("PATH")

default: black ruff mypy pytest

pytest:
    pytest --verbose --doctest-modules *.py mongo_schema_exporter/*.py

mypy:
    mypy *.py mongo_schema_exporter/*.py

ruff:
    ruff check *.py mongo_schema_exporter/*.py

black:
    black *.py mongo_schema_exporter/*.py

