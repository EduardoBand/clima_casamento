import requests
from datetime import datetime, timedelta


def get_meteo_10_years_weather_data(latitude: float, longitude: float) -> dict:
    """
    This function is the API request to create the JSON file.
    
    Parameters:
        latitude: the user inputed latitude. 
        longitude: the user inputed longitude.
        
    Returns: 
        dict: a dictionary with all the the info requested from the API. 
    
    """
    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": (datetime.now() - timedelta(days=365.25 * 10)).strftime("%Y-%m-%d"),
        "end_date": datetime.now().strftime("%Y-%m-%d"),
        "hourly": ["temperature_2m", "precipitation"],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "rain_sum",
            "precipitation_hours",
        ],
        "timezone": "America/Sao_Paulo",
    }

    return requests.get(
        url="https://archive-api.open-meteo.com/v1/archive", 
        params=payload
    ).json()