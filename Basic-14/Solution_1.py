# Python Dictionary: How to Merge Two Dictionaries?

# Solution-1
# using | operator

dict1 = {"John": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}

print(dict1 | dict2)  #{'John': 89, 'Lisa': 94, 'Peter': 78}


# Solution-2
# using ** operator

dict1 = {"John": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}
print({**dict1,**dict2}) #{'John': 89, 'Lisa': 94, 'Peter': 78}

# Solution-3
# using Copy() and Update() Methods

dict1 = {"John": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}

dict3 = dict2.copy()
dict3.update(dict1)
print(dict3) #{'Lisa': 99, 'Peter': 78, 'John': 89}