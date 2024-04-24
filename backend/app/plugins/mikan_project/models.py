from pydantic import BaseModel
from datetime import datetime


class RssFeed(BaseModel):
    class Item(BaseModel):
        id: str
        link: str
        title: str
        length: int
        description: str
        season: int
        episode: int
    title: str
    link: str
    description: str
    items: list[Item]


class MikanSearchResult(BaseModel):
    class Bangumi(BaseModel):
        link: str
        title: str
        cover: str

    bangumis: list[Bangumi] = []


class MikanInfoTable(BaseModel):
    class Info(BaseModel):
        title: str
        link: str
        last_updated: datetime

    infos: list[Info] = []