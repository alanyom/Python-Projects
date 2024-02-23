#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
count = 0
for word in words:
    check=(word[-1])
    if check == 'e':
        new = word + "d"
        past_tense.append(new)
    else:
        new = word + "ed"
        past_tense.append(new)

print(past_tense)
