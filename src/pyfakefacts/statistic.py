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
    """Generate an obviously fictional statistic about a topic and category."""
    topic = require_text(topic, "topic")
    category = require_text(category, "category")

    template = random.choice(_STATISTIC_TEMPLATES)
    return template.format(
        percentage=random.randint(1, 99),
        topic=topic,
        category=category,
    )
