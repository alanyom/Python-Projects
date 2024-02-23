#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).


def sublist(x):
    lst = []
    for y in x:
        if y != 5:
            lst.append(y)
        else:
            break
    return lst
print(sublist([1,8,7,4,3,9,5,6,2]))
