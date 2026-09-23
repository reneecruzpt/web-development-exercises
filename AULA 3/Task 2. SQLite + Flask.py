from flask import Flask, url_for, redirect
import sqlite3
 
def index():
    # Establish a connection to the database and send a request
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()
 
    # When processing a request, consider a few options:
    #Option #1 - there is no data on artists born in the specified year in the database
    if len(data) == 0:
        return 'There is no data in the database about artists born in ' + str(year) + 'year'
    
    #Option #2 - there is only one artist born in the specified year
    elif len(data) == 1:
        return 'In ' + str(year) + 'year was born (born)' + data[0][0]
    
    #Option #3 - several artists were born in the specified year
    else:
        result = '<h3>List of artists born in ' + str(year) + ' year:</h3><ol>'
        for person in data:
            result += '<li>' + person[0] + '</li>'
        result += '</ol>'
    return result
 
# The requested year of birth will be stored in a global variable
year = int(input("Enter the artist's year of birth: "))        
app = Flask(__name__)
app.add_url_rule('/', 'index', index)   
 
if __name__ == "__main__":
    # Starting the web server:
    app.run()
