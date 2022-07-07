FROM python:3.9-slim-buster

# working directory of container is myportfolio
WORKDIR /myportfolio

# copy requirements.txt into working directory of container
# splitting copy lines so that docker can use layer caching
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# copy contents of current directory into working directory of container
COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
