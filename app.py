import streamlit as st
st.title("Flight Delaying Detector")
    # st.subheader("ML App with Streamlit")
html_temp = """
    <div style="background-color:blue;padding:10px">
    <h1 style="color:white;text-align:center;">Streamlit ML App </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
 
AIRLINE= st.text_input("AIRLINE","Type Here",key='1')
ORIGIN_AIRPORT= st.text_input("ORIGIN_AIRPORT","Type Here",key='2')
DESTINATION_AIRPORT=st.text_input("DESTINATION_AIRPORT","Type Here",key='3')
SCHEDULED_DEPARTURE= st.text_input("SCHEDULED_DEPARTURE","Type Here",key='4')
DEPARTURE_TIME= st.text_input("DEPARTURE_TIME","Type Here",key='5')
DEPARTURE_DELAY= st.text_input("DEPARTURE_DELAY","Type Here",key='6')
SCHEDULED_ARRIVAL= st.text_input("SCHEDULED_ARRIVAL","Type Here",key='7')
ARRIVAL_TIME= st.text_input("ARRIVAL_TIME","Type Here",key='8')