from datetime import datetime

# Get the current date
datetime_now = datetime.today()

# Ask user for their birthday in YYYY-MM-DD format
birthday_str = input("What's your birthday? (YYYY-MM-DD): ")

# Parse input string into a datetime object
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

# Calculate the age in years
date_result = datetime_now.year - birthday.year

# Adjust if the birthday hasn't occurred yet this year
if (datetime_now.month, datetime_now.day) < (birthday.month, birthday.day):
    date_result -= 1

print(f"You are {date_result} years old")
