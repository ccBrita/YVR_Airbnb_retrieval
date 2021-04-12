import pymongo as pm

def query(table, ql):
    res = table.find(ql)
    res = res[:3]
    for result in res:
        for term in result.keys():
            if (term != "reviews"):
                print(term + ":", result[term])

        print()

def main():
    conn = pm.MongoClient("mongodb://localhost:27017")
    dbs = conn["A5db"]
    table = dbs["listings"]
    keyw_s = input("please input a set of words (use ',' to sep): ")
    words = keyw_s.split(",")

    concat_str = []
    for word in words:
        concat_str.append({"reviews.comments": {"$regex": word}})

    concat_str = {"$and": concat_str}

    query(table, concat_str)

if __name__ == '__main__':
    main()