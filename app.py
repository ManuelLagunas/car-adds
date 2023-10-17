#Importamos las librerias necesarias para la aplicación
import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff

#Leemos los datos
car_data = pd.read_csv('vehicles_us.csv')

#Adecuación del datframe 
car_data = car_data.dropna(subset= ['model_year'])
car_data['model_year'] = car_data['model_year'].astype('int')
car_data['paint_color'] = car_data['paint_color'].fillna('Unknown')
car_data['is_4wd'] = car_data['is_4wd'].fillna('Unknown')
df_sample = car_data.head(20)

#Configuración de la pagina web
st.header('Car\'s add data analysis')
st.subheader('Hello, thereeee')
st.markdown('Welcome to the app!')
st.markdown('This app allows you to see in a graphic way the information about some car\'s add that was broadcast in the US. Hope you enjoy it')
st.markdown('### First take a look to a sample of the data.')

#Funcionalidades de la pagina web

#Tabla para visualizar los datos
table_button = st.button('See the 20 firts rows of the table')

if table_button:
    st.write('Please see the sample table in the window that just open')
    tab = ff.create_table(df_sample)
    tab.show()

#Botón para construir histogramas
hist_button = st.button('Draw an histogram')

if hist_button:
    st.write('Drawing an histogram for the car\'s add dataframe, base on the odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

#Botón para construir un grafico de dispersión
scatter_button = st.button('Draw a scatter graph')

if scatter_button:
    st.write('Drawing a scatter graph for the car\'s add dataframe, base on the odometer vs price')
    fig_sct = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_sct, use_container_width=True)