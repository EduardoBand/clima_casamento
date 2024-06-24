import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests
import json
import os
from datetime import datetime, timedelta, date


st.title('Histórico de condição climática')
st.subheader('Consulte as temperaturas e os índices de chuva com registros dos últimos 10 anos.')
st.sidebar.title('Insira as informações')

d = st.sidebar.date_input(
    "Escolha um dia para verificar o histórico de previsão:", 
    date(2023, 11, 23),
    format="DD/MM/YYYY"
)

#adicionar sidebar. para deixar ao lado 
st.sidebar.text_input("Digite a latitude:", key="latitude", value= -23.758344762315005)

st.sidebar.text_input("Digite a longitude:", key="longitude", value= -46.454074119562854)

if st.sidebar.button("Pesquisar"):
    map_data = pd.DataFrame([
        {
            'latitude': float(st.session_state.latitude),
            'longitude': float(st.session_state.longitude)
        }
    ])
    st.title('Localização:world_map:')
    st.map(map_data, zoom=15, size=50)

    current_date = datetime.now()
    ten_years_history = current_date - timedelta(days=365.25*10) #contando leap years

    payload = {
        "latitude": float(st.session_state.latitude),
        "longitude": float(st.session_state.longitude),
        "start_date": ten_years_history.strftime("%Y-%m-%d"),
        "end_date": current_date.strftime("%Y-%m-%d"),
        "hourly": [
            "temperature_2m",
            "precipitation",
            "rain"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "rain_sum",
            "precipitation_hours"
        ],
        "timezone": "America/Sao_Paulo"
    }

    file_name = "response.json"

    if os.path.exists(file_name):
        with open(file_name, "r") as arquivo:
            response = json.load(arquivo)
    else:
        response = requests.get(url="https://archive-api.open-meteo.com/v1/archive", params=payload).json()
        with open(file_name, "w") as arquivo:
            json.dump(response, arquivo)

    daily_data = response.get('daily', {})
    df_daily = pd.DataFrame(daily_data)
    df_daily['time'] = pd.to_datetime(df_daily['time'])

    filtered_daily_df = df_daily[
        (df_daily['time'].dt.month == d.month) & (df_daily['time'].dt.day == d.day)
    ]

    hourly_data = response.get('hourly', {})
    df_hourly = pd.DataFrame(hourly_data)
    df_hourly['time'] = pd.to_datetime(df_hourly['time'])
    
    filtered_hourly_df = df_hourly[
        (df_hourly['time'].dt.month == d.month) * (df_hourly['time'].dt.day == d.day)
    ]
#apenas algumas modificações visuais
    new_column_names = {
        'temperature_2m': 'Temperatura',
        'precipitation': 'Quantidade de chuva',
        'temperature_2m_max': 'Temp Máxima',
        'temperature_2m_min': 'Temp Mínima',
        'rain_sum': 'Quantidade de chuva',
        'precipitation_hours': 'Horas de chuva',
        'time': 'Data'
    }
    filtered_daily_df.rename(columns=new_column_names, inplace=True)
    filtered_hourly_df.rename(columns=new_column_names, inplace=True)
    filtered_daily_df.index.name = 'Posição'
    filtered_hourly_df.index.name = 'Posição'
    filtered_daily_df['Data'] = filtered_daily_df['Data'].dt.strftime('%d/%m/%Y')
    filtered_hourly_df['Data'] = filtered_hourly_df['Data'].dt.strftime('%d/%m/%Y %H:%M')
    filtered_daily_df.drop(columns=["precipitation_sum"],inplace=True)
    filtered_hourly_df.drop(columns=['rain'], inplace=True)

#fim das modificações

#dados tabulares
    st.title('Histórico Diário:calendar:')
    st.dataframe(filtered_daily_df)

    st.title('Histórico por Hora:watch:')
    st.dataframe(filtered_hourly_df)
    
#gráfico    
    st.title('Gráfico de Temperatura:mostly_sunny:')
    chart_data = pd.DataFrame(filtered_daily_df)
    st.line_chart(
        filtered_daily_df,
        x="Data",
        y=["Temp Mínima", "Temp Máxima"],
        color=["#FF0000", "#0000FF"],
    )
    st.title('Gráfico de Chuva :rain_cloud:')
    st.bar_chart(
        filtered_daily_df,
        x="Data",
        y=["Horas de chuva"],
        color=["#1E90FF"]
    )

 #https://docs.streamlit.io/develop/api-reference/charts   
#-23.758344762315005, -46.454074119562854
