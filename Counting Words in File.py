#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

fileref = "emotion_words.txt"
num_words = 0
with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())
