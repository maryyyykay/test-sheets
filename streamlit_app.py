import streamlit as st
import pandas as pd
import pygsheets

credenciais = pygsheets.authorize(service_file="/cred.json")
meuArquivoGoogleSheets = "https://docs.google.com/spreadsheets/d/1j3ZvFZutEHyfExBPSgX-5wBgLdReDwA-INYnayFfXF0/edit?gid=0#gid=0"
arquivo = credenciais.open_by_url(meuArquivoGoogleSheets)
aba = arquivo.worksheet_by_title ("stream")
data = aba.get_all_values()
df = pd.DataFrame(data)

st.title("Aprendendo a Conectar o Google Sheets ao Streamlit")
st.write("Conexão com Google Sheets")
st.write(df)
