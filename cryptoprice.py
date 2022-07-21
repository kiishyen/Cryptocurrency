import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Top 5 Cryptocurrency Price Monitor
This app shows you Top 5 Cryptocurrency Price and it's Market Supply
""")
st.image('https://www.hp.com/us-en/shop/app/assets/images/uploads/prod/cryptocurrency-trends_-is-bitcoin-mining-profitable-in-2021162075307076393.jpg')


option = st.sidebar.selectbox(
    'Select a Cryptocurrency',
     ['Bitcoin', 'Ethereum', 'Solana', 'BNB', 'Wrapped Bitcoin'])
if option=='Bitcoin':
  st.header('Bitcoin')
  st.write('Price(USD) = 1,866,276')
  st.write('Market Cap = 35,577,749,997,460.60')

