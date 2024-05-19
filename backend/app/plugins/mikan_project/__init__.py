from .mikan_downloader_engine import MikanDownloaderEngine
from madokami.db import engine, Session, SQLModel
from .subscription_manager import MikanSubscriptionManager
from .api import mikan_router


__metadata__ = {
    'name': '蜜柑计划订阅插件',
    'namespace': 'summerkirakira.mikan_project',
    'description': 'A plugin for Mikan Project',
    'version': '0.0.1',
    'author': 'summerkirakira',
    'license': 'MIT',
    'settings': [
        {
            'key': 'mikan_project.mikan_rss_url',
            'name': '蜜柑计划RSS订阅地址URL',
            'description': '请前往蜜柑计划网站获取RSS订阅地址'
        },
        {
            'key': 'mikan_project.download_path',
            'name': '番剧存放路径',
            'description': '使用Docker部署时请注意数据卷路径',
            'default': './data/downloads'
        },
        {
            'key': 'mikan_project.aria2_download_path',
            'name': 'Aria2下载路径',
            'description': 'Madokami会将此处下载完成的文件重命名后移动到番剧存放路径',
            'default': './data/aria2/downloads'
        },
    ],
    'engines': [
        'MikanDownloaderEngine'
    ],
    'subscription_manager': MikanSubscriptionManager()
}


with Session() as session:
    SQLModel.metadata.create_all(engine)