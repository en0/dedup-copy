from abc import ABC, abstractmethod
from typing import List, Generator


class FileHasher(ABC):

    @abstractmethod
    def get_hash_rate(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def hash_file(self, file_path: str) -> str:
        raise NotImplementedError()


class Clock(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def __enter__(self) -> "Clock":
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_seconds(self) -> float:
        raise NotImplementedError()


class Deduplicator(ABC):

    @abstractmethod
    def collect_files(self, files: List[str]) -> Generator[str, str, str]:
        raise NotImplementedError()

