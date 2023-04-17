import json
import psycopg2

conn = psycopg2.connect(database="*", user="*", password="*", host="*", port="*")
cur = conn.cursor()

#запись в бд
with open('./pages/db.json', mode='r', encoding='utf8') as f:
    data = json.load(f)

    vac_from = 0 # с какой вакансии добавлять
    vac_to = len(data) # до какой вакансии добавлять
    for i in range(vac_from, vac_to):
        cur.execute(f"INSERT INTO vacancies (vacancy_id, vacancy_name, employer) VALUES ({int(data[i]['id'])}, '{data[i]['name']}', '{data[i]['employer']}')")
        print(i)

conn.commit()
# просмотр добавленных вакансий
cur.execute("SELECT * FROM vacancies")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()