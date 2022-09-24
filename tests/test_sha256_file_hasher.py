from unittest import TestCase, skip
from unittest.mock import patch, Mock, MagicMock
from fixtures import a, an
from time import time

from dedupe.typing import FileHasher, Clock


class Sha256FileHasherTests(TestCase):

    def _mock_file_reader(self, mock, data):
        mock().__enter__().read.side_effect = [d.encode('utf8') for d in data] + [None]

    def test_is_file_hasher(self):
        unit = a.sha256_file_hasher.build()
        self.assertIsInstance(unit, FileHasher)

    @patch("dedupe.file_hasher.open")
    def test_hash_file(self, open_mock):
        unit = a.sha256_file_hasher.build()
        self._mock_file_reader(open_mock, ["foo"])
        hash = unit.hash_file("foo")
        self.assertEqual(
            hash,
            "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
        )

    @patch("dedupe.file_hasher.open")
    def test_get_hash_rate(self, open_mock):
        mock_clock = MagicMock(spec=Clock)()
        mock_clock.__enter__().get_seconds.return_value = 1

        unit = (
            a.sha256_file_hasher
            .with_clock(mock_clock)
            .build()
        )

        self._mock_file_reader(open_mock, ["foo", "bar", "baz"])

        unit.hash_file("foo")
        self.assertEqual(unit.get_hash_rate(), 9)
