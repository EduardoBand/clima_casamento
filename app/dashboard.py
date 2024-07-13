import pandas as pd
import streamlit as st
from datetime import datetime, date


def create_latitude_text_sidebar() -> float:
    latitude = st.sidebar.text_input(
        "Digite a latitude:", value=-23.758344762315005, key="latitude_input"
    )
    return float(latitude)


def create_longitude_text_sidebar() -> float:
    longitude = st.sidebar.text_input(
        "Digite a longitude:", value=-46.454074119562854, key="longitude_input"
    )
    return float(longitude)


def create_weather_forecast_date_sidebar() -> datetime:
    selected_date = st.sidebar.date_input(
        "Escolha um dia para verificar o histórico de previsão:",
        date(2023, 11, 23),
        key="date_input",
    )
    return selected_date


def create_map(latitude: float, longitude: float):
    st.title("Localização")
    map_data = pd.DataFrame(
        [
            {
                "latitude": latitude, 
                "longitude": longitude
            }
        ]
    )
    st.map(map_data, zoom=15, size=50)


def create_table_dataframe(df: pd.DataFrame, title: str):
    st.title(title)
    st.dataframe(df)


def create_temperature_chart(temperature_df: pd.DataFrame):
    st.title("Gráfico de Temperatura:mostly_sunny:")
    st.line_chart(
        temperature_df,
        x="Data",
        y=["Temp Mínima", "Temp Máxima"],
        color=["#FF0000", "#0000FF"]
    )


def create_rain_chart(rain_df: pd.DataFrame):
    st.title("Gráfico de Chuva :rain_cloud:")
    st.bar_chart(rain_df, x="Data", y=["Horas de chuva"], color=["#1E90FF"])
