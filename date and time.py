from datetime import date , time , datetime

today = date.today()
now = datetime.now()
print("todays date is",today)
print("\n current date and time is",now)

print("\ndate components", today.year, today.month , today.day)