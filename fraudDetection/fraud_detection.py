import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('fraud_detection_model1.pkl')
# Define the Streamlit app
st.title("Fraud Detection App")
st.markdown("Enter transaction details to predict if it's fraudulent or not.")
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT","DEPOSIT"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance of Origin Account(sender)", min_value=0.0, value=5000.0)
newbalanceOrig = st.number_input("New Balance of Origin Account(sender)", min_value=0.0, value=4000.0)
oldbalanceDest = st.number_input("Old Balance of Destination Account(receiver)", min_value=0.0, value=3000.0)
newbalanceDest = st.number_input("New Balance of Destination Account(receiver)", min_value=0.0, value=3500.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result: {int(prediction)}") 
    if prediction == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be LEGITIMATE.")
