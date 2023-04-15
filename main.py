import requests
import json
import time
import datetime

def getPage(date_from, date_to, page):
    # Справочник для параметров GET-запроса
    params = {
        #'text': '', # Текст фильтра. https://tyumen.hh.ru/article/1175 - параметры фильтрации DESCRIPTION:текст
        'area': 95, # 95 - код Тюмени, 1342 - код Тюменской области
        'page': page, # Индекс страницы поиска на HH
        'per_page': 100, # Кол-во вакансий на 1 странице, больше 100 нельзя
        'date_from': date_from,
        'date_to': date_to
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data

vacancies_id = []
vacancies_names = []
vacancies_employers = []
start_time = datetime.datetime.now() - datetime.timedelta(days=30) #hhru выдает вакансии только за последний месяц
end_time = datetime.datetime.now()
filename = 0

while start_time <= end_time:
    interval_end = start_time + datetime.timedelta(hours=12) # сбор вакансий с интервалом в 12 часов
    start_time_iso = start_time.isoformat()
    interval_end_iso = interval_end.isoformat()
    for page in range(0, 20):
        jsObj = json.loads(getPage(start_time_iso, interval_end_iso, page))
        try:
            for i in range(0, len(jsObj['items'])):
                vacancies_id.append(jsObj['items'][i]['id'])
                vacancies_names.append(jsObj['items'][i]['name'])
                vacancies_employers.append(jsObj['items'][i]['employer']['name'])
        except:
            print('so')
        nextFileName = f'./pages/{filename}.json'
        # запись в json
        f = open(nextFileName, mode='w', encoding='utf8')
        f.write(json.dumps(jsObj, ensure_ascii=False))
        f.close()

        # проверка на последнюю страницу
        if (jsObj['pages'] - page) <= 1:
            break

        # задержка между страницами
        time.sleep(0.1)
        filename+=1
        print(filename)
    start_time = interval_end


#вывод айдишников в файл
listFileName = f'./pages/ids.txt'
f = open(listFileName, mode='w', encoding='utf8')
for i in range(0, len(vacancies_id)):
    str = vacancies_id[i] + '|' + vacancies_names[i] + '|' + vacancies_employers[i] + '\n'
    f.write(str)

f.close()
print('готово')