# importing required libraries
from pymongo import MongoClient
import pandas as pd
from gspread_pandas import Client, Spread
# from utils.fetch_data import get_data

spread_name = "Sample Survey Data"
sheet_name = "data"

def get_data(spread_name=spread_name, sheet_name=sheet_name):
    
    dfc = []
    
    try:
        # Reading spreadsheet from google sheets    
        spread = Spread(spread_name)

        # converting the sheet to a df
        df = Spread.sheet_to_df(spread, sheet=sheet_name)

        # querying and filtering dataframe
        df['duration'] = [int(d) for d in df['duration']]
        df['is_accepted'] = [bool(a.title()) for a in df['is_accepted']]
        dfc = df.to_dict('records')
        
        return dfc
    except Exception as e:
        return print(e)


# create a collection instane
def connect():
    client = MongoClient("mongodb+srv://sourav:QmtiBaFhb7naPERI@cluster0.ojjhkq2.mongodb.net/?retryWrites=true&w=majority")
    db = client['jms']
    collection = db['surveyData']

    return collection

# define a function to bulk insert data
def bulk_insert():

    collection = connect()
    documents = get_data()
    
    try:
        collection.insert_many(documents)
        return print("Succesfully inserted")
    except Exception as e:
        return print(e)


# define a function to 
def query_documents():

    collection = connect()
    documents = []
    try:
        cursor = collection.find({"duration": {"$lt": 1200}, "audio_audit": {"$ne": ""}})
        documents = list(cursor)
        return documents
    except Exception as e:
        return print(e)


# query a single document using KEY field
def query_one(KEY):
    collection = connect()
    query_dict = {"KEY": KEY}
    
    try:
        cursor = collection.find_one(query_dict)
        return cursor
    except Exception as e:
        return print(e)


# update a single document using KEY field
def update_one(KEY, comments, rating, is_accepted):
    collection = connect()
    query_dict = {"KEY": KEY}
    update_dict = {"$set": {'comments': comments, 'rating': rating, 'is_accepted': is_accepted}}

    try:
        cursor = collection.update_one(query_dict, update_dict)
    except Exception as e:
        return print(e)


if __name__ == '__main__':
    bulk_insert()