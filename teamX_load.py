from events import clean_events
from emissionsdf import clean_emissions
from worldbankdf import clean_worldbank
from mydb import dbConnect

db = dbConnect()

events_df = clean_events()
events_df.to.sql('Events', con=db, if_exists='replace', index=False)

emissions_df = clean_emissions()
emissions_df.to.sql('Emissions', con=db, if_exists='replace', index=False)


worldbank_df = clean_worldbank()
worldbank_df.to.sql('WorldBank', con=db, if_exists='replace', index=False)
