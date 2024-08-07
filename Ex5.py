# Ex5 Enter text and display only letter "A" index
text = input("Enter text: ")
indexA=0
for i in range(len(text)):
    if text[i] == "A":
        indexA+=1
        print("Index A:", i)