import unittest
import fun_with_collections.sort_and_search_array as topic1
import array as arr


class TestSortAndSearchArray(unittest.TestCase):
    def test_search(self):
        the_array = arr.array('d', [2, 4, 6])
        self.assertEqual(topic1.search_array(the_array, 4), 1)

    def test_failed_search(self):
        the_array = arr.array('d', [2, 4, 6])
        self.assertEqual(topic1.search_array(the_array, 8), -1)

    def test_sort(self):
        the_array = arr.array('d', [3, 1, 2])
        topic1.sort_array(the_array)
        self.assertEqual(the_array, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
