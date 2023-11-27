FROM python:3.11

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "82", "--workers", "4"]