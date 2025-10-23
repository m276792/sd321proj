#cleaning global_climate_events_economic_impact_2020_2025.csv

import pandas as pd
df = pd.read_csv('global_climate_events_economic_impact_2020_2025.csv')
df = df[['year', 'country','event_type','economic_impact_million_usd', 'international_aid_million_usd','impact_per_capita']]
#print(df)
df = df.dropna(how='any', axis=0, subset=['year', 'country','event_type','economic_impact_million_usd', 'international_aid_million_usd','impact_per_capita'])
#print(df)



def events_impact(df, events_impact):
    mapping = {
        'year': 'INT', 
        'country': 'VARCHAR(50)',
        'event_type': 'VARCHAR(50)',
        'economic_impact_million_usd': 'INT',
        'international_aid_million_usd': 'INT',
        'impact_per_capita': 'INT'
    }

create = f"CREATE TABLE {events_impact} (\n"
