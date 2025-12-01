import pandas as pd
import MySQLdb
import matplotlib.pyplot as plt
import seaborn as sns


conn = MySQLdb.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="yourdatabase"
)

#query
query = """
SELECT 
    w.Country, w.Year, 
    CAST(w.GDP AS DECIMAL(15,2)) AS GDP,
    CAST(e.Total AS DECIMAL(15,2)) AS Emissions
FROM WorldBank w
JOIN Emissions e 
    ON w.Country = e.Country AND w.Year = e.Year
WHERE w.GDP IS NOT NULL AND e.Total IS NOT NULL;
"""

df = pd.read_sql(query, conn)

#create plot
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="GDP", y="Emissions", hue="Country")
plt.title("GDP vs CO₂ Emissions")
plt.xlabel("GDP")
plt.ylabel("Total Emissions")
plt.tight_layout()
plt.show()
