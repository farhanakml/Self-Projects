import pandas as pd
from utils.transform import transform_to_DataFrame, convert_price, clean_dataframe

def test_transform_to_DataFrame():
    sample_data = [
        {"Title": "Shirt 1", "Price": "$100.00"},
        {"Title": "Shirt 2", "Price": "$200.00"}
    ]
    df = transform_to_DataFrame(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Title", "Price"]

def test_convert_price():
    df = pd.DataFrame({"Price": ["$100.50", "$200.75"]})
    result = convert_price(df, exchange_rate=15000)
    assert result["Price"].tolist() == [1507500, 3011250]

def test_clean_dataframe():
    df = pd.DataFrame({
        "Title": ["Hoodie", "T-shirt", "Invalid"],
        "Price": [100000, 200000, 300000],
        "Rating": ["Rating: ⭐ 4.5 / 5", "Rating: ⭐ 3.9 / 5", "Rating: ⭐ Invalid Rating / 5"],
        "Size": ["Size: M", "Size: L", "Size: ?"],
        "Gender": ["Gender: Men", "Gender: Women", "Gender: Unknown"],
        "Colors": ["3 Colors", "5 Colors", "No Colors"]
    })

    cleaned_df = clean_dataframe(df)
    
    # Ensure only valid rows remain
    assert cleaned_df.shape[0] == 2
    assert all(col in cleaned_df.columns for col in ["Rating", "Size", "Gender", "Colors"])
    assert cleaned_df["Rating"].tolist() == [4.5, 3.9]
    assert cleaned_df["Size"].tolist() == ["M", "L"]
    assert cleaned_df["Gender"].tolist() == ["Men", "Women"]
    assert cleaned_df["Colors"].tolist() == [3.0, 5.0]
