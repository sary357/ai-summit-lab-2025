# AI summit 2025
# Folder structure
```
├── README.md: Introduction
├── sample_codes
|   ├─── ingest_data
|   |    ├── 0_create_db.py: create databases (1 is for RAG while the other one is for Semantic cache).
|   |    ├── 1_create_cache_collection.py: create a collection for semantic cache.
|   |    ├── 1_create_collection.py: create a collection for RAG. 
|   |    ├── 2_list_collection.py: list collections in the databases. 
|   |    └── 3_ingest_data.py: ingest data into RAG VectorDB.
|   └─── semantic_cache
|        ├── 1_query_with_sqlite.ipynb: semantic cache implementation with FAISS + SQLite.
|        └── 2_query_with_milvus.ipynb: semantic cache implementation with Milvus.
|── milvus
|   ├── README.md: describe how to launch milvus with Docker on local environment.
|   └── standalone_embed.sh: the script which can lauch milvus. Please feel free to ignore this file if you follow the instruction described in README.md.
└── start.sh: launch jupyter notebook

```
# How can I use this repo?
- launch milvus by following the instructions described in [milvus/README.md](milvus/README.md)
- create the following
  - databases: follow the instructions described in [sample_codes/0_create_db.py](sample_codes/0_create_db.py)
  - collections: follow the instructions described in [sample_codes/1_create_collection.py](sample_codes/1_create_collection.py) and [sample_codes/1_create_cache_collection.py](sample_codes/1_create_cache_collection.py)
- verify db and collections with [sample_codes/2_list_collection.py](sample_codes/2_list_collection.py)
- ingest sample data: follow the instructions described in [sample_codes/3_ingest_data.py](sample_codes/3_ingest_data.py)
- launch jupyter notebook with [start.sh](start.sh)
- Execute the Jupyter notebook like [sample_codes/semantic_cache/1_query_with_sqlite.ipynb](sample_codes/semantic_cache/1_query_with_sqlite.ipynb) and [sample_codes/semantic_cache/2_query_with_milvus.ipynb]([sample_codes/semantic_cache/2_query_with_milvus.ipynb)
# Slides
- [Presentation slides](https://gamma.app/docs/LLM-semantic-cache-dxqy891owffkt81?mode=doc)
