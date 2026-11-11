"""Generate fictional facts."""

import random


_FACT_TEMPLATES = {
    "animals": (
        "In {category} research, {topic} secretly organize wildlife elections.",
        "Experts in {category} claim that {topic} can translate bird songs.",
        "A fictional {category} study found that {topic} teach squirrels accounting.",
        "According to {category} experts, {topic} negotiate treaties with penguins.",
        "A questionable {category} report claims that {topic} invented migration.",
    ),
    "technology": (
        "In {category} research, {topic} power computers using potato energy.",
        "Experts in {category} claim that {topic} invented wireless toast.",
        "A fictional {category} study found that {topic} communicate through printers.",
        "According to {category} experts, {topic} store passwords inside microwaves.",
        "A questionable {category} report claims that {topic} taught robots sarcasm.",
    ),
    "food": (
        "In {category} research, {topic} discovered a new flavor called Tuesday.",
        "Experts in {category} claim that {topic} invented edible alarm clocks.",
        "A fictional {category} study found that {topic} season soup with moonlight.",
        "According to {category} experts, {topic} use spaghetti to predict rain.",
        "A questionable {category} report claims that {topic} grow pizza underground.",
    ),
    "space": (
        "In {category} research, {topic} secretly control the moon's thermostat.",
        "Experts in {category} claim that {topic} run a hotel on Saturn.",
        "A fictional {category} study found that {topic} deliver mail using comets.",
        "According to {category} experts, {topic} invented zero-gravity bowling.",
        "A questionable {category} report claims that {topic} charge rent to aliens.",
    ),
    "general": (
        "In {category} research, {topic} secretly control the weather.",
        "Experts in {category} claim that {topic} invented the weekend.",
        "A fictional {category} study found that {topic} can communicate with aliens.",
        "According to {category} experts, {topic} can smell tomorrow's headlines.",
        "A questionable {category} report claims that {topic} invented invisible hats.",
    ),
}


def generate_fact(topic: str, category: str) -> str:
    """Generate a fictional fact containing a topic and category.

    Args:
        topic: Nonempty text describing the subject.
        category: One of animals, technology, food, space, or general. Case-insensitive.

    Returns:
        A fictional fact with surrounding input whitespace removed.
        Internal whitespace and capitalization are preserved.

    Raises:
        TypeError: If either argument is not a string.
        ValueError: If either argument is empty after trimming.
    """
    if not isinstance(topic, str):
        raise TypeError("topic must be a string")

    if not isinstance(category, str):
        raise TypeError("category must be a string")

    topic = topic.strip()
    category = category.strip().lower

    if not topic:
        raise ValueError("topic must not be empty or whitespace-only")

    if not category:
        raise ValueError("category must not be empty or whitespace-only")

    if category not in _FACT_TEMPLATES:
        supported = ", ".join(sorted(_FACT_TEMPLATES))
    raise ValueError(
        f"unsupported category: {category}. Choose from: {supported}"
    )

    template = random.choice(_FACT_TEMPLATES[category])

    return template.format(
        topic=topic,
        category=category,
    )