import pymongo

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    n = input("Please Enter a neighbourhood you are looking for:")
    cursor = mycol.aggregate([
        {"$match":{"neighbourhood":n}},
        {"$group":{"_id":"$neighbourhood","avg":{"$avg":"$price"}}}
    ]
    )
    result = cursor.find_one({},{"avg":1})
    print(result["avg"])


main()