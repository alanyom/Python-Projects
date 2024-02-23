#Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.

def total(b):
    x = 0
    for y in b:
        x += y
    return x
f = total([1, 2, 3, 4, 5])
