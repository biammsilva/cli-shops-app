FROM python:3.6

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN [ "python", "./setup.py"]
ENTRYPOINT [ "python", "./main.py"]