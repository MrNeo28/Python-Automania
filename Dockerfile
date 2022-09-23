FROM python:3.10

WORKDIR /python-automania

COPY . .

RUN pip install -r requirements.txt

RUN chmod 777 run.sh
RUN ./run.sh