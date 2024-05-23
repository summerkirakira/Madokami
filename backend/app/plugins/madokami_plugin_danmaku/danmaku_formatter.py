import requests
from danmaku_converter import get_video_width_height, get_danmaku_xml, generate_ass
import re
from pathlib import Path
from madokami.log import logger

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}


def get_page(url):
    response = requests.get(url, headers=headers)
    return response.text


def get_cid(url):
    page = get_page(url)
    videoInfo = re.search(r'<script>window\.__INITIAL_STATE__\s*=(.*?)</script>', page)
    result = videoInfo.group(1)
    cid = re.search(r'"cid":(\d+)', result).group(1)
    return cid


def download_danmaku(file_path: Path, url: str = None, cid: str = None):
    if cid is None:
        if url is None:
            raise ValueError("No url provided")
        cid = get_cid(url)
    width, height = get_video_width_height(file_path)
    danmaku_xml = get_danmaku_xml(cid)
    file_name = str(file_path.parent / file_path.name)
    generate_ass(danmaku_xml, f"{file_name}.danmaku.ass", width, height)
    xml_path = Path(f"{file_name}.danmaku.xml")
    with xml_path.open("w") as f:
        f.write(danmaku_xml)
    logger.success(f"成功为{file_path.name}下载弹幕文件")


if __name__ == "__main__":
    url = 'https://www.bilibili.com/video/BV12z421m7zL/'
    cid = get_cid(url)
    danmuku = get_danmaku_xml(cid)
    a = 1