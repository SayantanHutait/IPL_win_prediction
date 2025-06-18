import streamlit as st
import pickle
import pandas as pd
import google.generativeai as genai

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
players = pickle.load(open('players.pkl', 'rb'))

# Configure Gemini
genai.configure(api_key="AIzaSyC8qBdl58LQXDJGw0Eaaw5zB7Ts6PI0edU")
model = genai.GenerativeModel("gemini-2.0-flash")

def get_explanation(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

striker = st.selectbox('Striker', players)

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs if overs > 0 else 0
    rrr = (runs_left*6)/balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'batter': [striker],
        'left_runs': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + " - " + str(round(win*100)) + "%")
    st.header(bowling_team + " - " + str(round(loss*100)) + "%")

    # LLM Explanation
    prompt = f"""
    Explain in simple terms in a short paragraph why {batting_team} has a win probability of {round(win*100)}%
    and {bowling_team} has a loss probability of {round(loss*100)}%, based on these match details:
    - Runs left: {runs_left}
    - Balls left: {balls_left}
    - Wickets in hand: {wickets}
    - Current run rate (CRR): {crr:.2f}
    - Required run rate (RRR): {rrr:.2f}
    - Match location: {selected_city}
    - Striker: {striker}
    """

    explanation = get_explanation(prompt)
    st.subheader("Explanation:")
    st.write(explanation)
