import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 

sns.set()


def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(
            value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot(fig=plt)
    return None

st.set_page_config(page_title='SINASC Rondônia', layout='wide', page_icon='https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Fpsd-premium%2Fmapa-do-estado-brasileiro-de-rondonia-em-renderizacao-3d-com-fundo-transparente_363450-4872.jpg&tbnid=uWVzc3flqZMVYM&vet=12ahUKEwj9w4TgmvmDAxVAGbkGHcvLBrAQMygTegUIARCQAQ..i&imgrefurl=https%3A%2F%2Fbr.freepik.com%2Fpsd-premium%2Fmapa-do-estado-brasileiro-de-rondonia-em-renderizacao-3d-com-fundo-transparente_42729634.htm&docid=Dmt-SwGvESZhqM&w=626&h=446&q=mapa%20rond%C3%B5nia&ved=2ahUKEwj9w4TgmvmDAxVAGbkGHcvLBrAQMygTegUIARCQAQ')
st.write('# Análise Sinasc')

sinasc = pd.read_csv('C:/Users/marce/Curso_Ciencia_de_Dados_Ebac/002_Cientista_de_dados/Modulo-15_streamlit/SINASC_RO_2019.csv')

sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)

min_data = sinasc.DTNASC.min()
max_data = sinasc.DTNASC.max()

st.write(min_data)
st.write(max_data)

datas = sinasc.DTNASC.unique()
# dataframe = pd.DataFrame(datas).sort_values(by='date')
st.dataframe(datas)

data_inicial = st.date_input('Data inicial', value=min_data, min_value=min_data, max_value=max_data)

data_final = st.date_input('Data final', value=max_data, min_value=min_data, max_value=max_data)

st.write('Data Inicial', data_inicial)
st.write('Data Final', data_final)


plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean',
                  'média idade mãe por data', 'data nascimento')

plota_pivot_table(sinasc, 'IDADEMAE', [
                  'DTNASC', 'SEXO'], 'mean', 'media idade mae', 'data de nascimento', 'unstack')

plota_pivot_table(sinasc, 'PESO', [
                  'DTNASC', 'SEXO'], 'mean', 'media peso bebe', 'data de nascimento', 'unstack')

plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median',
                  'PESO mediano', 'escolaridade mae', 'sort')

plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean',
                  'apgar1 medio', 'gestacao', 'sort')


