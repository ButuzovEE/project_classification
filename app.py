from fastapi import FastAPI
from pydantic import BaseModel
from transformers import RobertaForSequenceClassification, RobertaTokenizerFast

app = FastAPI()

model = RobertaForSequenceClassification.from_pretrained('./model')
tokenizer = RobertaTokenizerFast.from_pretrained('./tokenizer')


class Item(BaseModel):
    text: str


@app.post('/predict')
def predict(item: Item):
    inputs = tokenizer(item.text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    probabilities = outputs.logits.softmax(dim=-1)
    prediction = probabilities.argmax(dim=-1).item()
    return {'prediction': prediction}
