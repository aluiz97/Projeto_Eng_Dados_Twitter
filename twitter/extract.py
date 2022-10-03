# %%
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
start = '2022-09-26T23:39:01Z'
end = '2022-10-02T23:40:01Z'
# %%

resposta = api.search_recent_tweets(
    query='tebet', max_results=100, start_time=start, end_time=end)
# %%
dados = resposta.data

# %%
base = []

# %%
for i in dados:

    linha = [0 for j in range(6)]

    linha[0] = i.text

    texto = i.text

    if ('RT' in texto):
        posicao = texto.find(':')
        texto = texto[posicao+2:]
        linha[5] = 1

    linha[1] = 1 if ('bozo' in texto.lower()
                     or 'bolsonaro' in texto.lower()) else 0
    linha[2] = 1 if ('lula' in texto.lower()) else 0
    linha[3] = 1 if ('ciro gomes' in texto.lower()
                     or 'ciro' in texto.lower()) else 0
    linha[4] = 1 if ('simone tebet' in texto.lower()
                     or 'tebet' in texto.lower()) else 0

    base.append(linha)

# %%
baseEleicao = pd.DataFrame(base)
baseEleicao.columns = ['texto', 'bolsonaro', 'lula', 'ciro', 'tebet', 'RT']
display(baseEleicao)

# %%
baseView = baseEleicao.drop(['texto', 'RT'], axis=1)
# %%
comentarios = baseView.sum().sort_values(ascending=False).to_list()

# %%
participantes = baseView.sum().sort_values(ascending=False).index.to_list()
base2 = pd.DataFrame(zip(participantes, comentarios))
base2.columns = ['pessoas', 'comentarios']
display(base2)
# %%
total_comentarios = base2['comentarios'].sum()

base2['perc'] = base2['comentarios']/total_comentarios
display(base2)  # %%

# %%
base2['perc_acum'] = base2['perc'].cumsum()
display(base2)

# %%
base2['perc_form'] = base2['perc'].map("{:.1%}".format)
base2['perc_acum_form'] = base2['perc_acum'].map("{:.1%}".format)
display(base2)

# %%
display(base2[['pessoas', 'comentarios', 'perc_form', 'perc_acum_form']])
# %%
api.search_recent_tweets(query='tebet', max_results=100,
                         start_time=start, end_time=end)


