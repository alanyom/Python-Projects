#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.


def stop_at_z(x):
    lst = []
    for y in x:
        if y != 'z':
            lst.append(y)
        else:
            break
    return lst
print(stop_at_z(['a', 'z']))
