#Python Program to Safely Create a Nested Directory

# imports the Path class from the built-in pathlib module.
from pathlib import Path
Path("C:/xxx/xxx/xxx/Desktop/xxx/xxx/new_dict/demo_dict").mkdir(parents=True, exist_ok = True)

# It created a nested folder where demo_dict is inside the new_dict folder