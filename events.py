#cleaning global_climate_events_economic_impact_2020_2025.csv

import pandas as pd

df = pd.read_csv('global_climate_events_economic_impact_2020_2025.csv')
#specifiy columns - keeps countries where there is less available data but need/want total, coal, oil, gas for each country at least

df = df[['year', 'country','event_type','economic_impact_million_usd', 'international_aid_million_usd','impact_per_capita']]
#print(df)

clean = df.dropna(how='any', axis=0, subset=['year', 'country','event_type','economic_impact_million_usd', 'international_aid_million_usd','impact_per_capita'])

print(clean)