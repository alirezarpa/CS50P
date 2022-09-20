text = input("Input: ")

vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
newText = ""

for i in range(len(text)):
    if text[i] not in vowels:
        newText += text[i]

text = newText
print(text)