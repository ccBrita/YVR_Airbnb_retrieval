import pymongo as pm
import time

def query(table, sel_id):
    t1 = time.time()
    results = table.find({"id":int(sel_id)})
    t2 = time.time()
    for res in results:
        print("Host_name:", res["host_name"])
        print("Price:", res["price"])
        latest = res["reviews"].pop()
        print("Latest Review:", latest["comments"])
    print("Running time is: " + str((t2-t1)*10) + "ms.")

def main():
    conn = pm.MongoClient("mongodb://localhost:27017")
    dbs = conn["A5db"]
    table = dbs["listings"]
    sel_id = input("please select an id to execute: ")
    ids = table.distinct("id")
    if int(sel_id) in ids:
        query(table, sel_id)
    else:
        print("there's no such id in table.")

if __name__ == '__main__':
    main()