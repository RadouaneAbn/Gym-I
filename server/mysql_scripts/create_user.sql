CREATE USER 'radouane'@'localhost' IDENTIFIED BY 'radouane';

GRANT ALL PRIVILEGES ON *.* TO 'radouane'@'localhost';

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS gymni;
