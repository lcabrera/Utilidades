#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

f = open('modulo_08_cfg.yml')

settings = yaml.load(f)
print settings
