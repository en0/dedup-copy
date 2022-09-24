from time import time
from .typing import Clock


class HighPrecisionClock(Clock):

    def __init__(self):
        self._start = 0

    def __enter__(self):
        self._start = time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        ...

    def get_seconds(self) -> float:
        return time() - self._start
