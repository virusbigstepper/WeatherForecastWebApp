import streamlit as st
import plotly.express as pl

st.title('Weather Forecast')
place = st.text_input("Place: ")
days = st.slider("Days to Forecast", min_value=1, max_value=5, help="Number of days to be forecasted for a given "
                                                                    "location.")
option = st.selectbox('Select mode of view', ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    date = ["2024-11-15", "2024-11-16", "2024-11-17"]
    temperature = [11, 13, 16]
    temperature = [days * i for i in temperature]
    return date , temperature


d, t = get_data(days)

graph = pl.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(graph)