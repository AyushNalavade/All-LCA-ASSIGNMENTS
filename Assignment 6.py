import pandas as pd
import sys

filename = input("Enter file name (.csv/.xls/.xlsx): ").strip()
if filename.lower().endswith(".csv"):
    df = pd.read_csv(filename)
elif filename.lower().endswith((".xls", ".xlsx")):
    df = pd.read_excel(filename)
else:
    print("Invalid file format")
    sys.exit()
print("Original DataFrame:")
print(df)
print("Missing values:")
print(df.isnull().sum())
for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().any():
        mode_value = df[col].mode(dropna=True)
        if not mode_value.empty:
            df[col] = df[col].fillna(mode_value.iloc[0])
        else:
            df[col] = df[col].fillna("Unknown")
df = df.drop_duplicates().reset_index(drop=True)
print("Preprocessed DataFrame:")
print(df)
df.to_csv("preprocessed_data.csv", index=False)
print("Preprocessed data saved successfully!")
