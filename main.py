import streamlit as st

st.title('Weather Forecast')
place = st.text_input("Place: ")
days = st.slider("Days to Forecast", min_value=1, max_value=5, help="Number of days to be forecasted for a given "
                                                                    "location.")
option = st.selectbox('Select mode of view', ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
