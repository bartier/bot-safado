FROM python:3.7

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

ARG consumer_key
ARG consumer_secret
ARG access_token
ARG access_token_secret

ENV consumer_key=$consumer_key
ENV consumer_secret=$consumer_secret

ENV access_token=$access_token
ENV access_token_secret=$access_token_secret

COPY . /app
WORKDIR /app
CMD python main.py --verbos utils/verbos.txt --palavras utils/palavras_sem_verbos.txt --saida "/safadeza-generator/frases.txt"