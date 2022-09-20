import os
from tracemalloc import start
from datetime import datetime


from transformers import pipeline


model_name = "/Users/iruizdel/Developer/ML/models/bart-large-mnli"

print("Loading model...")

classifier = pipeline("zero-shot-classification",
                      model=model_name)

content_folder = './roberta-data/products_with_features/'

candidate_labels = ["CRM", "Remote support", "Helpesk", "Strategic Planning", "Digital Workplace"]

headerCsv = candidate_labels.copy()
headerCsv.insert(0, 'product_id')

results = [headerCsv];

rootIndex = 0

startTime = datetime.now()

print("Computing scores...")
for filename in os.listdir("./roberta-data/products"):
   with open("./roberta-data/products/" + filename, 'r') as f: # open in readonly mode
    try:
        f = open(content_folder + filename, "r")
        content_info = f.read()
        f.close()


        reviewsFilename =  "./roberta-data/reviews_short/"+ filename.split('.')[0] + ".txt"
        f = open(reviewsFilename, "r")
        content_reviews = f.read()
        f.close()
        
        content = content_info + "\n" + content_reviews
        res = classifier(content, candidate_labels)

        mapLabelsScores = {}
        for idx,lab in enumerate(res['labels']):
            mapLabelsScores[lab] = str(res['scores'][idx])
        
        result = [filename.split('.')[0]]

        for lab in candidate_labels:
            result.append(mapLabelsScores[lab])
        
        results.append(result)
    except:
        print("error loading " + filename)

    if(rootIndex % 5 == 0):
        endtime = datetime.now()
        print(str(rootIndex) + ". Took " + str(((endtime - startTime).total_seconds()) / 5) + " seconds per item")
        startTime = endtime
    if(rootIndex > 400):
            break
    rootIndex = rootIndex + 1

print("Writting file...")

outputFileName = './roberta-data/output_scores.csv'

if os.path.exists(outputFileName):
    os.remove(outputFileName)

with open(outputFileName, 'a') as outputFile:
    for result in results:
        outputFile.write(';'.join(result)+'\n')