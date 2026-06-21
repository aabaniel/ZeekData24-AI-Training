import pandas as pd

# Load the datasets
df1 = pd.read_csv("datasets/Raw_Datasets/zeekdata22fall.csv")
df2 = pd.read_csv("datasets/Raw_Datasets/zeekdata24.csv")
df3 = pd.read_csv("datasets/Raw_Datasets/zeekdata24fall.csv")

datasets = {
    "zeekdata22fall": df1,
    "zeekdata24": df2,
    "zeekdata24fall": df3
}

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