from searchfight.search_engines.google_engine import search


def test_google_search():
    assert search("lectures")
