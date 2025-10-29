

SELECT('world_bank table');

DROP TABLE IF EXISTS `WorldBank`;

CREATE TABLE `WorldBank` (
  country_name VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  Inflation VARCHAR(50) NOT NULL,
  GDP INT NOT NULL,
  GDPpercapita INT NOT NULL,
  Unemployment VARCHAR(50) NOT NULL,
  GDPgrowth VARCHAR(50)
  
);

SELECT('emissions table');

DROP TABLE IF EXISTS 'Emissions';

CREATE TABLE `Emissions` (
    country VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    total VARCHAR(50) NOT NULL,
    coal VARCHAR(50) NOT NULL,
    oil VARCHAR(50) NOT NULL,
    gas VARCHAR(50) NOT NULL
);


CREATE TABLE events_impact( 
    year INT, 
    country VARCHAR(50),
    event_type VARCHAR(50),,
    economic_impact_million_usd INT,
    international_aid_million_usd INT,
    impact_per_capita INT
);