#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


def main(entrada, saida):
    # Trata o arquivo palavras.txt para remover os verbos (palavras terminadas em ar,er,ir)

    # Ler todas as palavras do arquivo de entrada
    with open(entrada, 'r') as arquivo:
        palavras = [palavra.lower().rstrip() for palavra in arquivo.read().splitlines()]

    # Eliminar todas as palavras que são verbos
    palavras_sem_verbos = [palavra for palavra in palavras if not palavra.endswith(('ar', 'er', 'ir'))]

    # Escrever todas as palavras que não são verbos no arquivo de saída
    with open(saida, 'w') as f:
        for palavra in palavras_sem_verbos:
            f.write("%s\n" % palavra)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--entrada', type=str, required=False, default='palavras.txt',
                        help='Arquivo de entrada contendo as palavras')
    parser.add_argument('--saida', type=str, required=False, default='palavras_sem_verbos.txt',
                        help='Arquivo de saída contendo as palavras sem verbos')

    args = parser.parse_args()
    entrada = args.entrada
    saida = args.saida

    main(entrada, saida)
