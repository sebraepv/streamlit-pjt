import streamlit as st
import pandas as pd

st.set_page_config(page_title='Escritório de Projetos', page_icon = "📋")

st.markdown("""
# Boas vindas ao App de Gestão de Marcos críticos!

Utilize este repositório para acompanhar o andamento dos marcos críticos.             

""")

csv_projetos = r'C:\Users\paulo.goncalves\OneDrive - SEBRAE\Área de Trabalho\streamlit-projeto\marcos-criticos-pjt-pmo.csv'

# Leitura dos dados
df = pd.read_csv(csv_projetos, sep = ';')
df['prazo_entrega'] = df['prazo_entrega'].str.replace('Não informado', '')

df.drop(['id'], axis = 1, inplace=True)

df['dt_entrega'] = pd.to_datetime(df['dt_entrega'], format="%d/%m/%Y").dt.date
df['prazo_entrega'] = pd.to_datetime(df['prazo_entrega'], format="%d/%m/%Y").dt.date

df.set_index('prazo_entrega', inplace=True)

# Marcos por dia
qtd_status = df['status'].value_counts()
entregas_dia = df['dt_entrega'].value_counts().sort_index()
lista_projetos = df['projeto'].unique()


# Abas do App
tab_data, tab_contagem, tab_prazos = st.tabs(['Dados', 'Status de Entregas', 'Lista de Projetos'])

with tab_data:
    # date = st.date_input(
    #     "Prazo de Entrega",
    #     min_value=df['dt_entrega'].min(),
    #     max_value=df['dt_entrega'].max()
    # )
    st.dataframe(df)

with tab_contagem:
    st.bar_chart(qtd_status)

with tab_prazos:
    st.dataframe(lista_projetos, hide_index=True)
    # st.bar_chart(entregas_dia)
