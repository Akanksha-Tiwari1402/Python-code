num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
num3=int(input("Enter the number:"))
num4=int(input("Enter the number:"))
biggest = (num1 if num1 > num2 else num2)
biggest = (biggest if biggest > num3 else num3)
biggest = (biggest if biggest > num4 else num4)
print("The biggest number is:", biggest)
