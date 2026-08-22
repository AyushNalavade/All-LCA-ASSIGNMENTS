# Write a python program to find the largest of three numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 >= num2 and num1 >= num3:
    print("First number is greater", num1)
elif num2 >= num1 and num2 >= num3:
    print("Second number is greater", num2)
else:
    print("Third number is greater", num3)
