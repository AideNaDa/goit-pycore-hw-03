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
