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
  st.header('Bitcoin, BTC')
  st.write('Price(USD) = 1,866,276')
  st.write('Market Cap(USD) = 35,577,749,997,460.60')

elif option=='Ethereum':
  st.header('Ethereum, ETH')
  st.write('Price(USD) = 106,307')
  st.write('Market Cap(USD) = 12,875,584,996,925.90')
    
elif option=='Solana':
  st.header('Solana, SOL')
  st.write('Price(USD) = 2,396')
  st.write('Market Cap(USD) = 13,537,594,562')
    
elif option=='BNB':
  st.header('Binance, BNB')
  st.write('Price(USD) = 17,867')
  st.write('Market Cap(USD) = 46,801,210,081')
    
elif option=='Wrapped Bitcoin':
  st.header('Wrapped Bitcoin, WBTC')
  st.write('Price(USD) = 1,864,354')
  st.write('Market Cap(USD) = 8,241,528,653')
        
        
        
    
