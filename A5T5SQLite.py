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
    neighbourhood = input("Please Enter a neighbourhood you are looking for:")
    cursor.execute('''
                SELECT neighbourhood
                FROM listing
                ''')
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == neighbourhood:
            return neighbourhood
    return NULL

def query(neighbourhood):
    global connection
    global cursor
    cursor.execute('''SELECT AVG(price)
                    FROM listings
                    WHERE neighbourhood = :n
                    GROUP BY neighbourhood''',{'n':neighbourhood})
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])


def main():
    path = "./A5.db"
    connect(path)
    neighbourhood = find_nei()
    if neighbourhood:
        query(neighbourhood)
    else:
        print("No such Neighbourhood.")
    connection.commit()
    connection.close()

main()