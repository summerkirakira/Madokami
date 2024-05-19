from madokami.plugin.backend.engine import FileDownloaderEngine
from madokami.plugin.basic_plugin import Status
from madokami.internal.default_plugins.default_requester import DefaultRequester
from madokami.internal.default_plugins.default_downloader import Download
from .parser import MikanRssParser

from madokami import get_config, set_config
from typing import Dict, Callable
from .models import RssFeed, MikanRssStorage
from .utils import validated_filename
import shutil
from .utils import get_validated_path, apply_pattern_filter
from madokami.log import logger
from madokami import get_app
from madokami.crud import get_media_info_by_id, add_media_info
from madokami.models import Content
from madokami.models import Media as MediaInfo
import time
from madokami.internal.default_plugins.bangumi_requester import BangumiRequester

from .crud import get_rss_storages, record_rss_history, get_rss_by_link, add_rss_storage
from madokami.db import Session, engine


class MikanDownloaderEngine(FileDownloaderEngine):

    def __init__(self):
        self.downloads: list[Download] = []
        self._status = Status(
            success=False,
            message='Engine is idle'
        )
        self.downloader = None
        self.requested_download_ids: list[str] = []
        self.requester = DefaultRequester()
        self.parser = MikanRssParser()
        self.bangumi_requester = BangumiRequester()

    def _add_rss_link_callback(self, data: Dict[str, str]):
        for config_key in data:
            set_config(config_key, data[config_key])
        self.run()

    @property
    def status(self) -> Status:
        return self._status

    def _raise_error(self, message: str, rss_link: str = None):
        self._status.running = False
        self._status.success = False
        self._status.message = message

        with Session(engine) as session:
            record_rss_history(session, rss_link, success=False)
        logger.error(message)

    def run(self):
        rss_link_list = []
        mikan_rss_url = get_config('mikan_project.mikan_rss_url')
        if mikan_rss_url is not None and mikan_rss_url.startswith("https://mikanani.me"):
            rss_link_list.append(mikan_rss_url)
            with Session(engine) as session:
                rss_store = get_rss_by_link(session, mikan_rss_url)
                if rss_store is None:
                    add_rss_storage(session, mikan_rss_url, "Mikan RSS个人订阅", preferred_pattern="1080p", banned_pattern="720p")

        with Session(engine) as session:
            rss_storages = get_rss_storages(session)

        for rss_storage in rss_storages:
            self._run(rss_storage)

    def _run(self, rss_storage: MikanRssStorage):
        # mikan_rss_url = get_config('mikan_project.mikan_rss_url')
        # if mikan_rss_url is None:
        #
        #     self._status.running = False
        #     self._status.success = False
        #     self._status.message = 'Mikan RSS URL is not set'
        #     self._status.config_request = Status.ConfigRequest(
        #         configs=[
        #             Status.ConfigRequest.Config(
        #                 key='mikan_project.mikan_rss_url',
        #                 name='Mikan RSS URL'
        #             )
        #         ],
        #         method=self._add_rss_link_callback
        #     )
        #     return
        # self._status.running = True
        # self._status.message = 'Requesting Mikan RSS feed...'
        requester = self.requester
        parser = self.parser

        try:
            response = requester.request(rss_storage.rss_link, 'GET')
        except Exception as e:
            self._raise_error(f'Request failed with exception: {str(e)}', rss_storage.rss_link)
            return
        if response.status_code != 200:
            self._raise_error(f'Request failed with status code {response.status_code}', rss_storage.rss_link)
            return
        try:
            parsed_data = parser.parse(response.text, same_bangumi=rss_storage.rss_link.startswith("https://mikanani.me/RSS/Bangumi?bangumiId="))
        except Exception as e:
            self._raise_error(f'Parsing failed with exception: {str(e)}', rss_storage.rss_link)
            return

        self._download(rss_data=parsed_data, banned_pattern=rss_storage.banned_pattern, preferred_pattern=rss_storage.preferred_pattern)

        with Session(engine) as session:
            record_rss_history(session, rss_storage.rss_link, success=True)


    # def _download_cover(self, rss_data: RssFeed):

    def _download(self, rss_data: RssFeed, banned_pattern: str = None, preferred_pattern: str = None):
        # is_remove_duplicate = get_config('mikan_project.remove_duplicate', "1")
        rss_items = rss_data.items
        # if is_remove_duplicate == "1":
        #     items_need_download = remove_duplicate_items(rss_items)
        # else:
        #     items_need_download = rss_items
        items_need_download = apply_pattern_filter(rss_items, banned_pattern, preferred_pattern)
        for item in items_need_download:
            try:
                get_app().downloader.add_download(uri=item.link, callback=self.download_callback(item, rss_data=rss_data))
            except Exception as e:
                self._raise_error(f'Failed to add download {item.link} with exception: {str(e)}')
                continue
            logger.info(f"Added download {item.link} to downloader")

    def download_callback(self, item: RssFeed.Item, rss_data: RssFeed) -> Callable:
        def callback(download: Download):
            madokami_download_path = get_config('mikan_project.download_path', './data/downloads')
            madokami_download_path = get_validated_path(madokami_download_path)
            source_download_path = get_config('mikan_project.aria2_download_path', './data/aria2/downloads')
            source_download_path = get_validated_path(source_download_path)
            source_download_path = source_download_path / download.target_path.name

            source_extension = source_download_path.suffix

            if not source_download_path.exists():
                self._raise_error(f'Download file {source_download_path} does not exist')
                return

            target_path = madokami_download_path / validated_filename(item.title) / f"Season {item.season}"
            target_path.mkdir(parents=True, exist_ok=True)

            if item.episode_title is None:
                target_path = target_path / validated_filename(f"{item.title} - S{item.season}E{item.episode}{source_extension}")
            else:
                target_path = target_path / validated_filename(f"{item.title} - S{item.season}E{item.episode} - {item.episode_title}{source_extension}")
            shutil.move(source_download_path, target_path)

            logger.info(f"Downloaded {source_download_path} to {target_path}")

            content = Content(
                path=str(target_path),
                title=item.episode_title if item.episode_title is not None else f"Episode {item.episode}",
                link=item.link,
                season=item.season,
                episode=item.episode,
                add_time=int(time.time())
            )

            with Session(engine) as session:
                # add_content(session, content)
                media_info = get_media_info_by_id(session, rss_data.link.split('/')[-1])

                if media_info is None:
                    logger.info(f"Media info {rss_data.title} not found, creating new media info")
                    media_info = MediaInfo(
                        id=rss_data.link.split('/')[-1],
                        title=item.title,
                        description=rss_data.description,
                        link=rss_data.link,
                        contents=[content],
                        type="Teleplay",
                        season=item.season,
                        bangumi_id=item.bangumi_id
                    )
                else:
                    logger.info(f"Media info {rss_data.title} found, adding content")
                    new_contents = [con for con in media_info.contents if con.episode != content.episode]
                    new_contents.append(content)
                    media_info.contents = new_contents
                add_media_info(session, media_info)

        return callback

    def cancel(self):
        pass

    @property
    def namespace(self) -> str:
        return 'summerkirakira.mikan_project.mikan_downloader_engine'

    @property
    def name(self) -> str:
        return '蜜柑计划RSS下载引擎'

    @property
    def description(self) -> str:
        return '蜜柑计划RSS下载引擎（默认）'


