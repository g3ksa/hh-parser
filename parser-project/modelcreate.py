import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("ru")
with open("./pages/funcs.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

training_data = []
for line in lines:
    text = line.strip()
    entities = [(0, len(text), "FUNCTION")]
    training_data.append((text, entities))


db = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")
