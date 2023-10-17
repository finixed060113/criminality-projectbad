import streamlit as st
import pandas as pd
# importamos matplotlibexpres
import plotly.express as px
import folium


st.title("Criminality Project")
st.markdown("## **Visualización de conjunto de datos**")



df = pd.read_csv("../data/crims2010-22.csv")


# Obtener una lista de nombres únicos de la columna 'name'
nombres = df['name'].unique()

# Widget para permitir a los usuarios elegir entre mostrar todos o nombres específicos
mostrar_todos = st.checkbox("Mostrar todos los nombres")

# Widget para que el usuario elija uno o más nombres
if mostrar_todos:
    nombres_elegidos = nombres
else:
    nombres_elegidos = st.multiselect("Elige uno o más nombres:", nombres)

# Filtrar el DataFrame según los nombres elegidos
df_filtrado = df[df['name'].isin(nombres_elegidos)]

# Mostrar los datos del DataFrame filtrado
st.write("Datos para nombres elegidos:", df_filtrado)

