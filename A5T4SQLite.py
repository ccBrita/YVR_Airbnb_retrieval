import sqlite3
import csv
import time
connection = None
cursor = None



def connect(path):
    global connection, cursor
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()

def query():
    global connection
    global cursor
    t1 = time.time()
    cursor.execute('''SELECT S.id
                    FROM listings S
                    LEFT JOIN reviews R ON S.id = R.listing_id
                    WHERE R.listing_id IS NULL
                    ORDER BY S.id
                    LIMIT 10''')
    t2 = time.time()
    rows = cursor.fetchall()
    for row in rows:
        print("listing id:",row[0])
    print("Running time is: " + str((t2-t1)*1000) + "ms.")


def main():
    path = "./A5.db"
    connect(path)
    query()
    connection.commit()
    connection.close()

main()