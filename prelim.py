import csv

def count_unique(csv_file):
    unique_values = {}
    row_count = 0

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for header in reader.fieldnames:
            unique_values[header] = set()


        for row in reader:
            row_count += 1
            for header, value in row.items():
                if value is not None and value.strip() != "":
                    unique_values[header].add(value.strip())


    unique_counts = {col: len(values) for col, values in unique_values.items()}

    return row_count, unique_counts



rows, counts = count_unique("combined.csv")

print(f"Total rows: {rows}\n")
print("=============================")
print("Unique value count per column")
print("=============================")
for column, count in counts.items():
    print(f"{column}: {count}")
