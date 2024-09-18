FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

# Use a process manager or run both commands properly
CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]
