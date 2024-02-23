#iterating through a list with a while loop
#stopping at a specific element

#Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.


def stop_at_four(x):
    lst = []
    for y in x:
        if y != 4:
            lst.append(y)
        else:
            break
    return lst
print(stop_at_four([1,8,7,4,3,9,5,6,2]))
