from madokami.plugin.backend.engine import FileDownloaderEngine
from madokami.internal.core_config import get_config
from .crud import get_danmaku_storage, get_danmaku_storage_by_url
from madokami.db import Session, engine
from .video_downloader import VideoDownloader
from pathlib import Path
from madokami import get_app


class DanmakuDownloadEngine(FileDownloaderEngine):

    def __init__(self):
        self.downloading_urls = []

    def run(self):
        with Session(engine) as session:
            danmaku_storages = get_danmaku_storage(session)

        download_path = get_config("danmakudownload.download_path", "./data/downloads/bilibili_downloads")
        download_path = Path(download_path)
        if not download_path.exists():
            download_path.mkdir(parents=True)
        for danmaku_storage in danmaku_storages:
            if danmaku_storage.link in self.downloading_urls:
                continue
            with Session(engine) as session:
                history_record = get_danmaku_storage_by_url(session, danmaku_storage.link)
            if history_record is not None and history_record.is_download:
                continue
            self.downloading_urls.append(danmaku_storage.link)
            downloader = VideoDownloader(danmaku_storage.link, download_path)
            new_download = downloader.start_download()
            app = get_app()
            app.downloader.add_raw(new_download)


    @property
    def namespace(self) -> str:
        return 'summerkirakira.bilidownloader'

    @property
    def name(self) -> str:
        return 'B站视频下载器'

    @property
    def description(self) -> str:
        return 'A plugin for Danmaku Downloader'
