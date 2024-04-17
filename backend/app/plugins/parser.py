from typing import Tuple

from ..core.extension_manager import get_requester
from ..core.interface.parser import ParserInterface

import xml.etree.ElementTree as ET
from pydantic import BaseModel


class TorrentMeta(BaseModel):
    id: str
    title: str
    link: str
    description: str
    pubDate: str
    contentLength: int


class MikanParser(ParserInterface):

    @staticmethod
    def namespace(cls) -> str:
        return 'parser.default.mikan'

    @staticmethod
    def name(cls) -> str:
        return 'A Mikan project Parser'

    async def parse(self, data: str):
        mikan_requester = get_requester('requester.default.mikan')
        if mikan_requester is None:
            raise Exception('Requester not found')
        mikan_requester = mikan_requester()
        rss_data = await mikan_requester.request(data)
        root = ET.fromstring(rss_data)





    def status(self) -> Tuple[int, str]:
        pass

    def cancel(self) -> bool:
        pass