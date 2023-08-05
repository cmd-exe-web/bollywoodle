# Dockerfile

FROM python:3.9

WORKDIR /home/app

COPY requirements.txt /home/app/

RUN pip install --no-cache-dir -r /home/app/requirements.txt

COPY . /home/app

CMD ["python", "src/server.py"]
