text = input("Enter text: ")

uppercase_letters = ""
for i in range(len(text)):
    if text[i].isupper():
        uppercase_letters += text[i]
print("Uppercase letters:", uppercase_letters)
