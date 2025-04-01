year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The given month is a leap year.")
else:
    print("The give month is not a leap year.")