/* part 3 - 5 questions to answer with sql */

-- Q1: What is the single climate event that was most economically damaging?

SELECT * FROM Events ORDER BY EconomicImpact DESC LIMIT 5;

-- returns Russia, 2020 - heatwave that had an economic impact of 9.42 milllion USD, 
-- causes 18 deaths, and affected 1.7 million people.
-- interesting note: second most damaging event was a cold wave in Egypt that had an economic impact of 8.72 million USD

-- Q2: What countries had the three highest emissions in 2019? 2020?

 SELECT      Country,     AVG(CAST(Total AS DECIMAL(15,2))) AS AvgTotalEmissions 
 FROM Emissions 
 WHERE Year = '2019'
 GROUP BY Country 
 ORDER BY AvgTotalEmissions DESC 
 LIMIT 5;

 -- China had the most emissions in 2019, totalling at 10,741 billion metric tons compared to 5,249 for the US.
 
-- The same query, run for 2020, returns China at 10,956, US at 4,715. China is the only country in the top 5 whose emissions grew despite COVID-19.

-- Q3: Which fuel source contributes to total emissions the most for the top five countries?

SELECT
    Country,
    AVG(CAST(Coal AS DECIMAL(15,2))) AS AvgCoal,
    AVG(CAST(Oil AS DECIMAL(15,2))) AS AvgOil,
    AVG(CAST(Gas AS DECIMAL(15,2))) AS AvgGas
FROM Emissions
GROUP BY Country
ORDER BY Country;

-- China's AvgCoal is 7,701 compared to US's 983, but the US had more oil and gas emissions than China.

-- Q4 How many environmental events have occured in each country, and which country has had the most?

SELECT     country,     COUNT(*) AS EventCount 
FROM Events 
GROUP BY country 
ORDER BY EventCount DESC 
LIMIT 10;

-- Japan has had the most at 33, and then Singapore at 30. 

-- Q5 What are Japan's most frequent climate events?
SELECT      country,     event_type,     COUNT(*) AS EventCount FROM Events WHERE country = "Japan" GROUP BY country, event_type
ORDER BY EventCount DESC;

-- Japan's most frequent climate events are actually tornadoes. 
-- Followed by Volcanic eruptions then earthquakes. That tornadoes 
-- are the most frequent is suprising in that it's not expected and goes against what you might think of first about japan and climate events. 
