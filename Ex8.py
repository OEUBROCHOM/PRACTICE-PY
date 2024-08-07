#Ex8:Enter text and display the last index of letter "A"
text = input("Enter your text:")
position = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "a":
        position = i
print("Last index of A is:", position)