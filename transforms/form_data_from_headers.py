from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def form_data_from_headers(data, headers, separator):
    logger.info('starting to form data from headers')
    headers = headers.split(separator)
    indexes = []
    for header in headers:
        indexes.append(data[0].index(header))
    formed_data = [[] for _ in range(len(data))]
    for i in range(len(data)):
        for index in indexes:
            formed_data[i].append(data[i][index])
    logger.info('data formed successfully')
    return formed_data
