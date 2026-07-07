# How to Remove Punctuations From a String - Python Program

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter Anything here: ")

empty_string = ""


for i in string:
    if i not in punc:
        empty_string = empty_string + i
        
print(empty_string)


# Enter Anything here: hello!!! how are u ????
# hello how are u 