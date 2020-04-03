FROM python:3.7

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

ENV count=1

COPY . /app
WORKDIR /app
CMD python main.py --verbos utils/verbos_filtrados.txt --palavras utils/palavras_filtradas.txt --saida "output/frases.txt" --count $count