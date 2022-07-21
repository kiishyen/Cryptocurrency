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
    'Select Cryptocurrency',
     ['Bitcoin', 'Ethereum', 'BNB', 'Solana', 'Wrapped Bitcoin'])
if option=='Bitcoin':
  df = pd.DataFrame('Price in USD'(1,866,276),0)
                    

# Display a static table
st.dataframe(df)
