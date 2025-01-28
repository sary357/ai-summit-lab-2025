import os
import random
from dotenv import load_dotenv
#from pymilvus import connections, utility, Collection, FieldSchema, DataType, CollectionSchema
#from sentence_transformers import SentenceTransformer
from pymilvus import MilvusClient, DataType

import openai

load_dotenv()

# 設定 Milvus 連線資訊
MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")
DB_NAME = os.getenv("DATABASE_NAME")
CACHE_DB_NAME = os.getenv("CACHE_DATABASE_NAME")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
CACHE_COLLECTION_NAME=os.getenv("CACHE_COLLECTION_NAME")
CACHE_COLLECITON_DEFAULT_TTL=int(os.getenv("CACHE_COLLECITON_DEFAULT_TTL"))
DIMENSION = 512  # SentenceTransformer all-mpnet-base-v2 的輸出維度

# gpt-4o-mini
def create_milvus_collection(host_name, port, db_name, collection_name, dim, max_text_length=65535, collection_ttl=0):
    client = MilvusClient(
        uri="http://localhost:19530",
        db_name=db_name
    )

    if client.has_collection(collection_name=collection_name):
        print(f"collection exist {collection_name}. I'm going to delete this collection!!")
        # return # please uncomment this statement if you don't hope to remove existing collection
        client.drop_collection(collection_name=collection_name) 
 
    schema = MilvusClient.create_schema(
        auto_id=True,
        enable_dynamic_field=True,
    )

    schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True, auto_id=True)
    schema.add_field(field_name="embedding", datatype=DataType.FLOAT_VECTOR, dim=dim)
    schema.add_field(field_name="text", datatype=DataType.VARCHAR, max_length=max_text_length)

    index_params = client.prepare_index_params()

    index_params.add_index(
        field_name="id",
        index_type="STL_SORT"
    )

    index_params.add_index(
        field_name="embedding", 
        index_type="AUTOINDEX",
        metric_type="COSINE"
    )

    client.create_collection(
        collection_name=collection_name,
        schema=schema,
        index_params=index_params,
    )
    res = client.get_load_state(
        collection_name=collection_name
    )
    if collection_ttl != 0:
        client.alter_collection_properties(
                collection_name=collection_name,
                properties = {"collection.ttl.seconds": int(collection_ttl)}
                )
    print(f"collection {collection_name} status: {res}")
    client.close()
    return

if __name__ == "__main__":
    collection = create_milvus_collection(MILVUS_HOST, MILVUS_PORT, DB_NAME, COLLECTION_NAME, DIMENSION)
#    collection = create_milvus_collection(MILVUS_HOST, MILVUS_PORT, CACHE_DB_NAME, CACHE_COLLECTION_NAME, DIMENSION, max_text_length=65535, collection_ttl=CACHE_COLLECITON_DEFAULT_TTL )
