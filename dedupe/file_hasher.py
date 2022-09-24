from hashlib import sha256
from logging import Logger
from time import time

from .typing import FileHasher, Clock


class Sha256FileHasher(FileHasher):

    def __init__(self, clock: Clock, logger: Logger):
        self._log = logger
        self._clock = clock
        self._verbose = True
        self._total_bytes = 0
        self._total_time = 0

    def get_hash_rate(self) -> float:
        return self._total_bytes / self._total_time

    def hash_file(self, file_path) -> str:
        with self._clock as clock:
            hash, file_size = self._hash_file(file_path)
            time_to_hash = clock.get_seconds()
        self._log.debug("Computed hash for file %s -> %s", file_path, hash)
        self._update_statistics(file_size, time_to_hash)
        self._display_file_statistics(file_path, file_size, time_to_hash)
        return hash

    def _hash_file(self, file_path):
        hasher = sha256()
        file_size = 0
        with open(file_path, "rb") as fd:
            while True:
                data = fd.read(hasher.block_size * 8)
                if not data:
                    break
                hasher.update(data)
                file_size += len(data)
        return hasher.hexdigest(), file_size

    def _update_statistics(self, file_size, time_to_hash):
        self._total_bytes += file_size
        self._total_time += time_to_hash

    def _display_file_statistics(self, file_path, file_size, time_to_hash):
        self._log.debug("%s: %s bytes hashed in %s seconds", file_path, file_size, time_to_hash)
