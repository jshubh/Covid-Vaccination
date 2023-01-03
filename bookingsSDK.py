from data import Data
import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data")
conn=sqlite3.connect(db_path)

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS people
             (title TEXT, pages INTEGER, date TEXT, time TEXT)''')

slots=[['21-03','11:00'],['21-03','12:00'],['21-03','01:00'],['21-03','02:00'],['21-03','03:00']]

def cursor():
    #https://stackoverflow.com/questions/14511337/efficiency-of-reopening-sqlite-database-after-each-query/14520670
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data")
    return sqlite3.connect(db_path).cursor()

def add(people):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO people VALUES (?, ?, ?, ?)", (people.name, people.number,people.date,people.time))
    c.connection.close() 
    return c.lastrowid
        
def get_bookings():
    c = cursor()
    people = []
    for row in c.execute('SELECT * FROM people'):
        people.append(Data(row[0], row[1], row[2],row[3]))
    c.connection.close()
    return people

def see_slots():
    print("Available Slots")
    for i in slots:
        print(i[0],i[1])

def check(date,time):
    if [date,time] in slots:
        return True
    else:
        return False

def delete_book(people):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM people WHERE title=? AND pages=?', (people.name, people.number))
    rows = c.rowcount
    c.connection.close()
    return rows