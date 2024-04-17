from pydantic import BaseModel


class UserConfigEntry(BaseModel):
    name = str
    description = str
    placeholder = str


class UserConfigReq(BaseModel):
    entries = [UserConfigEntry]