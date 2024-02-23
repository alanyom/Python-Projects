#Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.

def addit(x):
    return x+5

def mult(x):
    return x*addit(x)
print(mult(addit(-2)))
