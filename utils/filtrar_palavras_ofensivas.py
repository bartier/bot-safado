#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


# Filtra palavras ofensivas nos arquivos palavras_sem_verbos.txt e verbos.txt.
def main(palavras_entrada, verbos_entrada, filtro_entrada, palavras_saida, verbos_saida):
    # Lê os arquivos de entrada
    palavras = cria_lista_por_arquivo(palavras_entrada)
    verbos = cria_lista_por_arquivo(verbos_entrada)
    palavras_proibidas = cria_lista_por_arquivo(filtro_entrada)

    # Filtra palavras e verbos
    palavras_sem_verbos_filtradas = [palavra for palavra in palavras if palavra not in palavras_proibidas]
    verbos_filtrados = [verbo for verbo in verbos if verbo not in palavras_proibidas]

    # Escrever as palavras e verbos filtrados em seus respectivos arquivos
    escreve_saida(palavras_saida, palavras_sem_verbos_filtradas)
    escreve_saida(verbos_saida, verbos_filtrados)


def cria_lista_por_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return [linha.lower().rstrip() for linha in arquivo.read().splitlines()]


def escreve_saida(nome_arquivo, lista):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write("%s\n" % item)
        arquivo.truncate(arquivo.tell() - 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--palavras-entrada', type=str, required=False, default='palavras_sem_verbos.txt',
                        help='Arquivo de entrada contendo as palavras')
    parser.add_argument('--verbos-entrada', type=str, required=False, default='verbos.txt',
                        help='Arquivo de entrada contendo os verbos')
    parser.add_argument('--filtro-entrada', type=str, required=False, default='palavras_ofensivas.txt',
                        help='Arquivo de entrada contendo palavras ofensivas a serem filtradas')
    parser.add_argument('--palavras-saida', type=str, required=False, default='palavras_filtradas.txt',
                        help='Arquivo de saída contendo as palavras filtradas')
    parser.add_argument('--verbos-saida', type=str, required=False, default='verbos_filtrados.txt',
                        help='Arquivo de saída contendo os verbos filtrados')

    args = parser.parse_args()
    palavras_entrada = args.palavras_entrada
    verbos_entrada = args.verbos_entrada
    filtro_entrada = args.filtro_entrada
    palavras_saida = args.palavras_saida
    verbos_saida = args.verbos_saida

    main(palavras_entrada, verbos_entrada, filtro_entrada, palavras_saida, verbos_saida)
