from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017")
#connect to mongo serve
mydb = client["A5db"]

def create_listing(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365):
    global client
    global mydb
    col = mydb["listing"]
    i = 0
    while (i < len(id1)):
        listing = {"id":id1[i], "name":name[i], "host_id":host_id[i], "host_name":host_name[i], "neighbourhood":neighbourhood[i], "room_type":room_type[i], "price":price[i], "minmum_nights":minimum_nights[i],"availability_365": availability_365[i]}
        col.insert_one(listing)
        i += 1
    
def create_reviews(listing_id, id2, date, reviewer_id, reviewer_name, comments):
    global client
    global mydb
    col = mydb["reviews"]
    i = 0
    while (i < len(id2)):
        review = {"listing_id":listing_id[0], "id":id2[i], "date":date[i], "reviewer_id":reviewer_id[i], "reviewer_name":reviewer_name[i], "comments":comments[i]}
        col.insert_one(review)
        i += 1

def read_csv(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365, listing_id, id2, date, reviewer_id, reviewer_name, comments):
    file1 = open("YVR_Airbnb_listings_summary.csv","r")
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
    file1.close()
    file2 = open("YVR_Airbnb_reviews.csv","r")
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
    file2.close()

    

def main():
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
    create_listing(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365)
    create_reviews(listing_id, id2, date, reviewer_id, reviewer_name, comments)

if __name__ == "__main__":
    main()
