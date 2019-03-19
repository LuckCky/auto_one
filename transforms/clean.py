#!/usr/bin/python3

import re

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def clean(data, unwanted_data, separator):
    """
    Remove row if it has unwanted data as one of elements
    Args:
        data: list; list of lists with data, first row is headers
        unwanted_data: string; if this data in row, row is excluded from data
        separator: string; separator (delimiter) used in file to separate one field from other
    Returns: list; data without rows with unwanted data
    """
    logger.info('starting to clean data from {}'.format(unwanted_data))
    cleaned_data = []
    for i in range(len(data)):
        if i == 0:
            cleaned_data.append(data[i])
        else:
            regex = r'({sep}|\s)?{unwanted}(\s|{sep})'.format(sep=separator, unwanted=unwanted_data)
            if not re.search(regex, separator.join(data[i]) + separator):
                cleaned_data.append(data[i])
            else:
                logger.info('removing line {} because it has "{}"'.format(data[i], unwanted_data))
    return cleaned_data
