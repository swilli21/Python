import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite') #make a database connection
cur = conn.cursor() #cursor is like a filehandle you send sql commands to the cursor and then you read the cursor to get the data back

# Do some setup
# UNIQUE means if you try to insert the same string into this column twice, it will fail to create a new record
# If the database was already created then you it would be problematic to execute this script which adds data to the table each time you run the script, DROP TABLE creates a fresh new DB
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()   #open the file with read only permission
json_data = json.loads(str_data)  #open the json filehandle
# parse through the dayta which is an array of array's
for entry in json_data:      # entry is the first list/array eg: [ "Charley", "si110", 1 ]

    name = entry[0];  #name is the first item: Charley
    title = entry[1]; #title is the second item : sill0
    role = entry[2]; #role is the third item : 1

    print((name, title, role))   #print out name and title as a tuple
# if you insert name twice or ignore will pretend like the insert never happens and prevents blow up. ?- place holder (name,) is a tuple with 1 item in it. Select gives us back a cursor to write to the database. Since we are inserting one thing we do fetchone[0]
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        ( user_id, course_id, role) )
# if the user_id, course_id, role already exist REPLACE tells it to become an update
    conn.commit()
