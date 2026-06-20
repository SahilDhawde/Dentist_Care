import streamlit as st
from database import conn
st.title('Claims')
amt=st.number_input('Amount',0.0)
if st.button('Submit'):
 d=conn();c=d.cursor();c.execute('INSERT INTO claims(user_email,amount,status) VALUES(?,?,?)',('demo',amt,'Submitted'));d.commit()
 st.success('Submitted')
