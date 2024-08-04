
# Imports
import pandas as pd
import streamlit as st

from io import BytesIO
from pycaret.classification import load_model, predict_model


def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


# Função para converter o df para excel
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data


# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(
        page_title='PyCaret',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    # Título principal da aplicação
    st.write("""## Escorando o modelo gerado no pycaret """)
    st.markdown("---")
    
    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader(
        "Bank Credit Dataset", 
         type=['csv', 'ftr'])

    # Verifica se há conteúdo carregado na aplicação
    if (data_file_1 is not None):
        df_credit = pd.read_feather(data_file_1)
        df_credit = df_credit.sample(50000)

        model_saved = load_model('Final_LGBM_Model_03Ago2024')
        predict = predict_model(model_saved, data=df_credit)

        df_xlsx = to_excel(predict)
        st.download_button(label='📥 Download',
                            data=df_xlsx,
                            file_name='predict.xlsx')
        
        # Carregar modelo treinado
        try:
            modelo_treinado = load_model('Final_LGBM_Model_03Ago2024')
        except FileNotFoundError:
            st.error("Modelo 'Final LGBM Model 03Ago2024.pkl' não encontrado. Certifique-se de que o arquivo está no diretório.")
            return
        
        # Predições
        predict = predict_model(modelo_treinado, data=df_credit)
        
        # Mostrar resultados
        st.write('Resultados da escoragem: ')
        st.write(predict[['prediction_label', 'prediction_score']].head())
        
        
        
if __name__ == '__main__':
    main()
    









