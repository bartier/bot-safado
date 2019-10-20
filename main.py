#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import tweepy
import click
import os
from dicio import Dicio

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
        exit(1)



@click.command()
@click.option("--count", default=1, help="Quantidade de frases que deve ser gerada")
@click.option("--saida", required=True,
              help="Arquivo onde deve ser guardadas as frases geradas.")
@click.option("--verbos", required=True,
              help="Arquivo de verbos.")
@click.option("--palavras", required=True,
              help="Arquivo de palavras sem verbos.")
def main(count, saida, verbos, palavras):
    """ Gerador de frases de atos libidinosos. """

    print('Arquivo onde será salvo as frases: ' + saida)

    frases_geradas = []

    for i in range(count):
        print(str(i + 1) + ".")
        verbo_escolhido = escolher_verbo(verbos)
        print('Verbo escolhido --> ' + verbo_escolhido)

        palavra_escolhida = escolher_palavra(palavras)
        print('Palavra escolhida --> ' + palavra_escolhida + '\n')

        frase = gerar_frase(palavra_escolhida, verbo_escolhido)
        print('Frase  --> ' + frase + '\n')
        frases_geradas.append(frase)

    if not os.path.exists(os.path.dirname(saida)):
        diretorio_para_criar = os.path.dirname(saida)
        if diretorio_para_criar != "":
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
