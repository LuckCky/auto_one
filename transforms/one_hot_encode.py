#!/usr/bin/python3

from collections import OrderedDict
import json

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def one_hot_encode(data, column, save_file=True):
    """
    Encodes string data to list of 1 and 0
    Args:
        data: list; list of lists with data, first row is headers
        column: string; column where data needs to be one-hot-encoded
        save_file: boolean; if true mapping of strings to list of 1 and 0 is save on disk
    Returns: list; list of lists with one column encoded
    """
    logger.info('starting one-hot-encode for {}'.format(column))
    distinct_values = OrderedDict()
    index_of_column = data[0].index(column)
    for i in range(1, len(data)):
        distinct_values[data[i][index_of_column]] = True
    value_to_int = dict((c, i) for i, c in enumerate(distinct_values.keys()))
    int_to_value = dict((i, c) for i, c in enumerate(distinct_values.keys()))
    integer_encoded = [value_to_int[line[index_of_column]] for line in data[1:]]
    one_hot_encoded = {}
    for value in integer_encoded:
        column_data = [0 for _ in range(len(distinct_values))]
        column_data[value] = 1
        one_hot_encoded[int_to_value[value]] = column_data
    for line in data[1:]:
        line[index_of_column] = one_hot_encoded[line[index_of_column]]
    if save_file:
        with open('one_hot_encoded_{}.txt'.format(column), 'w') as file:
            file.write(json.dumps(one_hot_encoded))
        logger.info('{} one-hot-encoded and saved to file {}'.format(column, 'one_hot_encoded_{}.txt'.format(column)))
    logger.info('{} one-hot-encoded and NOT saved to file'.format(column))
    return data
