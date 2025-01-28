from pymilvus import connections, db
import os
from dotenv import load_dotenv

load_dotenv()

# 設定 Milvus 連線資訊
MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")
DB_NAME = os.getenv("DATABASE_NAME")
CACHE_DB_NAME = os.getenv("CACHE_DATABASE_NAME")

def create_database(database_name):
    conn = connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)
    database = db.create_database(database_name)


if __name__ == "__main__":
    create_database(DB_NAME)
    create_database(CACHE_DB_NAME)
