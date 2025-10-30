import csv

csv_file = "emissions.csv"
table_name = "Emissions"

# We’ll look for these keys in a case-insensitive way
wanted_cols = ["Country", "Year", "Total", "Oil", "Gas", "Coal"]

with open(csv_file, newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    # Normalize header names for case-insensitive access
    field_map = {name.lower(): name for name in reader.fieldnames}

    # Match the desired columns with actual header names
    actual_cols = [field_map.get(c.lower()) for c in wanted_cols]

    for row in reader:
        # Skip invalid or missing year
        year_str = str(row.get(actual_cols[1], "")).strip()
        if not year_str.isdigit():
            continue
        year = int(year_str)
        if year < 2019 or year > 2021:
            continue

        # Extract only the needed columns
        values = [str(row.get(col, "")).strip() if col else "" for col in actual_cols]

        formatted_values = []
        for v in values:
            v_clean = v.replace(",", "").strip()
            if v_clean == "":
                formatted_values.append("NULL")
            else:
                try:
                    float(v_clean)
                    formatted_values.append(v_clean)
                except ValueError:
                    formatted_values.append(f"'{v_clean.replace("'", "''")}'")

        sql = (
            f"INSERT INTO {table_name} "
            f"({', '.join(wanted_cols)}) VALUES ({', '.join(formatted_values)});"
        )

        print(sql)



