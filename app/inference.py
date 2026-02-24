import pandas as pd
import os

# Load CSV once (relative path)
CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/movie-recommender-final.csv")
GOLD_DF = pd.read_csv(CSV_PATH)

def recommend_for_user(user_id: int):
    """
    Returns a DataFrame with all recommendation info for the given user
    """
    df = GOLD_DF[GOLD_DF["userId"] == user_id]
    return df