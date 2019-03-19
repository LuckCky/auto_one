import unittest

from utils.pipeline_actions import get_pipeline, get_actions_mapping


class TestPipelineActions(unittest.TestCase):
    def test_get_pipeline(self):
        pipeline = get_pipeline('../pipelines/pipeline_test.json', 'price_prediction')
        self.assertEqual(pipeline,
                         [['load_from_file', {}],
                          ['clean', {'unwanted_data': '-'}],
                          ['one_hot_encode', {'column': 'engine-location'}],
                          ['convert_field_to_num', {'column': 'num-of-cylinders'}],
                          ['convert_field_to_num', {'column': 'aspiration'}]])

    def test_get_error_pipeline(self):
        pipeline = get_pipeline('not_existing_pipeline_test.json', 'price_prediction')
        self.assertEqual(pipeline, None)


class TestPipelineActions(unittest.TestCase):
    def test_get_actions_mapping(self):
        actions = get_actions_mapping()
        self.assertIsInstance(actions, dict)
