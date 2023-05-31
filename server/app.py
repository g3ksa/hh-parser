import json
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import spacy
from spacy import displacy

def get_vacancy_description(str):
    link = f'https://api.hh.ru/vacancies/{str}' if str.isdigit() else f'{str}'
    req = requests.get(link)
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    return BeautifulSoup(jsObj['description'], "html.parser").text

def spacy_visualizer(text):
    colors = {"TEXT": "pink", "MATH": "darkblue", "IMG": "green", "VOICE": "orange", "REC": "cyan", "DEV": "yellow"}
    options = {"ents": ["TEXT", "MATH", "IMG", "VOICE", "REC", "DEV"], "colors": colors}
    nlp = spacy.load("data/output/model-best")
    doc = nlp(text)
    return displacy.render(doc, style="ent", options=options, minify=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://159.223.230.93"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Vacancy(BaseModel):
    description: str


@app.post("/process_vacancy")
def process_vacancy(vacancy: Vacancy):
    print(vacancy.description)
    return spacy_visualizer(vacancy.description)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)






