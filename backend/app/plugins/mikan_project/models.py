from pydantic import BaseModel


class RssFeed(BaseModel):
    class Item(BaseModel):
        id: str
        link: str
        title: str
        length: int
        description: str
        series: int
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