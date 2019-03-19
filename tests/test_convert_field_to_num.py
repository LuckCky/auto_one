import unittest

from transforms import convert_field_to_num


class TestConvertFieldToNum(unittest.TestCase):
    def test_convert_aspiration_to_num(self):
        raw_data = [[1, 2, 'aspiration'], [1, 2, 'std'], [1, 2, 'turbo'], [3, 4, 'std']]
        data = convert_field_to_num(raw_data, 'aspiration')
        self.assertEqual(data, [[1, 2, 'aspiration'], [1, 2, 0], [1, 2, 1], [3, 4, 0]])
