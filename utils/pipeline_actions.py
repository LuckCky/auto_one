import json

from load import load_mapping
from sys_logger import init_sys_logger
from transforms import transforms_mapping

logger = init_sys_logger('pipeline_actions')


def get_pipeline(pipeline_file, pipeline_name):
    logger.info('starting to extract pipeline ({}) from {}'.format(pipeline_name, pipeline_file))
    try:
        with open(pipeline_file) as file:
            pipeline = json.load(file)
            logger.info('file {} opened'.format(pipeline_file))
    except Exception as e:
        logger.error('could not extract pipeline ({}) from {}'.format(pipeline_name, pipeline_file))
        logger.error(e)
        return
    pipeline = pipeline['pipelines'][pipeline_name]
    logger.info('pipeline loaded')
    return pipeline


def get_actions_mapping():
    all_actions_mapping = {}
    for mapping in (load_mapping, transforms_mapping):
        all_actions_mapping.update(mapping)
    return all_actions_mapping
