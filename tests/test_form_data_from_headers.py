import unittest

from transforms import form_data_from_headers


class TestFormDataFromHeaders(unittest.TestCase):
    def test_form_data_from_headers_straight(self):
        raw_data = [['header 1', 'header 2', 'header 3', 'header 4'], [1, 2, 3, 4], [11, 22, 33, 44]]
        headers = 'header 2; header 4'
        separator = '; '
        formed_data = form_data_from_headers(raw_data, headers, separator)
        self.assertEqual(formed_data, [['header 2', 'header 4'], [2, 4], [22, 44]])

    def test_form_data_from_headers_mixed(self):
        raw_data = [['header 1', 'header 2', 'header 3', 'header 4'], [1, 2, 3, 4], [11, 22, 33, 44]]
        headers = 'header 4; header 1'
        separator = '; '
        formed_data = form_data_from_headers(raw_data, headers, separator)
        self.assertEqual(formed_data, [['header 4', 'header 1'], [4, 1], [44, 11]])
