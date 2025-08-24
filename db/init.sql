DROP DATABASE IF EXISTS challenge_db;
CREATE DATABASE challenge_db;
USE challenge_db;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) UNIQUE,
  email VARCHAR(200)
);

CREATE TABLE admin (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100),
  password VARCHAR(200)
);

INSERT INTO users (username, email) VALUES
('ankit', 'ankit@gmail.com'),
('shah', 'ankitshah@gmail.com');

INSERT INTO admin (username, password) VALUES ('admin', 'FLAG{un10n_1nject10n_d0ne}');
