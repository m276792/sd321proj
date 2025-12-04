DROP TABLE IF EXISTS WorldBank ;
CREATE TABLE WorldBank (
  Country                  VARCHAR(20)   NOT NULL,
  Year                      INT           NULL,
  Inflation                 VARCHAR(64)   NULL,
  GDP                     VARCHAR(64)   NULL,
  Unemployment             VARCHAR(64)   NULL,
  GDPGrowth                 VARCHAR(64)   NULL
);

DROP TABLE IF EXISTS Events ;
CREATE TABLE Events (
  year                            INT           NULL,
  country                         VARCHAR(64)   NULL,
  event_type                      VARCHAR(64)   NULL,
  EconomicImpact     VARCHAR(64)   NULL,
  InternationalAid   VARCHAR(64)   NULL,
  ImpactPerCapita               VARCHAR(64)   NULL
);

DROP TABLE IF EXISTS Emissions ;
CREATE TABLE Emissions (
  Country            VARCHAR(20)   NOT NULL,
  Year                 INT           NULL,
  Total                VARCHAR(64)   NULL,
  Coal                 VARCHAR(64)   NULL,
  Oil                  VARCHAR(64)   NULL,
  Gas                  VARCHAR(64)   NULL
);

