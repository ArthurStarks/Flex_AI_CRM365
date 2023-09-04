import streamlit as st
import os
from TargetJournee import TargetJournee  # Assurez-vous que cette fonction existe et est importée correctement
import pandas as pd
import aspose.words as aw
import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyperclip
# Configuration des pages
st.set_page_config(
    page_title="Bienvenue chez Flex IA",
    page_icon="👋",
)

#Positionnement du logo en haut de la page 
from PIL import Image

def show_logo():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "flex.png")
    logo = Image.open(logo_path)
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

# Liste des options pour le premier bouton radio
options1 = list(options.keys())[:1]

# Liste des options pour le deuxième bouton radio
options2 = list(options.keys())[1:]

# Créer le premier bouton radio avec l'option "visible" sélectionnée
page = st.sidebar.radio("Que voulez-vous faire ? 👇", options1, index=0)

# Créer le deuxième bouton radio et le désactiver
selected_option2 = st.sidebar.radio("", options2, index=0, disabled=True)

#Fonction pour le mail 
def send_email(subject, message, sender_email, sender_password, receiver_email):
    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #Create server object with SSL option
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Perform operations via server
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Afficher le logo en haut de chaque page
show_logo()
# Afficher les options dans une grille 2x4 sur la page d'accueil
if page == 'Homepage':
    col1, col2 = st.columns(2)
    for option in options:
        if option == 'Daily Task':
            # Afficher le bouton 'Daily Task' en couleur normale
            col = col1 if options[option] % 2 == 0 else col2
            col.button(f"{options[option]} {option}")
        else:
            # Afficher les autres boutons en couleur grise et désactivés
            col = col1 if options[option] % 2 == 0 else col2
            col.button(f"{options[option]} {option}", disabled=True, key=option, help='Option désactivée')

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

        # Add a button to copy the generated text to clipboard
    if st.button('Copier'):
            pyperclip.copy(prompt)
            # Display the copied text again to prevent it from disappearing
            st.write(prompt)

        # Add a button to send the generated text via email
    col1, col2 = st.columns(2) # Create two columns for the logos and buttons
    col1.image("gmail.png", width=50) # Display the gmail logo in the first column
    col2.image("outlook.png", width=50) # Display the outlook logo in the second column
        
    if col1.button('Gmail'): # Create a button with Gmail in the first column
            sender_email = st.text_input("Entrez votre adresse email Gmail", type="password")
            sender_password = st.text_input("Entrez votre mot de passe Gmail", type="password")
            receiver_email = st.text_input("Entrez l'adresse email du destinataire")
            send_email("Daily Task", prompt, sender_email, sender_password, receiver_email)
        
    if col2.button('Outlook'): # Create a button with Outlook in the second column
            sender_email = st.text_input("Entrez votre adresse email Outlook", type="password")
            sender_password = st.text_input("Entrez votre mot de passe Outlook", type="password")
            receiver_email = st.text_input("Entrez l'adresse email du destinataire")
            send_email("Daily Task", prompt, sender_email, sender_password, receiver_email)
            
####################   Partie Fitgap  ######################################################################################################################################################

# Upload user's file


@st.cache_data
def analyze_data(df):
    # Analyze the data here
    # ...
    return df

if page == 'Fitgap':
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