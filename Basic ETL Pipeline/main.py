from utils.transform import transform_to_DataFrame, convert_price, clean_dataframe
from utils.load import save_to_csv, save_to_google_sheets
from utils.extract import scrape_clothes


BASE_URL = 'https://fashion-studio.dicoding.dev/'
all_clothing_data = scrape_clothes(BASE_URL)

SPREADSHEET_ID = '179m9rqVodTt0cZ6oJvdGRQtjKyqgBUQM0Uh3G0dx_zk'
RANGE_NAME = 'Sheet1!A1'

if all_clothing_data:
     # Transform data to DataFrame
    df = transform_to_DataFrame(all_clothing_data)
    # Clean the DataFrame
    df = clean_dataframe(df)
    # Convert price to rupiah
    df = convert_price(df, 16000)

    print(df.info())
    
    # Save to CSV
    if save_to_csv(df, file_path='products.csv'):
        print("Data berhasil disimpan ke products.csv")
    else:
        print("Gagal menyimpan data.")
        
    # Save to Google Sheets
    if save_to_google_sheets(df, SPREADSHEET_ID, RANGE_NAME):
        print("Data berhasil disimpan ke Google Sheets.")
    else:
        print("Gagal menyimpan data ke Google Sheets.")
else:
    print("Tidak ada data yang ditemukan.")

