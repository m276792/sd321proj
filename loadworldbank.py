#!/usr/bin/python

# CHANGETHIS
# Filename to read
filename = 'world_bank_data_2025.csv'

# CHANGETHIS
# Table to place data into
tableName = 'WorldBank'

# auto generate table design
design = {}
with open(filename) as f:
    data = f.readlines()

# Retrieve header row
headers = data[0].strip().split(',')
headers = [name.replace(" ","_") for name in headers]  #replace spaces with _
headers = [name.replace("-","_") for name in headers]  #replace - with _


# CHANGETHIS if different default type desired for columns 
# Default type for each column in our table.
# format for each column design is  [IS_STR, TYPE, NULL OR NOT NULL]
default     = [1,       'VARCHAR(64)',    'NULL']

# If want all columns, store the default design info for each of this
# If not all columns are desired, skip this 
for i in range(len(headers)):
    design[i] = default

# CHANGETHIS
# If we only want specific columns, or if we want to redefine types, define new
# design info
#     [INDEX]= [IS_STR, CREATE TABLE TYPE, NULL OR NOT NULL]
# e.g. if column 0 should be a VARCHAR(20), and not null, use the line below
design[0]    = [1,      'VARCHAR(20)',    'NOT NULL']
# e.g. if column 1 should be a VARCHAR(60), use the line below
design[1]    = [1,      'VARCHAR(60)',    'NULL']
# e.g. if column 2 should be an INT, use the line below
design[2]    = [0,      'INT',            'NULL']

# Create the CREATE TABLE statement
print('DROP TABLE IF EXISTS', tableName, ';')
print('CREATE TABLE', tableName, '(')
create = []
# use maxsize to align things to print pretty
maxSize = [10,10]
for i in range(len(headers)):
    maxSize[0] = max(maxSize[0], len(headers[i])+2)
    maxSize[1] = max(maxSize[1], len(design[i][1])+2)
for i in range(len(headers)):
    create.append(" ".join([headers[i].ljust(maxSize[0]), design[i][1].ljust(maxSize[1]), design[i][2]]))
print(' ', ",\n  ".join(create))
print(");")

# # Read data
# import csv

# # We will try to import a csv file and treat commas in quotes as comma,
# # and not as separator. csv.reader knows know to do that
# for row in csv.reader(data[1:], quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
#     insert = []
#     for index in design:
#         # NULL if value is missing, quotes for strings, value for numbers
#         if row[index] == '':
#             insert.append('NULL')
#         elif design[index][0]:
#             # Escape the quotes
#             row[index] = row[index].replace("'", "\\'")
#             insert.append("'"+str(row[index])+"'")
#         else:
#             insert.append(str(row[index]))
#     print ('INSERT INTO', tableName, 'VALUES (', ','.join(insert),');')