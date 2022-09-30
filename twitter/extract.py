# %%
import tweepy as tw
from dotenv import load_dotenv
from os import getenv
#%%
load_dotenv('/home/antonio-linux/PROJETOS/Projeto_Eng_Dados_Twitter/.env')
api_key = str(getenv('api_key'))
api_key_secret = str(getenv('api_key_secret'))
access_token = str(getenv('access_token'))
access_token_secret = str(getenv('access_token_secret'))
#%%
#stream = tw.Stream(api_key, api_key_secret, access_token, access_token_secret)
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
#%%
api = tw.Client(auth)
#public_tweets = api.home_timeline()
# %%
public_tweets = api.search_all_tweets(query='voto')
# %%
for tweet in public_tweets:
    print(tweet.text)
# %%
