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
    cursor.execute('''SELECT S.id
                    FROM listings S
                    LEFT JOIN reviews R ON S.id = R.listing_id
                    WHERE R.listing_id IS NULL
                    ORDER BY S.id
                    LIMIT 10''')
    rows = cursor.fetchall()
    for row in rows:
        print("listing id:",row[0])


def main():
    path = "./A5.db"
    connect(path)
    query()
    connection.commit()
    connection.close()

main()