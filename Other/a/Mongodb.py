from pymongo import MongoClient
host = 'localhost'
port = 27017

client = MongoClient(host,port)
db     = client['test']
sheet  = db['sheet']
for i in range(1001):
    print(i)
    sheet.insert_one({
        'name': 'name' + str(i),
        'age': i,
    })

