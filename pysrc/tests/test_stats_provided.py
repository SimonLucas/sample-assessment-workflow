import unittest

from provided.stats_list import StatsList


class TestStats(unittest.TestCase):
    def test_n_0(self):
        stats_list = StatsList()
        self.assertEqual(stats_list.get_n(), 0)

    def test_n_1(self):
        stats_list = StatsList()
        stats_list.add(1)
        self.assertEqual(stats_list.get_n(), 1)

    def test_mean_1(self):
        stats_list = StatsList()
        stats_list.add(1)
        self.assertEqual(stats_list.get_mean(), 1)

    def test_mean_2(self):
        stats_list = StatsList()
        stats_list.add(1)
        stats_list.add(2)
        self.assertEqual(stats_list.get_mean(), 1.5)


if __name__ == '__main__':
    unittest.main()
