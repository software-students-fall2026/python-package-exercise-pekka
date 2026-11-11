# PyFakeFacts

[![Test and Build PyFakeFacts](https://github.com/software-students-fall2026/python-package-exercise-pekka/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2026/python-package-exercise-pekka/actions/workflows/python-package.yml)

PyFakeFacts provides a collection of generators for creating fictional trivia, historical events, statistics, and scientific discoveries. 

## Features

PyFakeFacts includes four generators:

- **Fake Facts:** Generate fictional facts about any topic.
- **Fake History:** Create imaginary historical events across different eras.
- **Fake Statistics:** Produce fake numerical claims and statistics.
- **Fake Discoveries:** Generate fictional scientific discoveries with adjustable absurdity levels.

## Available Functions

### 1. `generate_fact(topic, category)`

Generates a fictional fact based on a specified topic and category.

```python
from pyfakefacts import generate_fact

print(generate_fact("cats", "animals"))
```

### 2. `generate_history(subject, era)`

Generates a fictional historical event involving a subject and a historical era.

Supported eras: `ancient`, `medieval`, and `modern`.

```python
from pyfakefacts import generate_history

print(generate_history("penguins", "medieval"))
```

### 3. `generate_statistic(topic, category)`

Generates a fictional statistic using a topic and category.

```python
from pyfakefacts import generate_statistic

print(generate_statistic("students", "technology"))
```

### 4. `generate_discovery(field, absurdity)`

Generates a fictional scientific discovery based on a scientific field and an absurdity level.

Supported fields: `physics`, `biology`, and `astronomy`.

The `absurdity` parameter accepts an integer from **1 to 10**, where higher values produce increasingly ridiculous discoveries.

```python
from pyfakefacts import generate_discovery

print(generate_discovery("physics", 8))
```

All functions return strings and validate their input arguments.

## Installation

PyFakeFacts requires Python 3.10 or later.

The package will be available through PyPI once published.

**PyPI:** Coming soon.

## Development Setup

Clone the team repository:

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-pekka.git
cd python-package-exercise-pekka
```

Install the development dependencies using Pipenv:

```bash
pipenv sync --dev
```

Install the package in editable mode:

```bash
pipenv run python -m pip install -e .
```

No additional environment variables, external APIs, or databases are required.

## Running Tests

PyFakeFacts uses `pytest` for automated testing.

Run the complete test suite:

```bash
pipenv run pytest -v
```

GitHub Actions automatically runs the tests and builds the package on Python 3.12 and 3.13 for pull requests targeting `main` or `master`.

The workflow status badge at the top of this README displays the latest workflow status for the default branch.

## Building the Package

Build the source distribution and wheel:

```bash
pipenv run python -m build
```

The generated package distributions are saved in the `dist/` directory.

Validate the distributions using Twine:

```bash
pipenv run twine check dist/*
```

## Example Program

*Coming soon.*

An example Python program demonstrating all four generators will be added to the `examples/` directory.

This section will include instructions for running `examples/demo.py` once implemented.
