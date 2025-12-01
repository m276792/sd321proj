import pandas as pd
import MySQLdb
import matplotlib.pyplot as plt
import seaborn as sns

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
LIMIT 150;
"""

cursor = db.cursor()
cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])

#create plot
plt.figure(figsize=(20,20))
sns.scatterplot(data=df, x="GDP", y="Emissions", hue="Country")
plt.title("GDP vs CO₂ Emissions")
plt.xlabel("GDP")
plt.ylabel("Total Emissions")
plt.tight_layout()
plt.savefig("pt4.png")

#SELECT  w.Country, w.Year,  CAST(w.GDP AS DECIMAL(15,2)) AS GDP, CAST(e.Total AS DECIMAL(15,2)) AS EmissionsFROM WorldBank wJOIN Emissions e     ON w.Country = e.Country AND w.Year = e.YearWHERE w.GDP IS NOT NULL AND e.Total IS NOT NULL;