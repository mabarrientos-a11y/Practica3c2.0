# Usa la imagen oficial de PostgreSQL
FROM postgres:latest
# Copia el script SQL al directorio de inicialización de PostgreSQL
COPY init.sql /docker-entrypoint-initdb.d/01_init.sql
COPY save_sata.sql /docker-entrypoint-initdb.d/02_save_sata.sql
# PostgreSQL ejecutará automáticamente los scripts en /docker-entrypointinitdb.d/