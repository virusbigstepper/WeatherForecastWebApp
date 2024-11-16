import streamlit as st
import plotly.express as pl
from backend import get_data

# Added the basic frontend text
st.title('Weather Forecast')
place = st.text_input("Place: ")
days = st.slider("Days to Forecast", min_value=1, max_value=5, help="Number of days to be forecasted for a given "
                                                                    "location.")
option = st.selectbox('Select mode of view', ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
try:
    if place:
        # Get Temperature/sky data
        filtered_data = get_data(place, days)
        # Plot the data accordingly
        if option == "Temperature":
            temp = [dict["main"]["temp"] for dict in filtered_data]
            temperatures = []
            for t in temp:
                t = t / 10
                temperatures.append(t)
            dates =[dict["dt_txt"] for dict in filtered_data]
            graph = pl.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(graph)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds":"images/cloud.png", "Snow": "images/snow.png",
                      "Rain": "images/rain.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=100)
except KeyError:
    st.info("Entered a non-existing place!")
