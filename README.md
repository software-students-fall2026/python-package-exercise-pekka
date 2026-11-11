# PyFakeFacts

[![Test and Build PyFakeFacts](https://github.com/software-students-fall2026/python-package-exercise-pekka/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2026/python-package-exercise-pekka/actions/workflows/python-package.yml)

PyFakeFacts provides a collection of generators for creating fictional trivia, historical events, statistics, and scientific discoveries.

It's a just-for-fun package for developers who want silly, obviously fake text, like for demos, test data, or fun. Each function takes a couple of inputs and gives you back one made-up sentence.

## Features

PyFakeFacts includes four generators:

- **Fake Facts:** Generate fictional facts about any topic.
- **Fake History:** Create imaginary historical events across different eras.
- **Fake Statistics:** Produce fake numerical claims and statistics.
- **Fake Discoveries:** Generate fictional scientific discoveries with adjustable absurdity levels.

## Installation

PyFakeFacts is available on PyPI and requires Python 3.10 or later. It has no runtime dependencies.

Install the published package with pip:

```bash
pip install pyfakefacts
```

See [PyFakeFacts on PyPI](https://pypi.org/project/pyfakefacts/).

To install the package from a local checkout for development, follow the [Development Setup](#development-setup) instructions below.

## Using PyFakeFacts

All four functions are importable from `pyfakefacts`. Each returns a string; generated text is selected randomly, so exact output varies.

### Quick start

```python
from pyfakefacts import (
    generate_discovery,
    generate_fact,
    generate_history,
    generate_statistic,
)

print(generate_fact("cats", "animals"))
print(generate_history("penguins", "medieval"))
print(generate_statistic("students", "campus life"))
print(generate_discovery("physics", 8))
```

### `generate_fact(topic, category)`

Generates a fictional fact about a topic.

- `topic`: A nonempty string, best written as a plural noun such as `"cats"` so the sentence reads correctly. Leading and trailing whitespace is removed; internal whitespace and capitalization are preserved.
- `category`: A nonempty string. Leading and trailing whitespace is removed and the value is converted to lowercase. Supported categories are `animals`, `technology`, `food`, `space`, and `general`.
- **Returns:** A fictional fact string, randomly selected from five templates for the category.
- **Errors:** Raises `TypeError` if either argument is not a string. Raises `ValueError` if either value is blank after trimming or if the category is unsupported.

```python
from pyfakefacts import generate_fact

fact = generate_fact("cats", "animals")
print(fact)
```

### `generate_history(subject, era)`

Generates a fictional historical event about a subject and an era.

- `subject`: A nonempty string, best written as a plural noun such as `"pigeons"` so the sentence reads correctly. Leading and trailing whitespace is removed; internal whitespace and capitalization are preserved.
- `era`: A nonempty string. Leading and trailing whitespace is removed and the value is converted to lowercase. Supported eras are `ancient`, `medieval`, and `modern`.
- **Returns:** A fictional historical-event string with a randomly selected year and template. Ancient years are labeled `BC` (100–3000 BC); medieval years are labeled `AD` (500–1400 AD); modern years have no era suffix (1600–2000).
- **Errors:** Raises `TypeError` if either argument is not a string. Raises `ValueError` if the subject is blank after trimming or the era is unsupported.

```python
from pyfakefacts import generate_history

event = generate_history("penguins", "medieval")
print(event)
```

### `generate_statistic(topic, category)`

Generates an obviously fictional statistic about a topic and category.

- `topic`: A nonempty string, best written as a plural noun such as `"students"` so the sentence reads correctly. Leading and trailing whitespace is removed; internal whitespace and capitalization are preserved.
- `category`: A nonempty string. Leading and trailing whitespace is removed; internal whitespace and capitalization are preserved. Any nonblank string is accepted; there is no category allowlist.
- **Returns:** A fictional statistic string with a randomly selected template and a random percentage from 1 through 99.
- **Errors:** Raises `TypeError` if either argument is not a string. Raises `ValueError` if either value is blank after trimming.

```python
from pyfakefacts import generate_statistic

statistic = generate_statistic("students", "campus life")
print(statistic)
```

### `generate_discovery(field, absurdity)`

Generates a fictional scientific discovery.

- `field`: A string. Leading and trailing whitespace is removed and the value is converted to lowercase. Supported fields are `physics`, `biology`, and `astronomy`.
- `absurdity`: A built-in integer from 1 through 10. Values 1–3 use low-absurdity behaviors, 4–7 use medium behaviors, and 8–10 use high behaviors. Booleans are not accepted as integers.
- **Returns:** A fictional scientific-discovery string with a randomly selected subject and behavior for the field and absurdity level.
- **Errors:** Raises `TypeError` if `field` is not a string or `absurdity` is not a built-in integer. Raises `ValueError` if the field is unsupported or the integer is outside 1–10.

```python
from pyfakefacts import generate_discovery

discovery = generate_discovery("physics", 8)
print(discovery)
```

### Example program

[`examples/demo.py`](examples/demo.py) imports and calls all four generators, tries each supported history era, discovery field, and the low/high absurdity bounds, and demonstrates an invalid era.

After completing the development setup, run it from the repository root:

```bash
pipenv run python examples/demo.py
```

The output is random, so yours will differ.

## Development Setup

PyFakeFacts doesn't need any environment variables, database, starter data, outside APIs, or secret config files (like a `.env` file).

Clone the team repository and enter its directory:

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-pekka.git
cd python-package-exercise-pekka
```

Install Pipenv if it is not already installed:

```bash
python -m pip install pipenv
```

If you get "command not found" for `python`, try `python3 -m pip install pipenv` instead.

Create/synchronize the Pipenv environment and install development dependencies:

```bash
pipenv sync --dev
```

The root `Pipfile` includes the local package in editable mode. To explicitly install or refresh that local editable installation:

```bash
pipenv run python -m pip install -e .
```

## Running Tests

PyFakeFacts uses `pytest` for automated testing. Run the complete test suite from the repository root:

```bash
pipenv run pytest -v
```

GitHub Actions runs tests and builds the package on Python 3.12 and 3.13 for pull requests targeting `main` or `master`. The status badge at the top of this README links to that workflow.

## Building the Package

Build the source distribution and wheel:

```bash
pipenv run python -m build
```

The generated distributions are saved in `dist/`. Validate them with Twine:

```bash
pipenv run twine check dist/*
```

## Verifying a Published Release

After a new version is published to PyPI, check the available versions:

```bash
python3 -m pip index versions pyfakefacts
```

Install or upgrade to the latest published version:

```bash
python3 -m pip install --upgrade pyfakefacts
```

Confirm the installed version:

```bash
python3 -m pip show pyfakefacts
```

## Troubleshooting

### Python can't find `pyfakefacts`

If you get `ModuleNotFoundError` while working from a local clone, run this from the repository root:

```bash
pipenv run python -m pip install -e .
```

Then run your script with `pipenv run python` so it uses the same environment.

### `generate_fact()` rejects my category

`generate_fact()` accepts `animals`, `technology`, `food`, `space`, and `general`.
For example, use `generate_fact("cats", "animals")`. To use `biology`,
call `generate_discovery("biology", 5)`.

### Python can't find `examples/demo.py`

The demo doesn't come with `pip install pyfakefacts`, it's only in the GitHub repo.
Clone the repo, open a terminal in the `python-package-exercise-pekka` folder,
and run:

```bash
pipenv run python examples/demo.py
```

## Contributors

- [Alissa Wu](https://github.com/alissawu)
- [Pope Cruz](https://github.com/pope-cruz)
- [Khidir Ahmed](https://github.com/khidirahmed)
- [Adil Inayat](https://github.com/ai2652-png)
