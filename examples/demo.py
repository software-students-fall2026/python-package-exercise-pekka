"""Example program that uses every function in PyFakeFacts.

Run it from the repository root after installing the package:

    pipenv run python examples/demo.py
"""

from pyfakefacts import (
    generate_discovery,
    generate_fact,
    generate_history,
    generate_statistic,
)


def main():
    print("=== generate_fact(topic, category) ===")
    print(generate_fact("cats", "animals"))
    print(generate_fact("NYU students", "campus life"))

    print()
    print("=== generate_history(subject, era) ===")
    for era in ["ancient", "medieval", "modern"]:
        print(f"{era}: {generate_history('pigeons', era)}")

    print()
    print("=== generate_statistic(topic, category) ===")
    print(generate_statistic("developers", "coffee"))
    print(generate_statistic("cats", "the internet"))

    print()
    print("=== generate_discovery(field, absurdity) ===")
    for field in ["physics", "biology", "astronomy"]:
        print(f"{field} (absurdity 1): {generate_discovery(field, 1)}")
        print(f"{field} (absurdity 10): {generate_discovery(field, 10)}")

    print()
    print("=== Invalid input ===")
    try:
        generate_history("cats", "future")
    except ValueError as error:
        print(f"ValueError: {error}")


if __name__ == "__main__":
    main()
