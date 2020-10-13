fname = input("Enter file name: ")
fh = open(fname)
lst = list()
word = None
for line in fh:
    line = line.rstrip()
    line = line.split()
    for words in line:
        word = words
        if word not in lst:
            lst.append(word)
            lst.sort()
print(lst)
