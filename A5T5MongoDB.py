import pymongo

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["A5db"]
    mycol = mydb["listings"]
    neighbourhood = input("Please Enter a neighbourhood you are looking for:")
    agrt = mycol.aggregate([{$group : {_id : "$neighbourhood", avg_price : {$avg : 1}}}])
    result = agrt.find({"_id":neighbourhood})
    print(result["avg_price"])


main()