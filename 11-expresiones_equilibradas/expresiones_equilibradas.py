exp_balanceada = "{ [ a * ( c + d ) ] - 5 }"
exp_no_balanceada = "{ a * ( c + d ) ] - 5 }"
exp_no_ordenada = "{ [ a * ( [ c + d ) ] ] - 5 }"

exp_clean = [t for t in exp_balanceada if t in ["{", "[", "(", "}", "]", ")"]]

if len(exp_clean) % 2 == 0:
    long = len(exp_clean) // 2
    for index, value in enumerate(exp_clean):
        if value == "{" and exp_clean[-1] == "}" or value == "[" and exp_clean[-1] == "]" or value == "(" and exp_clean[-1] == ")":
            exp_clean.pop()
        else:
            print("la expresion no esta ordenada")
            break
        if index == long - 1:
            print(exp_clean)
            print("le expresion esta balanceada")
            break
else:
    print("la expresion no esta balanceada")
