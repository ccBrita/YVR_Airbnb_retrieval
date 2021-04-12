import pymongo as pm

def query(table, ql):
    table.createIndex({"reviews":"text"})
    res = table.find({"$text":{"$search":ql}},{"score":{"$meta":"textScore"}}).sort({"score":{"$meta":"textScore"}})
    res = list(res)
    res = sorted(res, key=lambda i: i["count"], reverse=True)[:10]
    for result in res:
        print(result)


def main():
    conn = pm.MongoClient("mongodb://localhost:27017")
    dbs = conn["A5db"]
    table = dbs["listings"]
    keyw_s = input("please input a set of words (use ',' to sep): ")
    words = keyw_s.split(",")


    concat_str = []
    for word in words:
        concat_str.append({"reviews.comments": {"$regex": word}})

    concat_str = {"$or": concat_str}


    query(table, concat_str)

if __name__ == '__main__':
    main()