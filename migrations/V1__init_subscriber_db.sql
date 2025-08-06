CREATE DATABASE subscriber_db;
CREATE USER 'subscriber_user' IDENTIFIED BY 'subscriber_password';
GRANT ALL PRIVILEGES ON subscriber_db.* TO 'subscriber_user';
