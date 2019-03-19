#!/usr/bin/python3

import logging
import logging.handlers


def init_sys_logger(name):
    _logger = logging.getLogger(name=name)
    path_to_log_file = "./logs/" + name + ".log"
    file_handler = logging.handlers.RotatingFileHandler(filename=path_to_log_file,
                                                        maxBytes=10485760,
                                                        backupCount=3)
    console_handler = logging.StreamHandler()
    log_formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s:%(message)s",
                                      datefmt="%d/%m/%Y %H:%M:%S")
    file_handler.setFormatter(log_formatter)
    console_handler.setFormatter(log_formatter)

    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)
    _logger.setLevel(logging.INFO)

    return _logger
