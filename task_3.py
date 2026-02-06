import re


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


if __name__ == '__main__':
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
