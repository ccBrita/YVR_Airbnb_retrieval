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
    number = input("Please Enter a listing_id you are looking for:")
    if not number.isdigit():
        return -1
    number = int(number)
    cursor.execute('''
                    SElECT listing_id
                    From   reviews
                        ''')
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == number:
            return number
    return -1


def query(select_id):
    global connection
    global cursor
    
    cursor.execute('''
                    SELECT host_name, price, comments
                    FROM reviews R,listings S
                    WHERE R.listing_id = :ID
                    AND R.listing_id = S.id
                    ORDER BY date DESC
                    LIMIT 1
                    ''',{'ID':select_id})
    rows = cursor.fetchall()
    for row in rows:
        print("Host name:",row[0],"\nPrice:",row[1],"\nLatest review:", row[2])


def main():
    path = "./A5.db"
    connect(path)
    select_id = find_listing_id()
    if select_id != -1:
        query(select_id)
    else:
        print("No such id")
    connection.commit()
    connection.close()

main()