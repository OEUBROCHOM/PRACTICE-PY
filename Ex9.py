#Enter number of line:
#Enter number of letter:
#Enter letter:
line=int(input("Enter number of line:"))
num_letter=int(input("Enter number of letter:"))
letter=input("Enter letter")
for i in range(line):
    letters=" "
    for i in range(num_letter):
            letters += letter
    print(letters)