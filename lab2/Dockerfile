FROM python:3.8

WORKDIR /workdir
COPY . .

RUN apt-get update \
    && apt-get install -y iputils-ping
RUN pip3 install -r requirements.txt
CMD ["./script.py", "--host=ya.ru", "--loglevel=INFO"]
# CMD ["./script.py", "--host=ya.ru"]