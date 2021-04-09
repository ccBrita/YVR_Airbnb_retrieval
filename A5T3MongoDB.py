import pymongo

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    hosts = mycol.find({},{"host_id":1}).sort("host_id").limit(10)
    
    [
        {"host_id":1231231}
        



    ]
    for host in hosts:
        number = mycol.find({"host_id":host["host_id"]}).count()
        print(host["host_id"], number)

main()

