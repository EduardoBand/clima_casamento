import pandas as pd
from typing import Optional, List, Dict, Any
from datetime import datetime


def create_weather_dataframe(
    weather_frequency_dict: Dict[str, Any], 
    exclude_columns: Optional[List[str]] = []
) -> pd.DataFrame:
    """
    This function creates the dataframe according to the parameters set, together with new column names and drops of useless ones.
    
    Parameters:
        weather_frequency_dict: creates a dictionary with the values from the df_weather
        exclude_columns: exclude the undesired columns.
        
    Returns: 
        pd.DataFrame: create dataframe. 
    
    """
    df_weather = pd.DataFrame(weather_frequency_dict)
    df_weather["time"] = pd.to_datetime(df_weather["time"])

    if exclude_columns:
        df_weather.drop(exclude_columns, inplace=True)
    
    new_column_names = {
        "temperature_2m": "Temperatura",
        "precipitation": "Quantidade de chuva",
        "temperature_2m_max": "Temp Máxima",
        "temperature_2m_min": "Temp Mínima",
        "rain_sum": "Quantidade de chuva",
        "precipitation_hours": "Horas de chuva",
        "time": "Data",
    }
    df_weather.rename(columns=new_column_names, inplace=True)

    return df_weather


def filter_weather_dataframe(df: pd.DataFrame, date_to_filter: datetime) -> pd.DataFrame:
    """
    This function filters the weather dataframe.
    
    Parameters:
        df(pd.DataFrame): historical dataframe to filter. 
        date_to_filter(datetime): user specified time to filter within the dataframe.
        
    Returns: 
        pd.DataFrame: filtered dataframe. 
    
    """
    df_copy = df.copy()
    df_copy_filtered = df_copy[
        (df_copy["Data"].dt.month == date_to_filter.month)
        & (df_copy["Data"].dt.day == date_to_filter.day)
    ]
    return df_copy_filtered