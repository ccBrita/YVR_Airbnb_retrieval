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

def find_listing_id():
    global connection
    global cursor
    a = random.randint(0,140000)
    cursor.execute('''
                    SElECT listing_id
                    From   reviews
                    Limit :number,1
                        ''',{'number':a})
    select_id = cursor.fetchall()
    return select_id[0][0]


def query(select_id):
    global connection
    global cursor
    cursor.execute('''
                    SELECT host_name, price, comments
                    FROM review R,listings S
                    WHERE R.listing_id = :ID
                    AND R.listing_id = S.id
                    ORDER BY date DESC
                    LIMIT 1
                    ''',{'ID':select_id})
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    path = "./A5.db"
    connect(path)
    select_id = find_listing_id()
    query(select_id)
    connection.commit()
    connection.close()

main()