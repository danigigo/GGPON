import streamlit as st
import gspread
import pandas as pd
import matplotlib.pyplot as plt

# Configura la aplicación Streamlit
st.title("Lectura y Gráficos de Google Sheets")
st.write("Esta aplicación lee datos de una hoja de cálculo de Google Sheets y crea gráficos.")

# Conecta a Google Sheets
gc = gspread.service_account(filename='credentialss.json')  # Reemplaza con la ruta de tu archivo JSON de credenciales

# Abre la hoja de cálculo por su URL
sheet_url = "https://docs.google.com/spreadsheets/d/1i6VkbBiR1ePNrWr8zEnw7DDnYEyTUfRrvBty_pJylvM/edit#gid=0"  # Reemplaza con la URL de tu hoja de cálculo
sh = gc.open_by_url(sheet_url)

# Selecciona la hoja de la que deseas leer los datos
worksheet_name = "Hoja1"  # Reemplaza con el nombre de la hoja
worksheet = sh.worksheet(worksheet_name)

# Lee los datos en un DataFrame de Pandas
data = worksheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])

# Muestra los datos en Streamlit
st.write("Datos en Google Sheets:")
st.write(df)

df['cont'] = df['cont']
df['velocidad'] = df['velocidad'].astype(float)

df_first_20 = df.iloc[-20:]


# Crea un gráfico de dispersión Tiempo vs. Velocidad
st.subheader("Gráfico de Tiempo vs. Velocidad")
plt.figure(figsize=(8, 6))
plt.scatter(df_first_20['direccion'], df_first_20['velocidad'])
plt.xlabel("Tiempo")
plt.ylabel("Velocidad")
st.pyplot(plt)