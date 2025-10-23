import pandas as pd

df = pd.read_csv('world_bank_data_2025.csv')


df = df[['country_name','year','Inflation (CPI %)','GDP (Current USD)','GDP per Capita (Current USD)','Unemployment Rate (%)','GDP Growth (% Annual)','Current Account Balance (% GDP)','Government Expense (% of GDP)','Government Revenue (% of GDP)','Gross National Income (USD)']]
df = df.dropna()
print(df.tail())