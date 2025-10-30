import csv

csv_file = "emissions.csv"     # your CSV file name
table_name = "Emissions"
columns = ["Country", "Year", "total", "oil", "gas", "coal"]

with open(csv_file, newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # Skip rows outside 2019–2021
        year_str = row.get("Year", "").strip()
        if not year_str.isdigit():
            continue
        year = int(year_str)
        if year < 2019 or year > 2021:
            continue

        # Extract only the needed columns
        values = [row.get(col, "").strip() for col in columns]

        formatted_values = []
        for v in values:
            if v == "":  # handle missing values
                formatted_values.append("NULL")
            elif v.replace('.', '', 1).isdigit():
                formatted_values.append(v)
            else:
                formatted_values.append(f"'{v.replace("'", "''")}'")

        # Build SQL insert statement
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(formatted_values)});"

        print(sql)

