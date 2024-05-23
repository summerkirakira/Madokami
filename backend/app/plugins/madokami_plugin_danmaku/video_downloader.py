import yt_dlp
from pathlib import Path
from madokami.log import logger
from madokami.internal.downloader import Download, Downloader, DownloadStatus
from typing import Optional, Callable, Any
import uuid
from madokami.internal.core_config import get_config
from .danmaku_formatter import download_danmaku
import threading
from madokami.db import Session, engine
from .crud import get_danmaku_storage_by_url


class VideoDownloader:
    def __init__(self, url: str, output_path: Path):
        self.url = url
        self.output_path = output_path
        self.download: Optional[Download] = None

    def _init_download(self) -> Download:
        return Download(
            id=str(uuid.uuid4()),
            is_metadata=False,
            name='元数据获取中...                    ',
            target_path=self.output_path,
            dir=self.output_path.parent,
            total_length=0,
            progress=0,
            current_download=0,
            status=DownloadStatus.WAITING,
            current_speed=0,
            finished_callback=self.get_finished_callback(),
            move_up=lambda: None,
            move_to_bottom=lambda: None,
            move_down=lambda: None,
            purge=lambda: None,
            pause=lambda _: None,
            resume=lambda: None,
            remove=lambda _: None,
            error_message=None,
        )

    def get_finished_callback(self) -> Callable[[Download], Any]:
        def finished_callback(download: Download):
            validate_path = Path(download.target_path.stem + download.target_path.suffix)
            validate_path = download.target_path.parent / validate_path
            download_danmaku(validate_path, self.url)
            with Session(engine) as session:
                old_record = get_danmaku_storage_by_url(session, self.url)
                if old_record:
                    session.delete(old_record)
                session.commit()
        return finished_callback

    def get_download_hook(self) -> Callable[[dict], None]:
        if self.download is None:
            self.download = self._init_download()

        def download_hook(data: dict):
            try:
                # logger.info(f'Updating download status: {data}')
                if data['status'] == 'finished':
                    self.download.status = DownloadStatus.COMPLETED
                elif data['status'] == 'downloading':
                    self.download.status = DownloadStatus.DOWNLOADING
                elif data['status'] == 'error':
                    self.download.status = DownloadStatus.FAILED
                # logger.info(self.download)
                self.download.total_length = data.get('total_bytes') if data.get('total_bytes') else 1e-3
                self.download.progress = data.get('downloaded_bytes') / self.download.total_length if data.get('downloaded_bytes') else 0
                self.download.current_speed = data.get('speed') if data.get('speed') else 0
                if '/' in data['filename']:
                    self.download.name = data['filename'].split('/')[-1]
                else:
                    self.download.name = data['filename']
                self.download.target_path = Path(data['filename'])

                self.download.total_length = int(self.download.total_length)
                self.download.progress = self.download.progress * 100
                self.download.current_speed = int(self.download.current_speed)

            except Exception as e:
                logger.error(f'Failed to update download status: {e}')

        return download_hook

    def get_file_path(self):
        return f"{self.output_path}/%(title)s.%(ext)s"

    def get_opts(self):
        return {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': self.get_file_path(),
            'progress_hooks': [self.get_download_hook()],
            'logger': logger,
            'http_headers': {
                'Cookie': get_config('danmakudownload.cookie', ''),
            },
        }

    def yt_download_thread(self):
        try:
            with yt_dlp.YoutubeDL(self.get_opts()) as ydl:
                ydl.download([self.url])
        except Exception as e:
            logger.error(f'下载视频失败: {e}')
            self.download.status = DownloadStatus.FAILED

    def yt_video_info(self):
        with yt_dlp.YoutubeDL(self.get_opts()) as ydl:
            info = ydl.extract_info(self.url, download=False)
            return info

    def start_download(self) -> Download:
        threading.Thread(target=self.yt_download_thread).start()
        return self.download
