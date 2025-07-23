import pandas as pd
import plotly.express as px
import streamlit as st

# Título principal de la aplicación
st.header('Análisis de Datos de Anuncios de Venta de Coches')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma de la distribución de kilometraje')

if build_histogram: # si la casilla está marcada
    st.write('Construyendo un histograma para la columna de kilometraje')
    # Crear el histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el histograma interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión de kilometraje vs precio')

if build_scatter: # si la casilla está marcada
    st.write('Construyendo un gráfico de dispersión de kilometraje vs precio')
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar el gráfico de dispersión interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)