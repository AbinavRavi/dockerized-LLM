FROM python:3.10-slim

COPY . .

RUN apt-get update && \
    apt-get install -y g++ make && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry 

RUN poetry install

WORKDIR /app

CMD python download_model.py && \
    uvicorn infer:app --host 0.0.0.0 --port 8000

# RUN python download_model,py

# CMD ["uvicorn", "infer:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000