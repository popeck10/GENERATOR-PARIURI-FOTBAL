
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title='Generator Ponturi Fotbal', layout='wide')

st.title('Generator Automat de Ponturi pentru Fotbal')

echipa = st.text_input('Introdu numele echipei (ex: AC Milan)')

if echipa:
    # Exemplu de apel API pentru date în timp real (API fictiv)
    url = f'https://api.fotbal.com/echipe?search={echipa}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.subheader(f'Informații pentru echipa {echipa}')
        st.write('Cote:', data.get('cote'))
        st.write('Ponturi:', data.get('ponturi'))
        st.write('Ultimele întâlniri:', data.get('ultime_intalniri'))
        st.write('Jucători accidentați:', data.get('jucatori_accidentati'))
        st.write('Goluri marcate per meci:', data.get('goluri_per_meci'))
        st.write('Forma echipei:', data.get('forma_echipei'))
        st.write('Media de goluri pe meci:', data.get('media_goluri_pe_meci'))
        st.write('Clasament:', data.get('clasament'))
    else:
        st.error('Nu s-au găsit informații pentru această echipă.')
