
import pytest

from pyfakefacts.facts import _FACT_TEMPLATES, generate_fact


def test_generate_fact_returns_string():
    result = generate_fact("cats", "animals")

    assert isinstance(result, str)


def test_generate_fact_is_not_empty():
    result = generate_fact("cats", "animals")

    assert len(result.strip()) > 0


def test_generate_fact_contains_inputs():
    result = generate_fact("cats", "animals")

    assert "cats" in result
    assert result in [
        template.format(topic="cats")
        for template in _FACT_TEMPLATES["animals"]
    ]


@pytest.mark.parametrize(
    "topic",
    [None, 123, 1.5, True, [], {}],
)
def test_invalid_topic_type(topic):
    with pytest.raises(TypeError, match="topic must be a string"):
        generate_fact(topic, "animals")


@pytest.mark.parametrize(
    "category",
    [None, 123, 1.5, True, [], {}],
)
def test_invalid_category_type(category):
    with pytest.raises(TypeError, match="category must be a string"):
        generate_fact("cats", category)


@pytest.mark.parametrize(
    "topic",
    ["", " ", "   ", "\t", "\n", " \t\n "],
)
def test_empty_topic(topic):
    with pytest.raises(ValueError, match="topic must not be empty"):
        generate_fact(topic, "animals")


@pytest.mark.parametrize(
    "category",
    ["", " ", "   ", "\t", "\n", " \t\n "],
)
def test_empty_category(category):
    with pytest.raises(ValueError, match="category must not be empty"):
        generate_fact("cats", category)


def test_topic_whitespace_is_trimmed():
    result = generate_fact("\t cats \n", "animals")

    assert "cats" in result
    assert "\t" not in result
    assert "\n" not in result
    assert "  " not in result


def test_category_whitespace_is_trimmed():
    result = generate_fact("cats", "\t animals \n")

    assert result in [
        template.format(topic="cats")
        for template in _FACT_TEMPLATES["animals"]
    ]
    assert "\t" not in result
    assert "\n" not in result
    assert "  " not in result


@pytest.mark.parametrize(
    "topic",
    ["New York students", "NYU Students", "café owners 文化"],
)
def test_topic_text_is_preserved(topic):
    assert topic in generate_fact(topic, "general")


@pytest.mark.parametrize(
    "category",
    ["animals", "technology", "food", "space", "general"],
)
def test_supported_categories(category):
    result = generate_fact("cats", category)

    assert "cats" in result
    assert result in [
        template.format(topic="cats")
        for template in _FACT_TEMPLATES[category]
    ]


def test_unsupported_category():
    with pytest.raises(ValueError, match="unsupported category"):
        generate_fact("cats", "magic")


def test_category_selects_matching_templates(monkeypatch):
    monkeypatch.setattr(
        "pyfakefacts.facts.random.choice",
        lambda templates: templates[0],
    )

    assert generate_fact("cats", " ANIMALS ") == (
        "Wildlife researchers claim that cats secretly organize wildlife elections."
    )
    assert generate_fact("cats", "space") == (
        "Astronomers claim that cats secretly control the moon's thermostat."
    )


def test_fact_templates_avoid_awkward_category_wording():
    awkward_phrases = (
        "animals experts",
        "animals research",
        "general experts",
        "general research",
    )

    for category, templates in _FACT_TEMPLATES.items():
        for template in templates:
            result = template.format(topic="cats")

            assert "cats" in result
            assert not any(
                phrase in result.lower()
                for phrase in awkward_phrases
            ), f"Awkward wording in category {category}: {result}"
