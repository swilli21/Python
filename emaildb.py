import sqlite3             #import the library to use the commands for sqlite
conn = sqlite3.connect('orgdb.sqlite')   #make a connection to the db, creates a db.sqlite
cur = conn.cursor()    #handle send sql commands through the cursor and you get output through it as well.

cur.execute('DROP TABLE IF EXISTS counts') #drop the table if it exist, but there is a no file so its just for checking

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)') #create a table called Counts where email and count are the columns/attributes

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    organ = pieces[1]
    email = organ.split('@')
    domain = email[1]   # this is looping through the file and extracting the email from the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,)) #dont allow Sql injection, the ? is a place holder which will be replaced by email it grabbed from the data
    row =cur.fetchone() #we are using a get method,where we are seeking the value in this row from the count column
    if row is None:  # when you grab the row value in the count column for that email, if the value is None then the email is appearing for the first time
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1) ''', (domain,)) #then insert into the count row under the count column for that email the value 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,)) # if you get a row that exist then you are adding to the exisiting value
    conn.commit() #write the data to disk?

#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'   #read the table, asking for 2 column with a limit of 10 data in tuple format in descending order
for row in cur.execute(sqlstr):  #go through each rows within the database
    print(str(row[0]), row[1]) #row[0] is email and row[1] is count
cur.close()
