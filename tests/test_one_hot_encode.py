import unittest

from transforms import one_hot_encode


class TestOneHotEncode(unittest.TestCase):
    def test_one_hot_encode(self):
        raw_data = [['header 1', 'header 2', 'header 3'], [1, 2, 'three'], [1, 2, 'four'], [1, 2, 'one']]
        encoded_data = one_hot_encode(raw_data, 'header 3', save_file=False)
        self.assertEqual(encoded_data, [['header 1', 'header 2', 'header 3'],
                                        [1, 2, [1, 0, 0]],
                                        [1, 2, [0, 1, 0]],
                                        [1, 2, [0, 0, 1]]])
