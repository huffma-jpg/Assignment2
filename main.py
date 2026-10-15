"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45

annual_cost = 0
credits = 0


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    return annual_cost/SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost/MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost/(2*CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost/(2*credits)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return ((annual_cost*CS1430_CREDITS)/(2*credits))/CS1430_MEETINGS_PER_SEMESTER

# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the cost of tuition per year: "))
    credits = float(input("Enter the ammount of credits taken this semester: "))

    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. cost per credit")
        print('5. cost per class')
        
        choice = input("Choose an option: ")
    
        if choice.lower == "q":
            break
        elif choice == "1":
            print(f"${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"${cost_per_class(annual_cost, credits):.2f}")
        else:
            break


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
