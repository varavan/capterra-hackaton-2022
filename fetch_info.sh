#!/bin/bash
input="./roberta-data/products.txt"
while IFS= read -r line
do
  eval "curl 'https://35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io/api/console/proxy?path=product_listings_main_data_query_alias_upc%2F_search&method=GET' \
    -H 'authority: 35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io' \
    -H 'accept: text/plain, */*; q=0.01' \
    -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -H 'cookie: sid=Fe26.2**4a97089a04e613663588db1144b2f7565d6fb32832aa76e7e05089066d0917cc*GSPBtaKj491y-JsrVOawqw*bb6tqRB3qgI2NtvzoLW0ZT6cUhj1R2QpQ3JamOanWU4lWa92hiHqvMndeLeBVjFREkCEOdKgWngDp1iU0vzVzSrtvjq4pYungWGV8koRSgNjscBh8ldbtkXOVrNSa12x4uNzKDRZvHY98iajkS4aC5IFpNQcimA2SzKte5kFw9NeiiJ8Itp_Ucf8oITuIie8PnSrdZaevZ47329WQR1WpVqh6pDQqCdKFyBaGetMD8PwdB9hp2naJXpPSBjUwUGc**be97106464b136490094e157f2be6afd187faa5adaa2e4fcbe8f54c3760ebc33*QHG_zxCeg8OvrgJoj2q8T1OIZGIqgzow9_ioG8hRMUw' \
    -H 'kbn-xsrf: kibana' \
    -H 'origin: https://35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io' \
    -H 'pragma: no-cache' \
    -H 'referer: https://35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io/app/dev_tools' \
    -H 'sec-ch-ua: \"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: \"macOS\"' \
    -H 'sec-fetch-dest: empty' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-site: same-origin' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
    --data-raw $'{\n    \"from\" : 0, \n  \"size\" : 100,\n   \"query\": {\n          \"bool\": {\n            \"must\": [\n              { \"term\": { \"is_best_category\": true } },\n              { \"term\": { \"upc_product_uuid.keyword\": \"$line\" } }\n            ]\n          }\n        }\n}\n' \
    --compressed > ./roberta-data/products/$line.json"
done < "$input"

# curl 'https://35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io/api/console/proxy?path=product_listings_main_data_query_alias_upc%2F_search&method=GET' \
#   -H 'authority: 35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io' \
#   -H 'accept: text/plain, */*; q=0.01' \
#   -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/json' \
#   -H 'cookie: sid=Fe26.2**4a97089a04e613663588db1144b2f7565d6fb32832aa76e7e05089066d0917cc*GSPBtaKj491y-JsrVOawqw*bb6tqRB3qgI2NtvzoLW0ZT6cUhj1R2QpQ3JamOanWU4lWa92hiHqvMndeLeBVjFREkCEOdKgWngDp1iU0vzVzSrtvjq4pYungWGV8koRSgNjscBh8ldbtkXOVrNSa12x4uNzKDRZvHY98iajkS4aC5IFpNQcimA2SzKte5kFw9NeiiJ8Itp_Ucf8oITuIie8PnSrdZaevZ47329WQR1WpVqh6pDQqCdKFyBaGetMD8PwdB9hp2naJXpPSBjUwUGc**be97106464b136490094e157f2be6afd187faa5adaa2e4fcbe8f54c3760ebc33*QHG_zxCeg8OvrgJoj2q8T1OIZGIqgzow9_ioG8hRMUw' \
#   -H 'kbn-xsrf: kibana' \
#   -H 'origin: https://35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://35d56a6882f44eabaa877cbd0fa09a54.us-east-1.aws.found.io/app/dev_tools' \
#   -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
#   --data-raw $'{\n    "from" : 0, \n  "size" : 100,\n   "query": {\n          "bool": {\n            "must": [\n              { "term": { "is_best_category": true } },\n              { "term": { "upc_product_uuid.keyword": "c7f00a1b-c5c0-4be8-8c9b-a6d200b37696" } }\n            ]\n          }\n        }\n}\n' \
#   --compressed