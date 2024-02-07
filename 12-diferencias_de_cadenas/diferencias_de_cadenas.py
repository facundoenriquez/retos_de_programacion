str1 = "Hello, World!"
str2 = "Hello, Python!"
out1 = ""
out2 = ""

def calcular_diferencias(str1, str2):
    for t2 in str2:
        if t2 in str1:
            print(t2)

calcular_diferencias(str1, str2)
