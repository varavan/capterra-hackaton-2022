from elasticsearch import Elasticsearch

apikey="cXI2anpIZ0JkMEJzQ05LaVlJN3A6VFdISTlFbXVTbUd5TDgwZ3dIMHZxQQ=="

client = Elasticsearch(
    "https://02b94c24df784e3eb7add87376f48775.us-east-1.aws.found.io:9200",
    api_key=("apiKey", apikey)
)


resp = client.search(index="vp_upc_categories",query={"match_all": {}, "size": 1})