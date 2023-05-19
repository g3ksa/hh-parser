from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

import spacy
from spacy import displacy

def spacy_visualizer(text):
    nlp = spacy.load("data/output/model-best")
    doc = nlp(text)
    html = displacy.render(doc, style="ent", minify=True)
    return html


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Здесь вы можете указать список разрешенных источников или использовать "*" для разрешения всех источников
    allow_credentials=True,  # Разрешить включение учетных данных (например, куки)
    allow_methods=["*"],  # Установить список разрешенных HTTP-методов
    allow_headers=["*"],  # Установить список разрешенных заголовков
)

templates = Jinja2Templates(directory="templates")

# Добавляем путь к статическим файлам
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_vacancy")
def process_vacancy(description: str = Form(...)):
    processed_description = spacy_visualizer(description)
    return processed_description






