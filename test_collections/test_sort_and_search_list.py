import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as topic1


class TestSortAndSearch(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[2, 4, 6])
    def test_search(self):
        self.assertEqual(topic1.search_list(4), 1)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[2, 4, 6])
    def test_failed_search(self):
        self.assertEqual(topic1.search_list(8), -1)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=[2, 3, 1])
    def test_sort(self):
        self.assertEqual(topic1.sort_list(), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
