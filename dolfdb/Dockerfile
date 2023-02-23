FROM mysql:latest

ADD https://raw.githubusercontent.com/decentaur/dolfje/master/wwmnot.sql /docker-entrypoint-initdb.d
RUN chmod 644 /docker-entrypoint-initdb.d/wwmnot.sql

EXPOSE 3306

