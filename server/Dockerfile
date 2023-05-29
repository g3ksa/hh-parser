FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY data/output/model-best /app/data/output/model-best

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "app.py"]