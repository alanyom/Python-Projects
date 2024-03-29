#Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

if 'physics'in nested:
    physics = True
else:
    physics = False

if 'data' in nested:
    data = True
else:
    data = False

if 'whole' not in nested['window']:
    whole = True
else:
    whole = False

if 24 in nested['data']:
    twentyfour = True
else:
    twentyfour = False


# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
