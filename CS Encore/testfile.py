import unittest
from bugs import on_every_line, most_common_word, sum_of_each_row, smallest_each, what_ranking, largest_on_each_row

class TestFunctions(unittest.TestCase):
    
    def test_on_every_line(self):
        self.assertTrue(on_every_line("hello", "read_file.txt"))
        self.assertFalse(on_every_line("world", "read_file.txt"))
        self.assertFalse(on_every_line("everyone", "read_file.txt"))
    
    def test_most_common_word(self):
        self.assertEqual(most_common_word("apple banana apple orange apple banana"), "apple")
        self.assertEqual(most_common_word("test test test check check"), "test")
        self.assertEqual(most_common_word("one two three four"), "one")  # First in case of tie
    
    def test_sum_of_each_row(self):
        self.assertEqual(sum_of_each_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [6, 15, 24])
        self.assertEqual(sum_of_each_row([[10, 10], [5, 5]]), [20, 10])
        self.assertEqual(sum_of_each_row([[]]), [0])  # Edge case: empty row
    
    def test_smallest_each(self):
        data = [("Alice", 10), ("Bob", 5), ("Alice", 3), ("Bob", 7)]
        self.assertEqual(smallest_each(data), [("Alice", 3), ("Bob", 5)])
        data = [("John", 100)]
        self.assertEqual(smallest_each(data), [("John", 100)])
    
    def test_what_ranking(self):
        self.assertEqual(what_ranking("Sean O'Malley", "pound_for_pound.txt"), "Sean O'Malley is ranked number 13")
        self.assertEqual(what_ranking("Jon Jones", "pound_for_pound.txt"), "Jon Jones is ranked number 2")
        self.assertEqual(what_ranking("Unknown Fighter", "pound_for_pound.txt"), "fighter is not ranked in pound for pound list")
    
    def test_largest_on_each_row(self):
        self.assertEqual(largest_on_each_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])
        self.assertEqual(largest_on_each_row([[10, 10], [5, 5]]), [10, 5])
        self.assertEqual(largest_on_each_row([[-1, -2, -3], [-4, -5, -6]]), [-1, -4])

if __name__ == "__main__":
    unittest.main()
