"""Small utilities for strings and temperature conversion."""


def reverse_string(text):
    """Return ``text`` with its characters in reverse order."""
    return text[::-1]


def count_words(sentence):
    """Return the number of whitespace-separated words in ``sentence``."""
    return len(sentence.split())


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32
