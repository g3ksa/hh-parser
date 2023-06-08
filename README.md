# hh-parser

# Запуск программы

* С помощью docker:

```bash
docker compose -f docker-compose.yml up -d
```

* Без помощи docker:
  1. Клиентская часть
     ```bash
     cd ./app
     npm install
     npm start
     ```
  2. Серверная часть
     ```bash
     cd ../server
     pip install -r requirements.txt
     python app.py
     ```
