FROM python:3.9

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "database.py", ">>", "/api/output.txt" ]
