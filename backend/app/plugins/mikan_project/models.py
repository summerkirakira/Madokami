from pydantic import BaseModel
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, Union
from madokami.api.models import InfoMessage
from madokami.plugin.backend.models import SearchItem


class RssFeed(BaseModel):
    class Item(BaseModel):
        id: str
        link: str
        title: str
        length: int
        description: str
        season: int
        episode: int
        episode_title: Optional[str] = None
        bangumi_id: Optional[int] = None
        cover: Optional[str] = None
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


class MikanRssHistory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    success: bool = Field()
    update_time: datetime = Field()
    rss_id: Optional[str] = Field(default=None, foreign_key="mikanrssstorage.id")
    rss: Optional['MikanRssStorage'] = Relationship(back_populates="history")


class MikanRssStorage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field()
    rss_link: str = Field()
    last_updated: datetime = Field()
    banned_pattern: Optional[str] = Field()
    preferred_pattern: Optional[str] = Field()
    history: list[MikanRssHistory] = Relationship(back_populates="rss")


class MikanSearchPostBody(BaseModel):
    keyword: str

class MikanSearchResponse(InfoMessage):
    data: list[SearchItem] = []


class MikanInfoPage(BaseModel):
    bangumi_id: Optional[int]
    title: str
    cover: str
