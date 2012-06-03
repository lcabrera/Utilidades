#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

import modulo_08_data

a = yaml.load(
"""
Local:
  - Zona Elaboracion:
    - Local:
      - Suelos:
        - Descripcion:
          - "Descripción de esta caracteristica..."
        - Prioridad:
          - 1
        - Dias:
          - [1, 2, 3, 4, 5]
      - Techos: [1, 2, 3, 4, 5]
      - Puertas: [1, 2, 3, 4, 5]
    - bbb
    - ccc
    - ddd
    - 4
    - 5
    - 10: [a, b, c]
    - 15
  - Zona Publica
  - Almacen
  - Aseos
"""
#"""
#Local Local:
#    [Zona Elaboración:
#        [Local:
#            [Suelos:
#                [Descripcion:
#                    []
#                ],
#                [Prioridad:
#                    []
#                ],
#                [Dias:
#                    [1,2,3,4,5]
#                ],
#            Techos: [1,2,3,4,5],
#            Puertas: [1,2,3,4,5]
#            ],
#        bbb,
#        ccc,
#        ddd
#        ],
#        4,
#        5,
#        10: [a,b,c],
#        15
#    ]
#"""
)

# Forma de cargar un fichero yaml
# 'document.yaml' contains a single YAML document.
# stream = file('document.yaml', 'r')
# yaml.load(stream)

print type(a)

print yaml.dump(a)
