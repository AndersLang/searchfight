from httpx import get
from search_engines.search_response import SearchResponse

api_key = "IzaSyCuvspD4FwH77YSlKP7Es0L8hIEjYRorDQ"


def search(term) -> SearchResponse:
    answer = get(
        url=f"https://www.googleapis.com/customsearch/v1?key=AIzaSyCuvspD4FwH77YSlKP7Es0L8hIEjYRorDQ&cx=2461c1029c04d4c41&q={term}"
    )
    search_time = answer.json()["searchInformation"]["searchTime"]
    hits = answer.json()["searchInformation"]["totalResults"]
    return SearchResponse(search_time=search_time, hits=hits)
