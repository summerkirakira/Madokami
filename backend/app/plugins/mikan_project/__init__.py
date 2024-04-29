from .mikan_downloader_engine import MikanDownloaderEngine
from madokami.db import engine, Session, SQLModel


__metadata__ = {
    'name': 'Mikan Plugin',
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
        }
    ],
    'engines': [
        'MikanDownloaderEngine'
    ]
}


with Session() as session:
    SQLModel.metadata.create_all(engine)