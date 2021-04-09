import pymongo

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    hosts = mycol.find({"reviews":[]}).sort("id").limit(10)
    for host in hosts:
        print(host["id"])

main()

