from events import clean_events
from emissionsdf import clean_emissions
from worldbankdf import clean_worldbank
from MySQLdb import dbConnect

db = dbConnect()

events_df = clean_events()
events_df.to.sql('Events', db, if_exists='replace', index=False)

emissions_df = clean_emissions()
emissions_df.to.sql('Emissions', db, if_exists='replace', index=False)


worldbank_df = clean_worldbank()
worldbank_df.to.sql('WorldBank', db, if_exists='replace', index=False)
