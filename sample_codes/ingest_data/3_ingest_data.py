import os
import random
from dotenv import load_dotenv
from pymilvus import connections, utility, Collection, FieldSchema, DataType, CollectionSchema
from sentence_transformers import SentenceTransformer
from pymilvus import MilvusClient
import openai

load_dotenv()
#print('Before load_dotenv()', os.getenv('OPENAI_API_KEY'))
#openai.api_key = os.getenv("OPENAI_API_KEY")

texts = [
    """第 3 條
本條例用辭定義如下：
一、公寓大廈：指構造上或使用上或在建築執照設計圖樣標有明確界線，得區分為數部分之建築物及其基地。
二、區分所有：指數人區分一建築物而各有其專有部分，並就其共用部分按其應有部分有所有權。
三、專有部分：指公寓大廈之一部分，具有使用上之獨立性，且為區分所有之標的者。
四、共用部分：指公寓大廈專有部分以外之其他部分及不屬專有之附屬建築物，而供共同使用者。
五、約定專用部分：公寓大廈共用部分經約定供特定區分所有權人使用者。
六、約定共用部分：指公寓大廈專有部分經約定供共同使用者。
七、區分所有權人會議：指區分所有權人為共同事務及涉及權利義務之有關事項，召集全體區分所有權人所舉行之會議。
八、住戶：指公寓大廈之區分所有權人、承租人或其他經區分所有權人同意而為專有部分之使用者或業經取得停車空間建築物所有權者。
九、管理委員會：指為執行區分所有權人會議決議事項及公寓大廈管理維護工作，由區分所有權人選任住戶若干人為管理委員所設立之組織。
十、管理負責人：指未成立管理委員會，由區分所有權人推選住戶一人或依第二十八條第三項、第二十九條第六項規定為負責管理公寓大廈事務者。
十一、管理服務人：指由區分所有權人會議決議或管理負責人或管理委員會僱傭或委任而執行建築物管理維護事務之公寓大廈管理服務人員或管理維護公司。
十二、規約：公寓大廈區分所有權人為增進共同利益，確保良好生活環境，經區分所有權人會議決議之共同遵守事項。""",
    """第 36 條
   管理委員會之職務如下：
   一、區分所有權人會議決議事項之執行。
   二、共有及共用部分之清潔、維護、修繕及一般改良。
   三、公寓大廈及其周圍之安全及環境維護事項。
   四、住戶共同事務應興革事項之建議。
   五、住戶違規情事之制止及相關資料之提供。
   六、住戶違反第六條第一項規定之協調。
   七、收益、公共基金及其他經費之收支、保管及運用。
   八、規約、會議紀錄、使用執照謄本、竣工圖說、水電、消防、機械設施、管線圖說、會計憑證、會計帳簿、財務報表、公共安全檢查及消防安全設備檢修之申報文件、印鑑及有關文件之保管。
   九、管理服務人之委任、僱傭及監督。
   十、會計報告、結算報告及其他管理事項之提出及公告。
   十一、共用部分、約定共用部分及其附屬設施設備之點收及保管。
   十二、依規定應由管理委員會申報之公共安全檢查與消防安全設備檢修之申報及改善之執行。
   十三、其他依本條例或規約所定事項。""",
   """第 37 條
   管理委員會會議決議之內容不得違反本條例、規約或區分所有權人會議決議。"""
]

MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT")

DB_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

DIMENSION = 768  # SentenceTransformer all-mpnet-base-v2 的輸出維度


# 注入 embedding
def insert_data(host_name, port, db_name, collection_name, texts):
    embedder = SentenceTransformer('distiluse-base-multilingual-cased-v1')
    client = MilvusClient(
        uri=f"http://{host_name}:{port}",
        db_name=db_name
    )
    entities = []
    for text in texts:
        embedding = embedder.encode(text)
        entities.append({"embedding": embedding, "text": text}) # 同時儲存 embedding 和原始文本
    print(entities)
    res=client.insert(collection_name=collection_name, data=entities)
    client.close()
    return res

if __name__ == "__main__":
    result=insert_data(MILVUS_HOST, MILVUS_PORT, DB_NAME, COLLECTION_NAME, texts=texts)
    print(result)
