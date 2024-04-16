-- Creates a database named hbnb_test_db if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates a user named 'hbnb_test' with the password 'hbnb_test_pwd' if the user does not already exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the hbnb_test_db database to the 'hbnb_test' user.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privilege on the performance_schema database to the 'hbnb_test' user.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flushes the privileges to ensure that the changes take effect.
FLUSH PRIVILEGES;
