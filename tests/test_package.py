import pyfakefacts


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


def test_every_function_returns_a_string():
    assert isinstance(pyfakefacts.generate_fact("cats", "animals"), str)
    assert isinstance(pyfakefacts.generate_history("cats", "modern"), str)
    assert isinstance(pyfakefacts.generate_statistic("cats", "pizza"), str)
    assert isinstance(pyfakefacts.generate_discovery("physics", 5), str)
