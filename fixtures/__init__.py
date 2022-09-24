from .high_percision_clock import HighPrecisionClockBuilder
from .sha256_file_hasher import Sha256FileHasherBuilder
from .deduplicator_impl import DeduplicatorImplBuilder


class _A:

    @property
    def high_precision_clock(self) -> HighPrecisionClockBuilder:
        return HighPrecisionClockBuilder()

    @property
    def sha256_file_hasher(self) -> Sha256FileHasherBuilder:
        return Sha256FileHasherBuilder()

    @property
    def deduplicator_impl(self) -> DeduplicatorImplBuilder:
        return DeduplicatorImplBuilder()


class _An:
    ...

a, an = _A(), _An()

