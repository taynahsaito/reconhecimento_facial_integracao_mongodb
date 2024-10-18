from pymongo import MongoClient

connection_string = "mongodb+srv://taynah:tay12345@cluster.sssbe.mongodb.net/"
client = MongoClient(connection_string)
db_connection = client["ReconhecimentoFacial"]

collection = db_connection.get_collection('passageiros')
# print(collection)

search_filter = {"nome": "Taynah"}
response = collection.find(search_filter)

for registry in response: print(registry)


collection .insert_one({
    "userId": "123456",
    "nome": "Taynah",
    "image_path": "/images/yasmin.jpg",
    "face_descriptor": [
        0.543,
        0.243,
        0.344,
        0.765,
    ],
    "data_registro": {
    "$date": "2024-10-18T15:54:00.000Z"
    }
})