import sqlite3
conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()
 
#Question #1. How many artists are represented in the database? 
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print('Number of artists in the database:', len(data))
 
#Question #2. How many women (Female) are in the database?
cursor.execute('SELECT * FROM artists WHERE gender == "Female"')
data = cursor.fetchall()
print('Number of women:', len(data))
 
#Question #3. How many people in the database were born before 1900?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
print('Born before 1900:', len(data))
 
#Question #4*. What is the name of the oldest artist?


#Solution option #1: use standard Python tools
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
oldest = {'name': '', 'birthday': 1900}
for person in data:
    if person[4] < oldest['birthday']:
        oldest['name'] = person[1]
        oldest['birthday'] = person[4]
print('The oldest:', oldest)
 
#Solution option #2: SQL only
cursor.execute('SELECT name FROM artists WHERE "Birth Year" < 1900 order by "Birth Year"')
data = cursor.fetchall()
print('The oldest:', data[0][0])
 
conn.commit()
