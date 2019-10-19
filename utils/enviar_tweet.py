#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tweepy
import click
import random
from dotenv import load_dotenv


def OAuth(consumer_key, consumer_secret, access_token, access_token_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


@click.command()
@click.option('--arquivo-input', required=False, default=None,
              help="Arquivo de frases já criadas. Por default utiliza o arquivo .env com a config "
                   "'arquivo_frases'. --arquivo-input substitui a declaração no .env, isto é, possui prioridade.")
def main(arquivo_input):
    """ Utilizando um arquivo de input como base (--arquivo-input), seleciona uma linha aleatoriamente e envia para o
    Twitter. Por default o arquivo a ser consumido é o declarado no arquivo .env, config 'arquivo_frases'

    É utilizado em conjunto com o arquivo main.py (que gera as frases de atos libidinosos).

    1. Primeiro é gerado uma lista de frases com o arquivo main.py e colocado no diretório declarado na config
    'arquivo_frases' no arquivo .env

    2. As frases são filtradas para verificar se não existe nenhuma frase imprópria (dica: cat <nome_do_arquivo>)

    3. Toda vez que esse script enviar_tweet.py for executado ele removerá automaticamente a linha do arquivo (para
    não existir repetições de tweets).
    """

    load_dotenv()

    if arquivo_input is None:
        arquivo_input = os.environ.get('arquivo_frases')

    consumer_key = os.environ.get('consumer_key')
    consumer_secret = os.environ.get('consumer_secret')

    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')

    print('consumer_key=' + consumer_key)
    print('consumer_secret=' + consumer_secret)
    print('access_token=' + access_token)
    print('access_token_secret=' + access_token_secret + "\n")
    print('arquivo_input=' + arquivo_input + "\n")

    oauth = OAuth(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(oauth)

    with open(arquivo_input, "r") as f:
        frases_geradas = [frase.lower().rstrip() for frase in f.read().splitlines()]

        if len(frases_geradas) > 0:
            frase_para_tweet = random.choice(frases_geradas)
        else:
            print('ERRO: Não há frases no arquivo ' + arquivo_input)
            exit(1)

        frases_geradas.remove(frase_para_tweet)

        print('Frase escolhida --> ' + frase_para_tweet)

    with open(arquivo_input, "w") as f:
        for frase in frases_geradas:
            if frase != frase_para_tweet:
                f.write(frase+"\n")

    if frase_para_tweet is not None and frase_para_tweet != "":
        try:
            api.update_status(frase_para_tweet)
            print('Tweet enviado.')
        except Exception as e:
            print('Não foi possível postar no Twitter, verifique o processo de autenticação.')
            exit(1)


if __name__ == '__main__':
    main()
