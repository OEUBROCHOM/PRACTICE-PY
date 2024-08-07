#Ex7:Enter text and display the first index of letter "A"
text = input("Enter your text:")
position = 0
is_found = False
for i in range(len(text)):
    if (text[i] == "A" or text[i] == "a") and not is_found:
        position = i
        is_found = True
print("First index of A is:", position)