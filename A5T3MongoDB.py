import pymongo
import time
def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    hosts = mycol.distinct("host_id")
    hosts.sort()
    hosts = hosts[:10]
    t1 = time.time()
    for host in hosts:
        number = mycol.find({"host_id":host}).count()
        print("listing id:",host, "count:",number)
    t2 = time.time()
    print("Running time is: " + str((t2-t1)*10) + "ms.")

main()

