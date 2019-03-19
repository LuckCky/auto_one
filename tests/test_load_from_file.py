import unittest

from load import load_from_file


class TestLoadFromFile(unittest.TestCase):
    def test_load_from_file_positive(self):
        data = load_from_file('../Challenge_me.txt', ';')
        self.assertIsInstance(data, list)

    def test_load_from_file_negative(self):
        try:
            load_from_file('not_existing_file', ';')
        except:
            self.assertRaises(FileNotFoundError)
