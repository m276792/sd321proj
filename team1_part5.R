
library(DBI)
library(RMariaDB)
library(ggplot2)
library(dplyr)
library(tidyr)

user     <- "m276792"
password <- "m276792"
host     <- "db.cs.usna.edu"
database <- "m276792"

library(RMariaDB)

db <- dbConnect(RMariaDB::MariaDB(),
    user     = user,
    password = password,
    host     = host,
    dbname   = database)

query <- "
SELECT    Country, Year,   
CAST(Inflation AS DECIMAL(10,2)) AS Inflation,  
CAST(GDPGrowth AS DECIMAL(10,2)) AS GDPGrowth,  
CAST(Unemployment AS DECIMAL(10,2)) AS Unemployment,   
CAST(GDP AS DECIMAL(17,2)) AS GDP   
FROM WorldBank   
WHERE Year IN ('2019')   
AND Unemployment IS NOT NULL   
ORDER BY GDP DESC   
LIMIT 16;
"


df <- dbGetQuery(db, query)

df_long <- df %>%
  pivot_longer(
    cols = c(Inflation, GDPGrowth, Unemployment),
    names_to = "Indicator",
    values_to = "Value"
  )

# bar plot
ggplot(df_long, aes(x = Year, y = Value, fill = Indicator)) +
  geom_col(position = "dodge") +
  facet_wrap(~ Country) +
  theme_minimal() +
  ggtitle("Economic Indicators by Country (2019–2021)") +
  ylab("Value") +
  xlab("Year")

ggsave("R_country_indicators_barplot.png", dpi = 300, width = 12, height = 6)


db <- dbConnect(RMariaDB::MariaDB(),
    user     = user,
    password = password,
    host     = host,
    dbname   = database)

query <- "
SELECT Country, Year, 
CAST(GDP AS DECIMAL(17,2)) AS GDP
FROM WorldBank
WHERE Year = '2019'
AND GDP IS NOT NULL
ORDER BY GDP DESC
LIMIT 16;
"

df <- dbGetQuery(db, query)

# pie chart
ggplot(df, aes(x = "", y = GDP, fill = Country)) +
  geom_col(width = 1) +
  coord_polar(theta = "y") +
  theme_void() +
  ggtitle("GDP Distribution (2019)") +
  theme(plot.title = element_text(hjust = 0.5))

ggsave("R_GDP_PieChart_2019.png", dpi = 300, width = 8, height = 8)



db <- dbConnect(RMariaDB::MariaDB(),
    user     = user,
    password = password,
    host     = host,
    dbname   = database)

query <- "
SELECT
    e.Country,
    AVG(CAST(e.Total AS DECIMAL(18,3))) AS avg_total_emissions,
    AVG(CAST(ev.EconomicImpact AS DECIMAL(18,2))) AS avg_impact,
    SUM(CAST(ev.EconomicImpact AS DECIMAL(18,2))) AS total_impact,
    COUNT(ev.event_type) AS event_count,
    SUM(total_impact) / SUM(avg_total_emissions) AS ratio
FROM Emissions e
LEFT JOIN Events ev
    ON e.Country = ev.Country
    AND e.Year = ev.Year

WHERE e.Year IN (2019, 2020, 2021)
  AND e.Country <> 'Global'
  AND ev.event_type IN ('Drought','Heatwave','Wildfire','Cold Wave','Flood','Landslide')

GROUP BY e.Country
ORDER BY event_count DESC
LIMIT 16;
"

df <- dbGetQuery(db, query)

# Prepare data for plotting
df_long <- df %>%
  pivot_longer(
    cols = c(avg_total_emissions, ratio, total_impact),
    names_to = "Metric",
    values_to = "Value"
  )

# Bar chart comparing Emissions vs Impact
ggplot(df_long, aes(x = Country, y = Value, fill = Metric)) +
  geom_col(position = "dodge") +
  theme_minimal() +
  ggtitle("Emissions vs Economic Impact per Country (2019–2021)") +
  xlab("Country") +
  ylab("Value") +
  theme(plot.title = element_text(hjust = 0.5),
        axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("R_emissions_vs_impact_per_country.png",
       dpi = 300, width = 12, height = 6)




