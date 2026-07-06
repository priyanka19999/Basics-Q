# Catch Multiple Exception Handling in Python


str = input("Please enter: ")

try:
    num = int(input("Please enter a number here: "))
    print(str + num)
except(ValueError, TypeError) as Err:
    print(Err)
    
print("Error resolved")


# Please enter: 45
# Please enter a number here: ppp
# invalid literal for int() with base 10: 'ppp'
# Error resolved