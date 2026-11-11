
"""Generate fictional facts."""

import random

from ._validation import require_text


_FACT_TEMPLATES = {
    "animals": (
        "Wildlife researchers claim that {topic} secretly organize wildlife elections.",
        "Zoologists believe that {topic} can translate bird songs.",
        "A fictional wildlife study found that {topic} teach squirrels accounting.",
        "According to wildlife experts, {topic} negotiate treaties with penguins.",
        "A questionable zoology report claims that {topic} invented migration.",
    ),
    "technology": (
        "Computer scientists claim that {topic} power computers using potato energy.",
        "Technology experts believe that {topic} invented wireless toast.",
        "A fictional engineering study found that {topic} communicate through printers.",
        "According to software engineers, {topic} store passwords inside microwaves.",
        "A questionable tech report claims that {topic} taught robots sarcasm.",
    ),
    "food": (
        "Food researchers claim that {topic} discovered a new flavor called Tuesday.",
        "Culinary experts believe that {topic} invented edible alarm clocks.",
        "A fictional culinary study found that {topic} season soup with moonlight.",
        "According to chefs, {topic} use spaghetti to predict rain.",
        "A questionable food report claims that {topic} grow pizza underground.",
    ),
    "space": (
        "Astronomers claim that {topic} secretly control the moon's thermostat.",
        "Space researchers believe that {topic} run a hotel on Saturn.",
        "A fictional astronomy study found that {topic} deliver mail using comets.",
        "According to astronomers, {topic} invented zero-gravity bowling.",
        "A questionable space report claims that {topic} charge rent to aliens.",
    ),
    "general": (
        "Some researchers claim that {topic} secretly control the weather.",
        "Experts believe that {topic} invented the weekend.",
        "A fictional study found that {topic} can communicate with aliens.",
        "According to researchers, {topic} can smell tomorrow's headlines.",
        "A questionable report claims that {topic} invented invisible hats.",
    ),
}


def generate_fact(topic: str, category: str) -> str:
    """Generate a fictional fact for a topic and category.

    Args:
        topic: Nonempty text describing the subject, preferably a plural
            noun (for example, "cats") for grammatical output.
        category: One of animals, technology, food, space, or general.
            Case-insensitive.

    Returns:
        A randomly selected fictional fact as a string.

    Raises:
        TypeError: If either argument is not a string.
        ValueError: If either argument is empty after trimming or if
            the category is unsupported.
    """
    topic = require_text(topic, "topic")
    category = require_text(category, "category").lower()

    if category not in _FACT_TEMPLATES:
        supported = ", ".join(sorted(_FACT_TEMPLATES))
        raise ValueError(
            f"unsupported category: {category}. Choose from: {supported}"
        )

    template = random.choice(_FACT_TEMPLATES[category])

    return template.format(topic=topic)
