DROP TABLE IF EXISTS WorldBank ;
CREATE TABLE WorldBank (
  country_name                      VARCHAR(20)   NOT NULL,
  country_id                        VARCHAR(60)   NULL,
  year                              INT           NULL,
  Inflation_(CPI_%)                 VARCHAR(64)   NULL,
  GDP_(Current_USD)                 VARCHAR(64)   NULL,
  GDP_per_Capita_(Current_USD)      VARCHAR(64)   NULL,
  Unemployment_Rate_(%)             VARCHAR(64)   NULL,
  "Interest_Rate_(Real              VARCHAR(64)   NULL,
  _%)"                              VARCHAR(64)   NULL,
  "Inflation_(GDP_Deflator          VARCHAR(64)   NULL,
  _%)"                              VARCHAR(64)   NULL,
  GDP_Growth_(%_Annual)             VARCHAR(64)   NULL,
  Current_Account_Balance_(%_GDP)   VARCHAR(64)   NULL,
  Government_Expense_(%_of_GDP)     VARCHAR(64)   NULL,
  Government_Revenue_(%_of_GDP)     VARCHAR(64)   NULL,
  Tax_Revenue_(%_of_GDP)            VARCHAR(64)   NULL,
  Gross_National_Income_(USD)       VARCHAR(64)   NULL,
  Public_Debt_(%_of_GDP)            VARCHAR(64)   NULL
);

DROP TABLE IF EXISTS Events ;
CREATE TABLE Events (
  event_id                        VARCHAR(20)   NOT NULL,
  date                            VARCHAR(60)   NULL,
  year                            INT           NULL,
  month                           VARCHAR(64)   NULL,
  country                         VARCHAR(64)   NULL,
  event_type                      VARCHAR(64)   NULL,
  severity                        VARCHAR(64)   NULL,
  duration_days                   VARCHAR(64)   NULL,
  affected_population             VARCHAR(64)   NULL,
  deaths                          VARCHAR(64)   NULL,
  injuries                        VARCHAR(64)   NULL,
  economic_impact_million_usd     VARCHAR(64)   NULL,
  infrastructure_damage_score     VARCHAR(64)   NULL,
  response_time_hours             VARCHAR(64)   NULL,
  international_aid_million_usd   VARCHAR(64)   NULL,
  latitude                        VARCHAR(64)   NULL,
  longitude                       VARCHAR(64)   NULL,
  total_casualties                VARCHAR(64)   NULL,
  impact_per_capita               VARCHAR(64)   NULL,
  aid_percentage                  VARCHAR(64)   NULL
);

DROP TABLE IF EXISTS Emissions ;
CREATE TABLE Emissions (
  "Country"              VARCHAR(20)   NOT NULL,
  "ISO_3166_1_alpha_3"   VARCHAR(60)   NULL,
  "Year"                 INT           NULL,
  "Total"                VARCHAR(64)   NULL,
  "Coal"                 VARCHAR(64)   NULL,
  "Oil"                  VARCHAR(64)   NULL,
  "Gas"                  VARCHAR(64)   NULL,
  "Cement"               VARCHAR(64)   NULL,
  "Flaring"              VARCHAR(64)   NULL,
  "Other"                VARCHAR(64)   NULL,
  "Per_Capita"           VARCHAR(64)   NULL
);

