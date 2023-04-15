import requests
import json
import time
import os

def getPage(page = 0):
    # Справочник для параметров GET-запроса
    params = {
        'text': 'DESCRIPTION:текст', # Текст фильтра. https://tyumen.hh.ru/article/1175 - параметры фильтрации
        'area': 1342, # 95 - код Тюмени, 1342 - код Тюменской области
        'page': page, # Индекс страницы поиска на HH
        'per_page': 100 # Кол-во вакансий на 1 странице, больше 100 нельзя
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


# считать 20 страниц по 100 вакансий, больше не дает
for page in range(0, 20):
    jsObj = json.loads(getPage(page))

    nextFileName = f'./pages/{page}.json'

    # запись в json
    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    # Проверка на последнюю страницу, если вакансий меньше 2000
    if (jsObj['pages'] - page) <= 1:
        break

    # задержка между страницами
    time.sleep(0.25)

print('готово')