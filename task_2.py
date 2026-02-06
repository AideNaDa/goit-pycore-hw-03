import random


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers in the given range.

    :param min_value: Minimum value of the range (must be >= 1)
    :param max_value: Maximum value of the range (must be <= 1000)
    :param quantity: Number of unique random values to generate
    :return: Sorted list of unique random integers or an empty list if input is invalid
    """
    if not (1 <= min_value <= max_value <= 1000):
        return []

    if not (0 < quantity <= (max_value - min_value + 1)):
        return []

    try:
        numbers = random.sample(range(min_value, max_value + 1), quantity)
    except ValueError:
        return []

    return sorted(numbers)
