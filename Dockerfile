FROM python:3.10-slim

COPY . .

RUN pip install poetry && poetry install

RUN poetry run python app/download,py

WORKDIR /app

CMD ["uvicorn", "infer:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000