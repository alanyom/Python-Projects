#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num = original_str.split()
num_words_list = []
for x in num:
    x = len(x)
    num_words_list.append(x)
print(num_words_list)
