import pytest

from pyfakefacts._validation import require_text


def test_returns_string():
    assert isinstance(require_text("cats", "topic"), str)


def test_whitespace_is_trimmed():
    assert require_text("\t cats \n", "topic") == "cats"


def test_internal_spaces_and_capitalization_are_preserved():
    assert require_text("  New York Students ", "topic") == "New York Students"


def test_invalid_type():
    for value in [None, 123, 1.5, True, [], {}]:
        with pytest.raises(TypeError, match="topic must be a string"):
            require_text(value, "topic")


def test_empty_text():
    for value in ["", " ", "\t", "\n", " \t\n "]:
        with pytest.raises(ValueError, match="topic must not be empty"):
            require_text(value, "topic")


def test_name_is_used_in_error_messages():
    with pytest.raises(TypeError, match="era must be a string"):
        require_text(5, "era")

    with pytest.raises(ValueError, match="era must not be empty"):
        require_text("", "era")
