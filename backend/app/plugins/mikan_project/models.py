from pydantic import BaseModel
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, Union


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


class BangumiSearchResult(BaseModel):
    class Data(BaseModel):
        class Tag(BaseModel):
            name: str
            count: int

        date: str
        image: str
        type: int
        summary: str
        name: str
        name_cn: str
        tags: List[Tag]
        score: float
        id: int
        rank: int

    data: list[Data]


class BangumiSearchPostBody(BaseModel):
    class Filter(BaseModel):
        type: list[int] = [2]
    keyword: str
    filter: Filter = Filter()


class EpisodeInfo(BaseModel):
    class Datum(BaseModel):
        airdate: str
        name: str
        name_cn: str
        duration: str
        desc: str
        ep: int
        sort: int
        id: int
        subject_id: int
        comment: int
        type: int
        disc: int
        duration_seconds: int

    data: List[Datum]
    total: int
    limit: int
    offset: int


class BangumiSubject(BaseModel):
    class Images(BaseModel):
        small: str
        grid: str
        large: str
        medium: str
        common: str

    class Rating(BaseModel):

        rank: int
        total: int
        score: float

    class Tag(BaseModel):
        name: str
        count: int

    class Collection(BaseModel):
        on_hold: int
        dropped: int
        wish: int
        collect: int
        doing: int

    class InfoboxItem(BaseModel):
        class ValueItem(BaseModel):
            v: str

        key: str
        value: Union[str, List[ValueItem]]

    date: str
    platform: str
    images: Images
    summary: str
    name: str
    name_cn: str
    tags: List[Tag]
    infobox: List[InfoboxItem]
    rating: Rating
    total_episodes: int
    collection: Collection
    id: int
    eps: int
    volumes: int
    locked: bool
    nsfw: bool
    type: int

