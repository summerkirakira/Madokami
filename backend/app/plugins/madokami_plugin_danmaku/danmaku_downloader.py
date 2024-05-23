from madokami.plugin.backend.engine import FileDownloaderEngine


class DanmakuDownloadEngine(FileDownloaderEngine):
    def run(self):
        pass

    @property
    def namespace(self) -> str:
        return 'summerkirakira.bilidownloader'

    @property
    def name(self) -> str:
        return 'B站视频下载器'

    @property
    def description(self) -> str:
        return 'A plugin for Danmaku Downloader'
