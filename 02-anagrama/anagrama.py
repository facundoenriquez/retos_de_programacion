def anagrama(words):
    first_word = words[0]
    second_word = words[1]
    new_arr = []
    flag = False
    for char in first_word:
        if char not in second_word:
            flag = True
            break
        for index, char2 in enumerate(second_word):
            if char2 == char:
                new_arr.append(char2)
                second_word.replace(second_word[index], '')
                break
    if flag == True:
        return False
    return True


print(anagrama(["xextech", "txexech"]))
print(anagrama(["parrasect", "rrasectpa"]))
print(anagrama(["papa", "limon"]))
