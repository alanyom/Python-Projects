#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

fileref = open("travel_plans.txt","r")
num = fileref.read()

first_chars = num[:33]

fileref.close()
