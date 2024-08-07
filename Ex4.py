#Ex4: Enter text and display reverse text
text=input("Enter your love text:")
lastIndex=len(text)-1
result=" "
for i in range(len(text)):
    result+=text[lastIndex-i]
print(result)