# Python Program to Illustrate Different Set Operations 

A = {1,2,3,6,8,9}
B = {3,4,5,6,8,7}

print("The Union is", A|B)

print("The Intersection is", A&B)

print("The Difference is", A-B)

print("The Symmetric Difference is", A^B)


# The Union is {1, 2, 3, 4, 5, 6, 7, 8, 9}
# The Intersection is {8, 3, 6}
# The Difference is {1, 2, 9}
# The Symmetric Difference is {1, 2, 4, 5, 7, 9}