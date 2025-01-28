## Installation
- I installed milvus with docker
```
$ curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh

$ bash standalone_embed.sh start

```

##  Verification
- if everything is correct, you will get the result like the following with the command `docker ps`
```
$ docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS                    PORTS                                                                                                                                 NAMES
615af9cce98a   milvusdb/milvus:v2.5.2                "/tini -- milvus run…"   59 minutes ago   Up 58 minutes (healthy)   0.0.0.0:2379->2379/tcp, :::2379->2379/tcp, 0.0.0.0:9091->9091/tcp, :::9091->9091/tcp, 0.0.0.0:19530->19530/tcp, :::19530->19530/tcp   milvus-standalone

```
- Also, you can access Milvus WebUI at `http://127.0.0.1:9091/webui/`

## Reference
- https://milvus.io/docs/install_standalone-docker.md

