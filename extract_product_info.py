import json
import os
import sys

for filename in os.listdir("./roberta-data/products"):
   with open("./roberta-data/products/" + filename, 'r') as f: # open in readonly mode
    try: 
      data = json.load(f)
      hit = data['hits']['hits'][0]['_source'];
      upc_id = hit['upc_product_uuid']
      name = hit['product_name']
      description = hit['long_desc']
      pricing = hit['pricing_details']
      target = hit['target_audience']
      features = hit['features_tokenized_text']
      features_full = []
      for feat in hit['features']:
        features_full.append(feat['category_name'])
      text = "Software " + name + " is described as " + description + ".Features included: " + ', '.join(features_full) + ". Pricing described as " + pricing + " and a target audience " + target
    #   print(upc_id, name, description, pricing, target, features)
      w = open("./roberta-data/products_with_features/"+filename, "a")
      w.write(text)
      w.close()
    except Exception as e:
        print(e, file=sys.stderr)