
import pytest

import pyfakefacts
from pyfakefacts import (
    generate_discovery,
    generate_fact,
    generate_history,
    generate_statistic,
)


EXPECTED_FUNCTIONS = [
    "generate_discovery",
    "generate_fact",
    "generate_history",
    "generate_statistic",
]


def test_package_import():
    assert pyfakefacts is not None


def test_all_lists_every_function():
    assert sorted(pyfakefacts.__all__) == EXPECTED_FUNCTIONS


def test_every_function_is_exported_and_callable():
    for name in EXPECTED_FUNCTIONS:
        assert callable(getattr(pyfakefacts, name))


@pytest.mark.parametrize(
    "generator, args, expected_text",
    [
        (generate_fact, ("cats", "animals"), "cats"),
        (generate_history, ("penguins", "medieval"), "penguins"),
        (generate_statistic, ("students", "campus life"), "students"),
        (generate_discovery, ("physics", 8), "Scientists discovered that"),
    ],
)
def test_public_generator(generator, args, expected_text):
    assert expected_text in generator(*args)
