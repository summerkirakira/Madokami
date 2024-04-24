from typing import Tuple, Any

from madokami.plugin.backend.engine import FileDownloaderEngine, DownloadStatus
from madokami.plugin.basic_plugin import Status
from madokami.internal.default_plugins.default_requester import DefaultRequester
from madokami.internal.default_plugins.default_downloader import DefaultAria2Downloader, Download
from .parser import MikanRssParser

from madokami import get_config, set_config
from typing import Dict, Callable
from .models import RssFeed
from .utils import validated_filename
from aria2p.options import Options
import shutil
from pathlib import Path
from .utils import get_validated_path, remove_duplicate_items
from madokami.log import logger
from madokami import get_app


class MikanDownloaderEngine(FileDownloaderEngine):

    def __init__(self):
        self.downloads: list[Download] = []
        self._status = Status(
            success=False,
            message='Engine is idle'
        )
        self.downloader = None
        self.requested_download_ids: list[str] = []

    def _add_rss_link_callback(self, data: Dict[str, str]):
        for config_key in data:
            set_config(config_key, data[config_key])
        self.run()

    @property
    def status(self) -> Status:
        return self._status

    def _raise_error(self, message: str):
        self._status.running = False
        self._status.success = False
        self._status.message = message

    def run(self):
        mikan_rss_url = get_config('mikan_project.mikan_rss_url')
        if mikan_rss_url is None:

            self._status.running = False
            self._status.success = False
            self._status.message = 'Mikan RSS URL is not set'
            self._status.config_request = Status.ConfigRequest(
                configs=[
                    Status.ConfigRequest.Config(
                        key='mikan_project.mikan_rss_url',
                        name='Mikan RSS URL'
                    )
                ],
                method=self._add_rss_link_callback
            )
            return
        self._status.running = True
        self._status.message = 'Requesting Mikan RSS feed...'
        requester = DefaultRequester()
        parser = MikanRssParser()

        try:
            response = requester.request(mikan_rss_url, 'GET')
        except Exception as e:
            self._raise_error(f'Request failed with exception: {str(e)}')
            return
        if response.status_code != 200:
            self._raise_error(f'Request failed with status code {response.status_code}')
            return
        parsed_data = parser.parse(response.text)

        self._download(rss_items=parsed_data.items)

    def _download(self, rss_items: list[RssFeed.Item]):
        is_remove_duplicate = get_config('mikan_project.remove_duplicate', "1")
        if is_remove_duplicate == "1":
            items_need_download = remove_duplicate_items(rss_items)
        else:
            items_need_download = rss_items
        for item in items_need_download:
            get_app().downloader.add_download(uri=item.link, callback=self.download_callback(item))
            logger.info(f"Added download {item.link} to downloader")

    def download_callback(self, item: RssFeed.Item) -> Callable:
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

            target_path = madokami_download_path / item.title / f"Season {item.season}"
            target_path.mkdir(parents=True, exist_ok=True)

            target_path = target_path / validated_filename(f"{item.title} - S{item.season}E{item.episode}{source_extension}")
            shutil.move(source_download_path, target_path)

            logger.info(f"Downloaded {source_download_path} to {target_path}")

        return callback

    def cancel(self):
        pass

    @property
    def namespace(self) -> str:
        return 'summerkirakira.mikan_project.mikan_downloader_engine'

    @property
    def name(self) -> str:
        return 'Mikan Downloader Engine'

    @property
    def description(self) -> str:
        return 'A downloader engine for Mikan Project'


