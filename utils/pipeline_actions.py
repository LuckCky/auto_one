#!/usr/bin/python3

import json

from load import load_mapping
from utils.sys_logger import init_sys_logger
from transforms import transforms_mapping

logger = init_sys_logger(__name__)


def get_pipeline(pipeline_file, pipeline_name):
    """
    Gets pipeline from json
    Args:
        pipeline_file: string; path to file with steps of transforming data
        pipeline_name: string; name of ETL pipeline
    Returns: dict; dict of steps according to which data will be transformed
    """
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
    """
    Maps action names with corresponding functions
    Returns: dict; dict of action names and action functions
    """
    logger.info('starting to get actions mapping')
    all_actions_mapping = {}
    for mapping in (load_mapping, transforms_mapping):
        all_actions_mapping.update(mapping)
    logger.info('actions mapping loaded successfully')
    logger.info('actions mapping = {}'.format(all_actions_mapping))
    return all_actions_mapping
