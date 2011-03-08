#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

fn_log = 'a.log.conf'
my_logger = 'pepe'

logging.config.fileConfig(fn_log)

# create logger
logger = logging.getLogger(my_logger)

# "application" code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
