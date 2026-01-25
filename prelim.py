import csv

def count_unique_values_by_column(csv_file):
    unique_values = {}

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)


        for header in reader.fieldnames:
            unique_values[header] = set()


        for row in reader:
            for header, value in row.items():
                if value is not None:
                    unique_values[header].add(value.strip())

 
    unique_counts = {col: len(values) for col, values in unique_values.items()}
    return unique_counts



counts = count_unique_values_by_column("combined.csv")

print("Unique value counts per column:\n")
for column, count in counts.items():
    print(f"{column}: {count}")
