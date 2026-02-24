import os
import streamlit as st
from inference import GOLD_DF, recommend_for_user

# Environment setup
ENV = os.getenv("ENVIRONMENT", "dev").lower()

def get_environment_style(env):
    configs = {
        "dev": ("Dev Environment", "#90EE90"),
        "qa": ("QA Environment", "#FFFF99"),
        "prod": ("Production Environment", "#FF7F7F")
    }
    return configs.get(env, configs["dev"])

title, color = get_environment_style(ENV)

st.set_page_config(page_title=title)
st.markdown(f"<style>.stApp {{ background-color: {color}; }}</style>", unsafe_allow_html=True)
st.title(title)

# 🟢 Dropdown for user IDs
user_ids = sorted(GOLD_DF["userId"].unique())
user_id = st.selectbox("Select User ID", options=user_ids)

# 🟢 Display recommendations
if st.button("Get Recommendations"):
    recs_df = recommend_for_user(user_id)
    if not recs_df.empty:
        display_df = recs_df[["prediction", "title", "genres", "movieId"]].copy()
        # Round and format to 2 decimals
        display_df["prediction"] = display_df["prediction"].round(2).map("{:.2f}".format)
        # Sort by prediction descending
        display_df = display_df.sort_values(by="prediction", ascending=False)
        # Reset index to remove extra ID column
        display_df = display_df.reset_index(drop=True)
        # Show in Streamlit
        st.dataframe(display_df)
    else:
        st.write("No recommendations found for this user.")