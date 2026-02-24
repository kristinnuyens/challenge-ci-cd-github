from app.inference import recommend_for_user


def test_recommend_user_exists():
    """User ID 1 should exist in CSV"""
    recs = recommend_for_user(1)
    assert not recs.empty
    assert isinstance(recs, type(recs))


def test_recommend_user_unknown():
    """User ID not in CSV should return empty DataFrame"""
    recs = recommend_for_user(999999)  # unlikely user ID
    assert recs.empty


def test_recommend_user_type():
    """All titles should be strings"""
    recs = recommend_for_user(1)
    if not recs.empty:
        assert all(isinstance(title, str) for title in recs["title"])