import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Top 5 Cryptocurrency Price Monitor
This app shows you Top 5 Cryptocurrency Price and it's Market Supply
""")
st.image('https://www.hp.com/us-en/shop/app/assets/images/uploads/prod/cryptocurrency-trends_-is-bitcoin-mining-profitable-in-2021162075307076393.jpg')



# read data into a DataFrame
import pandas as pd
data = pd.read_csv('API.csv', sep=';')
data.head()
