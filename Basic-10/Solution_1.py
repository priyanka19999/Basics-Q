#Python Program to Find Numbers Divisible by Another Number


# Solution 1 using For Loop
n = int(input("Enter a number: "))
print("The Number Divisible By " , n,"are  :")
for i in range (1, 100):
    if i % n == 0:
        print(i)
        
# Enter a number: 13
# The Number Divisible By 13 are  :
# 13
# 26
# 39
# 52
# 65
# 78
# 91



# Solution 2 using lambda function and filter()
l = int(input("Enter a number: "))

result = list(filter(lambda x: x % l == 0, range(1, 101)))

print("The numbers divisible by", l, "are:")
print(result)