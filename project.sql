

print('world_bank table')

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
