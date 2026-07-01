#Python Calendar: Display Calendar in Python Programming

import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))


calendar = calendar.month(year,month)
print(calendar)


# Enter year: 2004    
# Enter month: 8
#     August 2004
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31