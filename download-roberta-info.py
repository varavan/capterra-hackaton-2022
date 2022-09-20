import json

f = open("./roberta-data/some-data.txt", "r")
data = f.read()
f.close();


dataObject = json.loads(data)

with open('roberta-data/data-1.txt', 'w') as f:
    for x in dataObject['hits']['hits']:
        productId = x['_source']['product_id']
        description = x['_source']['long_desc']
        pricing = x['_source']['pricing_details']
        product_name = x['_source']['product_name']

        rowString = 'Software ' + str(product_name) + '|'+ str(productId) + ' description is  ' + str(description)
        f.write(rowString)
    