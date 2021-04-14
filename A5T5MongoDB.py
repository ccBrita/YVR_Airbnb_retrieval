import pymongo
import time

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    n = input("Please Enter a neighbourhood you are looking for:")
    ns = mycol.distinct("neighbourhood")
    found = False
    for i in ns:
        if i == n:
            found = True
    if not found:
        print("Please enter a valid neighbourhood!!")
        return
    t1 = time.time()
    cursor = mycol.aggregate([
        {"$match":{"neighbourhood":n}},
        {"$group":{"_id":"$neighbourhood","avg":{"$avg":"$price"}}}
    ]
    )
    t2 = time.time()
    result = list(cursor)
    print("Average price of this neighbourhood is",result[0]["avg"])
    print("Running time is: " + str((t2-t1)*1000) + "ms.")

main()