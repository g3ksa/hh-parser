# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from flask_cors import CORS


import spacy
from spacy import displacy

def spacy_visualizer(text):
    nlp = spacy.load("D:/TechPractice/hh-parser/data/output/model-best")
    doc = nlp(text)
    html = displacy.render(doc, style="ent", minify=True)
    print()
    return html






app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form.get('text')
    #print(text1)
    #dictionary = find_keywords(text=text, keyword_dict=keyword_dict)
    #processed_text = paintkeyWord(text=text, keywords=dictionary)

    #processed_text = wrap_text_with_span(keyword_dict, text)
    #processed_text = apply_spans(text, find_keywords(keyword_dict, text))
    processed_text = spacy_visualizer(text)
    return processed_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



