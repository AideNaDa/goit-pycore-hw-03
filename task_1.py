from datetime import datetime


def get_days_from_today(data_str: str) -> int:
    """
    Calculates the difference in days between a specified date and the current date

    :param data: Days string in 'YYYY-MM-DD' format
    :return: Difference in days
    """
    try:
        user_data = datetime.strptime(data_str, '%Y-%m-%d').date()
        now_date = datetime.now().date() 
        return (now_date - user_data).days 
    except ValueError:
        raise ValueError(
            f"Invalid date format: {data_str}, expected YYYY-MM-DD"
        ) from None


if __name__ = '__main__':
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2027-10-09"))
