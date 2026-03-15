#10. Write a program to check if entered year is a leap year or not.
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

year = int(input("Enter year: "))
leap_year(year)