import streamlit as st
st.title('Dashboard')
c1,c2,c3=st.columns(3)
c1.metric('Users',0);c2.metric('Policies',3);c3.metric('Claims',0)
