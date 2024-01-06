import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


st.title("Application de Distribution normale")
st.subheader("Auteur: Deb")
st.write("Cette application permet d'afficher l'histogramme d'une distribution normale." 
          " L'utilisateur a la possibilité de varier le nombre de bins de l'histogramme"
          " et de donner un titre au graphique")
data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
st.write(data.head())
# or st.dataframe(data.head()) pour afficher un dataframe

#creation d'un graphique avec matplotlib

#plt.hist(data.Dist_norm)
#plt.show #rien ne s'affiche car streamlit a des fonctions dédiés qui fonctionnent avec des librairies comme mtlp seaborn etc
#st.pyplot()
#s'affiche mais y'a un warning car besoin d'un argument qui represente la figure en question et propose un code donc on le met

fig, ax = plt.subplots()
n_bins = st.number_input(
    label="Choisis un nombre de bins",
    min_value=20
)
ax.hist(data.Dist_norm, bins= n_bins)
graph_title = st.text_input(
    label="Choisi un titre"
)
st.title(graph_title)
st.pyplot(fig)
