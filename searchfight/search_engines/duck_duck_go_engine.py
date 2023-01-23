from duckduckgo_search import ddg


def search(term):
    result = ddg(term)
    print(result)
    return f"Duck Duck Go search took: Xms with X hits"


search("premier league")
