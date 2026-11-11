# PyFakeFacts

A lightweight Python package that generates fictional facts.

## Features

PyFakeFacts will support:

- Fictional fact generation
- Fake historical events
- Absurd statistics
- Imaginary scientific discoveries

## Development Setup

Clone the repository and install dependencies:

    pipenv sync --dev

## Run the Example

[`examples/demo.py`](examples/demo.py) calls all four functions with different
arguments and ends with an example of invalid input. From the repository root:

    pipenv run python examples/demo.py

The output is random, so yours will differ. It looks like this:

    === generate_fact(topic, category) ===
    Researchers in biology claim that cats invented the weekend.
    ...
    === Invalid input ===
    ValueError: era must be one of: ancient, medieval, modern

## Run Tests

    pipenv run pytest -v

## Build Package

    pipenv run python -m build

