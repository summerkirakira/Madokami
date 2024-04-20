from typing import Tuple, Any

from madokami.plugin.backend.engine import FileDownloaderEngine, DownloadStatus
from madokami.plugin.basic_plugin import Status
from madokami.internal.default_plugins.default_requester import DefaultRequester
from .parser import MikanRssParser

from madokami import get_config, set_config
from typing import Dict


class MikanDownloaderEngine(FileDownloaderEngine):

    def __init__(self):
        self.downloaders = []
        self._status = Status(
            success=False,
            message='Engine is idle'
        )

    def _add_rss_link_callback(self, data: Dict[str, str]):
        for config_key in data:
            set_config(config_key, data[config_key])
        self.run()

    @property
    def status(self) -> Status:
        return self._status

    def downloader_status(self) -> list[DownloadStatus]:
        pass

    def pause_downloader(self, id: str) -> bool:
        pass

    def cancel_downloader(self, id: str) -> bool:
        pass

    def resume_downloader(self, id: str) -> bool:
        pass

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

        a = 1


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


