from pydantic.dataclasses import dataclass


@dataclass
class SearchResponse:
    search_time: float
    hits: str
