year = int(input("Enter a year: "))
As= year if  year % 4 == 0 and year % 100 != 0 or (year % 400 == 0) else year
print(As)
