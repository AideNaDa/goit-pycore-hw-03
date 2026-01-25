from datetime import datetime
from datetime import timedelta
import random
import re

def get_days_from_today(data: str) -> int:
    """
    Calculates the difference in days between a specified date and the current date
    
    :param data: Days string in 'YYYY-MM-DD' format
    :return: Difference in days
    """
    try:
        user_data = datetime.strptime(data, '%Y-%m-%d').date()
        now_date = datetime.now().date() 
        return (now_date - user_data).days 

    except ValueError:
        raise ValueError(
            f"Invalid date format: {data}, expected YYYY-MM-DD"
        ) from None
    
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
    
def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone number to the required format.

    :param phone_number: Dirty phone number format
    :return: Phone number starting with "+380" and containing only digits
    """

    # remove spaces, dashes and other symbols, keep only digits and leading '+'
    clean = re.sub(r'[^\d+]', '', phone_number) 

    if clean.startswith('0'):
        correct_num = '+38' + clean
    elif clean.startswith('+'):
        correct_num = clean
    else:
        correct_num = '+' + clean

    return correct_num

def get_upcoming_birthdays(users):
    congr_date_list = []
    for user in users:
        birthday_date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        current_date = datetime.today().date()

        birthday_this_year = birthday_date.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_date.replace(year=current_date.year)
    
        difference_days = (birthday_this_year - current_date).days
        
        if 0 <= difference_days <= 7:

            congr_date = birthday_this_year

            match birthday_this_year.weekday():
                case 6:
                    congr_date += timedelta(days=1)
                case 5:
                    congr_date += timedelta(days=2)

            congr_date_list.append({
                'name': user['name'], 
                'congratulation_date': congr_date.strftime('%Y.%m.%d')
            })

    return congr_date_list


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.03"},
    {"name": "Jane ith", "birthday": "1990.02.01"},
    {"name": "John Doe", "birthday": "1985.01.31"},
    {"name": "Jane Smi", "birthday": "1990.01.27"},
    {"name": "Jane Smth", "birthday": "1990.01.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)