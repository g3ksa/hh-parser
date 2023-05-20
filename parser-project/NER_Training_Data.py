from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
import codecs
import json
import os

os.chdir(r'C:\some\path\on\your\pc')  # path to model directory

with codecs.open('annotations.json', 'r', 'utf_8') as f:  # annotations.json - NER training data
    data = json.load(f)

entity_name = "JOBS"  # Tag name

train_data = data['annotations']
train_data = [tuple(i) for i in train_data]


# Formatting training data

for i in train_data:
    if i[1]['entities'] == []:
        i[1]['entities'] = (0, 0, entity_name)
    else:
        i[1]['entities'][0] = tuple(i[1]['entities'][0])

nlp = spacy.load("ru_core_news_lg")  # russina spacy model

db = DocBin()  # create a DocBin object

for text, annot in tqdm(train_data):  # data in previous format
    doc = nlp.make_doc(text)  # create doc object from text
    ents = []
    for start, end, label in annot["entities"]:  # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents  # label the text with the ents
    db.add(doc)

os.chdir(r'C:\some\path\on\your\pc')  # path to model directory
db.to_disk("./train.spacy")  # save the docbin object
