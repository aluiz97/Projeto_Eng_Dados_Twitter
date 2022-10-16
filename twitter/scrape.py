# %%
from datetime import date
from abc import ABC, abstractmethod
import snscrape.modules.twitter as sntwitter

# %%

class Scrape(ABC):

    @abstractmethod
    def __init__(self, **kwargs) -> None:
        pass

    @abstractmethod
    def get_data(self, **kwarks):
        pass


# %%
class TwitterScrape(Scrape):

    def __init__(self, query: str, initial_date: date, final_date: date) -> None:

        since = f"{initial_date.year}-{initial_date.month}-{initial_date.day}"
        until = f"{final_date.year}-{final_date.month}-{final_date.day}"
        
        search = f'{query} since:{since} until:{until}'

        global tweets
        tweets = sntwitter.TwitterSearchScraper(search).get_items()

    def get_data(self, maxTweets: int) -> list:

        tweet_list = []
        i = 0

        for tweet in tweets:

            if i > maxTweets:
                break

            tweet_list.append([tweet.date, tweet.url, tweet.username,
                               tweet.content, tweet.likeCount, tweet.replyCount, 
                               tweet.coordinates, tweet.place, tweet.mentionedUsers])

            i += 1
        
        return tweet_list
