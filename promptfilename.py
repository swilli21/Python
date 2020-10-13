# Use words.txt as the file name
fname = input("Enter file name:")
fh = open(fname)
for lines in fh:
    lines = lines.upper() # changes all characters to uppercase
    lines = lines.rstrip() # strips the /n character at the end of every line
    print(lines) # print adds a new line but since strip the \n was strip you wont have a space between each line 
