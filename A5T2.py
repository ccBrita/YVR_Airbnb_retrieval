from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017")
#connect to mongo serve
mydb = client["A5db"]

def create_listing(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365,reviews):
    global client
    global mydb
    col = mydb["listings"]
    i = 0
    while (i < len(id1)):
        listing = {"id":int(id1[i]), "name":name[i], "host_id":int(host_id[i]), "host_name":host_name[i], "neighbourhood":neighbourhood[i], "room_type":room_type[i], "price":int(price[i]), "minmum_nights":int(minimum_nights[i]),"availability_365": int(availability_365[i]),"reviews":reviews[i]}
        col.insert_one(listing)
        i += 1
    
def create_reviews(id1, listing_id, id2, date, reviewer_id, reviewer_name, comments, reviews):
    i = 0
    while (i < len(id1)):
        a = []
        j = 0
        while (j < len(id2)):
            if id1[i] == listing_id[j]:
                a.append({"id":int(id2[j]), "date":date[j], "reviewer_id":int(reviewer_id[j]), "reviewer_name":reviewer_name[j], "comments":comments[j]})
            j += 1
        reviews.append(a)
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
    reviews = []
    read_csv(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365, listing_id, id2, date, reviewer_id, reviewer_name, comments)
    create_reviews(id1, listing_id, id2, date, reviewer_id, reviewer_name, comments,reviews)
    create_listing(name, id1, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365,reviews)

if __name__ == "__main__":
    main()
