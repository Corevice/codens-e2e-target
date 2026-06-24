from e2e_orange_review_check import build_greeting


def test_build_greeting_world():
    assert build_greeting("World") == "Hello, World!"
