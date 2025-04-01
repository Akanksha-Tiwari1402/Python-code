user_input = input("Enter a number: ")
sum_of_digits = 0
for digit in user_input:
    sum_of_digits += int(digit)
print("Sum of individual digits:", sum_of_digits)