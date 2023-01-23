import click

from search_engines.bing_engine import search as bing_search
from search_engines.google_engine import search as google_search
from search_engines.duck_duck_go_engine import search as duck_duck_go_search

@click.command()
@click.option("--search-terms", default="John Doe", help="Terms to search for.")
def search_with_terms(search_terms: list) -> str | None:
    
    

if __name__ == '__main__':
    search_with_terms()