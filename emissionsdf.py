#cleaning emissions.csv

import pandas as pd
def clean_emissions():
    df = pd.read_csv('emissions.csv')
    #specifiy columns - keeps countries where there is less available data but need/want total, coal, oil, gas for each country at least

    df = df.dropna(how='any', axis=0, subset=['Country','Total', 'Coal', 'Oil', 'Gas'])

    #returns first lines of df
    #print(df.head())
    #note, still has NaN values

    df = df[['Country','Year','Total', 'Coal', 'Oil', 'Gas']]
    return df

