import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#combiner plotly avec streamlit pour créer des graphiques intéractifs

st.subheader("Plotly")

temps = pd.DataFrame(
    {'day': ['Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'],
     'temps': [28,27,25,31,32,35,36]}
)
st.write(temps)

#diagramme à bar interactif

fig = px.bar(
    data_frame= temps, x="day",
    y='temps', title ='températures moyennes journalières'
)
st.plotly_chart(fig)

#nuage de points interactif
cars = pd.read_csv('Automobile_data.csv')
st.dataframe(cars)

numeric_cols = cars.select_dtypes(exclude='object').columns.to_list()
var_x = st.selectbox("Choisis la variable en abscisse", numeric_cols)
var_y = st.selectbox("Choisis la variable en ordonnée", numeric_cols)
categorical_cols = cars.select_dtypes(exclude='object').columns.to_list()
var_col = st.selectbox("gradient", categorical_cols)
fig2 = px.scatter(
    data_frame = cars,
    x=var_x,
    y=var_y,
    color = var_col,
    title = str(var_y) + ' vs ' +str(var_x)
)

st.plotly_chart(fig2)


############ Seaborn et Matplotlib #############

airbnb = pd.read_csv('AB_NYC_2019.csv')
st.subheader("Seaborn")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(airbnb["availability_365"])
plt.xlabel("Nombre de jours d'occupation de l'appartement sur l'année")
st.pyplot(fig_sb)

# construction de la meme chose mais avec matplotlib : 

st.subheader("Matplotlib")
fig_mt, ax_mt = plt.subplots()
ax_mt = plt.hist(airbnb["availability_365"])
plt.xlabel("Nombre de jours d'occupation de l'appartement sur l'année")
st.pyplot(fig_mt)