import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
# ==========================================================================================
# CONFIGURATION
# ==========================================================================================

# Avec cette option la page prend toute la largeur -> V2
# st.set_page_config(layout="wide")

# Création de la liste des datasets
dataframe_list = ['anagrams','anscombe','attention','car_crashes','car_crashes','dots','dowjones', 'exercise', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']

# ==========================================================================================
# TITRE
# ==========================================================================================

with st.container(border=True, horizontal_alignment='center',width='stretch'):
        st.title("Manipulation de données et création graphiques",text_alignment='center')


# ==========================================================================================
# SELECTION DU DATASET
# ==========================================================================================
with st.container(border=True):
        choix = st.selectbox(
                "Quel dataset veux-tu utiliser?",
                (dataframe_list)
        )
        url = f"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/{choix}.csv"
        df = pd.read_csv(url)
        st.dataframe(df.dropna(axis=0,))

# ==========================================================================================
# SELECTION DES COLONNES DU DATASET
# ==========================================================================================     
with st.container(border=True):
        col_x = st.selectbox(
                        "Choisi la colonne X",
                        (df.columns)
                )
        col_y = st.selectbox(
                        "Choisi la colonne Y",
                        (df.columns)
                )

        # ==========================================================================================
        # SELECTION DES GRAPHIQUES
        # ==========================================================================================
        graph_list = ['line_chart', 'bar_chart', 'scatter_chart']

        choix_graph = st.selectbox(
                "Quel graphique veux-tu utiliser?",
                (graph_list)
        )

        if choix_graph == 'line_chart':
                st.line_chart(df.dropna(), x = col_x, y = col_y)
        elif choix_graph == 'bar_chart':
                st.bar_chart(df.dropna(), x = col_x, y = col_y)
        elif choix_graph == 'scatter_chart':
                st.scatter_chart(df.dropna(), x = col_x, y = col_y)


# ==========================================================================================
# AFFICHAGE DE LA HEATMAP DE CORRELATION
# ==========================================================================================
agree = st.checkbox("Afficher la matrice de corrélation")

if agree:
        df1 = sns.load_dataset(choix)
        plt.figure(figsize=(10, 8))
        sns.heatmap(df1.select_dtypes('number').corr(), annot=True, cmap='coolwarm')
        st.pyplot(plt)
