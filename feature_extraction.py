import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

model_name = "/Users/iruizdel/Developer/ML/models/distilbert-labeler"

tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)

inputs = tokenizer("Perfect for small-medium businesses, monday sales CRM is a no-code fully-customizable CRM built on top of monday.com Work OS. Dubbed the CRM without the frustration, it handles all sales processes and client communication in one place. From capturing leads, managing contact info, tracking deals or collaborating across departments, monday sales CRM lets you manage it all. You can use built-in automations or easily create your own to streamline any manual work so you can focus more time on sales.", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
response = model.config.id2label[predicted_class_id]

print(response)