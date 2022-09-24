from unittest import TestCase, skip
from unittest.mock import Mock
from fixtures import a, an

from dedupe.typing import Deduplicator, FileHasher


class DeduplicatorImplTests(TestCase):

    def test_is_deduplicator(self):
        unit = a.deduplicator_impl.build()
        self.assertIsInstance(unit, Deduplicator)

    def test_collect_files(self):
        mock = Mock(spec=FileHasher)

        mock.hash_file.side_effect = lambda f: {
            "a": "hash_for_a_and_c",
            "b": "hash_for_c",
            "c": "hash_for_a_and_c",
        }[f]

        unit = (
            a.deduplicator_impl
            .with_file_hasher(mock)
            .build()
        )

        uniq = unit.collect_files(["a", "b", "c"])
        self.assertEqual(list(uniq), ["a", "b"])
