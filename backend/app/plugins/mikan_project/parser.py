from madokami.plugin.backend.parser import Parser
from .models import RssFeed
import xml.etree.ElementTree as ET
from .search_util import get_search_results
from madokami.internal.default_plugins.default_requester import DefaultRequester
from urllib.parse import quote
from .utils import get_episode, get_series




class MikanRssParser(Parser):
    def parse(self, data: str):
        root = ET.fromstring(data)
        items = root.findall('channel/item')
        rss_items = []
        requester = DefaultRequester()
        for item in items:
            title = item.find('title').text
            link = item.find('enclosure').attrib['url']
            length = int(item.find('enclosure').attrib['length'])
            description = item.find('description').text

            episode = get_episode(title)

            search_url = f'https://mikanani.me/Home/Search?searchstr={quote(title)}'

            response = requester.request(search_url, method='GET')
            search_results = get_search_results(response.text)

            if len(search_results.bangumis) != 1:
                continue

            title = search_results.bangumis[0].title

            series = get_series(title)

            if series is None or episode is None:
                continue

            rss_items.append(
                RssFeed.Item(
                    id=link.split('/')[-1],
                    link=link, title=title,
                    description=description,
                    length=length,
                    series=series,
                    episode=episode
                )
            )
        return RssFeed(
            title=root.find('channel/title').text,
            link=root.find('channel/link').text,
            description=root.find('channel/description').text,
            items=rss_items
        )

    def cancel(self):
        pass

    def status(self):
        pass

    @property
    def namespace(self) -> str:
        return 'summerkirakira.mikan_project.mikan_rss_parser'

    @property
    def name(self) -> str:
        return 'Mikan RSS Parser'

    @property
    def description(self) -> str:
        return 'A parser for Mikan Project RSS feed'

