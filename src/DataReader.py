from abc import ABC, abstractmethod

from src.Types import DataType


class DataReader(ABC):

    @abstractmethod
    def read(self, path: str) -> DataType:
        pass
