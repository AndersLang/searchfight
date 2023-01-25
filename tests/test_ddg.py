def test_ddg_search():
    from searchfight.search_engines.duck_duck_go_engine import search

    answer = search("premier league")

    assert answer.search_time
    assert answer.hits
