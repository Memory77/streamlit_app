#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

st.write("Hello World!")

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
ax.hist(data.Dist_norm)
st.pyplot(fig)