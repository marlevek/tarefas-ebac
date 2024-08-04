import streamlit as st 
import pandas as pd
import numpy as np

st.title('Extração de 20 códigos da Documentação do Streamlit')
st.write('# 1. Criando um DataFrame')
st.write(pd.DataFrame({
    'primeira_coluna': [1, 2, 3, 4],
    'segunda_coluna': [10, 20, 30, 40]
}))

st.markdown('## 2. Amostra aleatória')
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.markdown('<hr style="color: blue;"></hr>', unsafe_allow_html=True)

st.markdown('### 3. Realçando alguns elementos da tabela')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))


st.markdown('<hr style="color: blue;"></hr>', unsafe_allow_html=True)
st.markdown('## Gráficos e Mapas:')

st.markdown('### 4. Gráfico de linha')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

st.markdown('### 5. Histograma')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
st.subheader('Number of pickups by hour')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done! (using st.cache_data)')


hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.markdown('#### 6. Dados brutos')
st.subheader('Raw data')
st.write(data)

# Plotar dados em uma mapa
st.markdown('<hr style="color: blue;"></hr>', unsafe_allow_html=True)
st.markdown('#### 7. Plotando dados em um mapa e filtrar')
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


st.markdown('### 8. Mapa')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)
st.map(map_data)

st.markdown('<hr style="color: blue;"></hr>', unsafe_allow_html=True)
st.markdown('## 9. Widgets:')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.markdown('#### 10. Input')
st.text_input('Seu nome', key='name')
st.session_state.name

st.markdown('<hr style="color: blue;"></hr>', unsafe_allow_html=True)
st.markdown('## 11. Checkboxes e Selectbox:')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# organizando widgets em uma sidebar
# Add a selectbox to the sidebar:
st.markdown('#### 12. Selectbox')
st.markdown('#### 13. Slider')
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
# Mostrar progresso
import time

st.markdown('#### 14. Progresso')
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
st.markdown('#### 15. Escolhendo cor dos dados')
st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

st.markdown('#### 16. Imagem')
st.image('manha.jpg', caption='Manhã')


st.markdown('#### 17. Medidas')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown('#### 18. Escolhendo data')
import datetime 
d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)

st.markdown('#### 19. Câmera')
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))


st.markdown('#### 20. Chat')
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")



