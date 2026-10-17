CREATE DATABASE aircraftfleet;

CREATE TABLE `aircraftfleet`.`fleet` (
  `idFleet` INT NOT NULL AUTO_INCREMENT,
  `TailNumber` VARCHAR(45) NULL,
  `ShipNumber` INT NULL,
  `Type` VARCHAR(45) NULL,
  `Status` VARCHAR(45) NULL,
  `Location` VARCHAR(45) NULL,
  PRIMARY KEY (`idFleet`));
