# Start

import datetime

def welcome_message(name):
    print(f"Welcome, {name}!")

def display_birth_month(month):
    print(f"Your birth month is: {month}")

def calculate_age_in_months(birth_month, birth_year):
    current_date = datetime.datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    age_in_months = (current_year - birth_year) * 12 + (current_month - birth_month)
    print(f"Your age in months is: {age_in_months}")

def main():
    # Get user's name
    name = input("What is your Name: ")
    welcome_message(name)

    # Get user's birth month
    birth_month = int(input("What is your birth month (1-12): "))
    display_birth_month(birth_month)

    # Get user's birth year
    birth_year = int(input("What year where you born: "))

    # Calculate and display user's age in months
    calculate_age_in_months(birth_month, birth_year)

if __name__ == "__main__":
    main()

# End 
