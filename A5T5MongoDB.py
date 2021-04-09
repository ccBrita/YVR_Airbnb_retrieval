import pymongo

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    n = input("Please Enter a neighbourhood you are looking for:")
    result = mycol.aggregate(
        {"$match":{"neighbourhood":n}},
        {"$group":{"_id":"$neighbourhood","avg":{"$avg":"$price"}}}
    )
    print(result["avg"])


main()