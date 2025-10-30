import csv

csv_file = "global_climate_events_economic_impact_2020_2025.csv"
table_name = "GlobalImpactEvents"

# Columns to keep — mapping CSV headers to SQL-friendly names
column_map = {
    "event_type": "EventType",
    "country": "Country",
    "year": "Year",
    "economic_impact_million_usd": "EconomicImpact",
    "international_aid_million_usd": "InternationalAid",
    "impact_per_capita": "ImpactPerCapita"
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

        # Extract only the needed columns
        values = [row.get(csv_col, "").strip() for csv_col in column_map.keys()]

        formatted_values = []
        for v in values:
            if v == "":
                formatted_values.append("NULL")
            else:
                # Attempt to treat as numeric (remove commas, handle floats)
                try:
                    float(v.replace(",", ""))  # numeric check
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
