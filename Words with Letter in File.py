#Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

file = open("school_prompt.txt","r")
p_words = []
file = file.read()
wordlist = file.split()
for i in wordlist:
    if 'p' in i:
        p_words.append(i)
