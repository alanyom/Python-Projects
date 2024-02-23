#Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.

def decision(i):
    if len(i) > 17:
        return "This is a long string"
    else:
        return "This is a short string"
            
r = "well hello dolly"
z = "how do you do sir tuuuikoooooo"

print(decision(r))
print(decision(z))
