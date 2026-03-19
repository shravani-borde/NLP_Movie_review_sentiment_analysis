import streamlit as st
import pickle

model = pickle.load(open("sentiment_model.pkl","rb"))
vectorizer = pickle.load(open("tfidf.pkl","rb"))

st.title("Movie Review Sentiment Analysis")

review = st.text_area("Enter Movie Review")

if st.button("Predict"):

    data = vectorizer.transform([review])
    prediction = model.predict(data)

    st.success("Sentiment: " + prediction[0])