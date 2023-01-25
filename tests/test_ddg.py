from searchfight.search_engines.duck_duck_go_engine import search


def test_search():
    assert search("premier league") == ""
