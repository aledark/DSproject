CREATE TABLE tasks (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
content VARCHAR(200) NOT NULL,
date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
