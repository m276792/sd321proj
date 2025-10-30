import csv

csv_file = "world_bank_data_2025.csv"   
table_name = "WorldBankData"

# Columns to keep 
column_map = {
    "country_name": "Country",
    "year": "Year",
    "Inflation (CPI %)": "Inflation",
    "GDP (Current USD)": "GDP",
    "Unemployment Rate (%)": "Unemployment",
    "GDP Growth (% Annual)": "GDPGrowth"
}

with open(csv_file, newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # Skip rows outside 2019–2021
        year_str = row.get("year", "").strip()
        if not year_str.isdigit():
            continue
        year = int(year_str)
        if year < 2019 or year > 2021:
            continue

        # Extract only needed columns, using the mapping
        values = [row.get(csv_col, "").strip() for csv_col in column_map.keys()]

        formatted_values = []
        for v in values:
            if v == "":
                formatted_values.append("NULL")
            else:
                # Check if numeric (float or int)
                try:
                    float(v.replace(",", ""))  # remove commas for large numbers
                    formatted_values.append(v.replace(",", ""))
                except ValueError:
                    formatted_values.append(f"'{v.replace("'", "''")}'")

        # Build SQL insert statement
        sql = (
            f"INSERT INTO {table_name} "
            f"({', '.join(column_map.values())}) "
            f"VALUES ({', '.join(formatted_values)});"
        )

        print(sql)
