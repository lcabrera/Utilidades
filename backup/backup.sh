#!/bin/sh
#
# Este script realiza una copia de seguridad de
# los siguientes apartados:
#
#	* Paquetes del sistema
#	* Cron's personales
#	* Directorio de root
#	* Directorios de usuario
# 	* Directorio /etc
#	* Log's del sistema
#	* Correos no leidos
#	* Copia de /var/www
#	* Copia de los servicios en srv
#	* Backup de PostgreSQL
#	* Backup de MySQL
#
# TODO:
#   * Backup de /opt
#   * Backup de Mongodb
#   * Backup de Mailman

BACKUP=/var/backups

EXCLUDE="--exclude=\"*.iso\" --exclude=\"*.mp3\" --exclude=\"*.avi\" --exclude=\"*.mpg\""

# Copia del listado de paquetes del sistema:
( /usr/bin/dpkg --get-selections | grep '[[:space:]]install$'| awk '{print $1}' > ${BACKUP}/00-dpkg_selections ) > /dev/null 2>&1

# Copia de los cron del sistema:
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/01-cron.tar /var/spool/cron ) > /dev/null 2>&1

# Copia de /root
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/02-root.tar --exclude BACKUP /root ) > /dev/null 2>&1

# Copia de /home
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/03-home.tar /home ) > /dev/null 2>&1

# Copia de /etc
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/04-etc.tar /etc ) > /dev/null 2>&1

# Copia de los log's de apache:
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/05-var_log.tar /var/log ) > /dev/null 2>&1

# Copia de los correos no leidos
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/06-var_mail.tar /var/mail ) > /dev/null 2>&1

# Copia de los directorios web
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/07-var_www.tar /var/www ) > /dev/null 2>&1

# Copia de los servicios
( /bin/tar  ${EXCLUDE} -c -f ${BACKUP}/08-srv.tar /var/srv ) > /dev/null 2>&1

# POSTGRESQL: Backup de la Base de Datos
( su -c "/usr/bin/pg_dumpall > /tmp/09-pg_dumpall.sql" postgres ) > /dev/null 2>&1

# Ahora movemos el backup a su sitio definitivo:
( mv /tmp/09-pg_dumpall.sql ${BACKUP}/ ) > /dev/null 2>&1

# MYSQL: Backup de todas las bases de datos
( mysqldump  --max_allowed_packet=1G --all-databases --single-transaction > ${BACKUP}/10-all_databases.sql ) > /dev/null 2>&1

# Las copias de todo lo anterior, solo han de ser legibles por root
/bin/chown root:root ${BACKUP}/*
/bin/chmod 600 ${BACKUP}/*

