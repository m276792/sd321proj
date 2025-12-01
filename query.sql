/*
mysql -h db.cs.usna.edu -u m271974 -pm271974 m271974 -fcvvv < query.sql
*/

/* THIS QUERY SHOWS ALL TABLES JOINED */
SELECT 
    CAST(e.Total AS DECIMAL(18,3)) AS total_emissions,
    CAST(ev.EconomicImpact AS DECIMAL(18,2)) AS economic_impact,
    CAST(w.GDP AS DECIMAL(18,2)) AS gdp
FROM Emissions e
LEFT JOIN Events ev
    ON e.Country = ev.Country AND e.Year = ev.Year
LEFT JOIN WorldBank w
    ON e.Country = w.Country AND e.Year = w.Year;



/* THIS QUERY produces a summary table of natural disaster activity per country per year */

SELECT 
    Country, 
    Year,
    COUNT(*) AS event_count, /* how many events happened in each country */
    AVG(CAST(EconomicImpact AS DECIMAL(18,2))) AS avg_impact, /* average impact of each event */
    SUM(CAST(EconomicImpact AS DECIMAL(18,2))) AS total_impact /* total impact on country*/
FROM Events
GROUP BY Country, Year; 


/*HOW EMISSIONS AFFECT COUNTRIES*/

SELECT 
    e.Country,
    e.Year,
    MAX(CAST(e.Total AS DECIMAL(18,3))) AS total_emissions,
    MAX(CAST(e.Coal AS DECIMAL(18,3))) AS coal_emissions,
    MAX(CAST(e.Oil AS DECIMAL(18,3))) AS oil_emissions,
    MAX(CAST(e.Gas AS DECIMAL(18,3))) AS gas_emissions,

    AVG(CAST(ev.EconomicImpact AS DECIMAL(18,2))) AS avg_impact,
    SUM(CAST(ev.EconomicImpact AS DECIMAL(18,2))) AS total_impact,
    COUNT(*) AS event_count,
    AVG(CAST(ev.ImpactPerCapita AS DECIMAL(18,2))) AS avg_per_capita

FROM Emissions e
LEFT JOIN Events ev
    ON e.Country = ev.Country AND e.Year = ev.Year
GROUP BY e.Country, e.Year;
