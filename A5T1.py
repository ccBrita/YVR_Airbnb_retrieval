import sqlite3
import csv

connection = None
cursor = None

def createDB(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365, listing_id, id2, date, reviewer_id, reviewer_name, comments):
    global connection, cursor
    path = "./A5.db"
    connect(path)
    define_tables()
    i = 0
    a = len(id1)
    while i<a:
        insert_data_summary(name[i], id1[i], host_id[i], host_name[i], neighbourhood[i], room_type[i], price[i], minimum_nights[i], availability_365[i])
        i+=1
    j = 0
    b = len(id2)
    while j<b:
        insert_data_review(listing_id[j], id2[j], date[j], reviewer_id[j], reviewer_name[j], comments[j])
        j+=1


def connect(path):
    global connection, cursor
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()


def define_tables():
    global connection, cursor

    cursor.execute('''
                                Drop TABLE IF EXISTS summary;
                                ''')
    cursor.execute('''
                                Drop TABLE IF EXISTS review;
                                ''')
    summary = '''
                    CREATE TABLE summary (
                                        id                INT      PRIMARY KEY  NOT NULL,                                      
                                        name              CHAR(300)             NOT NULL,                                   
                                        host_id           INT                   NOT NULL,
                                        host_name         CHAR(50)              NOT NULL,
                                        neighbourhood     CHAR(50)              NOT NULL,
                                        room_type         CHAR(50)              NOT NULL,
                                        price             INT                   NOT NULL,
                                        minimum_nights    INT                   NOT NULL,
                                        availability_365  INT                   NOT NULL
                                        );
                '''

    review = '''
                CREATE TABLE review (
                                    listing_id           INT                   NOT NULL ,                                      
                                    id                   INT      PRIMARY KEY  NOT NULL,                                   
                                    date                 CHAR(15)              NOT NULL,
                                    reviewer_id          INT                   NOT NULL,
                                    reviewer_name        CHAR(50)              NOT NULL,
                                    comments             CHAR(1000)            NOT NULL
                                    );
            '''

    cursor.execute(review)
    cursor.execute(summary)
    connection.commit()


def insert_data_summary(name, id1,host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365):
    global connection, cursor

    cursor.execute(
        '''INSERT INTO summary VALUES 
        (:id, :name, :host_id, :host_name, :neighbourhood, :room_type, :price, :minimum_nights, :availability_365)''',
                   {"id": id1, "name": name, "host_id": host_id, "host_name": host_name, "neighbourhood": neighbourhood,
                    "room_type": room_type, "price": price, "minimum_nights": minimum_nights,
                    "availability_365": availability_365})
    connection.commit()


def insert_data_review(listing_id, id2, date, reviewer_id, reviewer_name, comments):
    global connection, cursor
    cursor.execute(
        '''INSERT INTO review VALUES 
        (:listing_id, :id, :date, :reviewer_id, :reviewer_name, :comments)''',
        {"listing_id": listing_id, "id": id2, "date": date, "reviewer_id": reviewer_id,
         "reviewer_name": reviewer_name, "comments": comments})
    connection.commit()


def read_csv(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365, listing_id, id2, date, reviewer_id, reviewer_name, comments):
    file1 = open("YVR_Airbnb_listings_summary.csv", "r", errors='ignore')
    reader1 = csv.reader(file1)
    for i in reader1:
        if reader1.line_num == 1:
            continue
        id1.append(i[0])
        name.append(i[1])
        host_id.append(i[2])
        host_name.append(i[3])
        neighbourhood.append(i[4])
        room_type.append(i[5])
        price.append(i[6])
        minimum_nights.append(i[7])
        availability_365.append(i[8])

    a = reader1.line_num-1

    file1.close()
    file2 = open("YVR_Airbnb_reviews.csv", "r", errors='ignore')
    reader2 = csv.reader(file2)
    for i in reader2:
        if reader2.line_num == 1:
            continue
        listing_id.append(i[0])
        id2.append(i[1])
        date.append(i[2])
        reviewer_id.append(i[3])
        reviewer_name.append(i[4])
        comments.append(i[5])
    b = reader2.line_num-1
    file2.close()

def main():
    global connection, cursor
    name = []
    id1 =[]
    host_id = []
    host_name = []
    neighbourhood = []
    room_type = []
    price = []
    minimum_nights = []
    availability_365 = []
    listing_id = []
    id2 =[]
    date = []
    reviewer_id = []
    reviewer_name = []
    comments = []
    read_csv(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365, listing_id, id2, date, reviewer_id, reviewer_name, comments)
    createDB(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365, listing_id, id2, date, reviewer_id, reviewer_name, comments)
    print("Database created")



if __name__ == "__main__":
    main()
