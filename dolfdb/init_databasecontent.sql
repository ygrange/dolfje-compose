CREATE USER 'pinger'@'localhost' ;
GRANT usage on *.* to 'pinger'@'localhost';

INSERT INTO games (gms_name, gms_created_at) values ('ww0',NULL);
