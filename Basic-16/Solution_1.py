# Python Program to Make a Simple Calculator | Complete Tutorial

print("~~~~~~~Mini Calculator~~~~~~~")


num1 = float(input("Enter First number here: "))
num2 = float(input("Enter Second number here: "))

print("Press 1 for addition\nPress 2 for Substraction\nPress 3 for Multiplication\nPress 4 for Division\nPress 5 for Percentage")

user_choice = int(input("Enter Your Choice from 1-4: "))
if user_choice == 1:
    print(num1 + num2)
elif user_choice == 2:
    print(num1-num2)
elif user_choice == 3:
    print(num1*num2)
elif user_choice == 4:
    print(num1/num2)
elif user_choice == 5:
    print((num1 / num2) * 100, "%")
else:
    print("Enter A Valid Input")
    
    
# Enter First number here: 25
# Enter Second number here: 50
# Press 1 for addition
# Press 2 for Substraction
# Press 3 for Multiplication
# Press 4 for Division
# Press 5 for Percentage
# Enter Your Choice from 1-4: 5
# 50.0 %