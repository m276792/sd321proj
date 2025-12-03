import pandas as pd
import MySQLdb
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

db = MySQLdb.connect('db.cs.usna.edu', # Hostname
                     'm276792',        # Username
                     'm276792',        # Password
                     'm276792')        # Schema/DB Name

db.autocommit(True)


#query
query = """
SELECT 
    w.Country,
    AVG(CAST(w.GDP AS DECIMAL(15,2))) AS GDP,
    AVG(CAST(e.Total AS DECIMAL(15,2))) AS Emissions
FROM WorldBank w
JOIN Emissions e 
    ON w.Country = e.Country AND w.Year = e.Year
WHERE w.GDP IS NOT NULL 
  AND e.Total IS NOT NULL
  AND w.Year IN (2019, 2020, 2021)
GROUP BY w.Country
ORDER BY GDP DESC
;
"""

cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])

#create plot
plt.figure(figsize=(15,8))
sns.scatterplot(data=df, x="GDP", y="Emissions", hue="Country")
plt.title("GDP vs CO₂ Emissions")
plt.xlabel("GDP")
plt.ylabel("Total Emissions")
plt.tight_layout()
plt.savefig("pt4.png")

#SELECT  w.Country, w.Year,  CAST(w.GDP AS DECIMAL(15,2)) AS GDP, CAST(e.Total AS DECIMAL(15,2)) AS EmissionsFROM WorldBank wJOIN Emissions e     ON w.Country = e.Country AND w.Year = e.YearWHERE w.GDP IS NOT NULL AND e.Total IS NOT NULL;


#graph 2

query = """
SELECT     Country, AVG(CAST(COALESCE(Coal, 0) AS DECIMAL(15,2))) AS AvgCoal,    
 AVG(CAST(COALESCE(Oil, 0) AS DECIMAL(15,2))) AS AvgOil,     
 AVG(CAST(COALESCE(Gas, 0) AS DECIMAL(15,2))) AS AvgGas,     
 AVG(CAST(COALESCE(Coal, 0) AS DECIMAL(15,2))) 
 + AVG(CAST(COALESCE(Oil, 0) AS DECIMAL(15,2))) 
+ AVG(CAST(COALESCE(Gas, 0) AS DECIMAL(15,2))) AS Total 
FROM Emissions 
WHERE Year IN ('2019','2020','2021')
GROUP BY Country 
ORDER BY Total DESC 
LIMIT 10;
"""
#this query averages 

cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])

#create plot
plt.figure(figsize=(15,8))

x = np.arange(len(df["Country"]))
width = 0.25


plt.bar(x - width, df["AvgCoal"], width, label="Avg Coal")
plt.bar(x,         df["AvgOil"],  width, label="Avg Oil")
plt.bar(x + width, df["AvgGas"],  width, label="Avg Gas")

plt.xticks(x, df["Country"], rotation=45, ha="right")

plt.title("Average Fossil Fuel Emissions per Country")
plt.xlabel("Country")
plt.ylabel("Average Emissions")
plt.legend()
plt.tight_layout()
plt.savefig("pt4num2.png")

plt.show()


#graph 3


#SELECT  w.Country, w.Year,  CAST(w.GDP AS DECIMAL(15,2)) AS GDP, CAST(e.Total AS DECIMAL(15,2)) AS EmissionsFROM WorldBank wJOIN Emissions e     ON w.Country = e.Country AND w.Year = e.YearWHERE w.GDP IS NOT NULL AND e.Total IS NOT NULL;


#graph 2

query = """
SELECT
    Country,
    
    COUNT(*) AS event_count, /* how many events happened in each country */
    AVG(CAST(EconomicImpact AS DECIMAL(18,2))) AS avg_impact, /* average impact of each event */
    SUM(CAST(EconomicImpact AS DECIMAL(18,2))) AS total_impact /* total impact on country*/
FROM Events
WHERE Year IN ('2019','2020','2021') AND event_type IN ('Drought','Heatwave','Wildfire','Cold Wave','Flood','Landslide')
GROUP BY Country
ORDER BY event_count DESC
LIMIT 30
;
"""
#this query averages 

cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])

#create plot
plt.figure(figsize=(15,8))

x = np.arange(len(df["Country"]))
width = 0.25


plt.bar(x - width, df["event_count"], width, label="Event count")
plt.bar(x,         df["avg_impact"],  width, label="Average Impact")


plt.xticks(x, df["Country"], rotation=45, ha="right")

plt.title("Economic Impact of Climate Events by Country")
plt.xlabel("Country")
plt.ylabel("Average Impact")
plt.legend()
plt.tight_layout()
plt.savefig("pt4num3.png")

plt.show()
