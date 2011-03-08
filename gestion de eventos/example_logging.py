#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cmdline-tool.txt 5546 2008-05-07 12:54:18Z goodger $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Ejemplo del uso del módulo Logging.

Se cargan dos logger's y quedan registradas dos entradas diferentes.
"""

import logging
import logging.config

FICHERO_INI = 'example_logging.ini'
LOG_NIVEL1 = 'nivel1'
LOG_NIVEL2 = 'nivel2'

logging.config.fileConfig(FICHERO_INI)

# create logger
LOGGER = logging.getLogger(LOG_NIVEL1)

# "application" code
LOGGER.debug('debug message')
LOGGER.info('info message')
LOGGER.warn('warn message')
LOGGER.error('error message')
LOGGER.critical('critical message')

# create logger
LOGGER2 = logging.getLogger(LOG_NIVEL2)

LOGGER2.debug('debug message 2')
LOGGER2.info('info message 2')
LOGGER2.warn('warn message 2')
LOGGER2.error('error message 2')
LOGGER2.critical('critical message 2')
