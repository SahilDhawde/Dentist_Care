import streamlit as st
from services.risk_engine import calculate_score
from services.disease_prediction import predict
from services.recommendation import recommend
st.title('Risk Assessment')
d={'smoker':st.checkbox('Smoker'),'diabetes':st.checkbox('Diabetes'),'bleeding':st.checkbox('Bleeding Gums'),'caries':st.checkbox('Previous Caries')}
if st.button('Calculate'):
 s=calculate_score(d)
 st.metric('Score',s)
 st.json(predict(d))
 st.write('Recommended Plan:',recommend(s))
