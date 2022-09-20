text = input("camelCase: ")

for n in text:
    if n.isupper():
        newText = "_" + n.lower()
        n = newText
    print(n, end="")