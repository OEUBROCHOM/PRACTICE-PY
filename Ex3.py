# Ex3: Enter text and display only letter in odd index
text=input("Enter your text:")
for i in range(len(text)):
    if i %2==1:
        print(text[i])