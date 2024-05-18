from madokami.plugin.backend.parser import Parser
from .models import RssFeed, MikanInfoTable, MikanInfoPage
from madokami.internal.models import EpisodeInfo
import xml.etree.ElementTree as ET
from .search_util import get_search_results
from madokami.internal.default_plugins.default_requester import DefaultRequester
from urllib.parse import quote
from .utils import get_episode, get_season, parse_subtitle_type, remove_brackets
from bs4 import BeautifulSoup
from madokami.plugin.backend.models import SearchItem
import datetime
import re
from madokami.internal.default_plugins.bangumi_requester import BangumiRequester
from typing import Optional


def get_episode_title(episode_id: int, episode_info: Optional[EpisodeInfo]) -> Optional[str]:
    if episode_info is None:
        return None
    for episode in episode_info.data:
        if episode.ep == episode_id:
            return episode.name_cn
    return None


class MikanRssParser(Parser):

    def __init__(self):
        self.episode_cache: dict[int, Optional[EpisodeInfo]] = {}
        self.requester = DefaultRequester()
        self.mikan_info_parser = MikanInfoPageParser()
        self.bangumi_requester = BangumiRequester()

    def search_mikan(self, title: str):
        search_url = f'https://mikanani.me/Home/Search?searchstr={quote(title)}'
        response = self.requester.request(search_url, method='GET')
        search_results = get_search_results(response.text)
        return search_results

    def parse(self, data: str, same_bangumi: bool = False) -> RssFeed:
        root = ET.fromstring(data)
        items = root.findall('channel/item')
        rss_items = []
        requester = DefaultRequester()
        bangumi_link = ""
        bangumi_title = ""
        cover = ""
        mikan_id = 0
        bangumi_id: Optional[int] = None
        for item in items:
            title = item.find('title').text
            link = item.find('enclosure').attrib['url']
            length = int(item.find('enclosure').attrib['length'])
            description = item.find('description').text

            episode = get_episode(title)
            if bangumi_title == "" or not same_bangumi:

                try:
                    search_results = self.search_mikan(title)
                except Exception as e:
                    continue

                if len(search_results.bangumis) == 0:
                    try:
                        search_results = self.search_mikan(remove_brackets(title))
                    except Exception as e:
                        continue

                if len(search_results.bangumis) != 1:
                    continue

                bangumi_link = search_results.bangumis[0].link

                mikan_id = int(bangumi_link.split('/')[-1])
                bangumi_title = search_results.bangumis[0].title
                cover = search_results.bangumis[0].cover

            if mikan_id not in self.episode_cache:
                info_page_detail = self.mikan_info_parser.parse(requester.request(bangumi_link, method='GET').text)
                bangumi_id = info_page_detail.bangumi_id
                if bangumi_id is None:
                    self.episode_cache[mikan_id] = None
                else:
                    episode_info = self.bangumi_requester.get_episode_info(bangumi_id)
                    self.episode_cache[mikan_id] = episode_info

            season = get_season(title)

            if season is None or episode is None:
                continue

            rss_items.append(
                RssFeed.Item(
                    id=str(mikan_id),
                    link=link, title=bangumi_title,
                    description=description,
                    length=length,
                    season=season,
                    episode=episode,
                    episode_title=get_episode_title(episode, self.episode_cache[mikan_id]),
                    bangumi_id=bangumi_id
                )
            )
        return RssFeed(
            title=root.find('channel/title').text,
            link=bangumi_link,
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


class MikanSearchItemParser(Parser):
    def __init__(self):
        self.requester = DefaultRequester()

    def parse(self, data: str) -> list[SearchItem]:
        root = BeautifulSoup(data, 'html.parser')
        subtitle_group_list = root.select('div.js-m-subgroup-item')
        subtitle_group_ids = [subtitle_group.get('id') for subtitle_group in subtitle_group_list]
        bangumi_rss_url = root.select_one('a.mikan-rss').get('href')
        bangumi_id = bangumi_rss_url.split('?')[-1].replace("bangumiId=", "")
        bangumi_id = int(bangumi_id)
        title = root.select_one('p.bangumi-title').text

        cover = root.select_one('div.bangumi-poster').get('style').replace('background-image: url(\'', '').replace(
            '\');', '')
        cover = f'https://mikanani.me{cover}'

        search_items = []
        group_tables = root.select('table.table')
        for index, subtitle_group_id in enumerate(subtitle_group_ids):
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
        pass

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


class MikanInfoPageParser(Parser):
    def parse(self, data) -> MikanInfoPage:
        root = BeautifulSoup(data, 'html.parser')
        bangumi_id = re.search(r'//bgm.tv/subject/(\d+)', data)
        if bangumi_id is not None:
            bangumi_id = int(bangumi_id.group(1))
        cover = root.select_one('div.bangumi-poster').get('style').replace('background-image: url(\'', '').replace(
            '\');', '')
        cover = f'https://mikanani.me{cover}'
        title = root.select_one('p.bangumi-title').text
        return MikanInfoPage(
            title=title,
            cover=cover,
            bangumi_id=bangumi_id
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
