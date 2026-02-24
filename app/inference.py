from pathlib import Path
import pandas as pd

# Load CSV once (relative path)
CSV_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "movie-recommender-final.csv"
)

GOLD_DF = pd.read_csv(CSV_PATH)


def recommend_for_user(user_id: int):
    """
    Returns a DataFrame with all recommendation info
    for the given user.
    """
    df = GOLD_DF[GOLD_DF["userId"] == user_id]
    return df
