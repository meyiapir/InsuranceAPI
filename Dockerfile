FROM python:3.9

EXPOSE 8000

WORKDIR /

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
COPY /app /app
COPY main.py /
COPY .env /

CMD ["python", "main.py"]
