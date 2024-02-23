#Using with to open file

with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
