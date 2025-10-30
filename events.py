#cleaning global_climate_events_economic_impact_2020_2025.csv

import pandas as pd
def clean_events():
    df = pd.read_csv('global_climate_events_economic_impact_2020_2025.csv')
    df = df[['year', 'country','event_type','economic_impact_million_usd', 'international_aid_million_usd','impact_per_capita']]
    df = df.dropna(how='any', axis=0, subset=['year', 'country','event_type','economic_impact_million_usd', 'international_aid_million_usd','impact_per_capita'])
    return df



