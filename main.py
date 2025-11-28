import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv('vacinacao_corrigido.csv')

fig2=px.line(df,x='date', y='total_vaccinations', color='location',
             title='Total de pessoas vacinadas por data e país - Segundo OMS')

fig2.update_layout(xaxis_title='Data', yaxis_title='Total de pessoas vacinadas')
fig2.show()

st.plotly_chart(fig2, use_container_width=True)

df_filtro=df.query('location == "BRAZIL" or location == "INDIA" or location =="UNITED STATES"')

fig3=px.pie(df_filtro, values='people_fully_vaccinated', 
            names='location', title='Dados comparativos de pessoas totalmente vacinadas')
fig3.show()

st.plot_chart(fig3, user_container_width=True)
