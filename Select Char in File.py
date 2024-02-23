#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

fileref = open("school_prompt.txt","r")
num = fileref.read()

beginning_chars = num[:30]

fileref.close()
