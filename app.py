import streamlit as st
from database import init_db
init_db()
st.set_page_config(page_title='DentaSure')
st.title('🦷 DentaSure')
st.write('Use the Pages menu in Streamlit sidebar.')
