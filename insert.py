import csv

csv_file = "world_bank_data_2025.csv"
output_file = "world_bank_inserts.sql"
table_name = "WorldBankData"

# Correct column map with exact CSV headers
column_map = {
    "country_name": "Country",
    "year": "Year",
    "Inflation (CPI %)": "Inflation",
    "GDP (Current USD)": "GDP",
    "Unemployment Rate (%)": "Unemployment",
    "GDP Growth (% Annual)": "GDPGrowth"
}

with open(csv_file, newline='', encoding='utf-8') as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)

    for row in reader:
        # Read year safely
        year_str = row.get("year", "").strip()
        if not year_str.isdigit():
            continue

        year = int(year_str)

        # FIX: Allow 2019–2025 (or remove this check if you want all rows)
        if year < 2019 or year > 2025:
            continue

        # Extract the needed CSV columns
        values = [row.get(csv_col, "").strip() for csv_col in column_map.keys()]

        formatted_values = []
        for v in values:
            if v == "":
                formatted_values.append("NULL")
            else:
                # Numeric check
                try:
                    float(v.replace(",", ""))
                    formatted_values.append(v.replace(",", ""))
                except ValueError:
                    # Escape single quotes
                    safe_v = v.replace("'", "''")
                    formatted_values.append(f"'{safe_v}'")

        sql = (
            f"INSERT INTO {table_name} "
            f"({', '.join(column_map.values())}) "
            f"VALUES ({', '.join(formatted_values)});"
        )

        outfile.write(sql + "\n")

print(f"Done! SQL insert statements written to: {output_file}")

