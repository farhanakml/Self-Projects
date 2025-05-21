import pandas as pd

def transform_to_DataFrame(data):
    df = pd.DataFrame(data)
    return df

def convert_price(data, exchange_rate):
    data['Price'] = (data['Price'].replace(r'[^\d.]', '', regex=True).astype(float)) * exchange_rate
    return data


def clean_dataframe(df):
    df["Rating"] = df["Rating"].str.extract(r"(\d+\.\d+)").astype(float)

    # Extract size (e.g., M, XL)
    df["Size"] = df["Size"].str.extract(r"Size:\s*(\w+)")

    # Extract gender (e.g., Men, Women, Unisex)
    df["Gender"] = df["Gender"].str.extract(r"Gender:\s*(\w+)")

    # Extract number of colors (e.g., 3, 5)
     # Extract color count, fill NaN with 0, convert to int
    df["Colors"] = df["Colors"].str.extract(r"(\d+)").fillna(0).astype(int)
    df = df[df["Colors"] > 0]
    
    
    df = df.dropna(subset=["Rating", "Size", "Gender", "Colors"])
    
    df = df.drop_duplicates(subset=["Title", "Rating", "Size", "Gender", "Colors"])

    # Reset index after dropping rows
    df.reset_index(drop=True, inplace=True)

    return df
