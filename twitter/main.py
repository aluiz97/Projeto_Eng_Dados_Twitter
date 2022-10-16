# %%
import scrape
from datetime import date

# %%
scrape_tw = scrape.TwitterScrape('Ukraine', date(2022, 10, 5), date(2022, 10, 8))
# %%
data = scrape_tw.get_data(500)
# %%
