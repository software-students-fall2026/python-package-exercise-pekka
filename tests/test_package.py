import pytest

from pyfakefacts import (
    generate_discovery,
    generate_fact,
    generate_history,
    generate_statistic,
)


@pytest.mark.parametrize(
    "generator, args, expected_text",
    [
        (generate_fact, ("cats", "animals"), "cats"),
        (generate_history, ("penguins", "medieval"), "penguins"),
        (generate_statistic, ("students", "campus life"), "students"),
        (generate_discovery, ("physics", 8), "Fictional discovery:"),
    ],
)
def test_public_generator(generator, args, expected_text):
    assert expected_text in generator(*args)