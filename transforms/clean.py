import re

from sys_logger import init_sys_logger

logger = init_sys_logger('clean')


def clean(data, unwanted_data, separator):
    cleaned_data = []
    for i in range(len(data)):
        if i == 0:
            cleaned_data.append(data[i])
        else:
            regex = r'({sep}|\s)?{unwanted}(\s|{sep})'.format(sep=separator, unwanted=unwanted_data)
            if not re.search(regex, separator.join(data[i]) + separator):
                cleaned_data.append(data[i])
    return cleaned_data
