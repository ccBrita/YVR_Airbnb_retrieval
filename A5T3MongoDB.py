import pymongo

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    hosts = mycol.distinct("host_id")
    hosts.sort()
    hosts = hosts[:10]
    
    for host in hosts:
        number = mycol.find({"host_id":host}).count()
        print(host, number)

main()