# %%
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import tweepy as tw
from dotenv import load_dotenv
import pandas as pd
from os import getenv

# %%
load_dotenv('/home/antonio-linux/PROJETOS/Projeto_Eng_Dados_Twitter/.env')

# %%
class Twitter(ABC):

    consumer_key = str(getenv('consumer_key'))
    consumer_secret = str(getenv('consumer_secret'))
    access_token = str(getenv('access_token'))
    access_token_secret = str(getenv('access_token_secret'))
    bearer_token = str(getenv('bearer_token'))

    client = tw.Client(bearer_token=bearer_token,
                            consumer_key=consumer_key,
                            consumer_secret=consumer_secret,
                            access_token=access_token,
                            access_token_secret=access_token_secret)

    @abstractmethod
    def __init__(self, **kwargs) -> None:
        pass

    @abstractmethod
    def _get_api(self):
        pass


# %%
class TwitterApi(Twitter):

    def __init__(self, query: str, max_results: int, final_day: int, initial_day: int) -> None:

        self.query = query
        self.max_results = max_results
        self.final_day = final_day
        self.initial_day = initial_day
    
    def _get_api(self):

        return self.client.search_recent_tweets(
            query=self.query, max_results=self.max_results,
            start_time=datetime.today() - timedelta(days=self.initial_day), end_time=datetime.today() - timedelta(days=self.final_day))

# %%

