#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tweepy
import click
import random


def OAuth(consumer_key, consumer_secret, access_token, access_token_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


@click.command()
@click.option('--arquivo-input', required=True,
              help="Arquivo de frases já criadas.")
def main(arquivo_input):
    """ Utilizando um arquivo de input como base (--arquivo-input), seleciona uma linha aleatoriamente e envia para o
    Twitter.'

    É utilizado em conjunto com o arquivo main.py (que gera as frases de atos libidinosos).
    """
    consumer_key = os.environ.get('consumer_key')
    consumer_secret = os.environ.get('consumer_secret')

    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')

    print('consumer_key=' + str(consumer_key))
    print('consumer_secret=' + str(consumer_secret))
    print('access_token=' + str(access_token))
    print('access_token_secret=' + str(access_token_secret) + "\n")
    print('arquivo_input=' + str(arquivo_input) + "\n")

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
