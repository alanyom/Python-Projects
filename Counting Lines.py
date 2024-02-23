#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.

fileref = open("emotion_words.txt","r")
num = fileref.readlines()
num_lines = 0
for line in fileref:
    num_lines += 1
    
fileref.close()
