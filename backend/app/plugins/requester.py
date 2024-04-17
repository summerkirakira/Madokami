import typing
import aiohttp

from app.core.interface.requester import RequesterInterface


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


class MikanRequester(RequesterInterface):

    def __init__(self):
        self._status = 'Waiting for start...'

    @classmethod
    def namespace(cls) -> str:
        return 'requester.default.mikan'

    def name(self) -> str:
        return 'A Mikan Project Requester'

    async def request(self, url: str, **kwargs) -> typing.Any:
        self._status = 'Requesting...'
        async with aiohttp.ClientSession() as session:
            self._status = 'Fetching...'
            result = await fetch(session, url)
            self._status = 'Done'
            return result

    def status(self) -> typing.Tuple[int, str]:
        return 100, self._status

