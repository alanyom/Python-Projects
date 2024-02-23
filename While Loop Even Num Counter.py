#While loop
#counter
#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.

eve_nums = []
x = 0
while (x <= 15):
    if x % 2==0:
        eve_nums.append(x)
    x = x+1
