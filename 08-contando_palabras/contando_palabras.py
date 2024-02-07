text = "papa pepe pipo popo popo pepe papa"
arr = []
word_count_dict = {}
text_to_list = text.split(" ")

for word in text_to_list:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)

# Convert the dictionary to a list of dictionaries
for key, value in word_count_dict.items():
    arr.append({key: value})

print(arr)
