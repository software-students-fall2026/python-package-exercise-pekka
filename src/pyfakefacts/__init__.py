"""PyFakeFacts, a package that generates fake facts"""

from .discoveries import generate_discovery
from .facts import generate_fact
from .history import generate_history
from .statistic import generate_statistic

__all__ = [
    "generate_discovery",
    "generate_fact",
    "generate_history",
    "generate_statistic",
]
