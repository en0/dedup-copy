from unittest.mock import Mock
from logging import Logger

from dedupe.deduplicator import DeduplicatorImpl
from dedupe.typing import FileHasher

from .high_percision_clock import HighPrecisionClockBuilder


class DeduplicatorImplBuilder:

    def __init__(self):
        self._logger = Mock(spec=Logger)
        self._file_hasher = Mock(spec=FileHasher)
        self._clock = HighPrecisionClockBuilder().build()

    def with_file_hasher(self, value: FileHasher) -> "DupeFinderImplBuilder":
        self._file_hasher = value
        return self

    def with_logger(self, value: Logger) -> "DupeFinderImplBuilder":
        self._logger = value
        return self

    def build(self) -> DeduplicatorImpl:
        return DeduplicatorImpl(self._file_hasher, self._clock, self._logger)

