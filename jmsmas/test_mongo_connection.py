from pymongo import MongoClient

client = MongoClient("mongodb+srv://sourav:QmtiBaFhb7naPERI@cluster0.ojjhkq2.mongodb.net/?retryWrites=true&w=majority")
db = client['sample_mflix']
collection = db['movies']

collection.insert_one({"plot": "It involves culture of Kambla and Bhootha Kola. A human and nature conflict where Shiva is a rebel who defends his village and nature. A death leads to war between villagers and evil forces. Will he able to regain peace in the village?",
"genres": ["action", "adventure", "drama"], "runtime": 148, "cast": ["Rishab Shetty", "Sapthami Gowda", "Kishore Kumar G"], 
"title": "Kantara", "directors": ["Rishab Shetty"], "writers": ["Rishab Shetty"], "year": 2022, "imdb": {"rating": 9.1, "votes": 66000, "id": 15327088}, "type": "movie"})
