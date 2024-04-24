from madokami.plugin.backend.engine import SearchEngine
from madokami.plugin.backend.models import SearchItem
from .search_util import get_search_results
from madokami.internal.default_plugins.default_requester import DefaultRequester
from urllib.parse import quote


class MikanSearchEngine(SearchEngine):

    def __init__(self):
        self.requester = DefaultRequester()

    def search(self, query: str) -> list[SearchItem]:

        search_url = f'https://mikanani.me/Home/Search?searchstr={quote(query)}'
        response = self.requester.request(search_url, method='GET')
        search_results = get_search_results(response.text)
        search_items = []
        for bangumi in search_results.bangumis:
            ...

    def run(self):
        pass

    @property
    def namespace(self) -> str:
        return 'summerkirakira.mikan_project.mikan_search_engine'

    @property
    def name(self) -> str:
        return 'Mikan Search Engine'

    @property
    def description(self) -> str:
        return 'A search engine for Mikan Project'

