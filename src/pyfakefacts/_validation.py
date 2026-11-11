"""Input validation shared by the generator functions."""


def require_text(value: str, name: str) -> str:
    """Check that a value is a nonblank string and trim it.

    Args:
        value: The argument to check.
        name: The argument's name, used in the error messages.

    Returns:
        The value with surrounding whitespace removed. Internal whitespace
        and capitalization are preserved.

    Raises:
        TypeError: If value is not a string.
        ValueError: If value is empty after trimming.
    """
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")

    value = value.strip()

    if not value:
        raise ValueError(f"{name} must not be empty or whitespace-only")

    return value
