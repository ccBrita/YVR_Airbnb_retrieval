import pymongo
import time

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    t1 = time.time()
    hosts = mycol.find({"reviews":[]}).sort("id").limit(10)
    t2 = time.time()
    for host in hosts:
        print("listing_id:", host["id"])
    print("Running time is: " + str((t2-t1)*1000) + "ms.")    

main()

