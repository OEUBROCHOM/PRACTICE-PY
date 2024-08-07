#Ex6 Enter text and display counter of lowercase letter "B" and uppercase letter "B"
text = input("Enter text: ")
counterB=0
for i in range(len(text)):
    if text[i] == "b" or text[i]=="B":
        counterB+=1
print("letter B:", counterB)