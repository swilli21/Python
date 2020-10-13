# Use the file name mbox-short.txt as the file fname
fname = input("Enter file name: ")
fh = open(fname) # the read parameter is defaulted when left out of open
count = 0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else :
        count = count + 1
        first = line.find("0")
        new = float(line[first : ])
        num = num + new
        avg = num/count
print ("Average spam confidence:", avg)
