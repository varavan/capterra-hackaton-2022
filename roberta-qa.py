
# import certifi
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

f = open("./roberta-data/data-1.txt", "r")
contextFromFile = f.read()
f.close();

model_name = "/Users/iruizdel/Developer/ML/models/roberta-base-squad2"


# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name, local_files_only=True)
QA_input = {
    'question': 'What is a cheap software for team management?',
    'context': contextFromFile
}
res = nlp(QA_input)

# b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name, local_files_only=True)
# tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)

print(res)