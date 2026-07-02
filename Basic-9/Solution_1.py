#Check Whether a String is Palindrome or Not

result = input("Enter a word here: ")
reverse = result[::-1]

if result == reverse:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    
# Ans
# Enter a word here: hello
# it is not a palindrome

# Enter a word here: wow
# it is a palindrome