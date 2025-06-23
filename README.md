# 🏏 IPL Win Predictor

**Live App:** [Access the App](https://iplwinprediction-wzpgzfmnep9eo3cuxzjwrk.streamlit.app)

---

## 📌 Overview

The **IPL Win Predictor** is a machine learning-powered web app that predicts the winning chances of a cricket team in an IPL match, based on real-time match conditions.

---

## What the App Does

- Predicts the probability of each team winning during an IPL match.
- Provides an easy-to-understand percentage-based prediction.
- Uses AI to explain the prediction in simple terms.

---

## How the Model Was Built

- **Data Source**: Real IPL ball-by-ball and match summary data from Kaggle
- **Feature Engineering**:
  - Runs left
  - Balls left
  - Wickets in hand
  - Current and required run rates
  - Match context (teams, city, etc.)
- **Model Used**: XGBoost classifier for accurate predictions.
- **Model Deployment**:
  - The trained model is saved and integrated into a Streamlit app.
  - The app uses this model to make real-time predictions.

---

## How the App Works

1. User inputs match conditions:
   - Batting and bowling teams
   - City
   - Target score
   - Current score
   - Overs completed
   - Wickets fallen
   - Current batter (optional)
2. The app calculates derived features like runs left, balls remaining, and run rate.
3. The machine learning model predicts win probabilities.
4. Results are displayed as:
   - Win probability for both teams
   - A simple AI-generated explanation of the prediction

---

## Why It’s Useful

- Ideal for **fans**, **commentators**, and **analysts**.
- Provides insights at any point in the match.
- Explains results in plain English — no technical knowledge needed.
- Bridges the gap between sports and data science.

---

## Tech Stack

- Python
- Streamlit
- XGBoost
- Scikit-learn
- Pandas & NumPy
- Google Gemini API (for natural language explanations)

---

## Future Enhancements

- Add more contextual features like pitch type and player form.
- Enable real-time match tracking via API.
- Add visualizations (e.g., win probability graphs over time).

---

## 🙌 Acknowledgements

Thanks to open-source IPL dataset from Kaggle and the data science community for enabling this project.

---
