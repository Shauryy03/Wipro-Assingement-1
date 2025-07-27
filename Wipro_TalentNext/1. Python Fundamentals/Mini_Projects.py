# Project 1: Travel Suggestion Program

# Create a python program that asks the user how far they want to travel.
# If they want to travel less than three miles tell them to ride Bicycle.
# If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle.
# If they want to travel three hundred miles or more tell them to drive Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

def travel_suggestion():
    distance = float(input("How far would you like to travel in miles? "))
    if distance < 3:
        print("I suggest Bicycle to your destination.")
    elif distance < 300:
        print("I suggest Motor-Cycle to your destination.")
    else:
        print("I suggest Super-Car to your destination.")

# Project 2: Cloud Server Cost Calculator

# Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
# You decide to host your application on servers running in the cloud.
# You pick a hosting provider that charges $0.51 per hour.
# You will launch your service using one server and want to know how much it will cost to operate per day, per week, per month.
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How many days can I operate one server with $918?

def server_cost_calculator():
    hourly_rate = 0.51
    hours_per_day = 24
    days_per_week = 7
    days_per_month = 30  # Approximate

    daily_cost = hourly_rate * hours_per_day
    weekly_cost = daily_cost * days_per_week
    monthly_cost = daily_cost * days_per_month

    budget = 918
    days_operable = budget / daily_cost

    print(f"Cost per day: ${daily_cost:.2f}")
    print(f"Cost per week: ${weekly_cost:.2f}")
    print(f"Cost per month: ${monthly_cost:.2f}")
    print(f"With ${budget}, you can operate one server for {days_operable:.2f} days.")

# Run both projects
if __name__ == "__main__":
    print("=== Project 1: Travel Suggestion ===")
    travel_suggestion()
    print("\n=== Project 2: Server Cost Calculator ===")
    server_cost_calculator()
