from typing import List, Generator
from logging import Logger

from .typing import Deduplicator, FileHasher, Clock


class DeduplicatorImpl(Deduplicator):

    def __init__(self, hasher: FileHasher, clock: Clock, logger: Logger):
        self._clock = clock
        self._hasher = hasher
        self._log = logger

    def collect_files(self, files: List[str]) -> Generator[str, str, str]:
        seen_hashes = set()
        for i, file in enumerate(files):
            hash = self._hasher.hash_file(file)
            if hash in seen_hashes:
                self._log.info("Found Duplicate: %s", file)
            else:
                yield file
                seen_hashes.add(hash)
            self._log.info("Progress: %s%% | bps: %s", round((i / len(files)) * 100, 2), self._hasher.get_hash_rate())

