# Chemical Lab Inspector

Chemical Lab Inspector is a small Python project that explores a laboratory directory and reports:

- the number of files and directories
- the total size of the files
- the file extensions found
- basic system information

It uses only Python's standard library, including `os`, `pathlib`, and `collections.Counter`.

## Run it

Use Python 3.10 or newer from the project directory:

```bash
python3 main.py
```

The program inspects the `chemical_project/` directory. Add files to that directory to see the report change.

## Run the tests

The test suite uses Python's built-in `unittest` runner:

```bash
python3 -m unittest discover -s tests -v
```

## Project layout

```text
main.py                 # Directory inspector
tests/test_main.py      # Tests for the inspection logic
chemical_project/       # Directory being inspected
study.ipynb             # Standard-library filesystem experiments
```

This project is intended as a learning exercise in filesystem operations and simple data aggregation.