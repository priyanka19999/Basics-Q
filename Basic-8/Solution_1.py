#Python Program to Find Factorial of Number Using Recursion 


def fact(n):
    if n == 1:
        return  1
    else: 
        return (n * fact(n-1))
    
    
n = int(input("Enter a Number here: "))
if n <= 0:
    print('Factorial of number less than 1 does not exists')

else:
    print("Factorial of given number is", fact(n))
    
# Ans
# Enter a Number here: 3
# Factorial of given number is 6