import streamlit as st
import joblib
import numpy as np

# Chargement du modèle
model = joblib.load('modele.pkl')

st.title("🔧 Simulateur de prédiction de panne")

st.write("Remplissez les valeurs suivantes pour prédire s'il y aura une panne ou non.")

# Création des sliders pour entrer les variables
footfall = st.slider("footfall", 0.0, 500.0, 100.0)
AQ = st.slider("AQ", 0.0, 100.0, 50.0)
USS = st.slider("USS", 0.0, 100.0, 50.0)
CS = st.slider("CS", 0.0, 100.0, 50.0)
VOC = st.slider("VOC", 0.0, 100.0, 50.0)
RP = st.slider("RP", 0.0, 100.0, 50.0)
IP = st.slider("IP", 0.0, 100.0, 50.0)
Temperature = st.slider("Temperature", 0.0, 100.0, 25.0)

if st.button("Prédire"):
    # Préparation des données
    input_data = np.array([[footfall, AQ, USS, CS, VOC, RP, IP, Temperature]])
    
    # Prédiction
    prediction = model.predict(input_data)[0]
    
    # Affichage du résultat
    if prediction == 1:
        st.error("🛑 Panne probable")
    else:
        st.success("✅ Pas de panne")
