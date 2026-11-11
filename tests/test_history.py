import pytest

from pyfakefacts.history import generate_history


def test_returns_string():
    result = generate_history("cats", "ancient")

    assert isinstance(result, str)


def test_not_empty():
    result = generate_history("cats", "medieval")

    assert len(result.strip()) > 0


def test_contains_subject():
    for era in ["ancient", "medieval", "modern"]:
        result = generate_history("cats", era)

        assert "cats" in result


def test_ancient_year_is_bc():
    result = generate_history("cats", "ancient")

    assert "BC" in result


def test_medieval_year_is_ad():
    result = generate_history("cats", "medieval")

    assert "AD" in result


def test_modern_year_has_no_label():
    result = generate_history("cats", "modern")

    assert "BC" not in result
    assert "AD" not in result


def test_era_is_case_insensitive():
    result = generate_history("cats", "ANCIENT")

    assert "BC" in result


def test_era_whitespace_is_trimmed():
    result = generate_history("cats", "  medieval \n")

    assert "AD" in result


def test_subject_whitespace_is_trimmed():
    result = generate_history("\t cats \n", "modern")

    assert "cats" in result
    assert "\t" not in result
    assert "\n" not in result
    assert "  " not in result


def test_subject_capitalization_is_preserved():
    result = generate_history("NYU Students", "modern")

    assert "NYU Students" in result


def test_subject_internal_spaces_are_preserved():
    result = generate_history("New York students", "modern")

    assert "New York students" in result


def test_unicode_subject():
    result = generate_history("café owners", "medieval")

    assert "café owners" in result


def test_invalid_subject_type():
    for subject in [None, 123, 1.5, True, [], {}]:
        with pytest.raises(TypeError, match="subject must be a string"):
            generate_history(subject, "ancient")


def test_invalid_era_type():
    for era in [None, 123, 1.5, True, [], {}]:
        with pytest.raises(TypeError, match="era must be a string"):
            generate_history("cats", era)


def test_empty_subject():
    for subject in ["", " ", "\t", "\n", " \t\n "]:
        with pytest.raises(ValueError, match="subject must not be empty"):
            generate_history(subject, "ancient")


def test_unsupported_era():
    for era in ["future", "jurassic"]:
        with pytest.raises(ValueError, match="era must be one of"):
            generate_history("cats", era)


def test_empty_era():
    for era in ["", "   ", "\n"]:
        with pytest.raises(ValueError, match="era must not be empty"):
            generate_history("cats", era)

@pytest.mark.parametrize(
    "era, bounds, endpoint, expected_year",
    [
        ("ancient", (100, 3000), 0, "100 BC"),
        ("ancient", (100, 3000), 1, "3000 BC"),
        ("medieval", (500, 1400), 0, "500 AD"),
        ("medieval", (500, 1400), 1, "1400 AD"),
        ("modern", (1600, 2000), 0, "1600"),
        ("modern", (1600, 2000), 1, "2000"),
    ],
)
def test_history_year_boundaries(monkeypatch, era, bounds, endpoint, expected_year):
    def pick_endpoint(low, high):
        assert (low, high) == bounds
        return (low, high)[endpoint]

    monkeypatch.setattr("pyfakefacts.history.random.randint", pick_endpoint)

    result = generate_history("cats", era)
    assert result.startswith(f"In {expected_year}, ")