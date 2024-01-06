import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data():
    data = pd.read_csv('AB_NYC_2019.csv')
    return data

data = load_data()

# Prendre un échantillon aléatoire de 1000 lignes des données pour le graphique
sample_data = data.sample(n=400, random_state=42)

# Titre de l'application
st.title('Analyse des prix des appartements à New York')

# Afficher les premières lignes des données (optionnel)
st.write("Aperçu des données:")
st.write(sample_data.head())


# Créer un graphique à barres pour afficher les prix par quartier à New York
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='neighbourhood', y='price', data=sample_data, ax=ax)
plt.title('Prix des appartements par quartier à New York')
plt.xlabel('Quartier')
plt.ylabel('Prix')
plt.xticks(rotation=90)  # Faites pivoter les étiquettes de l'axe x pour une meilleure lisibilité
plt.tight_layout()

# Afficher le graphique dans Streamlit en passant la figure comme argument
st.pyplot(fig)

