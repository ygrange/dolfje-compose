FROM mariadb:latest

ADD https://raw.githubusercontent.com/decentaur/dolfje/master/wwmnot.sql /docker-entrypoint-initdb.d
RUN chmod 644 /docker-entrypoint-initdb.d/wwmnot.sql
RUN apt -y update && apt install -y curl && rm -rf /var/lib/apt/lists/*

EXPOSE 3306

