user_input = input("Enter a number: ")
number = int(user_input)
num_digits = len(user_input)
sum_of_powers = 0
for digit in user_input:
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")