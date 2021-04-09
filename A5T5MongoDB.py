import pymongo

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
    cursor = mycol.aggregate([
        {"$match":{"neighbourhood":n}},
        {"$group":{"_id":"$neighbourhood","avg":{"$avg":"$price"}}}
    ]
    )
    result = list(cursor)
    print(result[0]["avg"])


main()