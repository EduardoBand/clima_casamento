from app.historical_weather import get_meteo_10_years_weather_data
from app.data_preprocess import create_weather_dataframe, filter_weather_dataframe
from app.dashboard import create_latitude_text_sidebar, create_longitude_text_sidebar, create_weather_forecast_date_sidebar,create_map, create_table_dataframe, create_temperature_chart, create_rain_chart

import streamlit as st


def main():
    """
    This function creates a dashboard with historical weather data in a 10-year-span using the functions in the app. 
    
    """
    
    st.title("Histórico de condição climática :umbrella_with_rain_drops:")
    st.subheader("Consulte as temperaturas e os índices de chuva com registros dos últimos 10 anos.")

    st.sidebar.title("Insira as informações")
    latitude = create_latitude_text_sidebar()
    longitude = create_longitude_text_sidebar()
    weather_forecast_date = create_weather_forecast_date_sidebar()

    if st.sidebar.button("Pesquisar"):
        historical_weather_dict = get_meteo_10_years_weather_data(latitude, longitude)
        df_daily = create_weather_dataframe(historical_weather_dict["daily"])
        df_hourly = create_weather_dataframe(historical_weather_dict["hourly"])

        df_daily_filtered = filter_weather_dataframe(df_daily, weather_forecast_date)
        df_hourly_filtered = filter_weather_dataframe(df_hourly, weather_forecast_date)

        create_map(latitude, longitude)

        create_table_dataframe(df_daily_filtered, title="Dados Diários Filtrados:calendar:")
        create_table_dataframe(df_hourly_filtered, title="Dados Horários Filtrados:watch:")

        create_temperature_chart(df_daily_filtered)
        create_rain_chart(df_daily_filtered)


if __name__ == "__main__":
    main()
