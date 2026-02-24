from app.inference import recommend_for_user

def test_recommend_user_exists():
    # User ID 1 should exist in your CSV sample
    recs = recommend_for_user(1)
    assert isinstance(recs, list)
    assert len(recs) > 0

def test_recommend_user_unknown():
    # User ID not in CSV
    recs = recommend_for_user(999)
    assert recs == []

def test_recommend_user_type():
    recs = recommend_for_user(1)
    assert all(isinstance(title, str) for title in recs)