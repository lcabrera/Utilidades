#!/usr/bin/python
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

    """
    Clase que implementa los métodos necesarios para ...
    """

    def __init__(self):
        """
        Método inicial de la clase. Se ejecuta al carga la clase.
        """

        # importación de módulos
        import os
        import sys
        import optparse

        # import logging
        import logging.config

        # Declaramos algunas variables iniciales.
        self.var_a = ''
        self.var_b = []
        self.nombre = ''

        # Parámetros a recibir:
        # Si no pasamos parametros de ningún tipo, la llamada al programa recibe
        # al menos el envio del nombre del fichero. Por eso hay que sumar uno a
        # esta función.
        param = 0
        #param = param + 1

        #if len(sys.argv) == int(param):
        #    print 'Se han recibido %s argumentos.' % len(sys.argv)
        #    print 'Es lo correcto. Seguimos.'
        #else:
        #    print 'Se han recibido %s argumentos.' % len(sys.argv)
        #    print 'Estos argumentos son: %s' % sys.argv
        #    sys.stderr.write('\t' + str(self.usage()) + '\n\n')
        #    sys.exit(1)

        parser = optparse.OptionParser("usage: %prog [options] arg1 arg2")
        parser.add_option(
            "-H",
            "--host",
            dest="hostname",
            default="127.0.0.1",
            type="string",
            help="specify hostname to run on")
        parser.add_option(
            "-p",
            "--port",
            dest="portnum",
            default=80,
            type="int",
            help="port number to run on")

        parser.add_option(
            '--version',
            dest="version",
            default=1.0,
            type="float",
            )

        (options, args) = parser.parse_args()

        if len(args) > 0:
            print 'Se han recibido %s parámetros: %s' % (len(args), options)
            if len(args) != param:
                parser.error("Se ha recibido un número incorrecto de parámetros.\n\n\tSe han recibido exactamente %s parámetros.\n\n" % (param))
        else:
            print 'No se han pasado parámetros en la llamada de la app.'

        hostname = options.hostname
        portnum = options.portnum
        version = options.version

        (options, remainder) = parser.parse_args()
        print 'HOST      :', hostname
        print 'PUERTO    :', portnum
        print 'VERSION   :', options.version
        print 'REMAINING :', remainder

        nombre_base = os.path.basename(os.path.splitext(sys.argv[0])[0])
        filename_log = nombre_base + '.log'
        filename_log_ini = nombre_base + '_logging.ini'
        log_nivel1 = 'nivel1'

        if os.path.exists(filename_log_ini) and os.path.isfile(filename_log_ini):
            logging.config.fileConfig(filename_log_ini)
            # creamos un logger
            self.log = logging.getLogger(log_nivel1)
            self.log.info('Usaremos el fichero %s para el registro de eventos' % filename_log_ini)
        else:
            sys.stderr.write('''\n\tNo existe el archivo de configuración del log: %s\n''' % filename_log_ini)
            sys.exit(1)

        self.log.debug('TEST: This is a debug message (10)')
        self.log.info('TEST: This is an info message (20)')
        self.log.warning('TEST: This is a warning message (30)')
        self.log.error('TEST: This is an error message (40)')
        self.log.critical('TEST: This is a critical error message (50)')

        self.log.debug('Class::__init__: Entrando a la clase ejemplo().')

    def __del__(self):
        """
        Este método se invoca cuando se destruye la clase.
        """

        # self.log.debug('Class::__del__: Entrando en la clase.')
        pass
        # self.log.debug('Class::__del__: Saliendo de la clase.')
        pass

    def usage(self):
        """
        Mostramos las opciones necesarias para que esta aplicación funcione.
        """

        # self.log.debug('Class::usage: Entrando en la clase.')
        print "Usage: filter.py\n\t--bayes=bayes.pck\n\t--from=folder,folder,folder\n\t[--to=folder]\n\t[--detail]\n\t[--over=float|--under=float]"
        print """\n\nExample:\n\tpython filter.py --from=/Personal/Hotmail,/Personal/ExJunk --over=.35 --detail --to=/SpamMaybe"""
        # self.log.debug('Class::usage: Saliendo de la clase.')
        return

    def metodo_de_ejemplo(self, nombre):
        """
        Este método devuelve un saludo, a modo de ejemplo básico.
        """

        self.log.debug('Class::metodo_de_ejemplo: Entrando en el metodo_de_ejemplo().')

        self.nombre = nombre

        print 'Mi nombre es %s' % nombre

        self.log.debug('Class::metodo_de_ejemplo: Saliendo del metodo_de_ejemplo().')


# Test de funcionalidad
# ~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    MI_NOMBRE = 'Luis'
    TEST = Ejemplo()
    TEST.metodo_de_ejemplo(MI_NOMBRE)
    #TEST.log.info('Ejemplo::init un disoarate, zi zeñó')
