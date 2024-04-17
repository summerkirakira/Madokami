import abc
from typing import Tuple


class ParserInterface(metaclass=abc.ABCMeta):
    @staticmethod
    def namespace(cls) -> str:
        pass

    @staticmethod
    def name(cls) -> str:
        pass

    @abc.abstractmethod
    async def parse(self, data):
        pass

    @abc.abstractmethod
    def status(self) -> Tuple[int, str]:
        pass

    @abc.abstractmethod
    def cancel(self) -> bool:
        pass

