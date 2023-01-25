import click

import search_engines.google_engine as ge
import search_engines.duck_duck_go_engine as ddge


@click.command()
@click.option("-st", "--search-terms", help="Terms to search for.", multiple=True)
def search_with_terms(search_terms: list) -> str | None:

    for search_term in search_terms:
        google_res = ge.search(search_term)
        ddg_res = ddge.search(search_term)
        print(
            f"""
            ------------------------------------------------
            Google result for: {search_term} : Search time: {google_res.search_time}. Hits: {google_res.hits}
            ------------------------------------------------
            DDG result for: {search_term} : Search time: {ddg_res.search_time}. Hits: {ddg_res.hits}
            ------------------------------------------------
        """
        )


if __name__ == "__main__":
    search_with_terms()
