# 🎬 Movie Review Sentiment Analysis (NLP Project)

## 📌 Project Overview

This project focuses on building a **Natural Language Processing (NLP)** based sentiment analysis system that classifies movie reviews as **Positive** or **Negative**.

Multiple machine learning models were trained and compared to identify the best performing classifier.
The final model was deployed using a **Streamlit graphical user interface** for real-time sentiment prediction.

---

## 🎯 Aim

To develop a machine learning model that can automatically determine the sentiment of movie reviews using NLP techniques.

---

## 🧠 Objective

* Perform text preprocessing on movie review data
* Convert text data into numerical features using TF-IDF
* Train and evaluate multiple classification algorithms
* Compare model performance using evaluation metrics
* Deploy the best model using a GUI interface
* Upload the complete project on GitHub

---

## 📊 Dataset

* **Dataset Used:** IMDB Movie Review Dataset
* Contains **50,000 movie reviews** labeled as Positive or Negative
* Dataset Source:
  https://raw.githubusercontent.com/laxmimerit/All-CSV-ML-Data-Files-Download/master/IMDB-Dataset.csv

---

## ⚙️ Technologies Used

* Python
* Google Colab
* Scikit-learn
* Pandas & NumPy
* TF-IDF Vectorization
* Streamlit (GUI Deployment)
* Matplotlib & Seaborn

---

## 🔄 Project Workflow

1. Dataset Loading and Exploration
2. Text Preprocessing
3. Feature Extraction using TF-IDF
4. Training Multiple Models:

   * Logistic Regression
   * Naive Bayes
   * Support Vector Machine (SVM)
   * Random Forest
5. Model Evaluation using:

   * Accuracy
   * Precision
   * Recall
   * F1-Score
6. Best Model Selection
7. GUI Deployment using Streamlit

---

## 🏆 Best Performing Model

Support Vector Machine (SVM) achieved the highest performance among all models and was selected for deployment.

---

## 💻 How to Run the Project

### Step 1 — Install Dependencies

```bash
pip install streamlit scikit-learn pandas numpy
```

### Step 2 — Run Streamlit App

```bash
python -m streamlit run app.py
```

### Step 3 — Use the Application

* Enter a movie review
* Click **Predict**
* View predicted sentiment

---

## 📷 Sample Output

* Positive Review → Sentiment: Positive
* Negative Review → Sentiment: Negative

---

## 📁 Project Structure

```
movie-sentiment-analysis
│
├── app.py
├── sentiment_model.pkl
├── tfidf.pkl
├── movie_sentiment.ipynb
└── README.md
```

---

## ✅ Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be used to automatically classify text sentiment.
The developed system successfully predicts movie review sentiment and provides an interactive user interface for real-time predictions.

---

## 👩‍💻 Author

Shravani Borde
