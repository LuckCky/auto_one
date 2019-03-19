from .types_mapping import types_mapping
from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def change_field_type(data, column_name, new_type):
    for column in column_name:
        logger.info('starting to change field {} type to {}'.format(column, new_type))
        col_index = data[0].index(column)
        for line in data[1:]:
            try:
                if new_type == 'float':
                    line[col_index] = types_mapping[new_type](line[col_index].replace(',', '.'))
                else:
                    line[col_index] = types_mapping[new_type](line[col_index])
            except ValueError:
                data.pop(data.index(line))
    logger.info('finished changing fields {} to type {}'.format(column_name, new_type))
    return data
