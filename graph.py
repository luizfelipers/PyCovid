

##Importar libs do Python

import numpy as np
import pandas as pd
import os
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#importar Dataset do Covid19, que está na mesma pasta deste arquivo de código python
#Dataset referente ao numero de mortes e casos
dataframe = pd.read_csv("brazil_covid19.csv")

#salvar as colunas numa variável
cols = dataframe.columns

#Formatar a coluna 'date' do arquivo CSV para o formato de datas utilizando pandas
dataframe['date'] = pd.to_datetime(dataframe['date'])

# transformar as datas como índice da tabela
df = dataframe.set_index('date')

# Cortar o mês de março
marchdf = df['2020-03-01':'2020-03-31']


#Fiquei confuso na hora de extrair o último dia do mês e fiz na unha, via gambiarra. Ia fazer usando .max() mas me perdi
ultimodia = marchdf['2020-03-31':'2020-03-31']

#Agrupar os dados de casos e mortes de cada Estado, por Região do Brasil, e somá-los em suas colunas
region = ultimodia.groupby(['region']).sum()

#Conferir os dados do ultimo dia
print(region)

###PLOTLY DASH

#Graph Objs
fig = go.Figure(data=[

    #Barra de baixo - Mortes
 go.Bar(name='deaths', x=region.index, y=region['deaths']),
    #Barra de cima - Casos
 go.Bar(name='cases', x=region.index, y=region['cases'])])

#Layout do gráfico
fig.update_layout(barmode='stack', title='COVID 19 - Gráfico empilhado de casos e mortes por região do Brasil, no mês de Março(2020) pós-Carnaval .')

#Renderizar gráfico
fig.show()

