#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import tweepy
import click
import os
from dicio import Dicio
from dotenv import load_dotenv

dicio = Dicio()


def gerar_frase(palavra_escolhida, verbo_escolhido):
    resultado_dicio = dicio.search(palavra_escolhida)

    genero = verifica_genero(palavra_escolhida, resultado_dicio)

    artigo = 'a' if genero == 'f' else 'o'
    artigo += 's' if eh_plural(resultado_dicio) else ''

    frase = verbo_escolhido + ' ' + artigo + ' ' + palavra_escolhida

    return frase


def verifica_genero(palavra, resultado_dicio):
    try:
        if 'masculino' in resultado_dicio.extra['Classe gramatical']:
            return 'm'
        elif 'feminino' in resultado_dicio.extra['Classe gramatical']:
            return 'f'
        elif resultado_dicio.extra.get("Singular") is not None:
            palavra_singular = resultado_dicio.extra.get("Singular")

            resultado_dicio_singular = dicio.search(palavra_singular)

            return verifica_genero(palavra_singular, resultado_dicio_singular)
    except:
        if palavra.endswith('a'):
            return 'f'
        else:
            return 'm'


def eh_plural(resultado_dicio):
    return resultado_dicio.extra.get('Singular') is not None


def escolher_palavra(arquivo_palavras_sem_verbos):
    with open(arquivo_palavras_sem_verbos) as palavras_sem_verbos:
        lista_palavras_sem_verbos = palavras_sem_verbos.read().split('\n')
        palavra_escolhida = random.choice(lista_palavras_sem_verbos)
    return palavra_escolhida


def escolher_verbo(arquivo_verbo):
    try:
        with open(arquivo_verbo) as verbos:
            lista_verbos = verbos.read().split('\n')
            verbo_escolhido = random.choice(lista_verbos)
        return verbo_escolhido
    except Exception as e:
        print('Verifique os arquivos de verbos.')



@click.command()
@click.option("--count", default=1, help="Quantidade de frases que deve ser gerada")
@click.option("--saida", default=None,
              help="Arquivo onde as frases geradas são guardadas e posteriormente consumidas pelo enviar_tweet.py. Por default utiliza arquivo .env "
                   "com a config 'arquivo_frases'. Caso seja passado a flag --saida, o arquivo será o definido pela flag, isto é, a flag possui mais prioridade ")
def main(count, saida):
    """ Gerador de frases de atos libidinosos. """
    load_dotenv()

    if saida is None:
        saida = os.environ.get('arquivo_frases')

    arquivo_verbos = os.environ.get("arquivo_verbos")
    arquivo_palavras = os.environ.get("arquivo_palavras_sem_verbos")

    print('Arquivo onde será salvo as frases: ' + saida)

    frases_geradas = []

    for i in range(count):
        print(str(i + 1) + ".")
        verbo_escolhido = escolher_verbo(arquivo_verbos)
        print('Verbo escolhido --> ' + verbo_escolhido)

        palavra_escolhida = escolher_palavra(arquivo_palavras)
        print('Palavra escolhida --> ' + palavra_escolhida + '\n')

        frase = gerar_frase(palavra_escolhida, verbo_escolhido)
        print('Frase  --> ' + frase + '\n')
        frases_geradas.append(frase)

    if not os.path.exists(os.path.dirname(saida)):
        diretorio_para_criar = os.path.dirname(saida)
        try:
            os.mkdir(diretorio_para_criar)
        except OSError as e:
            print('ERRO: Não foi possível criar o diretório ' + diretorio_para_criar)
            exit(1)

    with open(saida, 'w+') as f:
        for frase in frases_geradas:
            f.write("%s\n" % frase)


if __name__ == "__main__":
    main()
