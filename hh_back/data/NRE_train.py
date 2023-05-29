from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
import codecs
import json
import os

#os.chdir(r'C:\some\path\on\your\pc')  # path to model directory

with codecs.open('./annotations.json', 'r', 'utf_8') as f:
    data = json.load(f)

entity_name = "JOBS"

data = data['annotations']
train_data = []
for i in data:
    try:
        train_data.append(tuple(i))
    except Exception:
        continue
        
#train_data = [tuple(i) for i in train_data]

for i in train_data:
    if i[1]['entities'] == []:
        i[1]['entities'] = (0, 0, entity_name)
    else:
        i[1]['entities'][0] = tuple(i[1]['entities'][0])

nlp = spacy.load("ru_core_news_lg")

db = DocBin().from_disk('./train.spacy')

for text, annot in tqdm(train_data):
    doc = nlp.make_doc(text)
    ents = []
    entities = annot["entities"]
    if isinstance(entities, list):
        for start, end, label in entities:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
    else:
        print("Invalid entities format")
    doc.ents = ents
    db.add(doc)


#os.chdir(r'C:\some\path\on\your\pc')  # path to model directory
db.to_disk("./train.spacy") 