import pytest
from pyfakefacts.discoveries import DISCOVERIES, generate_discovery

def test_valid_discovery():
    result = generate_discovery("physics", 5)

    assert isinstance(result, str)
    assert len(result.strip()) > 0


def test_valid_absurdity_boundaries():
    assert isinstance(generate_discovery("biology", 1), str)
    assert isinstance(generate_discovery("biology", 10), str)


def test_invalid_field():
    with pytest.raises(ValueError):
        generate_discovery("magic", 5)


def test_invalid_absurdity():
    with pytest.raises(ValueError):
        generate_discovery("physics", 11)

    with pytest.raises(ValueError):
        generate_discovery("physics", 0)


def test_invalid_field_type():
    for field in [None, 123, 1.5, True, [], {}]:
        with pytest.raises(TypeError, match="field must be a string"):
            generate_discovery(field, 5)


def test_blank_field():
    for field in ["", " ", "\t", "\n"]:
        with pytest.raises(ValueError, match="field must not be empty"):
            generate_discovery(field, 5)


def test_field_is_case_insensitive_and_trimmed():
    assert isinstance(generate_discovery("  PHYSICS \n", 5), str)


def test_invalid_absurdity_type():
    for absurdity in ["5", 5.5, None, True, False, []]:
        with pytest.raises(TypeError, match="Absurdity must be an integer"):
            generate_discovery("physics", absurdity)


def test_absurdity_levels_use_different_phrases():
    low = DISCOVERIES["physics"]["low"]
    medium = DISCOVERIES["physics"]["medium"]
    high = DISCOVERIES["physics"]["high"]

    for absurdity, phrases in [(1, low), (3, low), (4, medium), (7, medium), (8, high), (10, high)]:
        result = generate_discovery("physics", absurdity)

        assert any(phrase in result for phrase in phrases)
