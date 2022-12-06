FROM ubuntu

WORKDIR /workdir
COPY . .

RUN apt-get update && apt-get install -y python3
RUN pip install -r requirements.txt
