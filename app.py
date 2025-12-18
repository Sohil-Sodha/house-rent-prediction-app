# import streamlit as st
# import pandas as pd
# import joblib

# # ===============================
# # LOAD MODEL
# # ===============================
# @st.cache_resource
# def load_model():
#     return joblib.load("deployment/final_model.pkl")

# model = load_model()

# # ===============================
# # UI
# # ===============================
# st.set_page_config(page_title="Rent Price Predictor", layout="centered")

# st.title("🏠 Rent Price Prediction App")
# st.write("Enter property details to predict rent amount.")

# # ===============================
# # USER INPUTS
# # ===============================
# rooms = st.number_input("Rooms", min_value=1, max_value=10, value=2)
# bathroom = st.number_input("Bathrooms", min_value=1, max_value=10, value=1)
# parking_spaces = st.number_input("Parking Spaces", min_value=0, max_value=10, value=1)
# floor = st.number_input("Floor", min_value=1, max_value=100, value=3)

# city = st.selectbox("City", [
#     "Bangalore", "Chennai", "Delhi", "Kolkata", "Mumbai"
# ])

# area = st.text_input("Area / Neighborhood", "Centro")

# animal_allowance = st.selectbox("Animal Allowed?", ["yes", "no"])
# furniture = st.selectbox("Furniture", ["furnished", "unfurnished"])

# # ===============================
# # PREDICTION
# # ===============================
# if st.button("Predict Rent 💰"):
#     input_data = pd.DataFrame([{
#         "rooms": rooms,
#         "bathroom": bathroom,
#         "parking_spaces": parking_spaces,
#         "floor": floor,
#         "city": city,
#         "area": area,
#         "animal_allowance": animal_allowance,
#         "furniture": furniture
#     }])

#     prediction = model.predict(input_data)[0]

#     st.success(f"💵 Estimated Rent: {prediction:,.2f}")













import streamlit as st
import pandas as pd
import joblib
import os

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Rent Predictor",
    layout="centered"
)

# ===============================
# LOAD MODEL
# ===============================
MODEL_PATH = os.path.join("final_model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# ===============================
# UI
# ===============================
st.title("🏠 House Rent Price Predictior")
st.subheader("Important note: This model will only predict rental prices for the following cities across india:")
st.subheader("Bangalore, Chennai, Delhi, Mumbai, Kolkata")

rooms = st.number_input("Rooms", 1, 10, 2)
bathroom = st.number_input("Bathrooms", 1, 10, 2)
parking_spaces = st.number_input("Parking Spaces", 0, 10, 1)
floor = st.number_input("Floor", 1, 100, 3)

city = st.selectbox("City", [
    "Bangalore", "Chennai", "Delhi", "Kolkata", "Mumbai"
])
area = st.text_input("Area / Neighborhood")
animal_allowance = st.selectbox("Animal Allowed?", ["yes", "no"])
furniture = st.selectbox("Furniture", ["furnished", "unfurnished"])

if st.button("Predict Rent 💰"):
    input_df = pd.DataFrame([{
        "rooms": rooms,
        "bathroom": bathroom,
        "parking_spaces": parking_spaces,
        "floor": floor,
        "city": city,
        "area": area,
        "animal_allowance": animal_allowance,
        "furniture": furniture
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Rent: {prediction:,.2f}")

st.info("Predictions are based on historical data and may vary in real conditions.")
st.warning("Do not use this prediction as a legal or financial guarantee.")

