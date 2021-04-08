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
    cursor.execute('''SELECT count(*)
                    FROM summary 
                    ''')
    rows = cursor.fetchall()
    print("table summary has "+str(rows[0][0])+" lines")

    cursor.execute('''SELECT count(*)
                    FROM review 
                    ''')
    rows = cursor.fetchall()
    print("table review has "+str(rows[0][0])+" lines")

    cursor.execute('''SELECT *
                    FROM summary 
                    ORDER BY id
                    LIMIT 10
                    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.execute('''SELECT *
                    FROM review 
                    ORDER BY listing_id
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