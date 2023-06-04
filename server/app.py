import json
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request, Form
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import spacy
from spacy import displacy

def get_vacancy_description(str):
    pattern = r"hh.ru/vacancy/(\d+)"
    if match := re.search(pattern, str):
        vacancy_id = match.group(1)
        link = f'https://api.hh.ru/vacancies/{vacancy_id}'
    elif str.isdigit():
        link = f'https://api.hh.ru/vacancies/{str}'
    else:
        return None
    req = requests.get(link)
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    return BeautifulSoup(jsObj['description'], "html.parser").text

def spacy_visualizer(text):
    colors = {"TEXT": "#FFB6C1", "MATH": "#AEE4FF", "IMG": "#CEE9BE", "VOICE": "#DDA0DD", "REC": "#FEE5E1", "DEV": "#F0E68C"}
    options = {"ents": ["TEXT", "MATH", "IMG", "VOICE", "REC", "DEV"], "colors": colors}
    nlp = spacy.load("data/output/model-best")
    doc = nlp(text)
    return displacy.render(doc, style="ent", options=options, minify=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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






