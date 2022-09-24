from unittest import TestCase, skip
from unittest.mock import Mock, patch
from fixtures import a, an

from dedupe.typing import Clock


class HighPercisionClockTests(TestCase):

    def test_is_clock(self):
        clock = a.high_precision_clock.build()
        self.assertIsInstance(clock, Clock)

    def test_context_manager(self):
        clock = a.high_precision_clock.build()
        with clock as clk:
            self.assertIsInstance(clk, Clock)

    def test_get_seconds_returns_float(self):
        clock = a.high_precision_clock.build()
        with clock as clk:
            self.assertIsInstance(clk.get_seconds(), float)

    @patch("dedupe.clock.time")
    def test_get_seconds(self, time_mock):
        clock = a.high_precision_clock.build()
        time_mock.return_value = 100
        with clock as clk:
            time_mock.return_value = 200
            self.assertEqual(clk.get_seconds(), 100)

    @patch("dedupe.clock.time")
    def test_get_seconds_on_second_context_manager(self, time_mock):
        clock = a.high_precision_clock.build()
        time_mock.return_value = 100
        with clock as clk:
            time_mock.return_value = 200
            self.assertEqual(clk.get_seconds(), 100)

        with clock as clk:
            time_mock.return_value = 300
            self.assertEqual(clk.get_seconds(), 100)

