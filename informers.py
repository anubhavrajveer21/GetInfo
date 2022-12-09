'''
I have imported annotations from __future__ because
Techno Beast has python 3.9 and python 3.9 doesn't have this symbol |
Shinjan if you would run this program then comment out from __future__ import annotations
'''
from __future__ import annotations
from requests import get
from bs4 import BeautifulSoup
from wikipedia import summary
from pywikihow import search_wikihow
from typing import List


def google_search(query: str) -> List[str] | list:
    """Scraps the google Search results
    Args:
        query (str): What to search on google
    Returns:
        List[str] | list: Google search results
    """
    url = 'https://google.com/search?q=' + query

    # If the internet is off instead of raising error it will return empty list because try-except is there
    try:
        request_result = get(url)
    except:
        return []
    page = BeautifulSoup(request_result.text, "html.parser")
    # Getting all the h3 tags of the webpage because all the search results in google are h3 tags
    h3_headings = page.find_all('h3')
    search_results = []

    for heading in h3_headings:
        heading_text = heading.getText()
        search_results.append(heading_text)

    return search_results


def wiki_info(query: str) -> str:
    """
    Returns the wikipedia data of the query.
    And if there is no wikipedia page of the query then it returns ""
    """
    try:
        wiki_data = summary(query, 3)
    except:
        return ""
    return wiki_data


def how_to(query: str) -> str:
    """
    Tells how to do what is telling to do
    If internet is not connected to pc or
    it could find any of the query then it returns ""
    NOTE: The result may be inaccurate.
    """
    try:
        how = search_wikihow(query, 1)
        return how[0].summary
    except:
        return ""