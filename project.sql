
DROP TABLE IF EXISTS Emissions;
DROP TABLE IF EXISTS Events_Impact;
DROP TABLE IF EXISTS WorldBank;

SELECT('WorldBank Tabl');
CREATE TABLE WorldBank(
  country_name VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  Inflation VARCHAR(50) NOT NULL,
  GDP INT NOT NULL,
  GDPpercapita INT NOT NULL,
  Unemployment VARCHAR(50) NOT NULL,
  GDPgrowth VARCHAR(50) NOT NULL
);

SELECT('Emissions Table');
CREATE TABLE Emissions(
    country VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    total VARCHAR(50) NOT NULL,
    coal VARCHAR(50) NOT NULL,
    oil VARCHAR(50) NOT NULL,
    gas VARCHAR(50) NOT NULL
);

SELECT('Events Table');
CREATE TABLE Events( 
    year INT NOT NULL, 
    country VARCHAR(50) NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    economic_impact_million_usd INT NOT NULL,
    international_aid_million_usd INT NOT NULL,
    impact_per_capita INT NOT NULL
);


LOAD DATA INFILE 'global_climate_events_economic_impact_2020_2025.csv'
INTO TABLE Events
FIELDS TERMINATED BY ',' /*column seperator*/
ENCLOSED BY '"' /*if fields have quotes*/
LINES TERMINATED BY '\n' /*line seperator*/
IGNORE 1 ROWS /*skip header*/
(year, country, event_type, economic_impact_million_usd, international_aid_million_usd, impact_per_capita);


LOAD DATA INFILE 'emissions.csv'
INTO TABLE Emissions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(country, year, total, coal, oil, gas);


LOAD DATA INFILE 'world_bank_data_2025.csv'
INTO TABLE WorldBank
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(country_name, year, Inflation, GDP, GDPpercapita, Unemployment, GDPgrowth);
