import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model_save_path = "potato_sifra__model.pkl"
with open(model_save_path, 'rb') as file:
    loaded_model = pickle.load(file)

# Sidebar with input field descriptions and symbols
st.sidebar.header("📝 Description of The Required Input Fields")
st.sidebar.markdown("**📍 Province**: The provinces producing POTATO SIFRA (WASHED).")
st.sidebar.markdown("**📏 Size_Grade**: The sizes of the POTATO SIFRA (WASHED) packages.")
st.sidebar.markdown("**⚖️ Weight_Kg**: The weight of POTATO SIFRA (WASHED) in kilogram.")
st.sidebar.markdown("**💰 Low_Price**: The lowest price the POTATO SIFRA (WASHED) cost in the market.")
st.sidebar.markdown("**🛒 Sales_Total**: The total price purchase POTATO SIFRA (WASHED).")
st.sidebar.markdown("**📦 Stock_On_Hand**: The POTATO SIFRA (WASHED) stock currently available in the warehouse.")

# Streamlit interface
st.title("🥔 POTATO SIFRA (WASHED) Average Price Prediction")
st.image("/Users/da-m1-18/Downloads/PotatoWashed.webp")

background_image_url = "/Users/da-m1-18/Downloads/l-intro-1698258359.jpg"
background_css = f"""
<style>
    .stApp {{
        background: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)

# Function to preprocess user inputs and make predictions
def predict_price(Province, Size_Grade, Weight_Kg, Low_Price, Sales_Total, Stock_On_Hand, month, day):
    # Assuming label encoding mappings are known
    province_mapping = {
        'NORTHERN CAPE': 2, 'WESTERN CAPE - CERES': 7, 'WEST COAST': 6, 'SOUTH WESTERN FREE STATE': 4, 
        'WESTERN FREESTATE': 8, 'NATAL': 1, 'KWAZULU NATAL': 0, 'OTHER AREAS': 3, 'TRANSVAAL': 5
    }
    size_grade_mapping = {
        '1R': 2, '1M': 1, '1Z': 5, '2L': 6, '2Z': 11, '3M': 13, '1S': 3, '3R': 14, '2M': 7, '1U': 4, '3Z': 17,
        '1L': 0, '2S': 9, '2R': 8, '4Z': 21, '3L': 12, '3U': 16, '4M': 19, '4L': 18, '3S': 15, '2U': 10, '4R': 20
    }
    # Convert categorical inputs to numerical using label encoding
    province_encoded = province_mapping.get(Province, -1)  # Use -1 for unknown categories
    size_grade_encoded = size_grade_mapping.get(Size_Grade, -1)  # Use -1 for unknown categories

    # Prepare input data as a DataFrame for prediction
    input_data = pd.DataFrame(
        [[province_encoded, size_grade_encoded, Weight_Kg, Low_Price, Sales_Total, Stock_On_Hand, month, day]],
        columns=['Province', 'Size_Grade', 'Weight_Kg', 'Low_Price', 'Sales_Total', 'Stock_On_Hand', 'month', 'day']
    )

    # Make prediction
    predicted_price = loaded_model.predict(input_data)
    return predicted_price[0]

# Input fields in columns
col1, col2 = st.columns(2)
with col1:
    Province = st.selectbox('📍 Province', ['NORTHERN CAPE', 'WESTERN CAPE - CERES', 'WEST COAST', 'SOUTH WESTERN FREE STATE', 
                                            'WESTERN FREESTATE', 'NATAL', 'KWAZULU NATAL', 'OTHER AREAS', 'TRANSVAAL'])
    Size_Grade = st.selectbox("📏 Size Grade", ['1R', '1M', '1Z', '2L', '2Z', '3M', '1S', '3R', '2M', '1U', '3Z',
                                               '1L', '2S', '2R', '4Z', '3L', '3U', '4M', '4L', '3S', '2U', '4R'])
    Weight_Kg = st.number_input("⚖️ Weight per kilo (kg)", min_value=0.0)
    Low_Price = st.number_input("💰 Low Price (R)", min_value=0.0)
with col2:
    Sales_Total = st.number_input('🛒 Total Sale (R)', min_value=0.0)
    Stock_On_Hand = st.number_input('📦 Stock on Hand', step=1, min_value=0)
    month = st.slider("📅 Month", 1, 12)
    day = st.slider("📅 Day", 1, 31)

# Make prediction
if st.button("🔮 Predict"):
    prediction_price = predict_price(Province, Size_Grade, Weight_Kg, Low_Price, Sales_Total, Stock_On_Hand, month, day)
    st.success(f'Predicted Average Price of POTATO SIFRA (WASHED): R{prediction_price:.2f}')
    st.balloons()  # Add some celebratory balloons for a successful prediction!

