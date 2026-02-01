import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers in the given range.
    
    :param min: Minimum value of the range (must be >= 1)
    :param max: Maximum value of the range (must be <= 1000)
    :param quantity: Number of unique random values to generate
    :return: Sorted list of unique random integers or an empty list if input is invalid
    """
    if not (1 <= min <= max <= 1000) or not (0 < quantity <= (max - min + 1)):
        return []
    
    try:
        numbers = random.sample(range(min, max + 1), quantity)
    except ValueError:
        return []
    
    return sorted(numbers)