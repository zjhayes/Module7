import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as topic1


class TestSortAndSearch(unittest.TestCase):
    def test_search(self):
        the_list = [2,4,6]
        self.assertEqual(topic1.search_list(the_list, 4), 1)


if __name__ == '__main__':
    unittest.main()
