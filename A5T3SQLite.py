import sqlite3
import csv

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

    cursor.execute('''SELECT host_id, count(host_id)
                        FROM listings
                        ORDER BY host_id
                        LIMIT 10
                    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    path = "./A5.db"
    connect(path)
    query()
    connection.commit()
    connection.close()

main()