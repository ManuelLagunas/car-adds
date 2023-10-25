#Importamos las librerias necesarias para la aplicación
import streamlit as st
import pandas as pd
import plotly_express as px

#Leemos los datos
car_data = pd.read_csv('vehicles_us.csv')

#Adecuación del datframe 
car_data = car_data.dropna(subset= ['model_year'])
car_data['model_year'] = car_data['model_year'].astype('int')
car_data['paint_color'] = car_data['paint_color'].fillna('Unknown')
car_data['is_4wd'] = car_data['is_4wd'].fillna('Unknown')


#Configuración de la pagina web
st.image('math.jpg')
st.header('Car\'s add data analysis')
st.subheader('Hello, thereeee')
st.markdown('Welcome to the app!')
st.markdown('This app allows you to see in a graphic way the information about some car\'s add that was broadcast in the US. Hope you enjoy it')


#Funcionalidades de la pagina web

#Botón para construir histogramas

st.markdown('### Create an histogram based on the odometer column.')

hist_button = st.button('Draw an histogram')

if hist_button:
    st.write('Drawing an histogram for the car\'s add dataframe, base on the odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

#Botón para construir un grafico de dispersión

st.markdown('### Create a scatter graph based on dodometer vs price.')

scatter_button = st.button('Draw a scatter graph')

if scatter_button:
    st.write('Drawing a scatter graph for the car\'s add dataframe, base on the odometer vs price')
    fig_sct = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_sct, use_container_width=True)

#Crear contenido con checkboxes

st.markdown('### Please select a checkbox. You decide how you want to see the information.')

scatter_check = st.checkbox('Draw a scatter graph')
histogram_check = st.checkbox('Draw an histogram')

if scatter_check:
    st.write('Drawing a scatter graph for the car\'s add dataframe, base on the year vs price')
    check_sct = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(check_sct, use_container_width=True)

if histogram_check:
    st.write('Drawing an histogram for the car\'s add dataframe, base on the model year')
    hist = px.histogram(car_data, x='model_year')
    st.plotly_chart(hist, use_container_width=True)