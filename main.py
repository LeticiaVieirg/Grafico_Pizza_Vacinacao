import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv('/content/vacinacao_corrigido.csv')

fig2=px.line(df,x='date', y='total_vaccinations', color='location',
             title='Total de pessoas vacinadas por data e país - Segundo OMS')

fig2.update_layout(xaxis_title='Data', yaxis_title='Total de pessoas vacinadas')
fig2.show()

st.plotly_char(fig2, use_container_width=True)
