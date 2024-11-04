CREATE TABLE film_and_series (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    content_name VARCHAR(255) NOT NULL,
    runtime INT,  -- runtime in minutes
    director VARCHAR(255),
    genre VARCHAR(100),
    release_year YEAR
);
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL  
);
CREATE TABLE user_content_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    content_id INT,
    status ENUM('watched', 'watch later') NOT NULL,
    rating DECIMAL(3, 1), 
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES film_and_series(content_id) ON DELETE CASCADE
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dataset.csv'
INTO TABLE film_and_series
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(content_name, genre, director, release_year, runtime);
SHOW VARIABLES LIKE 'secure_file_priv';
DROP TABLE filmsandseries;



