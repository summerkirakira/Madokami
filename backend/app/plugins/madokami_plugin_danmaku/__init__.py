from madokami.db import engine, Session, SQLModel
from .subscription_manager import DanmakuSubscriptionManager


__metadata__ = {
    'name': '自动获取弹幕插件',
    'namespace': 'summerkirakira.danmakudownloadplugin',
    'description': 'A plugin for Danmaku Downloader',
    'version': '0.0.1',
    'author': 'summerkirakira',
    'license': 'MIT',
    'settings': [
        {
            'key': 'danmakudownload.download_path',
            'name': '番剧存放路径',
            'description': '使用Docker部署时请注意数据卷路径',
            'default': './data/downloads/bilibili_downloads'
        },
        {
            'key': 'danmakudownload.is_download_danmaku',
            'name': '是否同时下载弹幕文件',
            'description': '弹幕文件将以ASS字幕格式保存在视频文件夹下',
            'default': 'true'
        },
        {
            'key': 'danmakudownload.is_download_xml_danmaku',
            'name': '是否同时下载XML格式弹幕文件',
            'description': '弹幕文件将以XML格式保存在视频文件夹下',
            'default': 'true'
        }
    ],
    'engines': [],
    'subscription_manager': DanmakuSubscriptionManager()
}

with Session() as session:
    SQLModel.metadata.create_all(engine)