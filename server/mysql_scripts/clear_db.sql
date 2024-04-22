-- Select the database
USE gymni;

-- Disable foreign key checks to avoid potential issues
SET foreign_key_checks = 0;

DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `gymes`;
DROP TABLE IF EXISTS `cities`;
DROP TABLE IF EXISTS `amenities`;
DROP TABLE IF EXISTS `gym_amenity`;
DROP TABLE IF EXISTS `reviews`;

-- Re-enable foreign key checks
SET foreign_key_checks = 1;
