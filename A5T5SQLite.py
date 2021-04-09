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
    neighbourhood = input("Please Enter a neighbourhood you are looking for:")
    return neighbourhood

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
    query(neighbourhood)
    connection.commit()
    connection.close()

main()