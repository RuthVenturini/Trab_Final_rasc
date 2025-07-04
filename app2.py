# -*- coding: utf-8 -*-
"""app2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N7SfRvtdLC5DToITm4ty6X4m9vurTFiz
"""

import streamlit as st
from streamlit_folium import folium_static
import folium

m = folium.Map(location=[-25.5, -49.3], zoom_start=12)
folium.Marker(
        [-25.384618, -49.276169],
        popup="Ópera de Arame",
        icon=folium.Icon(color='gray', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.443083, -49.238214],
        popup="Jardim Botânico",
        icon=folium.Icon(color='green', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.379066, -49.282423],
        popup="Parque Tanguá",
        icon=folium.Icon(color='green', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.410112,-49.26723],
        popup="Museu Oscar Niemeyer",
        icon=folium.Icon(color='blue', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.426372, -49.307217],
        popup="Parque Barigui",
        icon=folium.Icon(color='green', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.400817, -49.334319],
        popup="Santa Felicidade",
        icon=folium.Icon(color='orange', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.404467, -49.288117],
        popup="Bosque do Alemão",
        icon=folium.Icon(color='green', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.427692, -49.273755],
        popup="Feira do Largo da Ordem",
        icon=folium.Icon(color='red', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.452439, -49.364862],
        popup="Memorial da Segurança no Transporte",
        icon=folium.Icon(color='blue', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.44293, -49.290818],
        popup="Shopping Pátio Batel",
        icon=folium.Icon(color='black', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.448305,-49.276924],
        popup="Ligga Arena",
        icon=folium.Icon(color='pink', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.454071, -49.285374],
        popup="Museu de Arte Indígena",
        icon=folium.Icon(color='blue', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.402374, -49.304958],
        popup="Memorial Ucraniano",
        icon=folium.Icon(color='white', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.43816, -49.267398],
        popup="Shopping Estação",
        icon=folium.Icon(color='black', icon='star')
        ).add_to(m)
folium.Marker(
        [-25.415166, -49.272559],
        popup="Museu do Holocausto de Curitiba",
        icon=folium.Icon(color='blue', icon='star')
        ).add_to(m)

PAGE_CONFIG = {"page_title":"Aplicação de Mapas","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():
	st.title("Mapa de Curitiba para rotas turísticas")
	st.subheader("Baseado num caderno do Colab")
	menu = ["Home","Mapa"]
	choice = st.sidebar.selectbox('Menu',menu)
	if choice == 'Home':
		st.subheader("Página Inicial")
	elif choice == 'Mapa':
		st.subheader("Visualizar Mapa")
		with st.echo():
			folium_static(m)
	else:
		st.subheader("")
if __name__ == '__main__':
	main()