import duckduckgo_search
import json

from time import time
from search_engines.search_response import SearchResponse


def search(term):
    t1 = time() * 10
    result = duckduckgo_search.ddg_answers("lectures")
    t2 = time() * 10
    search_time = t2 - t1
    return SearchResponse(search_time=search_time, hits=100)
