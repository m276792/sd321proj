import pandas as pd

df = pd.read_csv('file name add in later.csv')
#get number null values per column
#print(df.isnull().sum())

#drop null values
#df.dropna()

#fill null values with 0 or something else
#df.fillna(0)

#delete duplicate rows
#df_unique = df.drop_duplicates()

#get column data types
#df.dtypes()

#change data type
#df['seconds'] = df['seconds'].astype(str)

#useful snapshot of data
#print(df.info())

#useful stats
#print(df.describe())

for i in range(len(df)):
    row = df.iloc[i,:]          #iterates over total number of rows
    print(row)                  #grabs a row

    #clean up data and time column for example
    date, time = row['datetime'].split(' ')
    print(f'date: {date}')
    print(f'time: {time}')

    #clean up city column
    city = row['city'].upper()
