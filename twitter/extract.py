# %%
import datetime
from abc import ABC, abstractmethod
import tweepy as tw
from dotenv import load_dotenv
import pandas as pd
from os import getenv

# %%
load_dotenv('/home/antonio-linux/PROJETOS/Projeto_Eng_Dados_Twitter/.env')

api_key = str(getenv('api_key'))
api_key_secret = str(getenv('api_key_secret'))
access_token = str(getenv('access_token'))
access_token_secret = str(getenv('access_token_secret'))
bearer_token = str(getenv('bearer_token'))

# %%
api = tw.Client(bearer_token=bearer_token,
                consumer_key=api_key,
                consumer_secret=api_key_secret,
                access_token=access_token,
                access_token_secret=access_token_secret)
#public_tweets = api.home_timeline()
# %%
class TwitterAPI(ABC):

    def __init__(self) -> None:
        super().__init__()

    #start = '2022-09-26T23:39:01Z'
    #end = '2022-10-02T23:40:01Z'
    #resposta = api.search_recent_tweets(
#    query='minas gerais', max_results=100, start_time=start, end_time=end)