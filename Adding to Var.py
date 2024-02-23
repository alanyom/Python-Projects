#putting specific number of characters into a variable
#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

fileref = open("emotion_words2.txt","r")
num = fileref.read()

first_forty = num[:40]

fileref.close()
