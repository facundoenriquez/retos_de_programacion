text = "papa pepe pipo popo popo pepe papa"
arr = []
dict = {}
new_word = ""
count = 0

for t in text:
    if t == " ":
        dict['palabra'] = new_word
        dict['cantidad'] = count + 1
        arr.append(dict)
        new_word = ""
    else:
        new_word = new_word + t
print(arr)
