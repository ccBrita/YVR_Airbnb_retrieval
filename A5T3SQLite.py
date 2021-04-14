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
    cursor.execute('''SELECT host_id, count(host_id)
                    FROM listings
                    GROUP BY host_id
                    ORDER BY host_id
                    LIMIT 10
                    ''')
    t2 = time.time()
    rows = cursor.fetchall()
    for row in rows:
        print("listing id:",row[0],"count:",row[1])

    print("Running time is: " + str((t2-t1)*1000) + "ms.")    


def main():
    path = "./A5.db"
    connect(path)
    query()
    connection.commit()
    connection.close()

main()