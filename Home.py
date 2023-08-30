import streamlit as st
from TargetJournee import TargetJournee  # Assurez-vous que cette fonction existe et est importée correctement
import pandas as pd
import aspose.words as aw
# Configuration des pages
st.set_page_config(
    page_title="Bienvenue chez Flex IA",
    page_icon="👋",
)

#Positionnement du logo en haut de la page 
from PIL import Image

def show_logo():
    logo = Image.open("flex.png")
    st.image(logo, width=100)

# Définissez les options et leurs emojis
options = {
    'Daily Task': '🔍',
    'Fitgap': '🔍',
    'Modélisation': '📐',
    'Emailing': '📧',
    'Développement js': '💻',
    'Développement plugins': '🔌',
    'Power automate': '⚙️',
    'Learning CRM 365': '📚',
    'Spécifications': '📋',
    'Last day tasks': '🔍',
}

# Créez une page d'accueil avec 8 boutons
page = st.sidebar.radio("Que voulez-vous faire ?", list(options.keys()))
# Afficher le logo en haut de chaque page
show_logo()
# Afficher les options dans une grille 2x4 sur la page d'accueil
if page == 'Homepage':
    col1, col2 = st.columns(2)
    for i, option in enumerate(options):
        col = col1 if i % 2 == 0 else col2
        col.button(f"{options[option]} {option}")
else:
    st.title(f"Je suis l'Agent CRM FLEX - {page} à votre service")



    if page == 'Daily Task':
        client = st.text_input("Entrer le nom du client")
        language = st.selectbox("Choisir une langue", ["Anglais", "Francais"])

        # Add a section for the user to enter their targets
        user_targets = st.text_area("Entrer le contexte :", height=30)
        targets = st.text_area("Entrer les objectifs de la journée", height=350)
        if st.button('Générer les tâches de la journée'):
            prompt = TargetJournee(client, targets, language, user_targets)
            st.write(prompt)
            st.write("Cliquez sur le bouton ci-dessous pour copier la réponse dans votre presse-papiers :")
            # Copy the response to the clipboard
            st.button("Copier")
###########################################Partie Fitgap######################################################################################################################################################

# Upload user's file


@st.cache_data
def analyze_data(df):
    # Analyze the data here
    # ...
    return df

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(df)
    
    analyzed_df = analyze_data(df)
    
    # Save the analyzed data to a new Excel file
    analyzed_df.to_excel("analyzed_file.xlsx", index=False)
    
    st.success("New analyzed Excel file generated!")
    
    # Add a download button for the generated file
    st.download_button(label="Download analyzed file", data=open("analyzed_file.xlsx", "rb"), file_name="analyzed_file.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
