import abc


class EngineInterface(abc.ABC):
    @staticmethod
    def namespace(cls) -> str:
        pass

    @staticmethod
    def name(cls) -> str:
        pass

    @abc.abstractmethod
    def status(self):
        pass

    @abc.abstractmethod
    def parse(self, data):
        pass
