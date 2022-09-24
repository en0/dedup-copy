from dedupe.file_hasher import Sha256FileHasher
from logging import getLogger
from dedupe.typing import Clock

from .high_percision_clock import HighPrecisionClockBuilder


class Sha256FileHasherBuilder:

    def __init__(self):
        self._clock = HighPrecisionClockBuilder().build()
        self._logger = getLogger()

    def with_clock(self, value: Clock) -> "Sha256FileHasherBuilder":
        self._clock = value
        return self

    def build(self) -> Sha256FileHasher:
        return Sha256FileHasher(self._clock, self._logger)

