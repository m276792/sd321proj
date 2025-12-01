/* part 3 - 5 questions to answer with sql */

-- Q1: What is the single climate event that was most economically damaging?

SELECT * FROM Events ORDER BY EconomicImpact DESC LIMIT 5;

-- returns Russia, 2020 - heatwave that had an economic impact of 9.42 milllion USD, 
-- causes 18 deaths, and affected 1.7 million people.
-- interesting note: second most damaging event was a cold wave in Egypt that had an economic impact of 8.72 million USD

-- Q2: What countries had the three highest emissions in 2019? 2020? 2021?

-- Q3: 
