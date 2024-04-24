from madokami.plugin.backend.parser import Parser
from .models import RssFeed, MikanInfoTable
import xml.etree.ElementTree as ET
from .search_util import get_search_results
from madokami.internal.default_plugins.default_requester import DefaultRequester
from urllib.parse import quote
from .utils import get_episode, get_season, parse_subtitle_type
from bs4 import BeautifulSoup
from madokami.plugin.backend.models import SearchItem
import datetime




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

            season = get_season(title)

            if season is None or episode is None:
                continue

            rss_items.append(
                RssFeed.Item(
                    id=link.split('/')[-1],
                    link=link, title=title,
                    description=description,
                    length=length,
                    season=season,
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


class MikanInfoPageParser(Parser):
    def __init__(self):
        self.requester = DefaultRequester()

    def parse(self, data: str):
        root = BeautifulSoup(data, 'html.parser')
        subtitle_group_list = root.select('div.js-m-subgroup-item')
        subtitle_group_ids = [subtitle_group.get('id') for subtitle_group in subtitle_group_list]
        bangumi_rss_url = root.select_one('a.mikan-rss').get('href')
        bangumi_id = bangumi_rss_url.split('?')[-1].replace("bangumiId=", "")
        bangumi_id = int(bangumi_id)
        title = root.select_one('p.bangumi-title').text

        cover = root.select_one('div.bangumi-poster').get('style').replace('background-image: url(\'', '').replace('\');', '')
        cover = f'https://mikanani.me{cover}'

        search_items = []
        group_tables = root.select('table.table')
        for index, subtitle_group_id in enumerate(subtitle_group_ids):
            # subtitle_group_url = f'https://mikanani.me/Home/ExpandEpisodeTable?bangumiId={bangumi_id}&subtitleGroupId={subtitle_group_id}&take=65'
            # response = self.requester.request(subtitle_group_url, method='GET')
            group_table = self._parse_subtitle_group_table(group_tables[index])
            subtitle_group_name = root.select_one(f'div#{subtitle_group_id}').select_one('span').text
            for info in group_table.infos:
                if group_type := parse_subtitle_type(info.title):
                    search_items.append(
                        SearchItem(
                            title=info.title,
                            cover=cover,
                            bangumi_id=bangumi_id,
                            bangumi_name=title,
                            subtitle_group_id=int(subtitle_group_id[1:]),
                            subtitle_group_name=subtitle_group_name,
                            link=info.link,
                            group_type=group_type,
                            last_updated=info.last_updated,
                            callback=self._search_item_callback,
                            is_checked=False
                        )
                    )
        return search_items

    def _search_item_callback(self, search_item: SearchItem):
        ...


    def _parse_subtitle_group_table(self, table) -> MikanInfoTable:
        data_tr = table.select_one('tbody').select('tr')
        infos: list[MikanInfoTable.Info] = []
        for tr in data_tr:
            link_warp = tr.select_one('a.magnet-link-wrap')
            last_updated = tr.select_one('td:nth-child(3)').text
            last_updated = datetime.datetime.strptime(last_updated, '%Y/%m/%d %H:%M')
            link = link_warp.get('href')
            title = link_warp.text
            infos.append(
                MikanInfoTable.Info(
                    title=title,
                    link=f"https://mikanani.me{link}",
                    last_updated=last_updated
                )
            )
        return MikanInfoTable(
            infos=infos
        )



    def cancel(self):
        pass

    def status(self):
        pass

    @property
    def namespace(self) -> str:
        return 'summerkirakira.mikan_project.mikan_info_page_parser'

    @property
    def name(self) -> str:
        return 'Mikan Info Page Parser'


    @property
    def description(self) -> str:
        return 'A parser for Mikan Project info page'

