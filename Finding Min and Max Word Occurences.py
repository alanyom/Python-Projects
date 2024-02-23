#accumulating max and min value

#Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}

for c in placement:
    if c not in d:
        d[c] = 0
    d[c] += 1
    
keys = list(d.keys())
min_value = keys[0]
for x in keys:
    if d[x] < d[min_value]:
        min_value = x

#Practice
#Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.

product = "iphone and android phones"

lett_d = {}

for c in product:
    if c not in lett_d:
        lett_d[c] = 0
    lett_d[c] += 1
    
keys = list(lett_d.keys())
max_value = keys[0]
for x in keys:
    if lett_d[x] > lett_d[max_value]:
        max_value = x
