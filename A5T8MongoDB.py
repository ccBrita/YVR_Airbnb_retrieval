import pymongo as pm

def query(table, sel_id):
    results = table.find({"id":int(sel_id)})
    for res in results:
        print("host_name:", res["host_name"])
        print("rental_price:", res["price"])
        latest = res["reviews"].pop()
        print("latest review: \n", latest)

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