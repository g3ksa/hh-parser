import time
import requests
import json
from bs4 import BeautifulSoup

file = open('./pages/ids.csv', mode='r', encoding='utf8')
iddata = list(filter(None, file.read().split('\n')))
file.close()
items_from = 0
items_to = len(iddata)
jsout = []
try:
    for i in range(items_from, items_to):
        req = requests.get(f'https://api.hh.ru/vacancies/{iddata[i]}')
        data = req.content.decode()
        req.close()
        jsObj = json.loads(data)
        cleantext = BeautifulSoup(jsObj['description'], "html.parser").text
        print(i)
        jsout.append({'id': jsObj['id'], 'name': jsObj['name'], 'employer': jsObj['employer']['name'], 'description': cleantext})
        time.sleep(0.1)
except:
    print('failed')

file = open(f'./pages/db{items_from}.json', mode='w', encoding='utf8')
file.write(json.dumps(jsout, ensure_ascii=False, indent=2))
file.close()