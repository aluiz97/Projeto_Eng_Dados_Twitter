import tweepy
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')
api_key = getenv('api_key')
api_key_secret = getenv('api_key_secret')
access_token = getenv('acess_token')
access_token_secret = getenv('acess_token_secret')

stream = tweepy.Stream(api_key, api_key_secret, access_token, access_token_secret)

stream.filter(track=['voto', 'eleicao'])