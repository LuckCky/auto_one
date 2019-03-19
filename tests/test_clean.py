import unittest

from transforms import clean


class TestClean(unittest.TestCase):
    def test_clean_change_raw_data_middle_end(self):
        raw_data = [['this', 'stays'], ['but', 'not', 'this', '-'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_left_end(self):
        raw_data = [['this', 'stays'], ['but', 'not', 'this', '- '], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_right_end(self):
        raw_data = [['this', 'stays'], ['but', 'not', 'this', ' -'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_middle_start(self):
        raw_data = [['this', 'stays'], ['-', 'but', 'not', 'this'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_left_start(self):
        raw_data = [['this', 'stays'], ['- ', 'but', 'not', 'this'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_right_start(self):
        raw_data = [['this', 'stays'], [' -', 'but', 'not', 'this'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_middle_middle(self):
        raw_data = [['this', 'stays'], ['but', 'not', '-', 'this'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_left_middle(self):
        raw_data = [['this', 'stays'], ['but', 'not', '- ', 'this'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_change_raw_data_right_middle(self):
        raw_data = [['this', 'stays'], ['but', 'not', ' -', 'this'], ['this', 'stays', 'too']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, [['this', 'stays'], ['this', 'stays', 'too']])

    def test_clean_not_change_raw_data(self):
        raw_data = [[], ['1', '2', 'three', 'data-with-separator-but-not-really']]
        cleaned_data = clean(raw_data, '-', ';')
        self.assertEqual(cleaned_data, raw_data)
