import pandas as pd
from collections import Counter

# Load the datasets
df1 = pd.read_csv("datasets/Raw_Datasets/zeekdata22fall.csv")
df2 = pd.read_csv("datasets/Raw_Datasets/zeekdata24.csv")
df3 = pd.read_csv("datasets/Raw_Datasets/zeekdata24fall.csv")


datasets = {
    "zeekdata22fall": df1,
    "zeekdata24": df2,
    "zeekdata24fall": df3
}
def combined_unique_values(column_name, *dfs):
    values = set()

    for df in dfs:
        if column_name in df.columns:
            values.update(df[column_name].dropna().unique())

    values = sorted(values)

    print(f"\nCombined unique values in '{column_name}' ({len(values)}):")
    for value in values:
        print(value)

    return values


def combined_unique_values_with_counts(column_name, *dfs):
    counter = Counter()

    
    for df in dfs:
        if column_name in df.columns:
            values = df[column_name].dropna().values
            counter.update(values)

    
    sorted_items = counter.most_common()

    print(f"\nCombined value counts for '{column_name}':")
    for value, count in sorted_items:
        print(f"{value}: {count}")

    
    return dict(counter)

for name, df in datasets.items():
    print(f"\n{'='*50}")
    print(name)
    print(f"{'='*50}")

    # Missing values per column
    missing_count = df.isnull().sum()

    # Keep only columns that have missing values
    missing_count = missing_count[missing_count > 0]

    if missing_count.empty:
        print("No missing values found.")
        continue

    # Calculate percentages only for columns with missing values
    missing_percent = (missing_count / len(df)) * 100

    summary = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing Percentage (%)": missing_percent.round(2)
    })

    print("\nColumns with missing values:")
    print(summary)

    # Number of rows with at least one missing value
    rows_with_missing = df.isnull().any(axis=1).sum()
    print(f"\nInstances with at least one missing value: {rows_with_missing}")
    print(f"Total instances: {len(df)}")

protocol_unique_values = combined_unique_values("proto", df1, df2, df3)
label_tactics = combined_unique_values("label_tactic", df1, df2, df3)
attack_counts = combined_unique_values_with_counts("label_tactic", df1, df2, df3)