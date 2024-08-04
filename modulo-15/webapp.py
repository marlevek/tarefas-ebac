import streamlit as st

st.write('# Bem-Vindo')
st.title('Bem-Vindo')
st.header('Bem-Vindo')
st.subheader('Bem-Vindo')

st.markdown('# Texto com markdown e um [#]')
st.markdown('## Texto com markdown e dois [#]')
st.markdown('### Texto com markdown e três [#]')

st.markdown('----')

st.markdown('Markdown')
st.markdown('_Markdown itálico_')
st.markdown('*Markdown itálico*')
st.markdown('__Markdown negrito__')
st.markdown('**Markown negrito**')
st.markdown('__*Markown negrito e itálico*__')

st.markdown('Isso é um link para o [google](https://www.google.com)')
st.markdown('<h5 style="color: red;">Texto h5 em vermelho</h5>', unsafe_allow_html=True)

st.markdown('Olá Mundo :sunglasses:')
