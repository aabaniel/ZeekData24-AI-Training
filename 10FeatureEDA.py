import pandas as pd
from collections import Counter

# Load the datasets
df1 = pd.read_csv("datasets/Raw_Datasets/zeekdata22fall.csv")
df2 = pd.read_csv("datasets/Raw_Datasets/zeekdata24.csv")
df3 = pd.read_csv("datasets/Raw_Datasets/zeekdata24fall.csv")
df4 = pd.read_csv("datasets/Updated/final_train.csv") #Reconnaissance combined - train set
df5 = pd.read_csv("datasets/Updated/final_train.csv") #Reconnaissance combined - test set
df6 = pd.read_csv("datasets/final_train.csv") #Resource Development combined - train set
df7 = pd.read_csv("datasets/test.csv") #Resource Development combined - test set

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

import pandas as pd

def analyze_label_characteristics(label_column, label_value, *dfs, min_frequency=0.90):
    # Combine all matching rows
    combined = pd.concat(
        [df[df[label_column] == label_value] for df in dfs],
        ignore_index=True
    )

    if combined.empty:
        print(f"No samples found for '{label_value}'.")
        return

    print("=" * 100)
    print(f"Analysis for '{label_value}'")
    print(f"Total Samples: {len(combined)}")
    print("=" * 100)

    results = []

    for col in combined.columns:

        if col == label_column:
            continue

        counts = combined[col].value_counts(dropna=False)

        if counts.empty:
            continue

        most_common_value = counts.index[0]
        most_common_count = counts.iloc[0]
        percentage = (most_common_count / len(combined)) * 100

        # Skip columns where every value is unique
        if most_common_count == 1:
            continue

        if percentage >= min_frequency * 100:
            results.append({
                "Column": col,
                "Most Common Value": most_common_value,
                "Count": most_common_count,
                "Percentage": percentage
            })

    if not results:
        print(f"No columns met the {min_frequency*100:.0f}% threshold.")
        return

    result_df = (
        pd.DataFrame(results)
        .sort_values(by="Percentage", ascending=False)
        .reset_index(drop=True)
    )

    print(result_df.to_string(index=False))




protocol_unique_values = combined_unique_values("proto", df1, df2, df3)
label_tactics = combined_unique_values("label_tactic", df1, df2, df3)
attack_counts = combined_unique_values_with_counts("label_tactic", df1, df2, df3)

column_name = "label_tactic"

for name, df in datasets.items():
    print(f"\n{name}")
    print(df[column_name].value_counts(dropna=False))

for tactic in sorted(set(df5["label_tactic"])| set(df7["label_tactic"])):
    analyze_label_characteristics(
        "label_tactic",tactic,df5, df7)
    print("\n")