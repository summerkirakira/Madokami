import requests
from .danmaku_converter import get_video_width_height, get_danmaku_xml, generate_ass
import re
from pathlib import Path
from madokami.log import logger
from madokami.internal.core_config import get_config

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}


def get_page(url):
    response = requests.get(url, headers=headers)
    return response.text


def get_bv_cid(url):
    page = get_page(url)
    videoInfo = re.search(r'<script>window\.__INITIAL_STATE__\s*=(.*?)</script>', page)
    result = videoInfo.group(1)
    cid = re.search(r'"cid":(\d+)', result).group(1)
    return cid


def get_ep_cid(url):
    ep_id = re.search(r'https://www.bilibili.com/bangumi/play/ep(\d*)', url)
    ep_id = ep_id.group(1)
    result = requests.get(f'https://api.bilibili.com/pgc/view/web/season?ep_id={ep_id}', headers=headers)
    for ep in result.json()['result']['episodes']:
        if ep['ep_id'] == int(ep_id):
            return ep['cid']
    raise ValueError('cid not found')


def download_danmaku(file_path: Path, url: str = None, cid: str = None):
    if cid is None:
        if url is None:
            raise ValueError("No url provided")
        try:
            cid = get_bv_cid(url)
        except Exception as e:
            try:
                cid = get_ep_cid(url)
            except Exception as e:
                logger.error(f"无法获取cid: {e}")
                return
    is_download_xml = get_config('danmakudownload.is_download_xml_danmaku', 'false') == 'true'
    is_download_ass = get_config('danmakudownload.is_download_danmaku', 'false') == 'true'
    width, height = get_video_width_height(file_path)
    danmaku_xml = get_danmaku_xml(cid)
    file_name = str(file_path.parent / file_path.name)
    if is_download_ass:
        generate_ass(danmaku_xml, f"{file_name}.danmaku.ass", width, height)
        logger.success(f"成功为{file_path.name}下载弹幕文件")
    xml_path = Path(f"{file_name}.danmaku.xml")
    if is_download_xml:
        with xml_path.open("w") as f:
            f.write(danmaku_xml)
            logger.success(f"成功为{file_path.name}生成xml弹幕文件")
