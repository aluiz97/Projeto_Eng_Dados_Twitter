# %%
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import twitter as tw
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

    auth = tw.oauth.OAuth(access_token,
                          access_token_secret,
                          consumer_key,
                          consumer_secret)

    client = tw.Twitter(auth=auth)

    @abstractmethod
    def __init__(self, **kwargs) -> None:
        pass

    @abstractmethod
    def _get_api(self):
        pass


# %%
class TwitterApi(Twitter):

    def __init__(self, query: str, max_results: int) -> None:

        self.query = query
        self.max_results = max_results
    
    def _get_api(self):

        return self.client.search.tweets(
            q=self.query, count=self.max_results)

# %%

api = TwitterApi('Champions', 50)._get_api()
# %%
