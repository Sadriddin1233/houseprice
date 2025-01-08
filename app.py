import streamlit as st
import pandas as pd
import pickle

# Modelni yuklash
with open('homeprice.pkl', 'rb') as f:
    model = pickle.load(f)

# Kiruvchi parametrlar
st.title("Uy narxini bashorat qilish")
bedrooms = st.number_input("Xonalar soni", min_value=1, step=1)
bathrooms = st.number_input("Hammomlar soni", min_value=1, step=1)
sqft_living = st.number_input("Yashash maydoni (kvadratmetr)", min_value=500, step=50)

# Bashorat qilish
if st.button("Narxni bashorat qilish"):
    input_data = pd.DataFrame({
        'Kvadrat metr': [sqft_living],
        'Hammomlar soni': [bedrooms],
        'Lot olchami': [bathrooms]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Bashorat qilingan narx: {prediction:.2f} $")
