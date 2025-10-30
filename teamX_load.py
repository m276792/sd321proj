from events import clean_events
from emissionsdf import clean_emissions
from MySQLdb import dbConnect

db = dbConnect()

events_df = clean_events()
events_df.to.sql('Events', db, if_exists='replace', index=False)

emissions_df = clean_emissions()
emissions_df.to.sql('Emissions', db, if_exists='replace', index=False)
