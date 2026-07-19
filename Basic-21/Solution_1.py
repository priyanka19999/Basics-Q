# Function without Parameters
# Example-1
def greeetings():
    print("Welcome To India")
greeetings() #Welcome To India

# Function with Parameters
# Example-1
def add(a,b): #parameter(a,b)
    result = a+b
    print("The sum is:", result)
add(9,8) #arguments(9,8)
#The sum is: 17


# Function with Return Statement
# Example-1
def sub(a,b):
    return a - b
result = sub(10,9)
print(result)



# celsius to fareniet

def cel_to_far():
    degree = ((cel)*9/5) + 32
    return degree
cel = int(input("Enter a celsius"))
temp_f = cel_to_far()
print(temp_f) #48.2