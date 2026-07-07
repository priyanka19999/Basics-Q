# How to Parse a String to a Float or Integer using Python Codes

# solution- 1
# Parse string into integer

str = "1234567"
print(type(str))#<class 'str'>
int_str = int(str)
print(type(int_str)) #<class 'int'>


# solution- 2
# Parse string into float
str = "1234.56"
print(type(str))#<class 'str'>
float_str = float(str)
print(type(float_str)) #<class 'float'>


# solution- 3
# Parse string into float numeral into integer

string = "347.99"
print(type(string)) #<class 'str'>
string_float = int(float(string)) 
print(type(string_float)) #<class 'int'>