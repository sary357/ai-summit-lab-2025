import os
import random
from dotenv import load_dotenv
from pymilvus import MilvusClient, DataType

import openai

load_dotenv()

# 設定 Milvus 連線資訊
MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")
DB_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
CACHE_DB_NAME = os.getenv("CACHE_DATABASE_NAME")
CACHE_COLLECTION_NAME=os.getenv("CACHE_COLLECTION_NAME")

# gpt-4o-mini
def list_milvus_collection(host_name, port, db_name):
    client = MilvusClient(
            uri=f"http://{host_name}:{port}",
            db_name=db_name
    )
    c=client.list_collections()
   # print (client.list_collections())

    print(f"db name: {db_name}")
    for i in c:
        res = client.describe_collection(
            collection_name=i
        )
        print(f"collection name: {i}")
        print(f"info: {res}")
        print("-*-"*10)

    client.close()
if __name__ == "__main__":
    list_milvus_collection(MILVUS_HOST, MILVUS_PORT, DB_NAME)
    list_milvus_collection(MILVUS_HOST, MILVUS_PORT, CACHE_DB_NAME)
