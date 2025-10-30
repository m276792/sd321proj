from events import clean_events
from MySQLdb import dbConnect

db = dbConnect()

events_df = clean_events()
events_df.to.sql('Events', db, if_exists='replace', index=False)