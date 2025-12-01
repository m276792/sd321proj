
library(DBI)
library(RMariaDB)
library(ggplot2)
library(dplyr)

user     <- "m276792"
password <- "m276792"
host     <- "db.cs.usna.edu"
database <- "m276792"

library(RMariaDB)

db <- dbConnect(RMariaDB::MariaDB(),
    user <- user,
    password <- password,
    host     <- host,
    dbname   <- database )

query <- "
SELECT 
  w.Country, w.Year,
  CAST(w.Unemployment AS DECIMAL(10,2)) AS Unemployment,
  e.event_type,
  e.EconomicImpact
FROM WorldBank w
LEFT JOIN Events e
  ON w.Country = e.country AND w.Year = e.year;
"

df <- dbGetQuery(db, query)

ggplot(df, aes(x <- Year, y <- Unemployment, color <- event_type)) +
  geom_line() +
  facet_wrap(~Country) +
  theme_minimal() +
  ggtitle("Unemployment Trends During Economic Events")

ggsave("R_unemployment_events.png", dpi=300, width=10, height=6)