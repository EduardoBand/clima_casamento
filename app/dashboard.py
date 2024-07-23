import pandas as pd
import streamlit as st
from datetime import datetime, date


def create_latitude_text_sidebar() -> float:
    """
    This function creates a latitude input sidebar on the app.
    
    Returns:
        float: latitude position

    """
    latitude = st.sidebar.text_input(
        "Digite a latitude:", value=-23.758344762315005, key="latitude_input"
    )
    return float(latitude)


def create_longitude_text_sidebar() -> float:
    """
    This function creates a longitude input sidebar on the app.
    
    Returns:
        float: longitude position
    """
    longitude = st.sidebar.text_input(
        "Digite a longitude:", value=-46.454074119562854, key="longitude_input"
    )
    return float(longitude)


def create_weather_forecast_date_sidebar() -> datetime:
    """
    This function is a user input sidebar to select a date to create the weather forecast info. The placeholder is the original wedding date.
        
    Returns: 
        datetime: day and month to compare. 
    
    """    
    selected_date = st.sidebar.date_input(
        "Escolha um dia para verificar o histórico de previsão:",
        date(2023, 11, 23),
        key="date_input",
    )
    return selected_date


def create_map(latitude: float, longitude: float):
    """
    This function creates the map according to the latitude and longitude.
    
    Parameters:
        latitude: a float with the location's latitude. 
        longitude: a float with the location's longitude. 
        
    """    
    st.title("Localização :world_map:")
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
    """
    This function creates a dataframe table for better visualization of the data.
    
    Parameters:
        df(pd.DataFrame): it takes the dataframe to create the table. 
        title: the title of the dataframe.
        
    Returns: 
        pd.DataFrame: filtered dataframe. 
    
    """
    st.title(title)
    st.dataframe(df)


def create_temperature_chart(temperature_df: pd.DataFrame):
    """
    This function creates a temperature chart for comparison.
    
    Parameters:
        temperature_df: filtered data with the max and min temperatures of the selected dates.
    
    """
    st.title("Gráfico de Temperatura:mostly_sunny:")
    st.line_chart(
        temperature_df,
        x="Data",
        y=["Temp Mínima", "Temp Máxima"],
        color=["#FF0000", "#0000FF"]
    )


def create_rain_chart(rain_df: pd.DataFrame):
    """
    This function creates a rain chart similar to the temperature chart.
    
    Parameters:
        rain_df: filtered data from the rain parameter.
    
    """
    st.title("Gráfico de Chuva :rain_cloud:")
    st.bar_chart(rain_df, x="Data", y=["Horas de chuva"], color=["#1E90FF"])
