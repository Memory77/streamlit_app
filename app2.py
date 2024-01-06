#deux cas possibles lorsqu'on parle de visualisation des données avec streamlit 
#premier cas : fonctions de streamlit dédié a la datavisualisation dans stlit il y a des fonctions intégrés qui vont
#permettre de construire des graphiques directement en utilisant le pack stlit sans utiliser d'autres packge dédiés comme mtlib seaborn etc

#fonctions pour la datavisualisation intégré dans stlit : 

import streamlit as st
import pandas as pd
import numpy as np

st.title("Initialisation à la Data Visualisation avec Streamlit")
st.subheader("Auteur : Deb")
st.markdown("Cette application affiche différents types de graphiques")

# tracé linéaire(st.line_chart)
st.write("Voici nos valeurs random qui suivent une loi normal de taille 500")
random_data = np.random.normal(size=500)
st.write(random_data)
st.line_chart(random_data)

# diagramme à barre(st.bar_chart)
bar_data = pd.DataFrame(
    [100, 19, 88, 54],
    ["A","B", "C", "D"]
)
st.write(bar_data.head())
st.bar_chart(bar_data)

#carte(st.map)
df1 = pd.read_csv("AB_NYC_2019.csv").head(100) #.head(100) si on veut prendre que les 100 premiers du fichier
df1 = df1[['id','name','longitude', "latitude"]] #filtrage des champs que je veux
st.write(df1.head(20))
st.map(df1[['longitude', 'latitude']])




df2 = pd.read_csv("Automobile_data.csv")
st.write(df2.head(20))

