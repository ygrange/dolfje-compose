CREATE USER 'pinger'@'localhost' ;
GRANT usage on *.* to 'pinger'@'localhost';

INSERT INTO games (gms_name, gms_status, gms_vote_style, gms_revive) values ('ww0', 'ENDED', 'blind', 0);

