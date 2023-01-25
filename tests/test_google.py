def test_google_search():
    from search_engines.google_engine import search

    answer = search("lectures")

    assert answer.search_time
    assert answer.hits
