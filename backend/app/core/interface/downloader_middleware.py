import abc
import typing


class DownloaderMiddleware(abc.ABC):
    @staticmethod
    def namespace(cls) -> str:
        pass

    @staticmethod
    def name(cls) -> str:
        pass

    @abc.abstractmethod
    def download(self, url: str, **kwargs) -> typing.Any:
        pass

    @abc.abstractmethod
    def status(self) -> typing.Tuple[int, str]:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass