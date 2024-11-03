CREATE DATABASE Sinimini;
USE Sinimini;
CREATE TABLE MoviesAndSeries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    director VARCHAR(255),
    release_year YEAR,
    country_of_origin VARCHAR(100),
    runtime INT,  
    type ENUM('Movie', 'Series') NOT NULL
);