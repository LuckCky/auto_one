from sys_logger import init_sys_logger

logger = init_sys_logger('load_from')


def load_from_file(source, separator):
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
