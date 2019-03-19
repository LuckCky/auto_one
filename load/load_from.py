from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def load_from_file(source, separator):
    """
    Loads data from any file with proper formatted data, e.g. data1;data2;data3 and etc.
    Args:
        source: string; path to file with data
        separator: string; separator (delimiter) used in file to separate one field from other
    Returns: list; returns loaded data as list of lists having first list of headers
    """
    try:
        data = []
        with open(source) as file:
            lines = [line for line in file.read().split('\n') if line]
        for line in lines:
            data.append(line.split(separator))
        logger.info('file {} was loaded successfully'.format(source))
    except Exception as e:
        logger.error('could not load data from {}'.format(source))
        logger.error(e)
        raise
    return data
