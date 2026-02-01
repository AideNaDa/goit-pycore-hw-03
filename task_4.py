from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Finds birthdays within 7 days and carries over congratulations from weeks
    """
    current_date = datetime.today().date()
    congr_date_list = []

    for user in users:
        # convert srting to object date
        birthday_date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday_date.replace(year=current_date.year)

        # if birthday has already passed this year try next year
        if birthday_this_year < current_date:
            birthday_this_year = birthday_date.replace(year=current_date.year + 1)
    
        difference_days = (birthday_this_year - current_date).days
        
        # check if the date falls within the 7-day interval
        if 0 <= difference_days <= 7:

            congr_date = birthday_this_year
            # transfer from weekend to Monday
            # 6 - Sunday, 5 - Saturday
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