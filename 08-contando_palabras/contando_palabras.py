text = "papa pepe pipo popo popo pepe papa"
arr = []
word_count_dict = {}
text_to_list = text.split(" ")

for word in text_to_list:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

# Convert the dictionary to a list of dictionaries
for word, count in word_count_dict.items():
    arr.append({word: count})

print(arr)
