#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim:fileencoding=utf-8

"""
#       Copyright 2009 Luis Cabrera <lcabrera@sauco.org>
#
#       This program  is free software;  you can redistribute  it and/or
#       modify it under  the terms of the GNU General  Public License as
#       published by the  Free Software Foundation; either  version 2 of
#       the License, or (at your option) any later version.
#
#       This program is distributed in the  hope that it will be useful,
#       but WITHOUT ANY  WARRANTY; without even the  implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#       General Public License for more details.
#
#       You  should have  received  a  copy of  the  GNU General  Public
#       License  along with  this program;  if  not, write  to the  Free
#       Software  Foundation, Inc.,  51  Franklin  Street, Fifth  Floor,
#       Boston, MA 02110-1301, USA.

 * http://docs.python.org/dev/howto/logging.html
 * http://www.google.es/search?sourceid=chrome&ie=UTF-8&q=python+example+logging.conf
 * http://www.red-dove.com/python_logging.html
 * http://docs.python.org/library/logging.html

"""

__module__ = 'ejemplos'
__author__ = 'Luis Cabrera Sauco (lcabrera@sauco.org)'
__version__ = '0.1'
__revision__ = '$Revision: $'
__date__ = '$Date: $'
__copyright__ = 'Copyright (c) 2010 Luis Cabrera Sauco'
__license__ = 'GPL'
__file__ = '$Id: $'
__source__ = '$Source: $'
# Redefiniendo la documentación:
# __doc__ = 'Clase de ejemplo'

# importación de módulos

# importación de partes de módulos

# importación de módulos personalizados

# Variables:

class Ejemplo:

    """Clase que implementa los métodos necesarios para ...
    """

    def __init__(self):
        """MéŘtodo inicial de la clase. Se ejecuta al carga la clase.
        """

        # importación de módulos
        import os
        import sys
        # import logging
        import logging.config

        # Variables:

        # Parámetros a recibir:
        # Si no pasamos parametros de ningún tipo, la llamada al programa recibe
        # al menos el envio del nombre del fichero. Por eso hay que sumar uno a
        # esta función.
        param = 0
        param = param + 1

        nombre_base = os.path.basename(os.path.splitext(sys.argv[0])[0])
        filename_log = nombre_base + '.log'
        filename_log_conf = nombre_base + '_logging.conf'

        # Nivel de depuración:
        self.nivel = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL}

        # print dir(self.nivel)
        # print type(self.nivel)
        # print type(sys.argv)
        # print sys.argv

        # Declaramos algunas variables iniciales.
        self.var_a = ''
        self.var_b = []
        self.nombre = ''

        if (os.path.exists(filename_log_conf) and os.path.isfile(filename_log_conf)):
            logging.config.fileConfig(filename_log_conf)
        else:
            sys.stderr.write('\n\tNo existe el archivo de configuración del log: %s\n\n' % filename_log_conf)
            sys.exit(1)

        #logging.basicConfig(
        #            level=self.nivel['debug'],
        #            format='%(asctime)s %(levelname)-8s %(message)s',
        #            datefmt='%a, %d %b %Y %H:%M:%S',
        #            filename=filename_log,
        #            filemode='w')

        # create logger
        logger = logging.getLogger(nombre_base)

        # Entradas de ejemplo:
        logging.debug('This is a debug message (10)')
        logging.info('This is an info message (20)')
        logging.warning('This is a warning message (30)')
        logging.error('This is an error message (40)')
        logging.critical('This is a critical error message (50)')

        if len(sys.argv) == int(param):
            print 'Se han recibido %s argumentos.' % (len(sys.argv))
            print 'Es lo correcto. Seguimos.'
        else:
            print 'Se han recibido %s argumentos.' % (len(sys.argv))
            print 'Estos argumentos son: %s' % (sys.argv)
            print 'Redirigir a la función USAGE.'
            sys.stderr.write('\n\tArgumentos inválidos\n\n')
            sys.exit(1)

        print 'Entrando a la clase ejemplo().'

    def __del__(self):
        """Este metodo se invoca cuando se destruye la clase
        """

        print 'Saliendo de la clase ejemplo().'

    def metodo_de_ejemplo(self, nombre):
        """Este metodo devuelve un saludo
        """

        self.nombre = nombre

        print 'Mi nombre es %s' % nombre


# Test de funcionalidad
# ~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    MI_NOMBRE = 'Luis'
    TEST = Ejemplo()
    TEST.metodo_de_ejemplo(MI_NOMBRE)