import streamlit as st
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import random

# Download NLTK punkt tokenizer if not already installed
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# ----------------- Helper Functions -----------------

# Sample crop database
CROP_DB = {
    "wheat": {"soil": ["loamy", "sandy"], "climate": ["temperate", "cool"], "water": "moderate", "yield": 3},
    "rice": {"soil": ["clay", "loamy"], "climate": ["tropical", "humid"], "water": "high", "yield": 5},
    "maize": {"soil": ["loamy", "sandy"], "climate": ["tropical", "temperate"], "water": "moderate", "yield": 4},
    "soybean": {"soil": ["loamy", "sandy"], "climate": ["temperate"], "water": "moderate", "yield": 2.5},
    "cotton": {"soil": ["sandy"], "climate": ["tropical"], "water": "low", "yield": 2},
}

def analyze_conditions(description):
    """
    Extract keywords from farmer description
    """
    description = description.lower()
    tokens = word_tokenize(description)
    soil_types = ["loamy", "sandy", "clay", "black", "red"]
    climates = ["tropical", "temperate", "humid", "dry", "cool"]
    water_levels = ["low", "moderate", "high"]
    
    soil = [s for s in soil_types if s in tokens]
    climate = [c for c in climates if c in tokens]
    water = [w for w in water_levels if w in tokens]
    
    return {
        "soil": soil[0] if soil else None,
        "climate": climate[0] if climate else None,
        "water": water[0] if water else None
    }

def recommend_crops(conditions):
    """
    Recommend crops based on soil, climate, and water
    """
    recommendations = []
    for crop, props in CROP_DB.items():
        soil_match = conditions["soil"] in props["soil"] if conditions["soil"] else True
        climate_match = conditions["climate"] in props["climate"] if conditions["climate"] else True
        water_match = conditions["water"] == props["water"] if conditions["water"] else True
        if soil_match and climate_match and water_match:
            recommendations.append(crop)
    return recommendations

def predict_yield(crops, conditions):
    """
    Predict potential yield (simplified)
    """
    predicted_yield = {}
    for crop in crops:
        base_yield = CROP_DB[crop]["yield"]
        # Simple modifiers based on water availability
        if conditions["water"] == "low":
            factor = 0.8
        elif conditions["water"] == "high":
            factor = 1.1
        else:
            factor = 1.0
        predicted_yield[crop] = round(base_yield * factor, 2)
    return predicted_yield

def risk_analysis(crops, conditions):
    """
    Basic risk analysis
    """
    risks = {}
    for crop in crops:
        risk_factors = []
        # Simple rule-based risks
        if conditions["water"] == "low" and CROP_DB[crop]["water"] == "high":
            risk_factors.append("Water scarcity")
        if conditions["climate"] not in CROP_DB[crop]["climate"]:
            risk_factors.append("Climate mismatch")
        risks[crop] = risk_factors if risk_factors else ["Low risk"]
    return risks

# ----------------- Streamlit App -----------------

st.set_page_config(page_title="Smart Crop Advisor", layout="wide")
st.title("🌱 Smart Crop Advisor (NLP Powered)")

st.markdown("Describe your farm conditions (soil, climate, water availability, previous crops) and get crop recommendations, yield predictions, and risk analysis.")

# Input farm description
description = st.text_area("Describe your farm conditions:", height=200)

if st.button("Get Crop Recommendations"):
    if description.strip() == "":
        st.warning("Please enter farm conditions.")
    else:
        st.success("Analyzing farm conditions...")

        # Analyze conditions
        conditions = analyze_conditions(description)
        st.subheader("🌾 Detected Farm Conditions")
        st.json(conditions)

        # Recommend crops
        crops = recommend_crops(conditions)
        st.subheader("✅ Recommended Crops")
        if crops:
            st.write(", ".join(crops))
        else:
            st.write("No suitable crops detected based on the provided conditions.")

        # Predict yield
        predicted_yield = predict_yield(crops, conditions)
        st.subheader("📈 Yield Predictions (tons/acre)")
        st.table(predicted_yield)

        # Risk analysis
        risks = risk_analysis(crops, conditions)
        st.subheader("⚠️ Risk Analysis")
        for crop, risk in risks.items():
            st.write(f"{crop}: {', '.join(risk)}")
