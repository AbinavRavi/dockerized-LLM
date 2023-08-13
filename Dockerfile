FROM python:3.10-slim

COPY . .

RUN apt-get update && \
    apt-get install -y g++ make && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry 

RUN poetry install --no-dev

WORKDIR /app

CMD poetry run python download_model.py && \
    poetry run uvicorn infer:app --host 0.0.0.0 --port 8000

EXPOSE 8000