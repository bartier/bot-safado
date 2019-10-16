#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import tweepy
import sys
import os

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']

access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)


def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


def main():
    oauth = OAuth()
    api = tweepy.API(oauth)

    if len(sys.argv) > 1 and sys.argv[1] == '--post-to-twitter':

        frase = "O Bot twittou algo que não devia? Denuncie marcando o bot no tweet com o comando !badbot"

        try:
            api.update_status(frase)
        except Exception as e:
            print('Não foi possível postar no Twitter, verifique o processo de autenticação.')
            exit(1)

        print('\nEnviado ao twitter o post.')
    else:
        print('Não foi utilizado a flag --post-to-twitter para enviar a frase para o Twitter.')


if __name__ == "__main__":
    main()
