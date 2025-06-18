import pickle
import joblib

# Load existing .pkl files
with open("pipe.pkl", "rb") as f:
    pipe = pickle.load(f)

with open("players.pkl", "rb") as f:
    players = pickle.load(f)

# Save them as .joblib files
joblib.dump(pipe, "pipe.joblib")
joblib.dump(players, "players.joblib")
