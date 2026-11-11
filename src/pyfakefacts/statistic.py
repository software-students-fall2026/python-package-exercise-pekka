"""Generate fictional statistics."""

import random

from ._validation import require_text


_STATISTIC_TEMPLATES = (
    "{percentage}% of {topic} believe {category} is secretly controlled by pigeons.",
    "{percentage}% of {topic} use {category} to communicate with aliens.",
    "{percentage}% of {topic} are convinced {category} was invented by time-traveling hamsters.",
    "{percentage}% of {topic} claim {category} works better when nobody is watching.",
    "A highly questionable survey found that {percentage}% of {topic} think {category} is a government conspiracy.",
)


def generate_statistic(topic: str, category: str) -> str:
    """Generate an obviously fictional statistic about a topic and category.

    Args:
        topic: Nonempty text naming the group, written as a plural noun
            (for example "students") so the sentence reads correctly.
        category: Nonempty text naming the thing the statistic is about.

    Returns:
        A fictional statistic with a random percentage from 1 to 99.
        Surrounding input whitespace is removed. Internal whitespace and
        capitalization are preserved.

    Raises:
        TypeError: If either argument is not a string.
        ValueError: If either argument is empty after trimming.
    """
    topic = require_text(topic, "topic")
    category = require_text(category, "category")

    template = random.choice(_STATISTIC_TEMPLATES)
    return template.format(
        percentage=random.randint(1, 99),
        topic=topic,
        category=category,
    )
