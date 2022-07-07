FROM python:3.9

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY ./src ./src

COPY ./deployment/nginx.conf ./deployment/nginx.conf
