from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime


class DanmakuStorage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field()
    link: str = Field()
    is_download: bool = Field(default=False)