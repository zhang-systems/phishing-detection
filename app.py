import streamlit as st
import pandas as pd
import joblib

# ---------- Page setup ----------
st.set_page_config(page_title="Phishing Website Detector", page_icon="🎣")
st.title("🎣 Phishing Website Detector")
st.write(
    "This tool uses a Random Forest model trained on 10,000 websites "
    "(Kaggle Phishing Dataset) to predict whether a site is phishing or legitimate. "
    "Adjust the sliders below based on a website's characteristics."
)

# ---------- Load model bundle ----------
@st.cache_resource
def load_bundle():
    return joblib.load("phishing_model.pkl")

bundle = load_bundle()
model = bundle["model"]
all_columns = bundle["all_columns"]
top_features = bundle["top_features"]
medians = bundle["medians"]
ranges = bundle["ranges"]

# ---------- Build input form (only top features) ----------
st.subheader("Website Features")
user_input = {}

cols = st.columns(2)
for i, feat in enumerate(top_features):
    lo, hi = ranges[feat]
    is_percent_like = (lo in (0, -1)) and (hi == 1)  # features like PctExtHyperlinks, range 0-1 or -1 to 1
    with cols[i % 2]:
        if is_percent_like:
            default = float(medians[feat])
            user_input[feat] = st.slider(feat, min_value=float(lo), max_value=float(hi), value=default, step=0.01)
        else:
            default = int(medians[feat])
            user_input[feat] = st.slider(feat, min_value=lo, max_value=hi, value=default)

# ---------- Predict ----------
if st.button("Check Website", type="primary"):
    # Start with median values for every feature the model expects
    row = medians.copy()
    # Overwrite with the values the user actually chose
    for feat, val in user_input.items():
        row[feat] = val
    # Put columns in the exact order the model was trained on
    input_df = pd.DataFrame([row])[all_columns]

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]  # probability of class 1 = Phishing

    st.divider()
    if pred == 1:
        st.error(f"🚨 **Likely Phishing** — confidence: {prob*100:.1f}%")
    else:
        st.success(f"✅ **Likely Legitimate** — confidence: {(1-prob)*100:.1f}%")

    st.progress(float(prob))
    st.caption("Bar shows the model's estimated probability of phishing.")

st.divider()
st.caption(
    "Model: Random Forest (98.5% accuracy on Kaggle test set). "
    "Only the top 8 most important features are adjustable here; "
    "the rest are filled in with typical (median) values."
)
