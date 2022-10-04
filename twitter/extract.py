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

    def __init__(self) -> None:

        self.consumer_key = str(getenv('consumer_key'))
        self.consumer_secret = str(getenv('consumer_secret'))
        self.access_token = str(getenv('access_token'))
        self.access_token_secret = str(getenv('access_token_secret'))
        self.bearer_token = str(getenv('bearer_token'))

        self.client = tw.Client(bearer_token=self.bearer_token,
                        consumer_key=self.consumer_key,
                        consumer_secret=self.consumer_secret,
                        access_token=self.access_token,
                        access_token_secret=self.access_token_secret)

    @abstractmethod
    def _get_api(self, **kwargs) -> None:
        pass


# %%
class TwitterApi(Twitter):

    def _get_api(self, query: str, max_results: int) -> None:

        return self.client.search_recent_tweets(
            query=query, max_results=max_results, start_time=datetime.today() - timedelta(days=4), end_time=datetime.today())

# %%
twitterApi = TwitterApi
# %%
api = twitterApi._get_api(twitterApi,'Barcelona', 100)
# %%
