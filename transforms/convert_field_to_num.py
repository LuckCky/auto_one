from .column_mapping import column_mapping

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def convert_field_to_num(data, column):
    logger.info('starting to convert field {} to num'.format(column))
    column_index = data[0].index(column)
    for line in data[1:]:
        line[column_index] = column_mapping[column][line[column_index]]
    logger.info('converting {} to num successful'.format(column))
    return data
