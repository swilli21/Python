data = 'From swill@jmu.edu.gov Sat Jan 5 09:14:59 2008'
startpos = data.find('@') #find() tells you the index location of the string you are trying to locate
print(startpos)

endpos = data.find(' ',startpos) #you can pass find more than 1 variable, in this case its the string and where to start searching in the data
print(endpos)

email_host = data[startpos+1 : endpos]
print(email_host)
