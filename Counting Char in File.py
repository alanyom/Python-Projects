#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

fileref = open("travel_plans.txt","r")
numb = fileref.read()

num = len(numb)

fileref.close()
