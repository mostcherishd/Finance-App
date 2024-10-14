FROM python:3.13.0a5-slim-bullseye
WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python","run.py", "runserver", "0.0.0.0:8000" ]    