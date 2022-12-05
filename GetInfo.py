from informers import google_search, wiki_info


def GetInfo(query: str) -> dict:
    info = {"search_results": None,
            "google_search_link": None,
            "wiki_data": None}

    query = query.lower().replace('who is ', '').replace('what is ', '').replace('wikipedia ', '')

    info['search_results']     = google_search(query)
    info['google_search_link'] = f"https://www.google.com/search?q={query}"
    info['wiki_data']          = wiki_info(query)

    return info

