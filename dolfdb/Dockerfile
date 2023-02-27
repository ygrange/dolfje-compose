FROM mariadb:latest

ADD https://raw.githubusercontent.com/decentaur/dolfje/master/wwmnot.sql /docker-entrypoint-initdb.d/01-wwmnot.sql
ADD init_databasecontent.sql /docker-entrypoint-initdb.d/99-init_databasecontent.sql

RUN chmod 644 /docker-entrypoint-initdb.d/*.sql

EXPOSE 3306

