import sqlite3
import csv
import random
import time

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
                FROM listings
                ''')
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == neighbourhood:
            return neighbourhood
    return 0

def query(neighbourhood):
    global connection
    global cursor
    t1 = time.time()
    cursor.execute('''SELECT AVG(price)
                    FROM listings
                    WHERE neighbourhood = :n
                    GROUP BY neighbourhood''',{'n':neighbourhood})
    t2 = time.time()
    rows = cursor.fetchall()
    for row in rows:
        print("Average price of this neighbourhood is", row[0])
    print("Running time is: " + str((t2-t1)*10) + "ms.")


def main():
    path = "./A5.db"
    connect(path)
    neighbourhood = find_nei()
    if neighbourhood!=0:
        query(neighbourhood)
    else:
        print("No such Neighbourhood.")
    connection.commit()
    connection.close()

main()