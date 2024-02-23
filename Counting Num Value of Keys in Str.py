#Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.

stri = "what can I do"
char_d = {}

for x in stri:
    if x not in char_d:
        char_d[x] = 0
    char_d[x] += 1
