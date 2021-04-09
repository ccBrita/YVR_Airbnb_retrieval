import sqlite3
import csv
import random

connection = None
cursor = None



def connect(path):
    global connection, cursor
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()

def find_nei():
    global connection
    global cursor
    neighbourhood = []
    cursor.execute('''SELECT DISTINCT neighbourhood 
                    FROM summary S
                    ''')
    rows = cursor.fetchall()
    for row in rows:
        neighbourhood.append(row[0])
    a = len(neighbourhood)
    return neighbourhood[random.randint(0,a)]

def query(neighbourhood):
    global connection
    global cursor
    cursor.execute('''SELECT AVG(price)
                    FROM summary S, review R
                    WHERE S.id = R.listing_id
                    AND S.neighbourhood = :n
                    GROUP BY s.neighbourhood''',{'n':neighbourhood})
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])


def main():
    path = "./A5.db"
    connect(path)
    neighbourhood = find_nei()
    query(neighbourhood)
    connection.commit()
    connection.close()

main()