import pymongo as pm
import string
import time

def query(table, ql):
    t1 = time.time()
    res = table.aggregate([{"$unwind": "$reviews"},
                          {"$project": {"reviews.listing_id": 1, "reviews.comments": 1}}
                          ])
    res = list(res)
    listings = table.distinct("id")
    dic = {}
    for listing in listings:
        dic[listing] = 0
    punctuation_string = string.punctuation
    for result in res:
        w = result["reviews"]["comments"].split(" ")
        for word in w:
            for i in punctuation_string:
                word = word.replace(i,'')
            word.lower()
            if word in ql:
                dic[result["reviews"]["listing_id"]] += 1
    t2 = time.time()
    sort = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))
    start = len(sort)-1
    end = start - 3
    while start > end:
        print("Listing_id:",sort[start][0])
        start -= 1
    print("Running time is: " + str((t2-t1)*10) + "ms.")




def main():
    conn = pm.MongoClient("mongodb://localhost:27017")
    dbs = conn["A5db"]
    table = dbs["listings"]
    keyw_s = input("please input a set of words (use ',' to sep): ")
    words = keyw_s.split(",")
    for word in words:
        word.lower()
    query(table, words)

if __name__ == '__main__':
    main()