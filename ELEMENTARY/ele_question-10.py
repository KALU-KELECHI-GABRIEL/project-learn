#Write a program that prints the next 20 leap years.
import datetime

def leap_year(year):
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_leap_years(count):
    current_year = datetime.date.today().year
    listed_leap_years =  0
    years_to_check = current_year
    print(f"The next {count} leap years are: ")
    while listed_leap_years < count:
        if leap_year(years_to_check):
            print(years_to_check)
            listed_leap_years += 1
        years_to_check += 1

next_leap_years(20)