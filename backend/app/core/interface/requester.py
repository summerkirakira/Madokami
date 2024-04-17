import abc
import typing


class RequesterInterface(abc.ABC):
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    async def request(self, url: str, **kwargs) -> typing.Any:
        pass

    @abc.abstractmethod
    def status(self) -> typing.Tuple[int, str]:
        pass
