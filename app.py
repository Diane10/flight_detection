import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import pickle
st.title("Flight Delaying Detector")
    # st.subheader("ML App with Streamlit")
html_temp = """
    <div style="background-color:blue;padding:10px">
    <h1 style="color:white;text-align:center;">Streamlit ML App </h1>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
 'ORIGIN', 'DEST', 'DISTANCE', 'Carrier mean distance',
        'Origin Delay', 'Origin TaxiOut']]
model=pickle.load(open('models.pkl','rb'))        
MONTH= st.text_input("MONTH","Type Here",key='1')
DAY_OF_MONTH= st.text_input("DAY_OF_MONTH","Type Here",key='2')
DAY_OF_WEEK=st.text_input("DAY_OF_WEEK","Type Here",key='3')
CRS_DEP_TIME= st.text_input("CRS_DEP_TIME","Type Here",key='4')
ORIGIN= st.text_input("ORIGIN","Type Here",key='5')
DEST= st.text_input("DEST","Type Here",key='6')
DISTANCE= st.text_input("DISTANCE","Type Here",key='7')
Carriermeandistance= st.text_input("Carrier mean distance","Type Here",key='8')
OriginDelay= st.text_input("Origin Delay","Type Here",key='9')
OriginTaxiOut= st.text_input("Origin TaxiOut","Type Here",key='10')
if st.button("predict"):
   input=np.array([[MONTH,DAY_OF_MONTH,DAY_OF_WEEK, CRS_DEP_TIME,ORIGIN,DEST,DISTANCE,Carriermeandistance,OriginDelay,OriginTaxiOut]]).astype(np.float64)
   prediction=model.predict(input)
    
