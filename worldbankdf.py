import pandas as pd

def clean_worldbank():
    df = pd.read_csv('world_bank_data_2025.csv')

    #might take more columns out
    df = df[['country_name','year','Inflation (CPI %)','GDP (Current USD)','GDP per Capita (Current USD)','Unemployment Rate (%)','GDP Growth (% Annual)']]
    df = df.dropna()
    return df