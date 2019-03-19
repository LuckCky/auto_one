import unittest

from transforms import change_field_type


class TestChangeFieldType(unittest.TestCase):
    def test_change_field_type_int(self):
        raw_data = [['header 1', 'header 2'], ['1', 2], ['3', 4]]
        data = change_field_type(raw_data, ['header 1'], 'int')
        self.assertEqual(data, [['header 1', 'header 2'], [1, 2], [3, 4]])

    def test_change_field_type_float(self):
        raw_data = [['header 1', 'header 2'], ['1', 2], ['3', 4]]
        data = change_field_type(raw_data, ['header 1'], 'float')
        self.assertEqual(data, [['header 1', 'header 2'], [1.0, 2], [3.0, 4]])

    def test_change_fields_type_int(self):
        raw_data = [['header 1', 'header 2', 'header 3'], ['1', 2, '3'], ['3', 4, '5']]
        data = change_field_type(raw_data, ['header 1', 'header 3'], 'int')
        self.assertEqual(data, [['header 1', 'header 2', 'header 3'], [1, 2, 3], [3, 4, 5]])

    def test_change_fields_type_float(self):
        raw_data = [['header 1', 'header 2', 'header 3'], ['1', 2, '3,0'], ['3', 4, '5']]
        data = change_field_type(raw_data, ['header 1', 'header 3'], 'float')
        self.assertEqual(data, [['header 1', 'header 2', 'header 3'], [1.0, 2, 3.0], [3.0, 4, 5.0]])

    def test_change_field_type_error(self):
        raw_data = [['header 1', 'header 2', 'header 3'], ['one', 2, '3'], ['3', 4, '5']]
        data = change_field_type(raw_data, ['header 1'], 'float')
        self.assertEqual(data, [['header 1', 'header 2', 'header 3'], [3.0, 4, '5']])

    def test_change_fields_type_error(self):
        raw_data = [['header 1', 'header 2', 'header 3'], ['one', 2, None], ['three', 4, 'five']]
        data = change_field_type(raw_data, ['header 1', 'header 3'], 'float')
        self.assertEqual(data, [['header 1', 'header 2', 'header 3']])
