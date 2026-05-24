import streamlit as st
import joblib
import pandas as pd


# Load trained model
model = joblib.load('best_car_price_model.pkl')

# Load training columns
training_columns = joblib.load('model_columns.pkl')

st.title("Japan Car Price Prediction")

# User inputs
year = st.number_input("Year", min_value=1990, max_value=2024, value=2010)

mileage = st.number_input(
    "Mileage (km)",
    min_value=0,
    value=50000
)

engine_cc = st.number_input(
    "Engine (CC)",
    min_value=500,
    value=1500
)

model_code = st.text_input(
    "Model Code",
    value="ABC123"
)

# Create input dataframe
input_data = pd.DataFrame({
    'Year': [year],
    'Mileage (km)': [mileage],
    'Engine (CC)': [engine_cc],
    'Model Code': [model_code]
})

if st.button("Predict Price"):

    # Encode categorical variables
    input_encoded = pd.get_dummies(input_data)

    # Match training columns
    input_encoded = input_encoded.reindex(
        columns=training_columns,
        fill_value=0
    )

    # Predict
    predicted_price = model.predict(input_encoded)[0]

    st.success(
        f"Predicted Price: ${predicted_price:,.2f}"
    )

    st.table(input_data)